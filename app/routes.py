from app import app, db

@app.route("/")
def index():
    return "Welcome to Spendy.AI!"

@app.route("/add", methods=["POST"])
def add_data():
    sample_data = {"item": "Sample Item", "price": 100}
    db["expenses"].insert_one(sample_data)
    return "Data added!"

@app.route("/view", methods=["GET"])
def view_data():
    data = list(db["expenses"].find())
    return {"expenses": data}
