# openfunction

![Version: 0.5.0](https://img.shields.io/badge/Version-0.5.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.0.0](https://img.shields.io/badge/AppVersion-1.0.0-informational?style=flat-square)

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
| https://openfunction.github.io/charts/ | knative-serving | 1.3.2   | 1.3.2      |
| https://openfunction.github.io/charts/ | shipwright-build | 0.10.0  | 0.10.0     |
| https://openfunction.github.io/charts/ | tekton-pipelines | 0.37.2  | 0.37.2     |
| https://charts.bitnami.com/bitnami | contour | 8.0.4   | 1.21.1     |
| https://dapr.github.io/helm-charts/ | dapr | 1.8.3   | 1.8.3      |
| https://kedacore.github.io/charts | keda | 2.8.2   | 2.8.1      |

## Install the Chart

Ensure Helm is initialized in your Kubernetes cluster.

For more details on initializing Helm, [read the Helm docs](https://helm.sh/docs/)

1. Run the following command to add the OpenFunction chart repository first:
   ```shell
   helm repo add openfunction https://openfunction.github.io/charts/
   helm repo update
   ```

2. Then you have several options to setup OpenFunction, you can choose to:

    - Install all components:
       ```shell
       kubectl create namespace openfunction
       helm install openfunction openfunction/openfunction -n openfunction
       ```

    - Install Serving only (without build):
       ```shell
       kubectl create namespace openfunction
       helm install openfunction --set global.ShipwrightBuild.enabled=false --set global.TektonPipelines.enabled=false openfunction/openfunction -n openfunction
       ```

    - Install Knative sync runtime only:
       ```shell
       kubectl create namespace openfunction
       helm install openfunction --set global.Keda.enabled=false openfunction/openfunction -n openfunction
       ```

    - Install OpenFunction async runtime only:
       ```shell
       kubectl create namespace openfunction
       helm install openfunction --set global.Contour.enabled=false  --set global.KnativeServing.enabled=false openfunction/openfunction -n openfunction
       ```

## Verify installation

```
kubectl get po -n openfunction
```

## Uninstall the Chart

To uninstall/delete the `openfunction` release:
```
helm uninstall openfunction -n openfunction
```

## Upgrading Chart

```shell
helm upgrade [RELEASE_NAME] openfunction/openfunction -n openfunction --no-hooks
```

With Helm v3, CRDs created by this chart are not updated by default and should be manually updated.
Consult also the [Helm Documentation on CRDs](https://helm.sh/docs/chart_best_practices/custom_resource_definitions).

_See [helm upgrade](https://helm.sh/docs/helm/helm_upgrade/) for command documentation._

### Upgrading an existing Release to a new version


### From OpenFunction v0.8.x to OpenFunction v1.0.x

#### Uninstall the Chart

First, you'll need to uninstall the old `openfunction` release:
```shell
helm uninstall openfunction -n openfunction
```

#### Upgrade OpenFunction CRDs
Then you'll need to upgrade the new OpenFunction CRDs

```shell
kubectl apply -f https://openfunction.sh1a.qingstor.com/crds/v1.0.0/openfunction.yaml
```

#### Install new chart

```shell
helm repo update
helm install openfunction openfunction/openfunction -n openfunction
```

### From OpenFunction v0.7.x to OpenFunction v0.8.x

```shell
helm upgrade openfunction openfunction/openfunction -n openfunction --no-hooks
```

### From OpenFunction v0.6.0 to OpenFunction v0.7.x

There is a breaking change when upgrading from v0.6.0 to 0.7.x which requires additional manual operations.
#### Uninstall the Chart

First, you'll need to uninstall the old `openfunction` release:
```shell
helm uninstall openfunction -n openfunction
```

Confirm that the component namespaces have been deleted, it will take a while:
```shell
kubectl get ns -o=jsonpath='{range .items[?(@.metadata.annotations.meta\.helm\.sh/release-name=="openfunction")]}{.metadata.name}: {.status.phase}{"\n"}{end}'
```

> If the knative-serving namespace is in the terminating state for a long time, try running the following command and remove finalizers:
```shell
kubectl edit ingresses.networking.internal.knative.dev -n knative-serving
```

#### Upgrade OpenFunction CRDs
Then you'll need to upgrade the new OpenFunction CRDs

```shell
kubectl apply -f https://openfunction.sh1a.qingstor.com/crds/v0.7.0/openfunction.yaml
```

#### Upgrade dependent components CRDs
You also need to upgrade the dependent components' CRDs
> You only need to deal with the components included in the existing Release.
- knative-serving CRDs
    ```shell
    kubectl apply -f https://openfunction.sh1a.qingstor.com/crds/v0.7.0/knative-serving.yaml
    ```
- shipwright-build CRDs
    ```shell
    kubectl apply -f https://openfunction.sh1a.qingstor.com/crds/v0.7.0/shipwright-build.yaml
    ```
- tekton-pipelines CRDs
    ```shell
    kubectl apply -f https://openfunction.sh1a.qingstor.com/crds/v0.7.0/tekton-pipelines.yaml
    ```

#### Install new chart
```shell
helm repo update
helm install openfunction openfunction/openfunction -n openfunction
```

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| config.daprProxyImage | string | `"openfunction/dapr-proxy:v0.1.1"` |  |
| config.eventsourceHandlerImage | string | `"openfunction/eventsource-handler:v4"` |  |
| config.knativeServingConfigFeaturesName | string | `"config-features"` |  |
| config.knativeServingNamespace | string | `"knative-serving"` |  |
| config.pluginsTracing | string | `"enabled: false\nprovider:\n  name: \"skywalking\"\n  oapServer: \"localhost:xxx\"\ntags:\n  func: function-with-tracing\n  layer: faas\n  tag1: value1\n  tag2: value2\nbaggage:\n  key: sw8-correlation\n  value: \"base64(string key):base64(string value),base64(string key2):base64(string value2)\"\n"` |  |
| config.triggerHandlerImage | string | `"openfunction/trigger-handler:v4"` |  |
| contour.configInline.gateway.controllerName | string | `"projectcontour.io/projectcontour/contour"` |  |
| contour.contour.ingressClass.name | string | `"contour"` |  |
| contour.fullnameOverride | string | `"contour"` |  |
| contour.namespaceOverride | string | `"projectcontour"` |  |
| controllerManager.kubeRbacProxy.image.repository | string | `"openfunction/kube-rbac-proxy"` |  |
| controllerManager.kubeRbacProxy.image.tag | string | `"v0.8.0"` |  |
| controllerManager.openfunction.image.repository | string | `"openfunction/openfunction"` |  |
| controllerManager.openfunction.image.tag | string | `"v1.0.0"` |  |
| controllerManager.openfunction.resources.limits.cpu | string | `"500m"` |  |
| controllerManager.openfunction.resources.limits.memory | string | `"500Mi"` |  |
| controllerManager.openfunction.resources.requests.cpu | string | `"100m"` |  |
| controllerManager.openfunction.resources.requests.memory | string | `"20Mi"` |  |
| controllerManager.replicas | int | `1` |  |
| global.Contour.enabled | bool | `true` |  |
| global.Dapr.enabled | bool | `true` |  |
| global.Keda.enabled | bool | `true` |  |
| global.KnativeServing.enabled | bool | `true` |  |
| global.ShipwrightBuild.enabled | bool | `true` |  |
| global.TektonPipelines.enabled | bool | `true` |  |
| keda.image.keda.repository | string | `"openfunction/keda"` |  |
| keda.image.keda.tag | string | `"2.8.1"` |  |
| keda.image.metricsApiServer.repository | string | `"openfunction/keda-metrics-apiserver"` |  |
| keda.image.metricsApiServer.tag | string | `"2.8.1"` |  |
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
| revisionController.enable | bool | `false` |  |
| revisionController.image.pullPolicy | string | `"IfNotPresent"` |  |
| revisionController.image.repository | string | `"openfunction/revision-controller"` |  |
| revisionController.image.tag | string | `"v1.0.0"` |  |
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
