import time
current_hour = time.localtime().tm_hour  # gets current hour (0–23)
if current_hour < 12:
    print("Good Morning!")
elif current_hour < 17:
    print("Good Afternoon!")
elif current_hour < 21:
    print("Good Evening!")
else:
    print("Good Night!")
