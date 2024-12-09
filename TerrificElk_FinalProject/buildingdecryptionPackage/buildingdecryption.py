#main.py
# Name: Ben Ujvagi, Jacob Shultze, Danny Barnhouse, Dobry Shaw
# email:  ujvagibw@mail.uc.edu, schul2jt@mail.uc.edu, barnhodw@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  12/10/2024
# Course #/Section:  IS4010-001
# Semester/Year:  Fall 2024
# Brief Description of the assignment: decrypt two different codes and take a picture at the location

# Brief Description of what this module does. decrypts the building location 
# Citations: Microsoft Copilot
# buildingdecryption.py 
import json 
def get_group_numbers(json_file_path, group_name): 
    with open(json_file_path, 'r', encoding='utf-8') as file: 
        data = json.load(file) 
    for group in data["groups"]: 
        if group["name"] == group_name: 
            return group["numbers"] 
    return None
