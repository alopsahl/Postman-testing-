from neo4j import GraphDatabase,Driver, AsyncGraphDatabase, AsyncDriver
import json
URI = "neo4j+s://488e3958.databases.neo4j.io"
AUTH = ("neo4j", "MCfSaOEihB7Yki5qXfdCnxBxLNUlS2D0GNVc3LrWCqU")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI,auth=AUTH)
    driver.verify_connectivity()
    return driver

def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties

#Car functions

def findAllCars():
    with _get_connection().session() as session:
        cars = session.run('MATCH (a:Car) RETURN a;')
        nodes_json = [node_to_json(record['a']) for record in cars]
        print(nodes_json)
        return nodes_json

def findCarByReg(reg):
    with _get_connection().session() as session:
        cars = session.run('MATCH(a:Car) where a.reg=$reg RETURN a;',reg=reg)
        print(cars)
        nodes_json = [node_to_json(record['a'] for record in cars)]
        print(nodes_json)
        return nodes_json
    
    
def save_car(make, model, reg, year, capacity):

    cars= _get_connection().execute_query('MERGE (a:car{make: $make, model: @model, reg: $reg, year: $year,capacity: $capacity})RETURN a;'
                                          , make = make, model = model, reg = reg, year = year, capacity = capacity)

    nodes_json = [node_to_json(record['a'] for record in cars)]
    print(nodes_json)
    return nodes_json

def update_car(make,model,reg,year,capacity):
    with _get_connection().session() as session:

        cars = session.run('MATCH (a:car{reg: $reg} set a.make=$make, a.model = $model, a.year = $year, a.capacity = $capacity RETURN a;'
                                          , make = make, model = model, reg = reg, year = year, capacity = capacity)
        
        print(cars)
        nodes_json = [node_to_json(record['a']) for record in cars]

        print(nodes_json)
        return nodes_json
    
def delete_car(reg):
    _get_connection().execute_query('MATCH(a:Car{reg:$reg}) delete a;',reg = reg)

#Customer functions

def findAllCustomers():
    with _get_connection().session() as session:
        customers = session.run('MATCH (a:Customer) RETURN a;')
        nodes_json = [node_to_json(record['a']) for record in customers]
        print(nodes_json)
        return nodes_json

#employees

def findAllEmployees():
    with _get_connection().session() as session:
        employees = session.run('MATCH (a:Employee) RETURN a;')
        nodes_json = [node_to_json(record['a']) for record in employees]
        print(nodes_json)
        return nodes_json
    

#Business endpoints

#def order_car(customer_id,car_id):

class Car:
    def __init__(self, car_id, make, model, reg, year, capacity, status):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.reg = reg
        self.year = year
        self.capacity = capacity
        self. status = status
        
    def get_Make(self):
        return self.make

    def set_Make(self, value):
        self.make = value

    def get_Email(self):
        return self.email

    def set_Email(self, value):
        self.email = value


class Customer:
    def __init__(self, customer_id, name, age, address):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.address = address

    def get_customer_id(self):
        return self.customer_id
    
    def set_customer_id(self, value):
        self.name = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_age(self):
        return self.age

    def set_age(self, value):
        self.age = value

    def get_address(self):
        return self.address

    def set_address(self, value):
        self.address = value

class Employee:
    def __init__(self, employee_id, name, address,branch):
        self.employee_id = employee_id
        self.name = name
        self.address = address
        self.branch = branch

    def get_employee_id(self):
        return self.customer_id
    
    def set_get_employee_id(self, value):
        self.customer_id = value

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_address(self):
        return self.address

    def set_address(self, value):
        self.address = value

    def get_branch(self):
        return self.branch

    def set_branch(self, value):
        self.branch = value