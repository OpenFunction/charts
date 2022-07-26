# openfunction

![Version: 0.2.0](https://img.shields.io/badge/Version-0.2.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.7.0](https://img.shields.io/badge/AppVersion-0.7.0-informational?style=flat-square)

A Helm chart for OpenFunction on Kubernetes

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| wangyifei | <wangyifei@kubesphere.io> |  |

## Source Code

* <https://github.com/OpenFunction/OpenFunction>

## Requirements

Kubernetes: `>=v1.21.0-0`

| Repository | Name | Version | AppVersion |
|------------|------|---------|------------|
| https://openfunction.github.io/charts/ | knative-serving | 1.3.2 | 1.3.1      |
| https://openfunction.github.io/charts/ | shipwright-build | 0.10.0 | 0.10.0     |
| https://openfunction.github.io/charts/ | tekton-pipelines | 0.37.2 | 0.37.2     |
| https://charts.bitnami.com/bitnami | contour | 8.0.4 | 1.21.1     |
| https://dapr.github.io/helm-charts/ | dapr | 1.8.0 | 1.8.0      |
| https://kedacore.github.io/charts | keda | 2.7.2 | 2.7.1      |

## Install the Chart

Ensure Helm is initialized in your Kubernetes cluster.

For more details on initializing Helm, [read the Helm docs](https://helm.sh/docs/)

1. Add `openfunction.github.io` as an helm repo
    ```
    helm repo add openfunction https://openfunction.github.io/charts/
    helm repo update
    ```

2. Install the openfunction chart on your cluster in the `openfunction` namespace:
   - If your environment does not contain any openfunction-dependent components and you want to install all components 
   directly, You can install openfunction with all dependencies with the following command:
      ```
      kubectl create namespace openfunction
      helm install openfunction openfunction/openfunction -n openfunction
      ```
   - If your environment already contains some of the openfunction-dependent components, or if you want to install some
   components separately for more flexibility and customizable capabilities. For example, if you already have dapr 
   installed in your environment, You can install openfunction with the following command:
      ```
      kubectl create namespace openfunction
      helm install openfunction --set Dapr.enabled=false openfunction/openfunction -n openfunction
      ```

## Verify installation

```
kubectl get pods -namespace openfunction
```

## Uninstall the Chart

To uninstall/delete the `openfunction` release:
```
helm uninstall openfunction -n openfunction
```

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| Contour.enabled | bool | `true` |  |
| Dapr.enabled | bool | `true` |  |
| Keda.enabled | bool | `true` |  |
| KnativeServing.enabled | bool | `true` |  |
| ShipwrightBuild.enabled | bool | `true` |  |
| TektonPipelines.enabled | bool | `true` |  |
| config.knativeServingConfigFeaturesName | string | `"config-features"` |  |
| config.knativeServingNamespace | string | `"knative-serving"` |  |
| config.pluginsTracing | string | `"enabled: false\nprovider:\n  name: \"skywalking\"\n  oapServer: \"localhost:xxx\"\ntags:\n  func: function-with-tracing\n  layer: faas\n  tag1: value1\n  tag2: value2\nbaggage:\n  key: sw8-correlation\n  value: \"base64(string key):base64(string value),base64(string key2):base64(string value2)\"\n"` |  |
| contour.configInline.gateway.controllerName | string | `"projectcontour.io/projectcontour/contour"` |  |
| contour.contour.ingressClass.name | string | `"contour"` |  |
| contour.fullnameOverride | string | `"contour"` |  |
| contour.namespaceOverride | string | `"projectcontour"` |  |
| controllerManager.kubeRbacProxy.image.repository | string | `"openfunction/kube-rbac-proxy"` |  |
| controllerManager.kubeRbacProxy.image.tag | string | `"v0.8.0"` |  |
| controllerManager.openfunction.image.repository | string | `"openfunction/openfunction"` |  |
| controllerManager.openfunction.image.tag | string | `"latest"` |  |
| controllerManager.openfunction.resources.limits.cpu | string | `"500m"` |  |
| controllerManager.openfunction.resources.limits.memory | string | `"500Mi"` |  |
| controllerManager.openfunction.resources.requests.cpu | string | `"100m"` |  |
| controllerManager.openfunction.resources.requests.memory | string | `"20Mi"` |  |
| controllerManager.replicas | int | `1` |  |
| keda.image.keda.repository | string | `"openfunction/keda"` |  |
| keda.image.keda.tag | string | `"2.7.1"` |  |
| keda.image.metricsApiServer.repository | string | `"openfunction/keda-metrics-apiserver"` |  |
| keda.image.metricsApiServer.tag | string | `"2.7.1"` |  |
| knative-serving.activator.activator.image.repository | string | `"openfunction/knative.dev-serving-cmd-activator"` |  |
| knative-serving.autoscaler.autoscaler.image.repository | string | `"openfunction/knative.dev-serving-cmd-autoscaler"` |  |
| knative-serving.configDeployment.queueSidecarImage.repository | string | `"openfunction/knative.dev-serving-cmd-queue"` |  |
| knative-serving.controller.controller.image.repository | string | `"openfunction/knative.dev-serving-cmd-controller"` |  |
| knative-serving.defaultDomain.job.image.repository | string | `"openfunction/knative.dev-serving-cmd-default-domain"` |  |
| knative-serving.domainMapping.domainMapping.image.repository | string | `"openfunction/knative.dev-serving-cmd-domain-mapping"` |  |
| knative-serving.domainmappingWebhook.domainmappingWebhook.image.repository | string | `"openfunction/knative.dev-serving-cmd-domain-mapping-webhook"` |  |
| knative-serving.netContourController.controller.image.repository | string | `"openfunction/knative.dev-net-contour-cmd-controller"` |  |
| knative-serving.webhook.webhook.image.repository | string | `"openfunction/knative.dev-serving-cmd-webhook"` |  |
| kubernetesClusterDomain | string | `"cluster.local"` |  |
| managerConfig.controllerManagerConfigYaml.health.healthProbeBindAddress | string | `":8081"` |  |
| managerConfig.controllerManagerConfigYaml.leaderElection.leaderElect | bool | `true` |  |
| managerConfig.controllerManagerConfigYaml.leaderElection.resourceName | string | `"79f0111e.openfunction.io"` |  |
| managerConfig.controllerManagerConfigYaml.metrics.bindAddress | string | `"127.0.0.1:8080"` |  |
| managerConfig.controllerManagerConfigYaml.webhook.port | int | `9443` |  |
| metricsService.ports[0].name | string | `"https"` |  |
| metricsService.ports[0].port | int | `8443` |  |
| metricsService.ports[0].targetPort | string | `"https"` |  |
| metricsService.type | string | `"ClusterIP"` |  |
| shipwright-build.shipwrightBuildController.shipwrightBuild.BUNDLE_CONTAINER_IMAGE.repository | string | `"openfunction/shipwright-bundle"` |  |
| shipwright-build.shipwrightBuildController.shipwrightBuild.GIT_CONTAINER_IMAGE.repository | string | `"openfunction/shipwright-io-build-git"` |  |
| shipwright-build.shipwrightBuildController.shipwrightBuild.MUTATE_IMAGE_CONTAINER_IMAGE.repository | string | `"openfunction/shipwright-mutate-image"` |  |
| shipwright-build.shipwrightBuildController.shipwrightBuild.WAITER_CONTAINER_IMAGE.repository | string | `"openfunction/shipwright-waiter"` |  |
| shipwright-build.shipwrightBuildController.shipwrightBuild.image.repository | string | `"openfunction/shipwright-shipwright-build-controller"` |  |
| tekton-pipelines.controller.tektonPipelinesController.entrypointImage.repository | string | `"openfunction/tektoncd-pipeline-cmd-entrypoint"` |  |
| tekton-pipelines.controller.tektonPipelinesController.gitImage.repository | string | `"openfunction/tektoncd-pipeline-cmd-git-init"` |  |
| tekton-pipelines.controller.tektonPipelinesController.gsutilImage.digest | string | `"sha256:27b2c22bf259d9bc1a291e99c63791ba0c27a04d2db0a43241ba0f1f20f4067f"` |  |
| tekton-pipelines.controller.tektonPipelinesController.gsutilImage.repository | string | `"openfunction/cloudsdktool-cloud-sdk"` |  |
| tekton-pipelines.controller.tektonPipelinesController.image.repository | string | `"openfunction/tektoncd-pipeline-cmd-controller"` |  |
| tekton-pipelines.controller.tektonPipelinesController.imagedigestExporterImage.repository | string | `"openfunction/tektoncd-pipeline-cmd-imagedigestexporter"` |  |
| tekton-pipelines.controller.tektonPipelinesController.kubeconfigWriterImage.repository | string | `"openfunction/tektoncd-pipeline-cmd-kubeconfigwriter"` |  |
| tekton-pipelines.controller.tektonPipelinesController.nopImage.repository | string | `"openfunction/tektoncd-pipeline-cmd-nop"` |  |
| tekton-pipelines.controller.tektonPipelinesController.prImage.repository | string | `"openfunction/tektoncd-pipeline-cmd-pullrequest-init"` |  |
| tekton-pipelines.controller.tektonPipelinesController.shellImage.digest | string | `"sha256:b16b57be9160a122ef048333c68ba205ae4fe1a7b7cc6a5b289956292ebf45cc"` |  |
| tekton-pipelines.controller.tektonPipelinesController.shellImage.repository | string | `"openfunction/distroless-base"` |  |
| tekton-pipelines.controller.tektonPipelinesController.shellImageWin.digest | string | `"sha256:b6d5ff841b78bdf2dfed7550000fd4f3437385b8fa686ec0f010be24777654d6"` |  |
| tekton-pipelines.controller.tektonPipelinesController.shellImageWin.repository | string | `"mcr.microsoft.com/powershell:nanoserver"` |  |
| tekton-pipelines.controller.tektonPipelinesController.workingdirinitImage.repository | string | `"openfunction/tektoncd-pipeline-cmd-workingdirinit"` |  |
| tekton-pipelines.controller.type | string | `"ClusterIP"` |  |
| tekton-pipelines.webhook.webhook.image.repository | string | `"openfunction/tektoncd-pipeline-cmd-webhook"` |  |
| webhookService.ports[0].port | int | `443` |  |
| webhookService.ports[0].targetPort | int | `9443` |  |
| webhookService.type | string | `"ClusterIP"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.10.0](https://github.com/norwoodj/helm-docs/releases/v1.10.0)
