from AInput import AInput
from httpRequester import httpRequester
import pprint
import sys

def main():
	
	if len(sys.argv)>1:
		requester = httpRequester(sys.argv[1])
	else:
		requester = httpRequester()
		
	quits = {"exit","quit","stop"}
	
	while True:
		command = AInput(requester.getPossibleCommands()).getString()
		if command in quits:
			break
		print(requester.doCommand(command))
		raw_input("Press ENTER to test an other request...")

if __name__ == "__main__": 
	main()