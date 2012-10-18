import flask 
from flask import Flask
import json
import pprint

app = Flask(__name__)
app.debug = True 


@app.route("/tripOffer", methods=['POST'])
def tripOfferPost():
	return dumpJsonFile('get_userById.json')

@app.route("/tripOffer", methods=['GET'])
@app.route("/tripOffer/<tripOfferId>", methods=['GET','PUT'])
def tripOfferGetvar(tripOfferId=0):
	if tripOfferId == 0:
		return dumpJsonFile('get_tripOffers.json')


	return dumpJsonFile('get_tripOfferById.json')

@app.route("/tripRequest")
def tripRequest():
	return dumpJsonFIle('get_tripRequest.json')




@app.errorhandler(404)
def page_not_found(error):
	content = {"status": "error","message":"This is a wrong request or the request isn't created yet"}
	return json.dumps(content)


def dumpJsonFile(filename):
	json_data=open('json/'+filename)
	data = json.load(json_data)
	return json.dumps(data)

if __name__ == "__main__":
	app.run()
