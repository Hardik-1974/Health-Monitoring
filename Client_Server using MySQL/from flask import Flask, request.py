from flask import Flask, request
import utils.execute as execute

# create server
server = Flask(__name__)

@server.route('/', methods=['GET'])
def homepage():
    return "Welcome to Fitness Management"

@server.route('/add', methods=['POST'])
def add_information():
    name = request.form.get('name')
    if not name:
        return "Name is required", 400

    age = request.form.get('age')
    city = request.form.get('city')
    steps = request.form.get('steps')
    Pulse = request.form.get('Pulse')
    Blood_Oxygenation = request.form.get('Blood_Oxygenation')
    Body_Temperature = request.form.get('Body_Temperature')

    print(name, age, city, steps, Pulse, Blood_Oxygenation, Body_Temperature)

    query = (
        f"INSERT INTO Health (name, age, city, steps, Pulse, Blood_Oxygenation, Body_Temperature) "
        f"VALUES ('{name}', {age if age else 'NULL'}, '{city}', {steps if steps else 'NULL'}, "
        f"{Pulse if Pulse else 'NULL'}, {Blood_Oxygenation if Blood_Oxygenation else 'NULL'}, "
        f"{Body_Temperature if Body_Temperature else 'NULL'});"
    )
    execute.execute_query(query)
    return "Person details added successfully", 201

@server.route('/all', methods=['GET'])
def person_health():
    query = "SELECT * FROM Health;"
    persons = execute.execute_select_query(query=query)
    return persons

@server.route('/info', methods=['GET'])
def single_info():
    name = request.form.get('name')
    if not name:
        return "Name is required", 400

    query = f"SELECT * FROM Health WHERE name='{name}';"
    persons = execute.execute_select_query(query=query)
    return persons

@server.route('/update', methods=['PUT'])
def update_person():
    name = request.form.get('name')
    city = request.form.get('city')
    if not name or not city:
        return "Name and City are required", 400

    query = f"UPDATE Health SET city = '{city}' WHERE name = '{name}';"
    execute.execute_query(query)
    return f"Person's city with name {name} is updated", 200

@server.route('/step', methods=['GET'])
def max_Steps():
    query = "SELECT * FROM Health WHERE steps = (SELECT MAX(steps) FROM Health);"
    persons = execute.execute_select_query(query=query)
    return persons

# execute server
if __name__ == '__main__':
    server.run(host="0.0.0.0", debug=True)
