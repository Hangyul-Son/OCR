import re
import json

from google_drive import get_images
from extract_id import extract_id
from extract_address import extract_address
from database import connect_db, insert_to_table
from verify_regex import verify_regex

def main(type):
  name_regex = re.compile(r'[A-Z]+,\s[A-Z][a-z]+')
  id_regex = re.compile(r'[A-Za-z]\d{6}')
  dob_regex = re.compile(r'\d{2}-\d{2}-\d{4}')
  doi_regex = re.compile(r'\d{2}-\d{2}-\d{2}')
  
  # Get images from Google Drive
  get_images()
 
  if type == "id":
   
    # Extract text from the images and save it to a json file
    id_dict = extract_id()
    with open('text_data/id.json', 'w') as f:
      json.dump(id_dict, f)
    
    # Verify the extracted text
    verified = verify_regex("id", id_dict)
    
    # Save the verified data to the MySQL database
    if verified == True:
      try:
        cnn = connect_db()
        insert_to_table(cnn, "HKID", id_dict)
      finally:
        cnn.close()
    else:
      print("Verification Failed")
      
  elif type == "address":
    
    # Extract text from the images and save it to a json file
    address_dict = extract_address()  
    with open('text_data/address.json', 'w') as f:
      json.dump(address_dict, f)
    
    # TODO: Verfitication method for address data
    verified = verify_regex("address", address_dict)

    # Save the verified data to the MySQL database
    if verified == True:
      try:
        cnn = connect_db()
        insert_to_table(cnn, "ADDRESS", address_dict)
      finally:
        cnn.close()
    else:
      print("Verification Failed")    
   

if __name__ == '__main__':
    main('id')