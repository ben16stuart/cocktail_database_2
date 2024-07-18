from flask import Flask, request, jsonify
from supabase import create_client
from dotenv import load_dotenv
import os
import random

load_dotenv()

app = Flask(__name__)

# Initialize Supabase client
app.config['SUPABASE_URL'] = os.getenv('SUPABASE_URL')
app.config['SUPABASE_KEY'] = os.getenv('SUPABASE_KEY')

supabase_client = create_client(app.config['SUPABASE_URL'], app.config['SUPABASE_KEY'])

@app.route('/random-drink', methods=['GET'])
def random_drink():
    drinks = supabase_client.table('drinks').select('*').execute()
    if drinks.data:
        random_drink = random.choice(drinks.data)
        return jsonify(random_drink), 200
    return jsonify({"error": "No drinks found"}), 404

@app.route('/search-drinks', methods=['GET'])
def search_drinks():
    query = request.args.get('query')
    if query:
        drinks = supabase_client.table('drinks').select('*').ilike('name', f'%{query}%').execute()
        return jsonify(drinks.data), 200
    return jsonify({"error": "Query parameter is required"}), 400

@app.route('/generate-drink', methods=['GET'])
def generate_drink():
    drinks = supabase_client.table('drinks').select('*').execute()
    if drinks.data:
        random_drink = random.choice(drinks.data)
        return jsonify(random_drink), 200
    return jsonify({"error": "No drinks found"}), 404

@app.route('/drinks', methods=['POST'])
def add_drink():
    data = request.json
    response = supabase_client.table('drinks').insert(data).execute()
    return jsonify(response.data), 201

if __name__ == '__main__':
    app.run(debug=True)
