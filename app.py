from flask import Flask, jsonify, render_template, redirect
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)
client = MongoClient("mongodb://127.0.0.1:27017")
db = client.pokemon_db
pokemon_collection = db.pokemon
initial_pokemon = [pokemon for pokemon in pokemon_collection.find()]
card_collection = db.cards
initial_card = [card for card in card_collection.find()]





@app.route('/api/pokemon/<pokemon>',methods=['GET'])
def api_pokemon(pokemon):
    pokemon = pokemon_collection.find({'pokemon_name': pokemon})
    json_dump = list(pokemon)
    if pokemon.count() == 0 :
        return jsonify({'pokemon':None})
    return jsonify(dumps(json_dump))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', pokemon_data=initial_pokemon)

@app.route('/pokemon/<pokemon>',methods=['GET'])
def get_pokemon(pokemon):
    pokemon = pokemon_collection.find({'pokemon_name': pokemon})
    if pokemon.count() == 0 :
        return jsonify({'pokemon':None})
    return render_template('pokemon.html', pokemon_data=pokemon)

@app.route('/card/<card>',methods=['GET'])
def get_card(card):
    card = card_collection.find({'card_id': card})
    if card.count() == 0 :
        return jsonify({'card':None})
    return render_template('card.html', card_data=card)

@app.route('/api/card/<card>',methods=['GET'])
def api_card(card):
    card = card_collection.find({'card_id': card})
    json_dump = list(card)
    if card.count() == 0 :
        return jsonify({'card':None})
    return jsonify(dumps(json_dump))

if __name__ == '__main__':
    app.run(debug=True)
