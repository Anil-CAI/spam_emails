# 📧 Spam Mail Detector - Mini Project 🚀

![Spam Detector](https://media.giphy.com/media/l3vR85PnGsBwu1PFK/giphy.gif)

## Overview 🎯
This project is a **Spam Mail Detector** built using **FastAPI** for the backend and **HTML/CSS/JavaScript** for the frontend. It utilizes **Logistic Regression** and **TF-IDF Vectorization** to classify emails as **Spam** or **Ham** (not spam).

## Features ✨
- ✅ **FastAPI Backend**: Handles requests for spam detection.
- 🧠 **Machine Learning Model**: Trained using **Logistic Regression** and **TF-IDF Vectorization**.
- 💻 **Web Interface**: A simple and interactive UI to enter email content and check for spam.
- 🔓 **CORS Enabled**: Allows cross-origin requests for seamless frontend-backend interaction.

## Tech Stack 🛠️
- **Backend**: FastAPI, Pandas, Scikit-Learn
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Logistic Regression with TF-IDF Vectorization

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Anil-CAI/spam_mail.git
cd spam_mail
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the FastAPI Server 🏃‍♂️
```bash
uvicorn dub:app --reload
```
Server will start at: `http://127.0.0.1:8000`

### 4️⃣ Open the Frontend 🌐
Open `index.html` in your browser and enter an email message to check for spam.

## 🎯 API Endpoint

### **Spam Detection Endpoint**
📌 **URL**: `POST http://127.0.0.1:8000/predict`
- **Request Body (JSON)**:
  ```json
  {
    "message": "Your email content here..."
  }
  ```
- **Response**:
  ```json
  {
    "prediction": "ham" // or "spam"
  }
  ```

## 📊 Dataset
The dataset (`mail_data.csv`) contains email messages labeled as **spam** or **ham**.

## 📂 Folder Structure
```
📁 spam-mail-detector
├── 📝 dub.py          # FastAPI backend with ML model
├── 🌍 index.html      # Frontend UI
├── 📊 mail_data.csv   # Dataset for training
├── 📜 requirements.txt # Required dependencies
├── 📖 README.md       # Project documentation
```

## 🎯 Future Enhancements
- 🚀 Improve model accuracy with advanced NLP techniques
- 🌎 Deploy the project on **Netlify** (Frontend) and **Render**/**Heroku** (Backend)
- 🔍 Add support for email subject & metadata analysis

## 📜 License
This project is licensed under the **MIT License**.

---
👨‍💻 Developed by **Anil-Cai** 🚀

![Email Security](https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif)
