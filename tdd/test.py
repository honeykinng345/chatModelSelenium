import os
from pathlib import Path

from model.User import User

user_map = {
    "kdkd": "kdkkd"
}

if len(user_map.values()) >= 1:
    print(len(user_map.values()))

    print("zero")
else:
    print("oks")
    print(len(user_map.values()))

for getUser in user_map.values():
    print("hello")

if '123456' in user_map:
    print("added")
    print(user_map["123456"])
else:
    print("Not Added")

extension_path = os.path.join(os.getcwd(), 'simple_vpn_extension')
print(extension_path)
