from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    # Indentation is required here
    return "Welcome to my Flask API!"

@app.route('/student')
def get_student():
    # Indentation is required here
    return jsonify({
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    })

# This part tells Python to run the app when you execute the script
if __name__ == '__main__':
    app.run(debug=True)
