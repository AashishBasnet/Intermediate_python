import json

people_string = '''
{
"people":[
{
"name" : "John Smith",
"phone" : "9876543210",
"emails" : ["johnsmith@gmail.com","jonsmith-work@gmail.com"],
"has_license" : false
},
{
"name" : "Jane Doe",
"phone" : "9786541230",
"emails" : null,
"has_license" : true
}
]
}
'''

data = json.loads(people_string)
print(data)
print(type(data)) #<-- This gives dictionary as it is a dict

#------JSON conversion chart is given as------

#   JSON ---> Python
#   object ---> dict
#   array ---> list
#   string ---> str
#   number(int) ---> int
#   number(real) ---> float
#   true ---> True
#   false ---> False
#   null ---> None

# The json.loads translates fluently to python

#To test:

print(type(data['people'])) #<-- THis is changed to list in python

for person in data['people']: 
    print(person['name']) #This prints value of both elements in list with key 'people' where name is accessed

# Here we learned how to load json string into python!

#---------Now, let's learn how to convert python into json---------

#i.e. using json.dumps()

# For eg. imagine you were given a task to delete phone number in backend from json data and send back...
# This is how you delete and dump back
for person in data['people']: 
    del person['phone']

new_string = json.dumps(data, indent = 2, sort_keys=True) #<-- here indent is used for readability of the code here 2 = indentation layer
# and sort key sorts keys by alphabet.

print(new_string)

#Loading JSON

# json.load() ---> loads file into json
# json.loads() <---loads json strings

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])

for state in data['states']:
    del state['area_codes']

with open('area_less_states.json','w') as f:
    json.dump(data,f, indent = 2)



