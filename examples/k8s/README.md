# Kubernetes example for showcase-3d-printer-anomaly-detection

Add repos:

```shell
helm repo add ihbr https://innovation-hub-bergisches-rheinland.github.io/helm-charts
helm repo add bitnami https://charts.bitnami.com/bitnami
```

Run the example:

```shell
# Create the namespace
kubectl create namespace showcase-3d-printer-anomaly-detection
# Create a config map
kubectl -n showcase-3d-printer-anomaly-detection create -f ./configmap.yaml
# Install Kafka
helm -n showcase-3d-printer-anomaly-detection install --set service.port=9094 --set service.externalPort=9092 kafka bitnami/kafka
# Install anomaly detection
helm -n showcase-3d-printer-anomaly-detection install --set config.existingConfigMap=showcase-3d-printer-anomaly-detection --set image.pullPolicy=Always --set resources.limits.cpu=1000m --set resources.limits.memory=256Mi --set resources.requests.cpu=100m --set resources.requests.memory=256Mi showcase-3d-printer-anomaly-detection showcase-3d-printer-anomaly-detection/showcase-3d-printer-anomaly-detection
```

Remove the example:

```
kubectl delete namespace showcase-3d-printer-anomaly-detection
```
