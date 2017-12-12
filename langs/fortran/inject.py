import sys
import base64
import json
import os
from subprocess import Popen, PIPE, call

filepath, variable_name,filestring = "","",""
if(len(sys.argv) == 5):
    filepath = sys.argv[1]
    variable_name = sys.argv[2]
    jsonString = base64.b64decode(sys.argv[3]).decode('ascii')
    scopeInfo = json.loads(jsonString)
    filestring = sys.argv[4]
else:
    raise ValueError("Incorrect number of arguments! Parse script takes exactly three arguments: filepath variable_name line_number")

def getTabs(line):
	trimmed = line.strip()
	index = line.find(trimmed)
	return line[0:index]

def Inject():
	#begin by running the fortran file and
	fileObj = open(filepath)
	fileContent = fileObj.read()
	fileObj.close()

	#split by lines
	lines = fileContent.split("\n")
	start = scopeInfo['decl']['line']
	end = scopeInfo['scope']['end']
	statement = "print *, \" {\"\"atomic_tracer\"\":true,\"\"line\"\":<line>,\"\"output\"\":\"\"\"," + str(variable_name) + ",\"\"\"}\""

	for i in range(start,end):
		lineNum = i+1
		if(lines[i] == ""):
			continue
		stmt = statement.replace("<line>",str(lineNum))
		lines[i] += "\n" + getTabs(lines[i]) + stmt
		i += 1

	#write code to temp file
	tempFile = filepath.replace(".f90","-temp.f90")
	fileObj = open(tempFile,"w")
	fileObj.write("\n".join(lines))
	fileObj.close()

	#run the file and get the output
	call(["gfortran", tempFile, "-o" + filestring + "temp_output"])
	process = Popen(["./" + filestring + "temp_output"], stdout=PIPE, shell=True)
	#process = Popen(["gfortran", tempFile, " && ./a.out"], stdout=PIPE)
	(output,err) = process.communicate()
	exit_code = process.wait()
	if(err):
		os.remove(tempFile)
		raise ValueError(err.decode('utf-8'))

	output = output.decode('utf-8')
	#parse output (only get the output that we injected)
	lines = output.split("\n")
	cleanOutput = []
	for line in lines:
		try:
			out = json.loads(line)
			if('atomic_tracer' in out):
				cleanOutput.append(out)
		except:
			pass

	#delete temp file
	os.remove(tempFile)
	os.remove(filestring + "temp_output")
	print(json.dumps(cleanOutput))
    #print("[{\"output\": 2, \"line\": 6, \"atom-tracer\": true}, {\"output\": 9, \"line\": 7, \"atom-tracer\": true}, {\"output\": 9, \"line\": 9, \"atom-tracer\": true}, {\"output\": 9, \"line\": 11, \"atom-tracer\": true}]")

Inject()
