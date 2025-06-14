# 🚀 NetWit AI – Smart Email Automation with AI ✉️💡

![NetWit Banner](https://img.shields.io/badge/Smart%20Email%20AI-FastAPI%20%7C%20React%20%7C%20LLM-blueviolet?style=flat-square)

**NetWit AI** is a fullstack intelligent application that automates hyper-personalized email outreach.  
Just upload a list of emails, and NetWit will:
- Extract contact details
- Scrape business websites
- Analyze them with AI
- Generate stylish HTML emails
- Send & track everything — fully automated!

---

## 🌟 Features

✅ Upload CSV of email contacts  
✅ Smart name & domain parsing  
✅ Company website scraping  
✅ Business summarization with LLM (Together.ai)  
✅ Auto-generated personalized HTML email  
✅ SendGrid-powered delivery  
✅ 📈 Dashboard with Sent / Failed / Opened / Clicked stats  
✅ Email preview modal  
✅ Error logging & local analytics  

---

## 🧠 Tech Stack

| Layer        | Tech                        |
|-------------|-----------------------------|
| Backend      | Python, FastAPI             |
| Frontend     | React, Axios, Chart.js      |
| AI/LLM       | Together.ai (LLaMA-3)       |
| Email        | SendGrid API                |
| Templating   | Jinja2                      |
| Storage      | CSV + Local Logs            |
| Deployment   | Uvicorn + Node              |

---

## 🔧 How It Works

1. 📤 Upload a `.csv` with emails
2. ✂️ Smart parser extracts names and domains
3. 🌐 Site scraper visits company domain
4. 🧠 Together.ai summarizes business + issues
5. 💌 Email is generated with personalized HTML
6. 📤 Email sent via SendGrid
7. 📊 Dashboard shows delivery stats

---

## 🖼️ Screenshots

> 📥 Upload CSV | 📬 Email Preview | 📈 Analytics Chart

| Upload CSV | Preview Email | Dashboard |
|------------|----------------|------------|
| ![upload](https://via.placeholder.com/250x120.png?text=Upload+CSV) | ![preview](https://via.placeholder.com/250x120.png?text=Email+Preview) | ![dashboard](https://via.placeholder.com/250x120.png?text=Analytics+Chart) |

---

## 🚀 Getting Started

### 🔹 Backend (Python + FastAPI)

```bash
cd netwit_ai
python -m venv .venv
# Activate virtual environment:
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

# Set your API keys in .env:
TOGETHER_API_KEY=your_together_api_key
SENDGRID_API_KEY=your_sendgrid_api_key

uvicorn backend.app:app --reload
```

![Banner](https://yourimageurl.com/banner.gif)




