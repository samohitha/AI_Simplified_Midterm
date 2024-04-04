import pandas as pd
import json

# Define a function to extract data from each JSON object
def extract_data(data):
    byteentropy = data['byteentropy']  
    formatted_input = {'NgramFeaturesList_pred': [byteentropy],
                       'importsCorpus_pred': ' '.join(data['imports'].keys()),
                       'sectionNames_pred': ' '.join([section['name'] for section in data['section']['sections']]),
                       'numSections_pred': str(len(data['section']['sections']))}
    label = data['label']
    return formatted_input, label

# Open the JSONL file
data_list = []
with open('/content/ember2018/train_features_1.jsonl', 'r') as f:
    # Read the first 1000 lines
    for _ in range(1000):
        line = f.readline().strip()
        if not line:
            break
        data = json.loads(line)
        data_list.append(data)

# Create DataFrame
df = pd.DataFrame(columns=['Formatted Input', 'Label'])

# Iterate over data_list and append to DataFrame
for item in data_list:
    formatted_input, label = extract_data(item)
    df = pd.concat([df, pd.DataFrame({'Formatted Input': [formatted_input], 'Label': [label]})], ignore_index=True)

# Display DataFrame
df.head()
