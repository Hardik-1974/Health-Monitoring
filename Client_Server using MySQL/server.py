from flask import Flask, request
import utils.execute as execute

# create server
server = Flask(__name__)

@server.route('/', methods = ['GET'])
def homepage():
    return "Welcome to Fitness Management"

@server.route('/add', methods = ['POST'])
def add_information():
    # get all data from form of request
    name  = request.form.get('name')
    if not name:
            return "Name is required", 400
    age   = request.form.get('age')
    city  = request.form.get('city')
    steps = request.form.get('steps')
    Pulse = request.form.get('Pulse')
    Blood_Oxygenation = request.form.get('Blood_Oxygenation')
    Body_Temperature = request.form.get('Body_Temperature')
    
    print(name,age,city,steps,Pulse,Blood_Oxygenation, Body_Temperature);
    # create a query
    query = (
        f"INSERT INTO Health (name, age, city, steps, Pulse, Blood_Oxygenation, Body_Temperature)"
        f"VALUES ('{name}', {age if age else 'NULL'}, '{city}', {steps if steps else 'NULL'},"
        f"{Pulse if Pulse else 'NULL'}, {Blood_Oxygenation if Blood_Oxygenation else 'NULL'},"
        f"{Body_Temperature if Body_Temperature else 'NULL'});"
    )

    # execute the query
    execute.execute_query(query)

    # send response to client
    return "Person details succesfully insert"

@server.route('/all', methods = ['GET'])
def person_health():
    # create a query
    query = f"select * from Health;"

    # execute the query
    persons = execute.execute_select_query(query=query)

    # return all records of persons to client
    return persons

@server.route('/info', methods = ['GET'])
def single_info():
    # create a query
    name=request.form.get('name')
    if not name :
         return "Name is required",400
    query = f"select * from Health where name='{name}';"

    # execute the query
    persons = execute.execute_select_query(query=query)

    # return all records of persons to client
    return persons

@server.route('/update', methods = ['PUT'])
def update_person():
    name  = request.form.get('name')
    city  = request.form.get('city')
    if not name or city:
        return "Name and City are required",400
    # create a query
    query = f"update persons SET city = '{city}' where name = '{name}';"

    # execute the query
    execute.execute_query(query)

    # give response to the client
    return f"Person's City with name {name} is updated",200

@server.route('/step', methods = ['GET'])
def max_Steps():
    # request.form.get('steps')

    query = "SELECT * FROM Health WHERE steps = (SELECT MAX(steps) FROM Health);"

    execute.execute_query(query=query)

    return f"Details of person with max steps are {max}"

# execute server
if __name__ == '__main__':
    server.run(host = "0.0.0.0", debug = True)