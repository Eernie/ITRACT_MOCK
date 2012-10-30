import flask 
from flask import Flask, request, Response, make_response, current_app
import json
import pprint
from functools import update_wrapper
from datetime import timedelta

app = Flask(__name__)
app.debug = True 

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


def controleValidAttributes(formAttributes):
	for attribute in formAttributes:
		if not request.form[attribute]:
			return abort(400)


@app.route("/trip_offer", methods=['POST'])
@crossdomain(origin='*')
def tripOfferPost():
	formAttributes = {'user','origin_long', 'origin_lat', 
					'origin_window', 'destination_long', 'destination_lat', 'destination_window', 
					'start_time_min', 'start_time_max', 'end_time_min', 'end_time_max', 'numberOfSeats'}
	if request.method == 'PUT':
		controleValidAttributes(formAttributes)	 
	return dumpJsonFile('get_userById.json')


@app.route("/trip_offer", methods=['GET'])
@app.route("/trip_offer/<int:tripOfferId>", methods=['GET','PUT'])
@crossdomain(origin='*')
def tripOfferGet(tripOfferId=0):
	if tripOfferId == 0:
		return dumpJsonFile('get_tripOffers.json')

	formAttributes = {'destination_long','destination_lat','numberOfSeats'}
	if request.method == 'PUT':
		controleValidAttributes(formAttributes)	 
	return dumpJsonFile('get_tripOfferById.json')



@app.route("/trip_request", methods=['POST'])
@crossdomain(origin='*')
def tripRequestPost():
	formAttributes = {'user','origin_long','origin_lat','origin_window','destination_long',
										'destination_lat','destination_window','start_time_min','start_time_max',
										'end_time_min','end_time_max','numberOfSeats'}
	if request.method == 'PUT':
		controleValidAttributes(formAttributes)	 
	return dumpJsonFile('get_tripRequestById.json')




@app.route("/trip_request", methods=['GET'])
@app.route("/trip_request/<int:tripRequestId>", methods=['GET','PUT'])
@crossdomain(origin='*')
def tripRequestGet(tripRequestId=0):
	if tripRequestId == 0:
		return dumpJsonFile('get_tripRequests.json')
	formAttributes = {'destination_long','destination_lat','numberOfSeats'}
	if request.method == 'PUT':
		controleValidAttributes(formAttributes)	 
	return dumpJsonFile('get_tripRequestById.json')


@app.route("/match/<int:matchId>", methods=['GET','PUT'])
@crossdomain(origin='*')
def matchGet(matchId):
	formAttributes = {'confirm','rating'}
	if request.method == 'PUT':
		controleValidAttributes(formAttributes)	 
	return dumpJsonFile('get_match.json')


@app.route("/user", methods=['POST'])
@crossdomain(origin='*')
def userPost():
	formAttributes = {'name'}
	if request.method == 'PUT':
		controleValidAttributes(formAttributes)	 
	return dumpJsonFile('get_userById.json')


@app.route("/user", methods=['GET'])
@app.route("/user/<int:userId>", methods=['GET','PUT'])
@crossdomain(origin='*')
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
	response = make_response(json.dumps(data))
	return json.dumps(data)





if __name__ == "__main__":
	app.run()
