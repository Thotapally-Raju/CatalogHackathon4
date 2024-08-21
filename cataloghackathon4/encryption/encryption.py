import random
import time
stored_password = "securepassword123"
stored_otp = None
def generate_otp():
    return random.randint(100000, 999999)
def verify_password(input_password):
    return input_password == stored_password
def verify_otp(input_otp):
    return input_otp == stored_otp
def authenticate():
    password = input("Enter your password: ")
    if verify_password(password):
        print("Password correct!")
        global stored_otp
        stored_otp = generate_otp()
        print(f"Your OTP is: {stored_otp}")
        time.sleep(2)
        otp = int(input("Enter the OTP: "))
        if verify_otp(otp):
            print("Authentication successful!")
        else:
            print("Incorrect OTP!")
    else:
        print("Invalid password!")
authenticate()
