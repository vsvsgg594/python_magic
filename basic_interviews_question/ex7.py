# Write a Python code to find how often the substring “Emma” appears in the given string.

def find_number(text):
    return text.count("Emma")  # Directly count occurrences

ans = find_number("Emma is a good developer. Emma is a writer")
print(ans)  # Output: 2
