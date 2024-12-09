#main.py
# Name: Ben Ujvagi, Jacob Shultze, Danny Barnhouse, Dobry Shaw
# email:  ujvagibw@mail.uc.edu, schul2jt@mail.uc.edu, barnhodw@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  12/10/2024
# Course #/Section:  IS4010-001
# Semester/Year:  Fall 2024
# Brief Description of the assignment: decrypt two different codes and take a picture at the location

# Brief Description of what this module does. decrypts the building location using json
# Citations: Microsoft Copilot
# buildingdecryption.py 
#buildingdecryption.py

import json

def get_group_numbers(json_file_path, group_name):
    try:
        print(f"JSON file path (group numbers): {json_file_path}")  # Debug print
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return None
    except FileNotFoundError:
        print(f"Error: The file {json_file_path} was not found.")
        return None
    except TypeError as e:
        print(f"TypeError: {e}")
        return None

    if group_name in data:
        return data[group_name]
    else:
        return None

def read_words(file_path):
    try:
        print(f"Reading words from: {file_path}")  # Debug print
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []

def decrypt_location(encrypted_numbers, words):
    # Example decryption logic using the provided numbers and words list
    try:
        location = ' '.join(words[int(num)] for num in encrypted_numbers)
        return location
    except IndexError as e:
        print(f"Error: One of the numbers is out of bounds in the word list: {e}")
        return ""
    except ValueError as e:
        print(f"Error: Invalid number format in encrypted numbers: {e}")
        return ""
    except Exception as e:
        print(f"Unexpected error during decryption: {e}")
        return ""

