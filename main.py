from flask import Flask, jsonify
import random

app = Flask(__name__)

# Sample list of quotes
quotes = [
    "The only way to odo great work is to love what you do. - steve jobs",
    "success is not final, failure is not fatal  It is the courage to continue that counts. - Winston Churchill",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
]
@app.route('/')
def get_quote():
    # Choose a random quote from the list
    quote = random.choice(quotes)
    return jsonify({'quote': quote})

if __name__ == '__main__':
    app.run(debug=True)
