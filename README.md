# Configuration-Management-Dashboard



## 🛠️ Configuration Management Dashboard  
**Automating Configuration Across Environments with Ansible**  

![GitHub Repo](https://img.shields.io/badge/Flask-2.0%2B-blue) ![GitHub Repo](https://img.shields.io/badge/Ansible-Automation-red) ![GitHub Repo](https://img.shields.io/badge/IBM%20Cloud-Deployment-green)

### **📌 Overview**  
The **Configuration Management Dashboard** is a web-based tool designed to automate and manage configurations across multiple environments (development, staging, and production) using **Flask, SQLite, and Ansible**.  

It provides an easy-to-use interface for managing configuration files and executing automated deployment tasks.

---

## 🚀 **Features**  
✅ **Centralized Configuration Management**: Easily manage configuration settings across different environments.  
✅ **Ansible Integration**: Automate deployment and configuration using Ansible playbooks.  
✅ **Flask Web Interface**: A simple and user-friendly UI for managing configurations.  
✅ **Database Storage**: Uses **SQLite** to store configuration details.  
✅ **Multi-Environment Support**: Separate configurations for **dev, staging, and prod** environments.  
✅ **IBM Cloud Deployment**: The project is designed to be deployed on **IBM Cloud**.  

---

## 🏗 **Project Structure**  
```plaintext
config-management-dashboard/
│── app/                     # Flask application package
│   ├── __init__.py           # App initialization
│   ├── config.py             # Configuration settings
│   ├── models.py             # Database models
│   ├── routes.py             # API routes
│   ├── services.py           # Business logic services
│   ├── utils.py              # Utility functions
│
│── ansible/                  # Ansible playbooks for automation
│   ├── config_playbook.yml    # Configuration management script
│
│── k8s/                      # Kubernetes deployment files
│   ├── deployment.yml         # Deployment configuration
│   ├── service.yml            # Service definition
│   ├── ingress.yml            # Ingress controller setup
│
│── templates/                 # HTML templates for the UI
│── static/                    # Static assets (CSS, JS, images)
│── migrations/                # Database migrations
│── instance/                  # SQLite database files
│── tests/                     # Unit tests
│── Vagrantfile                 # Vagrant setup
│── requirements.txt            # Python dependencies
│── run.py                      # Application entry point
│── README.md                   # Project documentation
```

---

## 🛠 **Installation & Setup**  

### **1️⃣ Prerequisites**  
Ensure you have the following installed:  
🔹 Python (3.8+)  
🔹 Flask  
🔹 SQLite  
🔹 Ansible  
🔹 IBM Cloud CLI (for deployment)  

### **2️⃣ Clone the Repository**  
```sh
git clone https://github.com/Almas-Farha/Configuration-Management-Dashboard.git
cd Configuration-Management-Dashboard
```

### **3️⃣ Create a Virtual Environment**  
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **4️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **5️⃣ Set Up the Database**  
```sh
python check_tables.py  # Creates necessary tables
```

### **6️⃣ Run the Application**  
```sh
python run.py
```
Your Flask app should now be running on **`http://127.0.0.1:5000/`** 🎉

---

## 🚀 **Deploying on IBM Cloud**  
To deploy this project on **IBM Cloud**, follow these steps:  

1️⃣ Login to IBM Cloud:  
```sh
ibmcloud login
```
2️⃣ Set up a container registry:  
```sh
ibmcloud cr namespace-add <your-namespace>
```
3️⃣ Build and push Docker image:  
```sh
docker build -t <your-image-name> .
docker tag <your-image-name> <your-namespace>/<your-image-name>
docker push <your-namespace>/<your-image-name>
```
4️⃣ Deploy using Kubernetes:  
```sh
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml
kubectl apply -f k8s/ingress.yml
```

---

## 🛠 **Usage**  
- **Add a new configuration** via the UI  
- **View and manage stored configurations**  
- **Run Ansible playbooks** to automate deployments  
- **Monitor configuration changes** across environments  

---

## 📌 **Future Improvements**  
🚀 Add user authentication and role-based access  
🚀 Implement logging and monitoring  
🚀 Enhance UI with a more modern frontend framework  

---

## 🤝 **Contributing**  
Contributions are welcome! 🎉  
Feel free to fork this repository and submit a pull request with improvements.

---

## 📜 **License**  
This project is licensed under the **MIT License**.  

---

## ⭐ **Show Your Support**  
If you find this project useful, **please give it a star ⭐ on GitHub!** 😊  

---

