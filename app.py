from flask import Flask, request, jsonify
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import supabase

app = Flask(__name__)

# Load environment variables from .env file if present
load_dotenv()

# Initialize Supabase client with environment variables
app.config['SUPABASE_URL'] = os.getenv('SUPABASE_URL')
app.config['SUPABASE_KEY'] = os.getenv('SUPABASE_KEY')

supabase_client = create_client(app.config['SUPABASE_URL'], app.config['SUPABASE_KEY'])

@app.route('/drinks', methods=['GET', 'POST'])
def drinks():
    if request.method == 'POST':
        data = request.json
        response = supabase_client.table('drinks').insert(data).execute()
        return jsonify(response.data), 201
    else:
        response = supabase_client.table('drinks').select('*').execute()
        return jsonify(response.data), 200

@app.route('/drinks/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def drink(id):
    if request.method == 'GET':
        response = supabase_client.table('drinks').select('*').eq('id', id).execute()
        return jsonify(response.data), 200
    elif request.method == 'PUT':
        data = request.json
        response = supabase_client.table('drinks').update(data).eq('id', id).execute()
        return jsonify(response.data), 200
    elif request.method == 'DELETE':
        response = supabase_client.table('drinks').delete().eq('id', id).execute()
        return jsonify(response.data), 204

if __name__ == '__main__':
    app.run(debug=True)