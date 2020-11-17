made by Anas Darwish

import urllib.request

arr = [{"img":"<<<url>>>","name":"photo"}]

for i in arr:
  urllib.request.urlretrieve(i["img"], i["name"]+".jpg")

