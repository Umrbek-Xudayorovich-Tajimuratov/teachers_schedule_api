import json
import requests


#  search teacher by hemis_id
MY_TOKEN = "evoPgQkNb2QiG41GiE8DI_VqW1VYar-c"
SCHEDULE_LIST_URL = "https://talaba.tsue.uz/rest/v1/data/attendance-control-list"

# todo:  API CALLING ----------------------------------
def hemis_api_call():
    headers = {"Authorization": f"Bearer {MY_TOKEN}"}
    response = requests.get(SCHEDULE_LIST_URL, headers=headers)
    res = response.json()["data"]["items"]
    
    print(res)


# todo: END ---------- API CALLING ---------------------
hemis_api_call()

