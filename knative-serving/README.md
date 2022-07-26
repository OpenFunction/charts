# knative-serving

![Version: 1.3.2](https://img.shields.io/badge/Version-1.3.2-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.3.2](https://img.shields.io/badge/AppVersion-1.3.2-informational?style=flat-square)

A Helm chart for Knative Serving on Kubernetes

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| wangyifei | <wangyifei@kubesphere.io> |  |

## Source Code

* <https://github.com/knative/serving>

## Requirements

Kubernetes: `>=v1.21.0-0`

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
| activator.activator.image.digest | string | `"sha256:01270196a1eba7e5fd5fe34b877c82a7e8c93861de535a82342717d28f81d671"` |  |
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
| autoscaler.autoscaler.image.digest | string | `"sha256:c5a03a236bfe2abdc7d40203d787668c8accaaf39062a86e68b4d403077835e2"` |  |
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
| configDeployment.queueSidecarImage.digest | string | `"sha256:2249dc873059c0dfc0783bce5f614a0d8ada3d4499d63aa1dffd19f2788ba64b"` |  |
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
| controller.controller.image.digest | string | `"sha256:cc33e6392485e9d015886d4443324b9a41c17f6ce98b31ef4b19e47325a9a7e8"` |  |
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
| defaultDomain.job.image.digest | string | `"sha256:cd392fc65e96c9b7361a477d0daa8ac5b29af41909296c74b4e58fad1a3df76f"` |  |
| defaultDomain.job.image.repository | string | `"gcr.io/knative-releases/knative.dev/serving/cmd/default-domain"` |  |
| defaultDomain.job.image.tag | string | `nil` |  |
| defaultDomain.ports[0].name | string | `"http"` |  |
| defaultDomain.ports[0].port | int | `80` |  |
| defaultDomain.ports[0].targetPort | int | `8080` |  |
| defaultDomain.type | string | `"ClusterIP"` |  |
| domainMapping.domainMapping.image.digest | string | `"sha256:00a26f25ef119952b0ecf890f9f9dcb877b5f5d496f43c44756b93343d71b66e"` |  |
| domainMapping.domainMapping.image.repository | string | `"gcr.io/knative-releases/knative.dev/serving/cmd/domain-mapping"` |  |
| domainMapping.domainMapping.image.tag | string | `nil` |  |
| domainMapping.domainMapping.resources.limits.cpu | string | `"300m"` |  |
| domainMapping.domainMapping.resources.limits.memory | string | `"400Mi"` |  |
| domainMapping.domainMapping.resources.requests.cpu | string | `"30m"` |  |
| domainMapping.domainMapping.resources.requests.memory | string | `"40Mi"` |  |
| domainmappingWebhook.domainmappingWebhook.image.digest | string | `"sha256:f8f09d3a509b0c25d50be7532d4337a30df4ec5f51b9ed23ad9f21b3940c16ca"` |  |
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
| kubernetesClusterDomain | string | `"cluster.local"` |  |
| netContourController.controller.image.digest | string | `"sha256:8a91ddd952225b231d05054698e381d3af9c36e86bc472261e3a865a00c206aa"` |  |
| netContourController.controller.image.repository | string | `"gcr.io/knative-releases/knative.dev/net-contour/cmd/controller"` |  |
| netContourController.controller.image.tag | string | `nil` |  |
| netContourController.controller.resources.limits.cpu | string | `"400m"` |  |
| netContourController.controller.resources.limits.memory | string | `"400Mi"` |  |
| netContourController.controller.resources.requests.cpu | string | `"40m"` |  |
| netContourController.controller.resources.requests.memory | string | `"40Mi"` |  |
| netContourController.replicas | int | `1` |  |
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
| webhook.webhook.image.digest | string | `"sha256:b001a58cb7eac7fbae4d83d8a111fa0f6726d36e86844d5b1dc3c9b8fdd5710a"` |  |
| webhook.webhook.image.repository | string | `"gcr.io/knative-releases/knative.dev/serving/cmd/webhook"` |  |
| webhook.webhook.image.tag | string | `nil` |  |
| webhook.webhook.resources.limits.cpu | string | `"500m"` |  |
| webhook.webhook.resources.limits.memory | string | `"500Mi"` |  |
| webhook.webhook.resources.requests.cpu | string | `"100m"` |  |
| webhook.webhook.resources.requests.memory | string | `"100Mi"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.10.0](https://github.com/norwoodj/helm-docs/releases/v1.10.0)
