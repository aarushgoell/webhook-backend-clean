# Webhook Repo

This repo receives GitHub webhooks (push, pull_request, merge), stores them in MongoDB,
and shows real-time updates in a React UI that polls every 15s.

## Features
- Flask backend (`/webhook`, `/events`)
- MongoDB Atlas integration
- React frontend using Tailwind CSS
- Live UI polling every 15 seconds
- Supports: push, pull request, (merge as bonus)

## How to Run
1. Clone this repo
2. Create `.env` with your MongoDB URL
3. Run backend: `python app.py`
4. Start frontend: `npm start` inside `/client`
