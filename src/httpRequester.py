import urllib2
import pprint
import json

class httpRequester:

	def __init__(self, url="localhost"):
		self.url = url
		self.commands = []
		self.addCommand('trip_offer','GET','')
		self.addCommand('trip_offer','POST', data='user=1&origin_long=-77.037852&origin_lat=38.898556&origin_window=500&destination_long=-78.037852&destination_lat=39.898556&destination_window=500&start_time_min=1350478871&start_time_max=1350478872&end_time_min=1350478873&end_time_max=1350478874&numberOfSeats=1')
		self.addCommand('trip_offer','GET','/1')
		self.addCommand('trip_offer','PUT','/1', 'destination_long=-70&destination_lat=38&numberOfSeats=4')
		self.addCommand('trip_request','GET')
		self.addCommand('trip_request','POST',data='user=1&origin_long=-77.037852&origin_lat=38.898556&origin_window=500&destination_long=-78.037852&destination_lat=39.898556&destination_window=500&start_time_min=1350478871&start_time_max=1350478872&end_time_min=1350478873&end_time_max=1350478874&numberOfSeats=1')
		self.addCommand('trip_request','GET','/1')
		self.addCommand('trip_request','PUT','/1','destination_long=-80&destination_lat=31&numberOfSeats=1')
		self.addCommand('match','GET','/1')
		self.addCommand('match','PUT','/1', 'confirm=true&rating=8')
		self.addCommand('user','GET')
		self.addCommand('user','POST', data='name=John')
		self.addCommand('user','GET','/1')
		self.addCommand('user','PUT','/1','name=John')
		

	def doCommand(self, index):
		try:
			index = int(index)
			if (index <0) or (index > len(self.commands)-1):
				return 'Commando bestaat niet'
			command = self.commands[index]

			opener = urllib2.build_opener(urllib2.HTTPHandler)
			request = urllib2.Request('http://'+self.url+'/'+command['name']+command['getvars'], data= command['data'])
			request.get_method = lambda: command['method']
			url = opener.open(request)
			answer = json.load(url)
			return(json.dumps(answer,sort_keys=True, indent=4))
		except ValueError:
			return 'Gegeven waarde is geen int'

	def addCommand(self,name,method,getvars="",data=''):
		self.commands.append( {'index':len(self.commands), 'name':name,'method':method,'data':data,'getvars':getvars})

	def getPossibleCommands(self):
		possibleCommands =  "Insert the number off the account you want to run \n" 

		for command in self.commands:
			possibleCommands += str(command['index'])+".\t"+command['method']+"\t"+command['name']+command['getvars']+"\n"

		return possibleCommands