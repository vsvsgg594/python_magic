import secrets
import string
secure_otp = string.digits
otp = ''.join(secrets.choice(secure_otp) for _ in range(6))

print("Your OTP is:", otp)


attempts = 3  
while attempts > 0:
    user_input_otp = input('Enter OTP: ')
    
   
    if user_input_otp == otp:
        print("OTP is correct")
        print("successfully verified your otp")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"OTP is incorrect. You have {attempts} attempts remaining.")
        else:
            print("OTP is incorrect. You've run out of attempts.")
