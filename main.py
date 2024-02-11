from flask import Flask, jsonify;
from populate_bot import task_populate_bot;

app = Flask(__name__, static_folder='./static')

@app.route('/')
def get_home():
    task_populate_bot()
    
    return jsonify({ 
        'success': True,
        'message': 'Working' 
    }), 200

if __name__ == '__main__':
    app.run(debug=True)