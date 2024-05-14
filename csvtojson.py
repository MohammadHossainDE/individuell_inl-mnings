import csv
import json


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def csvConvert(csv_Path, json_Path):
	
	# create a dictionary
	jsondata = {}
	
	# Open a csv reader called DictReader
	with open(csv_Path, encoding='utf-8') as csvfile:
		csvData = csv.DictReader(csvfile)
		
		# Convert each row into a dictionary 
		# and add it to data
		for rows in csvData:
			
			# Assuming a column named 'Givenname' to
			# be the primary key
			key = rows['Givenname']
			jsondata[key] = rows

	# Open a json writer, and use the json.dumps() 
	# function to dump data
	with open(json_Path, 'w', encoding='utf-8') as jsonfile:
		jsonfile.write(json.dumps(jsondata, indent=4))
		print("Data Convert")
# Driver Code

# Decide the two file paths according to your 
# computer system
csvFilePath = r'profiles1.csv'
jsonFilePath = r'data.json'

# Call the make_json function
csvConvert(csvFilePath, jsonFilePath)
