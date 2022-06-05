# knative-serving

![Version: 0.6.0](https://img.shields.io/badge/Version-0.6.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.0.1](https://img.shields.io/badge/AppVersion-1.0.1-informational?style=flat-square)

A Helm chart for Knative Serving on Kubernetes

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| wangyifei | <wangyifei@kubesphere.io> |  |

## Source Code

* <https://github.com/knative/serving>


## Prerequisites

* Kubernetes cluster with RBAC (Role-Based Access Control) enabled is required
* Helm 3.4.0 or newer

## Resources Required
* <https://knative.dev/docs/install/yaml-install/serving/install-serving-with-yaml/#prerequisites>

## Install the Chart

Ensure Helm is initialized in your Kubernetes cluster.

For more details on initializing Helm, [read the Helm docs](https://helm.sh/docs/)

1. Add openfunction.github.io as an helm repo
    ```
    helm repo add openfunction https://openfunction.github.io/helm-charts/
    helm repo update
    ```

2. Install the knative-serving chart on your cluster in the knative-serving namespace:
    ```
    helm install knative-serving openfunction/knative-serving -n knative-serving --create-namespace
    ```

## Verify installation

```
kubectl get pods -namespace knative-serving
```

## Uninstall the Chart

To uninstall/delete the `knative-serving` release:
```
helm uninstall knative-serving -n knative-serving
```

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| ScaleKourierGateway.kourierGateway.image.repository | string | `"docker.io/envoyproxy/envoy"` |  |
| ScaleKourierGateway.kourierGateway.image.tag | string | `"v1.17-latest"` |  |
| activator.activator.image.digest | string | `"sha256:ca607f73e5daef7f3db0358e145220f8423e93c20ee7ea9f5595f13bd508289a"` |  |
| activator.activator.image.repository | string | `"gcr.io/knative-releases/knative.dev/serving/cmd/activator"` |  |
| activator.activator.image.tag | string | `nil` |  |
| activator.activator.resources.limits.cpu | string | `"1"` |  |
| activator.activator.resources.limits.memory | string | `"600Mi"` |  |
| activator.activator.resources.requests.cpu | string | `"300m"` |  |
| activator.activator.resources.requests.memory | string | `"60Mi"` |  |
| activatorService.ports[0].name | string | `"http-metrics"` |  |
| activatorService.ports[0].port | int | `9090` |  |
| activatorService.ports[0].targetPort | int | `9090` |  |
| activatorService.ports[1].name | string | `"http-profiling"` |  |
| activatorService.ports[1].port | int | `8008` |  |
| activatorService.ports[1].targetPort | int | `8008` |  |
| activatorService.ports[2].name | string | `"http"` |  |
| activatorService.ports[2].port | int | `80` |  |
| activatorService.ports[2].targetPort | int | `8012` |  |
| activatorService.ports[3].name | string | `"http2"` |  |
| activatorService.ports[3].port | int | `81` |  |
| activatorService.ports[3].targetPort | int | `8013` |  |
| activatorService.type | string | `"ClusterIP"` |  |
| autoscaler.autoscaler.image.digest | string | `"sha256:31aed8b5b241147585cb0e48366451a96354fc6036d6a5667997237c1d302d98"` |  |
| autoscaler.autoscaler.image.repository | string | `"gcr.io/knative-releases/knative.dev/serving/cmd/autoscaler"` |  |
| autoscaler.autoscaler.image.tag | string | `nil` |  |
| autoscaler.autoscaler.resources.limits.cpu | string | `"1"` |  |
| autoscaler.autoscaler.resources.limits.memory | string | `"1000Mi"` |  |
| autoscaler.autoscaler.resources.requests.cpu | string | `"100m"` |  |
| autoscaler.autoscaler.resources.requests.memory | string | `"100Mi"` |  |
| autoscaler.ports[0].name | string | `"http-metrics"` |  |
| autoscaler.ports[0].port | int | `9090` |  |
| autoscaler.ports[0].targetPort | int | `9090` |  |
| autoscaler.ports[1].name | string | `"http-profiling"` |  |
| autoscaler.ports[1].port | int | `8008` |  |
| autoscaler.ports[1].targetPort | int | `8008` |  |
| autoscaler.ports[2].name | string | `"http"` |  |
| autoscaler.ports[2].port | int | `8080` |  |
| autoscaler.ports[2].targetPort | int | `8080` |  |
| autoscaler.replicas | int | `1` |  |
| autoscaler.type | string | `"ClusterIP"` |  |
| configAutoscaler | string | `nil` |  |
| configDefaults | string | `nil` |  |
| configDeployment.queueSidecarImage.digest | string | `"sha256:80dfb4568e08e43093f93b2cae9401f815efcb67ad8442d1f7f4c8a41e071fbe"` |  |
| configDeployment.queueSidecarImage.repository | string | `"gcr.io/knative-releases/knative.dev/serving/cmd/queue"` |  |
| configDeployment.queueSidecarImage.tag | string | `nil` |  |
| configDomain | string | `nil` |  |
| configFeatures | string | `nil` |  |
| configGc | string | `nil` |  |
| configKourier | string | `nil` |  |
| configLeaderElection | string | `nil` |  |
| configLogging | string | `nil` |  |
| configNetwork | string | `nil` |  |
| configObservability | string | `nil` |  |
| configTracing | string | `nil` |  |
| controller.controller.image.digest | string | `"sha256:c5a77d5642065ff3452d9b043a7226b85bfc81dc068f8dded905abf88d917a4d"` |  |
| controller.controller.image.repository | string | `"gcr.io/knative-releases/knative.dev/serving/cmd/controller"` |  |
| controller.controller.image.tag | string | `nil` |  |
| controller.controller.resources.limits.cpu | string | `"1"` |  |
| controller.controller.resources.limits.memory | string | `"1000Mi"` |  |
| controller.controller.resources.requests.cpu | string | `"100m"` |  |
| controller.controller.resources.requests.memory | string | `"100Mi"` |  |
| controller.ports[0].name | string | `"http-metrics"` |  |
| controller.ports[0].port | int | `9090` |  |
| controller.ports[0].targetPort | int | `9090` |  |
| controller.ports[1].name | string | `"http-profiling"` |  |
| controller.ports[1].port | int | `8008` |  |
| controller.ports[1].targetPort | int | `8008` |  |
| controller.type | string | `"ClusterIP"` |  |
| defaultDomain.job.image.digest | string | `"sha256:4bd6f5a7748644e56bb266d5c10f442b2548b484b57059ee64ec2a793dd1b976"` |  |
| defaultDomain.job.image.repository | string | `"gcr.io/knative-releases/knative.dev/serving/cmd/default-domain"` |  |
| defaultDomain.job.image.tag | string | `nil` |  |
| defaultDomain.ports[0].name | string | `"http"` |  |
| defaultDomain.ports[0].port | int | `80` |  |
| defaultDomain.ports[0].targetPort | int | `8080` |  |
| defaultDomain.type | string | `"ClusterIP"` |  |
| domainMapping.domainMapping.image.digest | string | `"sha256:6b5356cf3a2b64d52cbbf1bc0de376b816c4d3f610ccc8ff2dabf3d259c0996b"` |  |
| domainMapping.domainMapping.image.repository | string | `"gcr.io/knative-releases/knative.dev/serving/cmd/domain-mapping"` |  |
| domainMapping.domainMapping.image.tag | string | `nil` |  |
| domainMapping.domainMapping.resources.limits.cpu | string | `"300m"` |  |
| domainMapping.domainMapping.resources.limits.memory | string | `"400Mi"` |  |
| domainMapping.domainMapping.resources.requests.cpu | string | `"30m"` |  |
| domainMapping.domainMapping.resources.requests.memory | string | `"40Mi"` |  |
| domainmappingWebhook.domainmappingWebhook.image.digest | string | `"sha256:d0cc86f2002660c4804f6e0aed8218d39384c73a8b5006c9ac558becd8f48aa6"` |  |
| domainmappingWebhook.domainmappingWebhook.image.repository | string | `"gcr.io/knative-releases/knative.dev/serving/cmd/domain-mapping-webhook"` |  |
| domainmappingWebhook.domainmappingWebhook.image.tag | string | `nil` |  |
| domainmappingWebhook.domainmappingWebhook.resources.limits.cpu | string | `"500m"` |  |
| domainmappingWebhook.domainmappingWebhook.resources.limits.memory | string | `"500Mi"` |  |
| domainmappingWebhook.domainmappingWebhook.resources.requests.cpu | string | `"100m"` |  |
| domainmappingWebhook.domainmappingWebhook.resources.requests.memory | string | `"100Mi"` |  |
| domainmappingWebhook.ports[0].name | string | `"http-metrics"` |  |
| domainmappingWebhook.ports[0].port | int | `9090` |  |
| domainmappingWebhook.ports[0].targetPort | int | `9090` |  |
| domainmappingWebhook.ports[1].name | string | `"http-profiling"` |  |
| domainmappingWebhook.ports[1].port | int | `8008` |  |
| domainmappingWebhook.ports[1].targetPort | int | `8008` |  |
| domainmappingWebhook.ports[2].name | string | `"https-webhook"` |  |
| domainmappingWebhook.ports[2].port | int | `443` |  |
| domainmappingWebhook.ports[2].targetPort | int | `8443` |  |
| domainmappingWebhook.type | string | `"ClusterIP"` |  |
| kourier.ports[0].name | string | `"http2"` |  |
| kourier.ports[0].port | int | `80` |  |
| kourier.ports[0].protocol | string | `"TCP"` |  |
| kourier.ports[0].targetPort | int | `8080` |  |
| kourier.ports[1].name | string | `"https"` |  |
| kourier.ports[1].port | int | `443` |  |
| kourier.ports[1].protocol | string | `"TCP"` |  |
| kourier.ports[1].targetPort | int | `8443` |  |
| kourier.type | string | `"LoadBalancer"` |  |
| kourierBootstrap.envoyBootstrapYaml.admin.accessLogPath | string | `"/dev/stdout"` |  |
| kourierBootstrap.envoyBootstrapYaml.admin.address.pipe.path | string | `"/tmp/envoy.admin"` |  |
| kourierBootstrap.envoyBootstrapYaml.dynamicResources.adsConfig.apiType | string | `"GRPC"` |  |
| kourierBootstrap.envoyBootstrapYaml.dynamicResources.adsConfig.rateLimitSettings | object | `{}` |  |
| kourierBootstrap.envoyBootstrapYaml.dynamicResources.adsConfig.transportApiVersion | string | `"V3"` |  |
| kourierBootstrap.envoyBootstrapYaml.dynamicResources.cdsConfig.ads | object | `{}` |  |
| kourierBootstrap.envoyBootstrapYaml.dynamicResources.cdsConfig.resourceApiVersion | string | `"V3"` |  |
| kourierBootstrap.envoyBootstrapYaml.dynamicResources.ldsConfig.ads | object | `{}` |  |
| kourierBootstrap.envoyBootstrapYaml.dynamicResources.ldsConfig.resourceApiVersion | string | `"V3"` |  |
| kourierBootstrap.envoyBootstrapYaml.node.cluster | string | `"kourier-knative"` |  |
| kourierBootstrap.envoyBootstrapYaml.node.id | string | `"3scale-kourier-gateway"` |  |
| kourierInternal.ports[0].name | string | `"http2"` |  |
| kourierInternal.ports[0].port | int | `80` |  |
| kourierInternal.ports[0].protocol | string | `"TCP"` |  |
| kourierInternal.ports[0].targetPort | int | `8081` |  |
| kourierInternal.type | string | `"ClusterIP"` |  |
| kubernetesClusterDomain | string | `"cluster.local"` |  |
| netKourierController.controller.image.digest | string | `"sha256:cd70f2bb54f2575082e54b0df1b74908c3f4873ffc9750ca8da36d7b9bfe5b2d"` |  |
| netKourierController.controller.image.repository | string | `"gcr.io/knative-releases/knative.dev/net-kourier/cmd/kourier"` |  |
| netKourierController.controller.image.tag | string | `nil` |  |
| netKourierController.ports[0].name | string | `"grpc-xds"` |  |
| netKourierController.ports[0].port | int | `18000` |  |
| netKourierController.ports[0].protocol | string | `"TCP"` |  |
| netKourierController.ports[0].targetPort | int | `18000` |  |
| netKourierController.replicas | int | `1` |  |
| netKourierController.type | string | `"ClusterIP"` |  |
| webhook.ports[0].name | string | `"http-metrics"` |  |
| webhook.ports[0].port | int | `9090` |  |
| webhook.ports[0].targetPort | int | `9090` |  |
| webhook.ports[1].name | string | `"http-profiling"` |  |
| webhook.ports[1].port | int | `8008` |  |
| webhook.ports[1].targetPort | int | `8008` |  |
| webhook.ports[2].name | string | `"https-webhook"` |  |
| webhook.ports[2].port | int | `443` |  |
| webhook.ports[2].targetPort | int | `8443` |  |
| webhook.type | string | `"ClusterIP"` |  |
| webhook.webhook.image.digest | string | `"sha256:bd954ec8ced56e359bd4f60ee1886b20000df14126688c796383a3ae40cfffc0"` |  |
| webhook.webhook.image.repository | string | `"gcr.io/knative-releases/knative.dev/serving/cmd/webhook"` |  |
| webhook.webhook.image.tag | string | `nil` |  |
| webhook.webhook.resources.limits.cpu | string | `"500m"` |  |
| webhook.webhook.resources.limits.memory | string | `"500Mi"` |  |
| webhook.webhook.resources.requests.cpu | string | `"100m"` |  |
| webhook.webhook.resources.requests.memory | string | `"100Mi"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.10.0](https://github.com/norwoodj/helm-docs/releases/v1.10.0)
