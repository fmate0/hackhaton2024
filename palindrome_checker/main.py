import re

def process_string(s):
    filtered_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return filtered_s

def is_palindrome(s):
    filtered_s = process_string(s)
    return filtered_s == filtered_s[::-1]

def count_unique_characters(s):
    filtered_s = process_string(s)
    return len(set(filtered_s))

def analyze_string(s):
    if is_palindrome(s):
        unique_count = count_unique_characters(s)
        return f"YES, {unique_count}"
    else:
        return "NO, -1"

def read_input_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().splitlines()

# fájl beolvasása
input_strings = read_input_file('input.txt')

# eredmények kiírása
for s in input_strings:
    result = analyze_string(s)
    print(result)