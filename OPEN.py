import json

file = open("E:\\EDYODA\\New folder\\indian_states.json","r")
indian_states = json.load(file)
print(indian_states)
print(type(indian_states))


# import json

# file = open("E:\\portfolioproject","w")
# with open('indian_states.json', 'w') as file:
  
#   json.dump(indian_states, file)