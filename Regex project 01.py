import re
from datetime import datetime

# Name
while True:
    pattern = re.compile(r'^[A-Za-z ]+$')
    text = input("Enter Your Name: ")
    res = pattern.fullmatch(text)
    if res is not None:
        name = res.group()
        break
    else:
        print("Enter Name in Correct Format!")

# Date of Birth
while True:
    pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
    text = input("Enter Date of Birth(dd-mm-yyyy): ")
    res = pattern.fullmatch(text)
    if res is not None:
        # Convert to dd Month yyyy format
        dob_raw = res.group()
        dob_date = datetime.strptime(dob_raw, "%d-%m-%Y")
        dob = dob_date.strftime("%d %B %Y")
        break
    else:
        print("Enter DOB in Correct Format!")

# Email ID
while True:
    pattern = re.compile(r'[a-z0-9]+@gmail.com\Z')
    text = input("Enter Email id: ")
    res = pattern.fullmatch(text)
    if res is not None:
        mailid = res.group()
        break
    else:
        print("Enter Mail id in correct format!")

# Mobile Number
while True:
    pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
    text = input("Enter Mobile Number(xxx-xxx-xxxx): ")
    res = pattern.fullmatch(text)
    if res is not None:
        mobile = re.sub(r'-', '', res.group())
        break
    else:
        print("Enter Mobile Number in correct Format!")

# Final Output
print(f"Name : {name}")
print(f"Date of Birth: {dob}")
print(f"Mail id: {mailid}")
print(f"Mobile : {mobile}")
