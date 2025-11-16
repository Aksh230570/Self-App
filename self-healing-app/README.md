# 🧠 Self-Healing Web Application (DevOps Project)

## 🔧 Tech Stack
- Jenkins
- Docker & Docker Hub
- Kubernetes (Docker Desktop)
- GitHub
- Flask / Node.js
- kubectl CLI
- VS Code

## 🚀 Features
- CI/CD pipeline with Jenkins
- Containerized app via Docker
- Self-healing pods via Kubernetes Liveness & Readiness Probes
- Automatic redeployment from GitHub commits

## 🧩 Steps to Run
1. Clone repo
2. Build Docker image and push to Docker Hub
3. Apply Kubernetes manifests:
   ```bash
   kubectl apply -f k8s/
