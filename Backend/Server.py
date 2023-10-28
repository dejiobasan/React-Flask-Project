from flask import Flask

app = Flask(__name__)

@app.route("/Users", methods=['GET'])
def get_users():
    return {"Users": ["User1", "User2", "User3"]}

if __name__ == "__main__":
    app.run(debug=True, port=8000)