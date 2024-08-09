import requests

url = f"https://newsapi.org/v2/top-headlines/sources?apiKey=c024f05bef874b6bbc4837adeb798b78"
response = requests.get(url)

# Gives a dictionary which contains String and List
output = response.json() 
print (type(output))

   
# Gives a string and a list
for value in output.values():  
    print(type(value))      
    
    
# Gives Tuple inside the list
values1 = list(output.items())[1]  
print(type(values1))


# Gives List inside the Tuple
values2 = values1[1]    
print(type(values2))


# Gives Dict inside the List; Dict contanis actual news
values3 = values2[0]
print(type(values3))
print(values3)