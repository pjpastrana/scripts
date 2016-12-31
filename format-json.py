#!/usr/bin/python
import fileinput
import json
import sys

TEST_JSON_STRING='{"id":"2c928088535f35ca01536226bb5d0014","taskName":"Build","sessionId":73,"runId":null,"modelId":null,"status":"SUCCESS","statusMessage":null,"lastUpdated":1457640618845,"files":[{"id":271,"name":"mobile-sensor-accelerometer-data-1457640568942.csv","type":"Input"},{"id":272,"name":"inputfile.json","type":"Input"},{"id":273,"name":"ModelDetails.json","type":"ModelDetails"}]}'

# to use from as macros
# if __name__ == "__main__":
#     text = ''
#     for line in fileinput.input():
#         text = text + ' ' + line.strip()
#     jsonObj = json.loads(text)
#     print json.dumps(jsonObj, sort_keys=True, indent=2)

def format_json_file(jsonFilePath):
    print "Formatting json file"
    fin = open(jsonFilePath)
    jsonString = fin.read().strip()
    fin.close()
    format_json_string(jsonString)
    

def format_json_string(jsonString):
    print "Formatting json string"
    jsonObj = json.loads(jsonString)
    print json.dumps(jsonObj, sort_keys=True, indent=2)

def main(jsonInput):
    if jsonInput.endswith(".json") or jsonInput.endswith(".JSON"):
        format_json_file(jsonInput)
    else:
        format_json_string(jsonInput)
    
if __name__ == "__main__":
    #main(sys.argv[1])
    main(TEST_JSON_STRING)
    
    
# TODO:
# - strip scape characters
