import json
import sys

base_path = sys.argv[1]
train_data_path = base_path + "/train_dials.json"
dev_data_path = base_path + "/dev_dials.json"
test_data_path = base_path + "/test_dials.json"
data_paths = {"train": train_data_path, "dev": dev_data_path, "test": test_data_path}
data_path = data_paths[sys.argv[2]]
output_path = sys.argv[4] + "/" + sys.argv[2]+".json"
filename = sys.argv[3]

with open(data_path) as json_file:
    data = json.load(json_file)
json_file.close()

result = []
for item in data:
    #if len(result) < 10:
    if item["dialogue_idx"] == filename:
        result.append(item)
output_json = json.dumps(result)
with open(output_path, 'w') as output_file:
    output_file.write(output_json)
output_file.close()
