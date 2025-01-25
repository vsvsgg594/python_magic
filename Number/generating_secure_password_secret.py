import secrets
import string
desired_combination=string.ascii_uppercase+string.ascii_lowercase+string.ascii_letters+string.digits
password=''.join(secrets.choice(desired_combination) for _ in range(16))
print("Generated Password : " ,password)