import io
import os
import json

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client

def extract_address():
  client = vision.ImageAnnotatorClient()

  # The name of the image file to extract text
  file_name = os.path.abspath('image_data/sample_address_proof.png')
  
  # Loads the image into memory
  with io.open(file_name, 'rb') as image_file:
      content = image_file.read()
  
  '''
  Tresholding and denoising feature has been removed for performance enhancement
  '''
  # Load the image in grayscale
  # image = cv.imread('sample_address_proof.png', 0)
  
  # Apply denoising to the image
  # noiseless_image = cv.fastNlMeansDenoising(image, None, 20, 7, 21) 
  
  # Apply thresholding to the image
  # ret,thresh_image = cv.threshold(noiseless_image,150,255,cv.THRESH_BINARY)
 
  # Show Images
  # thresh_image = Image.fromarray(thresh_image)
  # thresh_image.show()
  
  image = vision.Image(content=content)

  # Performs text detection on the image file
  response = client.document_text_detection(image=image)

  texts = response.text_annotations
  
  # # Split the text by sentences
  texts = texts[0].description.split('\n')

  # Create a dictionary to arrange the extracted information
  address_dict = {}

  # Extract four lines of address information
  for i in range(len(texts)):
      text = texts[i].lower().replace(" ", "")
      if text in ["kowloon", "newterritories", "hongkongislands"]:
          address_dict["Address Line 1"] = texts[i-3] 
          address_dict['Address Line 2'] = texts[i-2]
          address_dict['Address Line 3'] = texts[i-1]
          address_dict['Address Line 4'] = texts[i]

  return address_dict
      
if __name__ == '__main__':
    extract_address()