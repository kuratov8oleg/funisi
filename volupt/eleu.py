import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Serialize the data
serialized_data = json.dumps(data)

# Choose a file location and format
file_path = "path/to/file.json"

# Write the serialized data to the file
with open(file_path, "w") as file:
    file.write(serialized_data)

print("Data serialized and saved successfully.")
