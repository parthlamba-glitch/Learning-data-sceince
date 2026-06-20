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
        
            
#Function to find pages you might like based on commmon interests
def find_pages_you_might_like(user_id, data):
    
    #Dictionary containg all liked pages of users
    user_pages = {}
    for user in data['users']:
        user_pages[user['id']] = set(user["liked_pages"])

    #Error prevention
    if user_id not in user_pages:
        return

    #Pages the given user liked
    user_liked_pages = user_pages[user_id]
    page_suggestion = {}

    for other_user, pages in user_pages.items():
        if other_user != user_id:
            shared_pages = user_liked_pages.intersection(pages)
        for page in pages:
            if page not in user_liked_pages:
                page_suggestion[page] = page_suggestion.get(page, 0) + len(shared_pages)

    sorted_pages = sorted(page_suggestion.items(), key = lambda x:x[1], reverse = True)
    return [page_id for page_id, _score in sorted_pages]



#Load the data
data = load_data("massive_data.json")
user_id = 10
recc = find_people_you_may_know(user_id, data)
print(recc)
print(find_pages_you_might_like(user_id, data))
