from flask import Flask, request, jsonify
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Initialize Supabase client
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/add_drink', methods=['POST'])
def add_drink():
    data = request.json
    response = supabase_client.table('drinks').insert(data).execute()
    return jsonify(response.data), 201

@app.route('/list_drinks', methods=['GET'])
def list_drinks():
    response = supabase_client.table('drinks').select('*').execute()
    return jsonify(response.data), 200

if __name__ == '__main__':
    app.run(debug=True)
