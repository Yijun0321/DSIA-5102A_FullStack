from flask import Flask, jsonify, request
from flask_cors import CORS
from pydantic import BaseModel

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return jsonify({"title": "Hello from api!"})


class Pokemon(BaseModel):
    Index : int
    Name : str
    Type : str
    Category : str
    Contest : str
    PP : int
    Power : int
    Accuracy : int
    Generation : int

Pokemon1 = Pokemon(Index=1, Name="Pound", Type="Normal", Category="Physical", Contest="Tough", PP=35, Power=40, Accuracy=100, Generation=1)

@app.route("/Pokemon", methods=["POST"])
def print_job():
    Index = request.json["Index"]
    Name = request.json["Name"]
    Type = request.json["Type"]
    Category = request.json["Category"]
    Contest = request.json["Contest"]
    PP = request.json["PP"]
    Power = request.json["Power"]
    Accuracy = request.json["Accuracy"]
    Generation = request.json["Generation"]
    result = {"Index": f"Index : {Index} Name : {Name} Type : {Type} Category : {Category} Contest : {Contest} PP : {PP} Power : {Power} Accuracy : {Accuracy} Generation : {Generation} "}
    return jsonify(result)

@app.get("/Pokemon1")
def pokemon1_get():
    return {"Pokemon 1": Pokemon1}

@app.get("/Pokemon/{Index}")
def pokemon_get(Index:int, Name:str = None, Type : str = None, Category : str = None, Contest : str = None, PP : int = None, Power : int = None, Accuracy : int = None, Generation : int = None):
    return {"Index": Index, "Name": Name, "Type": Type, "Category": Category, "Contest": Contest, "PP": PP, "Power": Power, "Accuracy": Accuracy, "Generation": Generation}

@app.get("/Equipe")
def equipe_get(Index:int = None, Name:str = None, Type : str = None, Category : str = None, Contest : str = None, PP : int = None, Power : int = None, Accuracy : int = None, Generation : int = None):
    return {"Index": Index, "Name": Name, "Type": Type, "Category": Category, "Contest": Contest, "PP": PP, "Power": Power, "Accuracy": Accuracy, "Generation": Generation}