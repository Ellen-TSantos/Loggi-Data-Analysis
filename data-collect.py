
import json

with open('deliveries.json', mode='r',encoding='utf8') as file:
     data = json.load(file)
     len(data)
    
     example =data[5] #getting the 5th instance
     print(example.keys()) # Dictionary keys
   
     example['name'] # accessing name instances
     print(example['name'])
    
     example['region'] # accessing Region Instances
     print(example['region']) # Dictionary keys
     
     example['origin']['lat'] # accessing the hub latitude Instances
     print(example['origin']['lat'])
     
     example['origin']['lng'] # accessing the hub's longitude Instances
     print(example['origin']['lng'])
   
     example['vehicle_capacity'] # accessing vehicle capacity Instances
     print(example['vehicle_capacity'])
    
     example['deliveries'][5]['id'] # accessing the deliveries Instances through the id
     print(example['deliveries'][5]['id'])
    
     example['deliveries'][5]['point']['lat'] # accessing deliveries instances through point and latitude
     print(example['deliveries'][5]['point']['lat'])
