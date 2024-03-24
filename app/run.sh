#!/bin/bash

# Function that stop second plans jobs this script started when pressing "ctrl+C"
stop_jobs() {
    jobs -p | xargs kill
}

cd backend
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cd ..
python backend/manage.py runserver & 
cd frontend
npm install
npm run dev -- --port 8080 &
wait