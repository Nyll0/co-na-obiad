from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Import CORS
import sqlite3
import random

app = Flask(__name__)
CORS(app) 

def get_db_connection():
    conn = sqlite3.connect('lunch_options.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_lunch', methods=['POST'])
def get_lunch():
    data = request.json
    diet = data.get('diet')
    cuisine = data.get('cuisine')
    budget = data.get('budget')

    print('Received request with:', data)

    conn = get_db_connection()
    query = "SELECT * FROM lunch_options WHERE 1=1"
    params = []

    if diet and diet != 'none':
        query += " AND diet = ?"
        params.append(diet)
    if cuisine and cuisine != 'none':
        query += " AND cuisine = ?"
        params.append(cuisine)
    if budget and budget != 'none':
        query += " AND budget = ?"
        params.append(budget)

    results = conn.execute(query, params).fetchall()
    conn.close()

    if results:
        lunch = random.choice(results)
        response = {
            'name': lunch['name'],
            'diet': lunch['diet'],
            'cuisine': lunch['cuisine'],
            'budget': lunch['budget'],
            'image_url': lunch['image_url'], 
            'recipe_url': lunch['recipe_url']
        }
        print('Responding with:', response)
        return jsonify(response)
    else:
        return jsonify({'error': 'No options available for the given preferences.'})

if __name__ == '__main__':
    app.run(debug=True)
