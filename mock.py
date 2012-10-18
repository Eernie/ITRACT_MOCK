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
@app.route("/tripOffer/<int:tripOfferId>", methods=['GET','PUT'])
def tripOfferGet(tripOfferId=0):
	if tripOfferId == 0:
		return dumpJsonFile('get_tripOffers.json')

	return dumpJsonFile('get_tripOfferById.json')


@app.route("/tripRequest", methods=['POST'])
def tripRequestPost():
	return dumpJsonFIle('get_tripRequestById.json')


@app.route("/tripRequest", methods=['GET'])
@app.route("/tripRequest/<int:tripRequestId>", methods=['GET','PUT'])
def tripRequestGet(tripRequestId=0):
	if tripRequestId == 0:
		return dumpJsonFile('get_tripRequests.json')

	return dumpJsonFile('get_tripRequestById.json')


@app.route("/match/<int:matchId>", methods=['GET','PUT'])
def matchGet(matchId):
	return dumpJsonFile('get_match.json')


@app.route("/user", methods=['POST'])
def userPost():
	return dumpJsonFile('get_userById.json')


@app.route("/user", methods=['GET'])
@app.route("/user/<int:tripOfferId>", methods=['GET','PUT'])
def userGet(tripOfferId=0):
	if userId == 0:
		return dumpJsonFile('get_users.json')

	return dumpJsonFile('get_userById.json')


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
