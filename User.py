from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import re

URI = "neo4j+s://488e3958.databases.neo4j.io"
AUTH = ("neo4j", "MCfSaOEihB7Yki5qXfdCnxBxLNUlS2D0GNVc3LrWCqU")


def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()

    return driver



def findUserByUsername(username):
    data = _get_connection().execute_query("MATCH (a:User) where a.username = $username RETURN a;", username=username)
    #hvis det er noe data, opprettes og returneres et objekt User med dataene, ellers opprettes et objekt User med inntastet brukernavn og teksten "not found in DB" som email
    
    if len(data[0]) > 0:
        user = User(username, data[0][0][0]['email'])
        print(type(data))
        print("data 0:",data[0])
        print("data 00:",data[0][0])
        print("data 000:",data[0][0][0])
        print("data 0000:",data[0][0][0]['username'])
        print("data:",data)
        return user
    else:
        return User(username, "Not found in DB")

def findCarByReg(reg):
    with _get_connection().session() as session:
        cars = session.run('MATCH(a:Car) where a.reg=$reg RETURN a;',reg=reg)
        print(cars)
        nodes_json = [node_to_json(record['a'] for record in cars)]
        print(nodes_json)
        return Car(test,test,test,test,test,test,test)
    

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_Username(self):
        return self.username

    def set_Username(self, value):
        self.username = value

    def get_Email(self):
        return self.email

    def set_Email(self, value):
        self.email = value

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

    def get_car_id(self):
        return self.email

    def set_car_id(self, value):
        self.email = value