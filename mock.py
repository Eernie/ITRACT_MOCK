from flask import Flask
import json
import pprint

app = Flask(__name__)
app.debug = True 


@app.route("/tripOffer", methods=['GET'])
def tripOfferGet():
	return dumpJsonFile('get_tripOffers.json')

@app.route("/tripOffer", methods=['POST'])
def tripOfferPost():
	return dumpJsonFile('get_userById.json')

@app.route("/tripOffer/<tripOfferId>", methods=['GET'])
def tripOfferGetvar(tripOfferId):
	return dumpJsonFile('get_tripOfferById.json')


def dumpJsonFile(filename):
	json_data=open('json/'+filename)
	data = json.load(json_data)
	return json.dumps(data)

if __name__ == "__main__":
	app.run()
