import requests
import datetime
nutritionx_key = '554b05aa8d6cb04231131e0df026bf81'
nutritionx_id = 'c0036871'
nutritionx_url = 'https://trackapi.nutritionix.com//v2/natural/exercise'
google_sheet_endpoint = 'https://api.sheety.co/8db44691b124b59752ef6ec5e13abcf4/myWorkouts/workouts'

# post exercise requests
exercise_req = '/v2/natural/exercise'

headers = {
    "x-app-id": nutritionx_id,
    "x-app-key": nutritionx_key
}
req = {
    "query" : input("Tell me about your exercise")
}

exercise_data = requests.post(nutritionx_url, headers=headers, json=req)
# print(exercise_data.json()['exercises'])
exercise_info = exercise_data.json()['exercises']
today_date = datetime.datetime.now()
print(exercise_info)
sheet_inputs = {
    "workout" : {
        "Date": today_date.strftime("%d/%m/%Y"),
        "Time": today_date.strftime("%H/%M/%S"),
        "Exercise": exercise_info[0]['name'].title(),
        "Duration": exercise_info[0]['duration_min'],
        "Calories": exercise_info[0]['nf_calories']
    }
}


# store data into speadsheet

store_data_sheets = requests.post(google_sheet_endpoint, json=sheet_inputs)
print(store_data_sheets.text)

