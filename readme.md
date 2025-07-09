# 🔔 GitHub Webhook Listener – Flask + MongoDB + React

This project receives GitHub webhook events (Push, Pull Request, Merge), stores them in MongoDB, and displays them in real-time via a React frontend.

---

## 🌐 Live Demo

- **Frontend (React + Tailwind)**: (https://webhook-backend-clean.vercel.app/)
- **Backend (Flask API)**: Have to run on local host by python app.py

---

## ⚙️ Tech Stack

| Layer      | Technology                                 |
| ---------- | ------------------------------------------ |
| Frontend   | React, Tailwind CSS                        |
| Backend    | Flask, Python, Flask-CORS                  |
| Database   | MongoDB (Atlas)                            |
| Deployment | Vercel (Frontend), Render (Backend)        |
| Dev Tools  | GitHub Webhooks, Ngrok (for local testing) |

---

## 🚀 Features

- ✅ Handles `push`, `pull_request`, and `merge_group` GitHub events
- ✅ Stores event type, author, branch info, and timestamp
- ✅ Converts timestamps to **Indian Standard Time (IST)**
- ✅ React frontend polls every 15 seconds to show real-time updates
- ✅ Clean, minimal UI with Tailwind styling

---

## 📦 MongoDB Schema

````json
{
  "event": "PULL_REQUEST",
  "author": "aarushgoell",
  "from_branch": "feature-2",
  "to_branch": "main",
  "timestamp": "10 July 2025 - 12:30 PM IST"
}
📌 Webhook Format Examples
## 📌 Webhook Format Examples

### ✅ Push
"Aarush" pushed to "main" on 10 July 2025 - 01:00 PM IST

shell
Copy
Edit

### ✅ Pull Request
"Aarush" submitted a pull request from "feature" to "main" on 10 July 2025 - 01:05 PM IST

shell
Copy
Edit

### ✅ Merge (Bonus)
"Aarush" merged branch "dev" to "main" on 10 July 2025 - 01:10 PM IST

yaml
Copy
Edit

---

## 🖥️ Local Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/aarushgoell/webhook-backend-clean.git
cd webhook-backend-clean
2. Create Virtual Environment
bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add .env File
Create a file named .env with this:

ini
Copy
Edit
MONGO_URL=your_mongodb_connection_string
5. Run Flask App
bash
Copy
Edit
python app.py
6. Start Frontend (if in same repo)
bash
Copy
Edit
cd client
npm install
npm start
🧪 Testing Webhooks Locally
To test GitHub webhooks from your local machine:

Start your backend locally:

bash
Copy
Edit
python app.py
Start a tunnel using ngrok:

bash
Copy
Edit
ngrok http 5000
Copy the ngrok HTTPS URL and set it as the Webhook URL in GitHub under:

Copy
Edit
action-repo → Settings → Webhooks
Example:

arduino
Copy
Edit
https://your-ngrok-id.ngrok-free.app/webhook
☁️ Hosting
Frontend: Deployed using Vercel

Backend: Deployed using Render or Railway

GitHub Webhook sends real data to deployed /webhook endpoint

✅ Submission Checklist
 Webhook events handled (push, pull_request)

 Timestamp converted to IST

 Data saved in MongoDB

 UI shows event updates every 15 seconds

 Hosted backend & frontend

 Bonus: Merge event handled ✅

🙋 About
This project was built as part of an internship assignment to demonstrate:

Full-stack development skills (MERN + Flask)

GitHub webhook integration

Real-time data processing

Deployment and DevOps fundamentals

🔗 Related Repositories
📥 Webhook Listener (Backend + Frontend)
https://github.com/aarushgoell/webhook-backend-clean

⚙️ Triggering Repo (GitHub Actions)
https://github.com/aarushgoell/action-repo

💡 Built with 💙 by Aarush Goel — Ready to learn and contribute.
````
