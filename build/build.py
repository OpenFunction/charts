import os
import subprocess
import shutil


class Build(object):
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(cur_dir)
    ns_mapping = {
        "dapr": "dapr-system",
        "keda": "keda",
        "ingress-nginx": "ingress-nginx",
        "knative-serving": "knative-serving",
        "tekton-pipelines": "tekton-pipelines",
        "shipwright-build": "shipwright-build"
    }

    def __init__(self, major: int = 0, minor: int = 1, patch: int = 0, region_cn: bool = False):
        self.src_dir = os.path.join(self.root_dir, "openfunction")
        self.dis_dir = os.path.join(self.root_dir, "dist", "openfunction")
        self.charts_dir = os.path.join(self.dis_dir, "charts")
        self.region_cn = region_cn
        self.major = major
        self.minor = minor
        self.patch = patch
        self.version = f"{self.major}.{self.minor}.{self.patch}"

    def prepare(self):
        if not os.path.exists(self.src_dir):
            return
        if not os.path.exists(self.dis_dir):
            os.makedirs(self.dis_dir)
        # subprocess.check_call(["cp", "-r", self.src_dir, self.dis_dir])
        shutil.copytree(self.src_dir, self.dis_dir, dirs_exist_ok=True)
        os.chdir(self.dis_dir)

    def pull(self):
        subprocess.check_call(["helm", "dependency", "update"])
        os.chdir(self.charts_dir)
        for file in os.listdir(self.charts_dir):
            file_path = os.path.join(self.charts_dir, file)
            if os.path.splitext(file)[1] == ".tgz":
                subprocess.check_call(["tar", "-xf", file_path])
                subprocess.check_call(["rm", file_path])

    def process_charts(self):
        if self.region_cn:
            self.process_values()
        for chart_name in os.listdir(self.charts_dir):
            namespace = self.ns_mapping[chart_name]
            namespace_field = f"  namespace: {namespace}\n"
            chart_dir = os.path.join(self.charts_dir, chart_name)
            self.process_chart(chart_dir, namespace, namespace_field, sub_dir="templates")
            # sub_chart may have sub_chart
            self.process_chart(chart_dir, namespace, namespace_field, sub_dir="charts")
            print(f"Process {chart_name} chart successfully!")

    def process_values(self):
        origin_path = os.path.join(self.dis_dir, "values.yaml")
        custom_path = os.path.join(self.cur_dir, "values.yaml")
        with open(origin_path) as f:
            origin_lines = f.readlines()
        with open(custom_path) as f:
            custom_lines = f.readlines()
        total_lines = custom_lines + origin_lines
        result = "".join(total_lines)
        with open(origin_path, "w") as f:
            f.write(result)

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
        src_path = os.path.join(self.cur_dir, "Chart.yaml")
        dis_path = os.path.join(self.dis_dir, "Chart.yaml")
        subprocess.check_call(["cp", src_path, dis_path])

    def add_subchart_ns(self):
        src_path = os.path.join(self.cur_dir, "subchart-ns.yaml")
        dis_path = os.path.join(self.dis_dir, "templates", "subchart-ns.yaml")
        subprocess.check_call(["cp", src_path, dis_path])

    def build(self):
        self.process_charts()
        self.update_ofn_chart()
        self.add_subchart_ns()
        os.chdir(self.dis_dir)
        subprocess.check_call(["helm", "package", ".", "--version", self.version])

    def run(self):
        self.prepare()
        self.pull()
        self.build()


if __name__ == '__main__':
    builder = Build(region_cn=True)
    builder.run()
