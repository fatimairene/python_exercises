import re

text = "hola mi nombre es pepe y mi email es: fatima@gmail.com y figarci@test.com"

# Regular expression to find email addresses
email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

# Find all matches in the text
emails = re.findall(email_pattern, text)

print(emails)
