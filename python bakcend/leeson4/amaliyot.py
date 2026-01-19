import json
# x = 10
# x_json = json.dumps(x)
# print(x_json)
# print(type(x_json))
bemor = {
    'ism':'ali',
    'familiya':'aliyev'
}
bemor_json = json.dumps(bemor, indent=2)
# print(bemor_json)

# with open('bemor.json','w') as file:
#     json.dump(bemor, file)
bemor = json.loads(bemor_json)
print(bemor)