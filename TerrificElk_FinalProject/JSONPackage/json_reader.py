# json_reader.py

import json
from cryptography.fernet import Fernet

class JSONDecryptor:
    def __init__(self, json_path, encryption_key):
        """
        Iniialize the JSONDecryptor woth the path to the JSON file
        """
        self.json_path = json_path
        self.encryption_key = encryption_key
        self.ferner = Fernet(encryption_key)

        def load_json(self):
            """
            Loads and parses JSON file
            """
            with open(self.json_path, 'r') as files:
                data = json.load(file)
            return data

        def decrypt_data(self, encrypted_data):
            """
            Decrypts the provided data using fernet
            """
            decrypted_data = self.fernet.decrypt(encrypted_data.encode()).decode()
            return decrypted_data

        def process_json(self):
            """
            Loads and decrypts data from the JSON file
            """
            json_data = self.load_json()

            #
            decrypted_data = {}
            for key, value in json_data.items():
                decrypted_data[key] = self.decrypt_data(value)

            return decrypted_data

        def find_team_hint(self, team_name):
            """
            """
            decrypted_data = self.process_json()
            team_hint = decrypted_data.get(team_name)
            if not team_hint:
                raise KeyError(f"Hint for team '(team_name)' not found.")
            return team_hint