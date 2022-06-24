import json

stringofJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

jsonDataAsPythonValue = json.loads(stringofJsonData)
print(jsonDataAsPythonValue)
