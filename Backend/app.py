from flask import Flask, render_template, request, jsonify
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, '..', 'frontend', 'templates'),
            static_folder=os.path.join(BASE_DIR, '..', 'frontend', 'static'))

def get_bot_response(user_message):
    try:
        message = user_message.lower().strip()

        if message in ["hi", "hello", "hey"]:
            return "Hello 👋 How can I help you today?"
        
        elif "how are you" in message:
            return "I'm doing great 😊"
        
        elif message == "bye":
            return "Goodbye 👋"
        
        else:
            return "I didn't understand that."
    
    except Exception as e:
        return "Something went wrong. Please try again."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    try:
        user_message = request.json["message"]
        bot_response = get_bot_response(user_message)
        return jsonify({"response": bot_response})
    except Exception as e:
        return jsonify({"response": "Error processing request."})

if __name__ == "__main__":
    app.run(debug=True)
