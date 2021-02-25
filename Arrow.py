# Use the Request library
import requests
# Set the target webpage
url = "https://www.ite.edu.sg/"
r = requests.get(url)
# This will get the full page
print(r.text)

# This will get the status code
print("Status code:")
print("\t *", r.status_code)
if (r.status_code == 200):
    print("OK")

# This will just get just the headers
h = requests.head(url)
print("Header")

# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("ok")

headers = {
    'User-Agent' : "Mobile"
}

