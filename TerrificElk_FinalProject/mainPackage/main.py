#main.py
# Name: Ben Ujvagi, Jacob Shultze, Danny Barnhouse, Dobry Shaw
# email:  ujvagibw@mail.uc.edu, schul2jt@mail.uc.edu, barnhodw@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  12/10/2024
# Course #/Section:  IS4010-001
# Semester/Year:  Fall 2024
# Brief Description of the assignment: decrypt two different codes and take a picture at the location
# Brief Description of what this module does. In this module, we call everything together and print it out
# Citations: Microsoft Copilot

import os
from buildingdecryptionPackage.buildingdecryption import file_reader as building_file_reader
from buildingdecryptionPackage.buildingdecryption import decryptor as building_decryptor
from buildingdecryptionPackage.buildingdecryption import json_reader as building_json_reader
from moviedecryptionPackage.moviedecryption import decryptor as movie_decryptor
from moviedecryptionPackage.moviedecryption import json_reader as movie_json_reader
from photoimportPackage.photoimport import photo as photo_module

def main():
    # File paths
    group_json_file_path = os.path.join('data', 'EncryptedGroupHints Fall 2024 Section 001.json')
    words_file_path = os.path.join('data', 'UCEnglish.txt')
    photo_path = os.path.join('data', 'FinalProjectImage.jpeg')
    movie_json_file_path = os.path.join('data', 'TeamsAndEncryptedMessagesForDistribution.json')
    
    # Group name and team name
    group_name = "TerrificElk"
    team_name = "Complete Duck"
    
    # Key for decryption
    # We used Complete Duck's Key instead of our own
    key = b'WVRqW7wUIQ1mgbz5PAonHGJn-XknVdDV74L_RNFjU0o='
    
    # Get the numbers for the specified group from the JSON file
    encrypted_numbers = building_json_reader.get_group_numbers(group_json_file_path, group_name)
    if encrypted_numbers is None:
        print(f"Group '{group_name}' not found in JSON file.")
        return
    
    # Get the encrypted movie title for the specified team from the JSON file
    encrypted_movie_title = movie_json_reader.get_encrypted_movie_title(movie_json_file_path, team_name)
    if encrypted_movie_title is None:
        print(f"Team '{team_name}' not found in JSON file.")
        return
    
    # Read the words from the .txt file for the location decryption
    words = building_file_reader.read_words(words_file_path)
    
    # Decrypt the location
    location = building_decryptor.decrypt_location(encrypted_numbers, words)
    print(f"Decrypted Location: {location}")
    
    # Decrypt the movie title
    movie_title = movie_decryptor.decrypt_message_fernet(encrypted_movie_title, key)
    print(f"Decrypted Movie Title: {movie_title}")
    
    # Display the photo
    photo_module.display_photo(photo_path)

if __name__ == "__main__":
    main()

