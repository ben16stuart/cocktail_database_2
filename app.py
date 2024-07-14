from flask import Flask, request, jsonify
import os
import supabase

app = Flask(__name__)

# Initialize Supabase client
app.config['SUPABASE_URL'] = os.getenv('SUPABASE_URL')
app.config['SUPABASE_KEY'] = os.getenv('SUPABASE_KEY')

supabase_client = supabase.create_client(app.config['SUPABASE_URL'], app.config['SUPABASE_KEY'])

@app.route('/drinks', methods=['GET', 'POST'])
def drinks():
    if request.method == 'POST':
        data = request.json
        response = supabase.table('drinks').insert(data).execute()
        return jsonify(response.data), 201
    else:
        response = supabase.table('drinks').select('*').execute()
        return jsonify(response.data), 200

@app.route('/drinks/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def drink(id):
    if request.method == 'GET':
        response = supabase.table('drinks').select('*').eq('id', id).execute()
        return jsonify(response.data), 200
    elif request.method == 'PUT':
        data = request.json
        response = supabase.table('drinks').update(data).eq('id', id).execute()
        return jsonify(response.data), 200
    elif request.method == 'DELETE':
        response = supabase.table('drinks').delete().eq('id', id).execute()
        return jsonify(response.data), 204

if __name__ == '__main__':
    app.run(debug=True)
