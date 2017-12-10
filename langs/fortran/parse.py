import sys
import json

filepath,variable_name,line_number = "","",""
if(len(sys.argv) == 4):
	filepath = sys.argv[1]
	variable_name = sys.argv[2]
	line_number = int(sys.argv[3])
else:
	raise ValueError("Incorrect number of arguments! Parse script takes exactly three arguments: filepath variable_name line_number")

def Parse():
	var_start = 0
	var_end = 0
	var_decl = 0
	with open(filepath) as fp:
		for cnt, line in enumerate(fp):
			for word in line.split():
				if word == variable_name:
					if var_decl == 0:
						var_decl = cnt+1
						var_start = cnt+1
					var_end = cnt+1
				#print word + " " + str(cnt)

		scopeData = {'scope':{
		'start':var_start,
		'end':var_end },
		'decl':{'line':var_decl}
		}
		print(json.dumps(scopeData))

Parse()
