import requests

MY_LAT = -44.1127
MY_LONG = 116.2927
# http req res
# http call with no parameter
def if_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    print(response.json())
    print(response.status_code)
    iss_lat = float(response.json()['iss_position']['latitude'])
    iss_long = float(response.json()['iss_position']['longitude'])
    if response.status_code == 404:
        raise Exception("Resource does not exist")
    response.raise_for_status()

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LONG-5 <= iss_long <= MY_LONG+5:
        return True

def is_night():
    # http call with parameter
    params = {
        'lat': MY_LAT,
        'lng': MY_LONG
    }
    weather_response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
    print(f"sunset info {weather_response.json()['results']}")
    print(f"sunrise info {weather_response.json()['results']['sunrise']}")
    print(f"sunset info {weather_response.json()['results']['sunset']}")

val_1 = if_iss_overhead()
val_2 = is_night()
print(val_1)
print(val_2)
from tkinter import *


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    print(response.json()['quote'])
    quote = response.json()['quote']
    canvas.itemconfig(quote_text, text=quote)




window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()