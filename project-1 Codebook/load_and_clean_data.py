import json

#Function to clean the data
def clean_data(data):
    #Remove users with missing names
    data["users"] = [user for user in data["users"] if user["name"].strip()]
    
    #Remove duplicate values
    for user in data["users"]:
        user["friends"] = list(set(user["friends"]))
        
    #Remove inactive users
    data["users"] = [user for user in data["users"] if user["friends"] or user["liked_pages"]]
    
    #Remove duplicate pages
    unique_pages = {}
    for page in data["pages"]:
        unique_pages[page['id']] = page
    data['pages'] = list(unique_pages.values())
    return data


#Loading the data and printing it into another json file
data = json.load(open("data.json"))
data = clean_data(data)
json.dump(data, open("clean_data2.json", "w"), indent = 4)
print("Data has been sucsessfully cleaned")