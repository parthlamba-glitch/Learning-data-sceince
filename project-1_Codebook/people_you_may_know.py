import json

def load_data(filename):
    with open(filename, "r") as f:
        return json.load(f)

def find_people_you_may_know(user_id, data):
    #Finding friends of everyone
    user_friend = {} 
    for user in data['users']:
        user_friend[user['id']] = set(user['friends'])

    if user_id not in user_friend:
        return
        
    #Finding direct friends
    direct_friends = user_friend[user_id]
    
    suggestions = {}
    for friend in direct_friends:
        for mutual in user_friend[friend]:
            if mutual != user_id and mutual not in direct_friends:
                suggestions[mutual] = suggestions.get(mutual, 0) + 1
                
    sorted_suggestions = sorted(suggestions.items(), key = lambda x:x[1], reverse = True)
    return [user_id for user_id,_ in sorted_suggestions]
        
            
            

#Load the data
data = load_data("massive_data.json")
user_id = 10
recc = find_people_you_may_know(user_id, data)
print(recc)
