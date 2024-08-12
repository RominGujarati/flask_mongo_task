# flask_mongo_task
task using flask and mongo db

This is a simple Flask application that connects to MongoDB Atlas to manage user payments. It provides a RESTful API endpoint to insert user payment data into the `user_payment` collection in MongoDB.

## Features
- POST endpoint to insert user payment data into MongoDB Atlas.
- Configured with Flask and PyMongo for database operations.

## Prerequisites
- Python 3.7 or higher
- MongoDB Atlas account and cluster


## Setup Instructions

1. Clone the Repository
git clone https://github.com/RominGujarati/flask_mongo_task
cd flask_mongo_task

2. Create a Virtual Environment
python -m venv venv
activate the venv

3. Install Dependencies
pip install -r requirements.txt

4. Configure MongoDB Atlas and Update Configuration in .env file accordingly

5. Run the Application
python run.py
