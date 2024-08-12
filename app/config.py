import os

class Config:
    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    MONGO_URI = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@cluster0.xmwiiwq.mongodb.net/payment_details?retryWrites=true&w=majority"