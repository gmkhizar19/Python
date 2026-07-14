import json

data = '''{
"name" : "Chuck"
"phone" : 
    {
    "type" : "intl",
    "number" : "1234567890"
    },
email : 
    {   
    "hide" : "yes"
    }
}'''

info = json.loads(data)
print("Name:", info["name"])
print("hide:", info["email"]["hide"])
