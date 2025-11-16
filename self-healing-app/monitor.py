import os, time
print("📊 Monitoring Kubernetes Pods...")
while True:
    os.system("kubectl get pods -o wide")
    time.sleep(10)
