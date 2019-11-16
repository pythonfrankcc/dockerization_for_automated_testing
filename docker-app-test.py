'''in the dockerfile we will be using the jazzdd/alpine-flask image as it is lightweight
each file in the dockerfile corresponds to a step in building of the docker image'''
from flask import Flask
import sys
import optpasrse
import time
from flask_cors import CORS

import warnings 
warnings.filterwarnings("ignore")

start = int(round(time.time()))
app = Flask(__name__)
#app.debug = True
'''assuming that a Js script is making a call to our API'''
CORS(app)

message = ("Hi this is an aotomated test using docker images")

@app.route("/")
def main():
    return message
#use an argument parser to declare the port
if __name__ == "__main__":
	parser = optparse.OptionParser(usage="docker-app-test.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print ("Missing required argument: -p/--port")
        sys.exit(1)
    app.run(host ="0.0.0.0",port=int(args.port),debug =True)