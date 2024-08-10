import multiprocessing
import requests

def downloadFile(url,name):
    response = requests.get(url)
    
    print(f"Started downloading {name}")
    open(f'files/{name}.jpg',"wb").write(response.content)
    print(f"Finished downloading {name}")

url = "https://picsum.photos/2000/3000"

pros = []

for i in range(5):   
    # downloadFile(url,i)   
    p = multiprocessing.Process(target=downloadFile,args=[url,i])
    p.start()
    pros.append(p)
    
for p in pros:
    p.join()