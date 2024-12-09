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
            decryted_data = {}
            for key, value in json_data.items():
                decrypted_data[key] = self.decrypt_data(value)

            return decrypted_data

