import re
import json 


def verify_regex(type, dict):
  if type == "id":
    name_regex = re.compile(r'[A-Z]+,\s[A-Z][a-z]+')
    id_regex = re.compile(r'[A-Za-z]\d{6}')
    dob_regex = re.compile(r'\d{2}-\d{2}-\d{4}')
    doi_regex = re.compile(r'\d{2}-\d{2}-\d{2}')

    with open('text_data/id.json') as f:
      dict = json.load(f)

    if re.fullmatch(name_regex, dict['Name']) == None:
      print("Name No Match")
      return False
      
    if re.fullmatch(id_regex, dict['ID']) == None:
      print("ID No Match")
      return False
    
    if re.fullmatch(dob_regex, dict['Date of Birth']) == None:
      print("Date of Birth No Match")
      return False
      
    if re.fullmatch(doi_regex, dict['Date of Issue']) == None:
      print("Date of Issue No Match")
      return False
    
    return True  
     
  elif type == "address":
    
    # TODO: Verfitication method for address data
    return True