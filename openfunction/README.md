# openfunction

![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.6.0](https://img.shields.io/badge/AppVersion-0.6.0-informational?style=flat-square)

A Helm chart for OpenFunction on Kubernetes

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| wangyifei | <wangyifei@kubesphere.io> |  |

## Source Code

* <https://github.com/OpenFunction/OpenFunction>

## Requirements
- helm: `>=v3.6.3`
- Kubernetes: `>=v1.20.0-0`

| Repository | Name | Version | AppVersion |
|------------|------|---------|------------|
| https://dapr.github.io/helm-charts/ | dapr | 1.5.1   | 1.5.1      |
| https://kedacore.github.io/charts | keda | 2.4.0   | 2.4.0      |
| https://kubernetes.github.io/ingress-nginx | ingress-nginx | 4.0.6   | 1.0.4      |
| https://openfunction.github.io/charts/ | knative-serving | 0.6.0   | 1.0.1      |
| https://openfunction.github.io/charts/ | shipwright-build | 0.6.0   | 0.6.1      |
| https://openfunction.github.io/charts/ | tekton-pipelines | 0.6.0   | 0.30.0     |

## Install the Chart

Ensure Helm is initialized in your Kubernetes cluster.

For more details on initializing Helm, [read the Helm docs](https://helm.sh/docs/)

1. Add `openfunction.github.io` as an helm repo
    ```
    helm repo add openfunction https://openfunction.github.io/charts/
    helm repo update
    ```

2. Install the openfunction chart on your cluster in the `openfunction` namespace:
   * If your environment does not contain any openfunction-dependent components and you want to install all components 
   directly, You can install openfunction with all dependencies with the following command:
      ```
      kubectl create namespace openfunction
      helm install openfunction openfunction/openfunction -n openfunction
      ```
   * If your environment already contains some of the openfunction-dependent components, or if you want to install some
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
1. You may need to remove the `ingresses.networking.internal.knative.dev` resource 
from the namespace `knative-serving` first, otherwise it may block the uninstallation of knative-serving, you can 
confirm it with the following command:
    ```
    kubectl get ingresses.networking.internal.knative.dev -n knative-serving
    ```
2. Uninstall the helm release:
    ```
    helm uninstall openfunction -n openfunction
    ```
3. Since the namespace ingress-nginx has added the `"helm.sh/hook": pre-install`, you need to remove it manually
    ```
    kubectl delete ns ingress-nginx
    ```

## Values

| Key | Type | Default | Description |
|-----|------|------|-------------|
| Dapr.enabled | bool | `true` |  |
| IngressNginx.enabled | bool | `true` |  |
| Keda.enabled | bool | `true` |  |
| KnativeServing.enabled | bool | `true` |  |
| ShipwrightBuild.enabled | bool | `true` |  |
| TektonPipelines.enabled | bool | `true` |  |
| config.knativeServingConfigFeaturesName | string | `"config-features"` |  |
| config.knativeServingNamespace | string | `"knative-serving"` |  |
| config.pluginsTracing | string | `"enabled: false\n# Provider name can be set to \"skywalking\", \"opentelemetry\"\n# A valid provider must be set if tracing is enabled.\nprovider:\n  name: \"skywalking\"\n  oapServer: \"localhost:xxx\"\n# Custom tags to add to tracing\ntags:\n  func: function-with-tracing\n  layer: faas\n  tag1: value1\n  tag2: value2\nbaggage:\n# baggage key is `sw8-correlation` for skywalking and `baggage` for opentelemetry\n# Correlation context for skywalking: https://skywalking.apache.org/docs/main/latest/en/protocols/skywalking-cross-process-correlation-headers-protocol-v1/\n# baggage for opentelemetry: https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/baggage/api.md\n# W3C Baggage Specification/: https://w3c.github.io/baggage/\n  key: sw8-correlation # key should be baggage for opentelemetry\n  value: \"base64(string key):base64(string value),base64(string key2):base64(string value2)\"\n"` |  |
| controllerManager.kubeRbacProxy.image.repository | string | `"openfunction/kube-rbac-proxy"` |  |
| controllerManager.kubeRbacProxy.image.tag | string | `"v0.8.0"` |  |
| controllerManager.openfunction.image.repository | string | `"openfunction/openfunction"` |  |
| controllerManager.openfunction.image.tag | string | `"v0.6.0"` |  |
| controllerManager.openfunction.resources.limits.cpu | string | `"500m"` |  |
| controllerManager.openfunction.resources.limits.memory | string | `"500Mi"` |  |
| controllerManager.openfunction.resources.requests.cpu | string | `"100m"` |  |
| controllerManager.openfunction.resources.requests.memory | string | `"20Mi"` |  |
| controllerManager.replicas | int | `1` |  |
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
| webhookServerCert.tlsCrt | string | `""` |  |
| webhookServerCert.tlsKey | string | `""` |  |
| webhookService.ports[0].port | int | `443` |  |
| webhookService.ports[0].targetPort | int | `9443` |  |
| webhookService.type | string | `"ClusterIP"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.10.0](https://github.com/norwoodj/helm-docs/releases/v1.10.0)
