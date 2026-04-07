# 🚀 Real-Time Log Anomaly Detection System (DevOps + AI)

A full-stack project that detects anomalies in system logs using Machine Learning and deploys it using DevOps practices.

---

# 🧠 Overview

This system:

* Detects anomalies in logs using **Isolation Forest**
* Provides a **FastAPI backend**
* Is **Dockerized for deployment**
* Includes a **Frontend dashboard**
* Logs predictions and generates alerts
* Uses **CI/CD (GitHub Actions)** for automation

---

# 🏗️ Project Structure

```
.
├── app.py                  # FastAPI backend
├── train.py                # Model training
├── generate_logs.py        # Data generation
├── simulate_logs.py        # Real-time simulation
├── dashboard.py            # Visualization
├── index.html              # Frontend UI
├── requirements.txt        # Dependencies
├── Dockerfile              # Docker setup
└── .github/workflows/ci.yml # CI/CD pipeline
```

---

# ⚙️ Prerequisites

Make sure you have installed:

* Python (3.9+)
* pip
* Git
* Docker (optional but recommended)
* VS Code (recommended)

---

# 🚀 STEP-BY-STEP SETUP GUIDE

---

## 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/<your-username>/log-anomaly-devops.git
cd log-anomaly-devops
```

---

## 🔹 Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔹 Step 3: Generate Dataset

```bash
python generate_logs.py
```

👉 Creates:

```
logs.csv
```

---

## 🔹 Step 4: Train Model

```bash
python train.py
```

👉 Creates:

```
model.pkl
```

---

## 🔹 Step 5: Run Backend (Without Docker)

```bash
uvicorn app:app --reload
```

👉 Open:

```
http://127.0.0.1:8000/docs
```

---

## 🔹 Step 6: Test API

Example input:

```json
{
  "response_time": 700,
  "error_rate": 0.9
}
```

---

## 🔹 Step 7: Run Frontend

Open:

```
index.html
```

👉 Features:

* Input logs
* Get prediction
* View live stats
* See graph

---

## 🔹 Step 8: Run Simulation (Optional)

```bash
python simulate_logs.py
```

👉 Generates real-time logs automatically

---

## 🔹 Step 9: Run Dashboard (Optional)

```bash
python dashboard.py
```

👉 Shows anomaly distribution graph

---

# 🐳 DOCKER SETUP (OPTIONAL)

---

## 🔹 Build Image

```bash
docker build -t log-anomaly .
```

---

## 🔹 Run Container

```bash
docker run -p 8000:8000 log-anomaly
```

---

## 🔹 With Live Code Updates

```bash
docker run -p 8000:8000 -v ${PWD}:/app log-anomaly
```

---

# 🔄 CI/CD PIPELINE

This project uses **GitHub Actions**.

### Trigger:

* Runs automatically on every push

### What it does:

* Installs dependencies
* Validates the app

👉 Check in GitHub:

```
Actions tab → CI Pipeline
```

---

# 📊 API ENDPOINTS

| Endpoint   | Description           |
| ---------- | --------------------- |
| `/predict` | Detect anomaly        |
| `/stats`   | Get system statistics |

---

# 🧪 Example Inputs

### Normal

```json
{
  "response_time": 150,
  "error_rate": 0.05
}
```

### Anomaly

```json
{
  "response_time": 800,
  "error_rate": 0.9
}
```

---

# 📁 Output Files

| File                | Purpose               |
| ------------------- | --------------------- |
| predictions_log.csv | Stores all logs       |
| alerts.txt          | Stores anomaly alerts |

---

# ⚠️ Common Issues & Fixes

---

### ❌ CORS Error

👉 Enable CORS in FastAPI

---

### ❌ CSV not updating

👉 Use Docker volume mapping OR `/stats`

---

### ❌ CI failed

👉 Handle missing `model.pkl`

---

### ❌ Docker build slow

👉 Network issue → reuse image

---

# 🧠 Concepts Covered

* Machine Learning (Isolation Forest)
* FastAPI (Backend)
* Docker (Containerization)
* CI/CD (GitHub Actions)
* Frontend Integration
* Logging & Monitoring

---

# 🚀 Future Improvements

* Deploy to cloud (AWS/GCP)
* Add authentication
* Use Kafka for streaming
* Integrate Grafana

---

# 🏁 Conclusion

This project demonstrates a **complete DevOps pipeline for AI deployment**, integrating model training, deployment, monitoring, and automation.

---

# 👨‍💻 Author

Your Name

---

⭐ If you found this useful, consider giving a star!
