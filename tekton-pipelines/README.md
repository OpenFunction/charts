# tekton-pipelines

![Version: 0.37.2](https://img.shields.io/badge/Version-0.37.2-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.37.2](https://img.shields.io/badge/AppVersion-0.37.2-informational?style=flat-square)

A Helm chart for Tekton Pipelines on Kubernetes

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| wangyifei | <wangyifei@kubesphere.io> |  |

## Source Code

* <https://github.com/tektoncd/pipeline>

## Requirements

Kubernetes: `>=v1.21.0-0`

## Install the Chart

Ensure Helm is initialized in your Kubernetes cluster.

For more details on initializing Helm, [read the Helm docs](https://helm.sh/docs/)

1. Add `openfunction.github.io` as a helm repo:
    ```
    helm repo add openfunction https://openfunction.github.io/charts/
    helm repo update
    ```

2. Install the `tekton-pipelines` chart on your cluster in the `tekton-pipelines` namespace:
    ```
    helm install tekton-pipelines openfunction/tekton-pipelines -n tekton-pipelines --create-namespace
    ```

## Verify installation

```
kubectl get po -n tekton-pipelines
```

## Uninstall the Chart

To uninstall/delete the `tekton-pipelines` release:
```
helm uninstall tekton-pipelines -n tekton-pipelines
```

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| configLeaderElection.leaseDuration | string | `"60s"` |  |
| configLeaderElection.renewDeadline | string | `"40s"` |  |
| configLeaderElection.retryPeriod | string | `"10s"` |  |
| configLogging.loglevelController | string | `"info"` |  |
| configLogging.loglevelWebhook | string | `"info"` |  |
| configLogging.zapLoggerConfig | string | `"{\n  \"level\": \"info\",\n  \"development\": false,\n  \"sampling\": {\n    \"initial\": 100,\n    \"thereafter\": 100\n  },\n  \"outputPaths\": [\"stdout\"],\n  \"errorOutputPaths\": [\"stderr\"],\n  \"encoding\": \"json\",\n  \"encoderConfig\": {\n    \"timeKey\": \"ts\",\n    \"levelKey\": \"level\",\n    \"nameKey\": \"logger\",\n    \"callerKey\": \"caller\",\n    \"messageKey\": \"msg\",\n    \"stacktraceKey\": \"stacktrace\",\n    \"lineEnding\": \"\",\n    \"levelEncoder\": \"\",\n    \"timeEncoder\": \"iso8601\",\n    \"durationEncoder\": \"\",\n    \"callerEncoder\": \"\"\n  }\n}\n"` |  |
| controller.ports[0].name | string | `"http-metrics"` |  |
| controller.ports[0].port | int | `9090` |  |
| controller.ports[0].protocol | string | `"TCP"` |  |
| controller.ports[0].targetPort | int | `9090` |  |
| controller.ports[1].name | string | `"http-profiling"` |  |
| controller.ports[1].port | int | `8008` |  |
| controller.ports[1].targetPort | int | `8008` |  |
| controller.ports[2].name | string | `"probes"` |  |
| controller.ports[2].port | int | `8080` |  |
| controller.ports[2].targetPort | int | `0` |  |
| controller.replicas | int | `1` |  |
| controller.tektonPipelinesController.entrypointImage.repository | string | `"gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/entrypoint"` |  |
| controller.tektonPipelinesController.entrypointImage.tag | string | `"v0.37.2"` |  |
| controller.tektonPipelinesController.gitImage.repository | string | `"gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/git-init"` |  |
| controller.tektonPipelinesController.gitImage.tag | string | `"v0.37.2"` |  |
| controller.tektonPipelinesController.gsutilImage.digest | string | `"sha256:27b2c22bf259d9bc1a291e99c63791ba0c27a04d2db0a43241ba0f1f20f4067f"` |  |
| controller.tektonPipelinesController.gsutilImage.repository | string | `"gcr.io/google.com/cloudsdktool/cloud-sdk"` |  |
| controller.tektonPipelinesController.gsutilImage.tag | string | `nil` |  |
| controller.tektonPipelinesController.image.repository | string | `"gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/controller"` |  |
| controller.tektonPipelinesController.image.tag | string | `"v0.37.2"` |  |
| controller.tektonPipelinesController.imagedigestExporterImage.repository | string | `"gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/imagedigestexporter"` |  |
| controller.tektonPipelinesController.imagedigestExporterImage.tag | string | `"v0.37.2"` |  |
| controller.tektonPipelinesController.kubeconfigWriterImage.repository | string | `"gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/kubeconfigwriter"` |  |
| controller.tektonPipelinesController.kubeconfigWriterImage.tag | string | `"v0.37.2"` |  |
| controller.tektonPipelinesController.nopImage.repository | string | `"gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/nop"` |  |
| controller.tektonPipelinesController.nopImage.tag | string | `"v0.37.2"` |  |
| controller.tektonPipelinesController.prImage.repository | string | `"gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/pullrequest-init"` |  |
| controller.tektonPipelinesController.prImage.tag | string | `"v0.37.2"` |  |
| controller.tektonPipelinesController.shellImage.digest | string | `"sha256:19f02276bf8dbdd62f069b922f10c65262cc34b710eea26ff928129a736be791"` |  |
| controller.tektonPipelinesController.shellImage.repository | string | `"ghcr.io/distroless/busybox"` |  |
| controller.tektonPipelinesController.shellImage.tag | string | `nil` |  |
| controller.tektonPipelinesController.shellImageWin.digest | string | `"sha256:b6d5ff841b78bdf2dfed7550000fd4f3437385b8fa686ec0f010be24777654d6"` |  |
| controller.tektonPipelinesController.shellImageWin.repository | string | `"mcr.microsoft.com/powershell:nanoserver"` |  |
| controller.tektonPipelinesController.shellImageWin.tag | string | `nil` |  |
| controller.tektonPipelinesController.workingdirinitImage.repository | string | `"gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/workingdirinit"` |  |
| controller.tektonPipelinesController.workingdirinitImage.tag | string | `"v0.37.2"` |  |
| controller.type | string | `"ClusterIP"` |  |
| featureFlags.disableAffinityAssistant | string | `"false"` |  |
| featureFlags.disableCredsInit | string | `"false"` |  |
| featureFlags.enableApiFields | string | `"stable"` |  |
| featureFlags.enableCustomTasks | string | `"false"` |  |
| featureFlags.enableTektonOciBundles | string | `"false"` |  |
| featureFlags.requireGitSshSecretKnownHosts | string | `"false"` |  |
| featureFlags.runningInEnvironmentWithInjectedSidecars | string | `"true"` |  |
| featureFlags.sendCloudeventsForRuns | string | `"false"` |  |
| kubernetesClusterDomain | string | `"cluster.local"` |  |
| pipelinesInfo.version | string | `"v0.37.2"` |  |
| webhook.ports[0].name | string | `"http-metrics"` |  |
| webhook.ports[0].port | int | `9090` |  |
| webhook.ports[0].targetPort | int | `9090` |  |
| webhook.ports[1].name | string | `"http-profiling"` |  |
| webhook.ports[1].port | int | `8008` |  |
| webhook.ports[1].targetPort | int | `8008` |  |
| webhook.ports[2].name | string | `"https-webhook"` |  |
| webhook.ports[2].port | int | `443` |  |
| webhook.ports[2].targetPort | int | `8443` |  |
| webhook.ports[3].name | string | `"probes"` |  |
| webhook.ports[3].port | int | `8080` |  |
| webhook.ports[3].targetPort | int | `0` |  |
| webhook.replicas | int | `1` |  |
| webhook.type | string | `"ClusterIP"` |  |
| webhook.webhook.image.repository | string | `"gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/webhook"` |  |
| webhook.webhook.image.tag | string | `"v0.37.2"` |  |
| webhook.webhook.resources.limits.cpu | string | `"500m"` |  |
| webhook.webhook.resources.limits.memory | string | `"500Mi"` |  |
| webhook.webhook.resources.requests.cpu | string | `"100m"` |  |
| webhook.webhook.resources.requests.memory | string | `"100Mi"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.10.0](https://github.com/norwoodj/helm-docs/releases/v1.10.0)
