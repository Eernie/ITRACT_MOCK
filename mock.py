from flask import Flask
import json
import pprint

app = Flask(__name__)
app.debug = True 


@app.route("/tripOffer", methods=['GET'])
def tripOfferGet():
	json_data=open('json/get_tripOffers.json')

	data = json.load(json_data)

	return json.dumps(data)

if __name__ == "__main__":
	app.run()