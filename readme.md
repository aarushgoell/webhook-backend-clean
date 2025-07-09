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

```json
{
  "event": "PULL_REQUEST",
  "author": "aarushgoell",
  "from_branch": "feature-2",
  "to_branch": "main",
  "timestamp": "10 July 2025 - 12:30 PM IST"
}
📌 Webhook Format Examples
Push
"Aarush" pushed to "main" on 10 July 2025 - 01:00 PM IST

Pull Request
"Aarush" submitted a pull request from "feature" to "main" on 10 July 2025 - 01:05 PM IST

Merge (bonus)
"Aarush" merged branch "dev" to "main" on 10 July 2025 - 01:10 PM IST

🖥️ Local Setup Instructions
1. Clone the Repo

git clone https://github.com/aarushgoell/webhook-backend-clean.git
cd webhook-repo
2. Create Virtual Environment

python -m venv venv
.\venv\Scripts\activate
3. Install Dependencies

pip install -r requirements.txt

4. Add .env File
Create a .env file:

MONGO_URL=your_mongodb_connection_string
5. Run Flask App

python app.py
6. Start Frontend (if inside same repo)

cd client
npm install
npm start
🧪 Testing Webhooks Locally
Use ngrok to expose your local Flask server:


ngrok http 5000
Copy the ngrok URL and set it as the webhook URL in your action-repo settings on GitHub.

☁️ Hosting
Frontend: Vercel

✅ Submission Checklist
 Webhook events handled

 Timestamp in IST

 Data shown in UI

 MongoDB schema correct

 Hosted links ready

 Bonus: Merge event handled

🙋 About
This project was built as part of an internship application assignment to demonstrate:

Full-stack development skills

GitHub integration via webhooks

Real-time data processing

Deployment knowledge

🔗 Related Repositories
Webhook Listener (this repo): https://github.com/aarushgoell/webhook-backend-clean

Triggering Repo (GitHub Actions): https://github.com/aarushgoell/action-repo

💡 Built with 💙 by Aarush Goel — Ready to learn and contribute.
```
