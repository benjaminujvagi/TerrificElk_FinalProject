
# moviedecryption/decryptor.py

# Name: Ben Ujvagi, Jacob Shultze, Danny Barnhouse, Dobry Shaw
# email:  ujvagibw@mail.uc.edu, schul2jt@mail.uc.edu, barnhodw@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  12/10/2024
# Course #/Section:  IS4010-001
# Semester/Year:  Fall 2024
# Brief Description of the assignment: decrypt two different codes and take a picture at the location
# Brief Description of what this module does. In this module we decrypt the code that tells us our movie
# Citations: Microsoft Copilot

from cryptography.fernet import Fernet
import json

"""
    Decrypts an encrypted message using a Fernet key.

    Args:
        encrypted_message (str): The message to decrypt.
        key (bytes): The Fernet key for decryption.

    Returns:
        str: The decrypted message.
"""

def get_encrypted_movie_title(json_file_path, team_name):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        return None
    except FileNotFoundError:
        print(f"Error: The file {json_file_path} was not found.")
        return None

    if team_name in data:
        return data[team_name][0]
    else:
        return None
     