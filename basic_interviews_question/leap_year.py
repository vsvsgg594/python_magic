def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400 → Leap year
            return False  # Divisible by 100 but not 400 → Not a leap year
        return True  # Divisible by 4 but not 100 → Leap year
    return False  # Not divisible by 4 → Not a leap year

# Test cases
print(check_leap_year(2016))  # ✅ True (Leap year)
print(check_leap_year(1900))  # ❌ False (Divisible by 100 but not 400)
print(check_leap_year(2000))  # ✅ True (Divisible by 400)
print(check_leap_year(2023))  # ❌ False (Not divisible by 4)
