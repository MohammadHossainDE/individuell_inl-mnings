import csv
import json

def csv_to_json(csv_path, json_path):
    json_data = []
    
    # Open CSV file and read data
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        csv_data = csv.DictReader(csvfile)
        
        # Convert each row into a dictionary and add it to json_data list
        for row in csv_data:
            json_data.append(row)
    
    # Write JSON data to file
    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

def test_csv_columns(csv_path, expected_columns):
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        return len(header) == expected_columns, f"Expected {expected_columns} columns, but found {len(header)}"

def test_csv_rows(csv_path, min_expected_rows):
    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        num_rows = sum(1 for row in csv_reader)
        return num_rows >= min_expected_rows, f"Expected at least {min_expected_rows} rows, but found {num_rows}"

def test_json_properties(json_path, expected_properties):
    with open(json_path, 'r', encoding='utf-8') as jsonfile:
        json_data = json.load(jsonfile)
        for item in json_data:
            return len(item) == expected_properties, f"Expected {expected_properties} properties in JSON data, but found {len(item)}"

def test_json_rows(json_path, min_expected_rows):
    with open(json_path, 'r', encoding='utf-8') as jsonfile:
        json_data = json.load(jsonfile)
        num_rows = len(json_data)
        return num_rows >= min_expected_rows, f"Expected at least {min_expected_rows} rows in JSON data, but found {num_rows}"

if __name__ == "__main__":
    # Paths
    csv_file_path = 'profiles1.csv'
    json_file_path = 'profiles1.json'

    # Convert CSV to JSON
    csv_to_json(csv_file_path, json_file_path)

    # Run tests
    print("testa till kolla csv kolumn",  test_csv_columns(csv_file_path, 12))
    print("testa till kolla csv rad",   test_csv_rows(csv_file_path, 900) )
    print("testa till kolls json properties",  test_json_properties(json_file_path, 12) ) # Assuming each CSV row becomes a JSON object
    print("testa till kolla json rad",  test_json_rows(json_file_path, 900))
