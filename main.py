import datetime as dt
import pandas as pd
import random
import smtplib
import os

MY_EMAIL = "shreshshende.777@gmail.com"
MY_PASSWORD = "heowhwzhfpuklxhi"  # Try an App Password if 2FA is on
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Debug: Print current working directory
print("Current directory:", os.getcwd())

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Debug: Print today's date and birthdays
print("Today's date:", today_tuple)
print("Birthdays in CSV:", birthdays_dict.keys())

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    
    
    # Debug: Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found - {file_path}")
    else:
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=birthday_person["email"],
                    msg=f"Subject:Happy Birthday!\n\n{contents}"
                )
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
else:
    print("No birthdays today.")