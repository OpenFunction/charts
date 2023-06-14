import os
import yaml
import subprocess
import shutil


class Build(object):
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(cur_dir)
    ns_mapping = {
        "dapr": "dapr-system",
        "keda": "keda",
        "contour": "projectcontour",
        "knative-serving": "knative-serving",
        "tekton-pipelines": "tekton-pipelines",
        "shipwright-build": "shipwright-build"
    }
    local_charts = {"knative-serving", "tekton-pipelines", "shipwright-build"}
    skipped_charts = {"contour"}

    def __init__(self, version, region_cn: bool = False):
        self.src_dir = os.path.join(self.root_dir, "openfunction")
        self.dis_dir = os.path.join(self.root_dir, "dist", "openfunction")
        self.charts_dir = os.path.join(self.dis_dir, "charts")
        self.region_cn = region_cn
        self.version = version

    def prepare(self):
        if not os.path.exists(self.src_dir):
            return
        if os.path.exists(self.dis_dir):
            shutil.rmtree(self.dis_dir)
        shutil.copytree(self.src_dir, self.dis_dir, dirs_exist_ok=True)
        for chart in self.local_charts:
            src_dir = os.path.join(self.root_dir, chart)
            dis_dir = os.path.join(self.charts_dir, chart)
            shutil.copytree(src_dir, dis_dir, dirs_exist_ok=True)
        os.chdir(self.dis_dir)

    def pull(self):
        subprocess.check_call(["helm", "dependency", "update"])
        os.chdir(self.charts_dir)
        for file in os.listdir(self.charts_dir):
            file_path = os.path.join(self.charts_dir, file)
            print(f"pull and tar {file_path}")
            if os.path.splitext(file)[1] == ".tgz":
                subprocess.check_call(["tar", "-xf", file_path])
                os.remove(file_path)

    def process_charts(self):
        for chart_name in os.listdir(self.charts_dir):
            if chart_name in self.skipped_charts:
                continue
            namespace = self.ns_mapping[chart_name]
            namespace_field = f"  namespace: {namespace}\n"
            chart_dir = os.path.join(self.charts_dir, chart_name)
            self.process_chart(chart_dir, namespace, namespace_field, sub_dir="templates")
            # sub_chart may have sub_chart
            self.process_chart(chart_dir, namespace, namespace_field, sub_dir="charts")
            print(f"Process {chart_name} chart successfully!")

    @staticmethod
    def process_chart(chart_dir, namespace, namespace_field, sub_dir):
        templates_path = os.path.join(chart_dir, sub_dir)
        for path, sub_dirs, files in os.walk(templates_path):
            for file in files:
                file_path = os.path.join(path, file)
                apiversion_index = None
                kind_index = None
                result = ""
                with open(file_path, "r") as f:
                    lines = f.readlines()
                    for index, line in enumerate(lines):
                        if line.startswith("---"):
                            apiversion_index = None
                            kind_index = None
                        if line.startswith("apiVersion"):
                            apiversion_index = True
                        elif line.startswith("kind"):
                            kind_index = True
                        elif line.startswith("metadata"):
                            result += line
                            try:
                                if all([apiversion_index, kind_index]):
                                    if "namespace" in lines[index + 1] or "namespace" in lines[index + 2]:
                                        continue
                                    else:
                                        result += namespace_field
                            except IndexError:
                                result += namespace_field
                                print(f"IndexError {line}")
                            continue
                        if '{{ .Release.Namespace }}' in line:
                            line = line.replace('{{ .Release.Namespace }}', namespace)
                        if '{{ .Release.Namespace | quote }}' in line:
                            line = line.replace('{{ .Release.Namespace | quote }}', namespace)
                        if '.Release.Namespace' in line:
                            quote_namespace = f"\"{namespace}\""
                            line = line.replace('.Release.Namespace', quote_namespace)
                        name_tpl = """{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}"""
                        if name_tpl in line:
                            line = line.replace(name_tpl, """{{- $name | trunc 63 | trimSuffix "-" }}""")
                        result += line
                with open(file_path, "w") as f:
                    f.write(result)

    def update_ofn_chart(self):
        dis_path = os.path.join(self.dis_dir, "Chart.yaml")
        with open(dis_path, "r") as f:
            chart = yaml.safe_load(f)
            dependencies = chart["dependencies"]
            for dependency in dependencies:
                name = dependency["name"]
                dependency["repository"] = f"file://{name}"
        with open(dis_path, "w") as f:
            yaml.dump(chart, f)

    def build(self):
        self.process_charts()
        self.update_ofn_chart()
        os.chdir(self.dis_dir)
        subprocess.check_call(["helm", "package", ".", "--version", self.version])

    def run(self):
        self.prepare()
        self.pull()
        self.build()


if __name__ == '__main__':
    builder = Build(version="0.6.1", region_cn=True)
    builder.run()
