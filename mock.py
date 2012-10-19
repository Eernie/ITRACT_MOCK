import flask 
from flask import Flask, request
import json
import pprint

app = Flask(__name__)
app.debug = True 


def controleValidAttributes(formAttributes):
	for attribute in formAttributes:
		if not request.args.get(attribute):
			return abort(400)


@app.route("/tripOffer", methods=['POST'])
def tripOfferPost():
	formAttributes = {'user','origin_long', 'origin_lat', 
					'origin_window', 'destination_long', 'destination_lat', 'destination_window', 
					'start_time_min', 'start_time_max', 'end_time_min', 'end_time_max', 'numberOfSeats'}
	if request.method == 'PUT':
		controleValidAttributes(formAttributes)	 
	return dumpJsonFile('get_userById.json')


@app.route("/tripOffer", methods=['GET'])
@app.route("/tripOffer/<int:tripOfferId>", methods=['GET','PUT'])
def tripOfferGet(tripOfferId=0):
	if tripOfferId == 0:
		return dumpJsonFile('get_tripOffers.json')

	formAttributes = {'destination_long','destination_lat','numberOfSeats'}
	if request.method == 'PUT':
		controleValidAttributes(formAttributes)	 
	return dumpJsonFile('get_tripOfferById.json')



@app.route("/tripRequest", methods=['POST'])
def tripRequestPost():
	formAttributes = {'user','origin_long','origin_lat','origin_window','destination_long',
										'destination_lat','destination_window','start_time_min','start_time_max',
										'end_time_min','end_time_max','numberOfSeats'}
	if request.method == 'PUT':
		controleValidAttributes(formAttributes)	 
	return dumpJsonFIle('get_tripRequestById.json')




@app.route("/tripRequest", methods=['GET'])
@app.route("/tripRequest/<int:tripRequestId>", methods=['GET','PUT'])
def tripRequestGet(tripRequestId=0):
	if tripRequestId == 0:
		return dumpJsonFile('get_tripRequests.json')
	formAttributes = {'origin_long','origin_lat','origin_window','destination_long','destination_lat',
										'destination_window','start_time_min','start_time_max','end_time_min','end_time_max',
										'numberOfSeats'}
	if request.method == 'PUT':
		controleValidAttributes(formAttributes)	 
	return dumpJsonFile('get_tripRequestById.json')


@app.route("/match/<int:matchId>", methods=['GET','PUT'])
def matchGet(matchId):
	formAttributes = {'confirm','rating'}
	if request.method == 'PUT':
		controleValidAttributes(formAttributes)	 
	return dumpJsonFile('get_match.json')


@app.route("/user", methods=['POST'])
def userPost():
	formAttributes = {'name'}
	if request.method == 'PUT':
		controleValidAttributes(formAttributes)	 
	return dumpJsonFile('get_userById.json')


@app.route("/user", methods=['GET'])
@app.route("/user/<int:userId>", methods=['GET','PUT'])
def userGet(userId=0):
	if userId == 0:
		return dumpJsonFile('get_users.json')
	formAttributes = {'name'}
	if request.method == 'PUT':
		controleValidAttributes(formAttributes)	 
	return dumpJsonFile('get_userById.json')



@app.errorhandler(404)
@app.errorhandler(405)
def page_not_found(error):
	content = {"status": "error","message":"This is a wrong request or the request isn't created (yet)"}
	return json.dumps(content)


def dumpJsonFile(filename):
	json_data=open('json/'+filename)
	data = json.load(json_data)
	return json.dumps(data)

if __name__ == "__main__":
	app.run()
