import io
import os
import json
import cv2 as cv
from PIL import Image

# Imports the Google Cloud client library
from google.cloud import vision

def extract_id():
  # Instantiates a client
  client = vision.ImageAnnotatorClient()

  # The name of the image file to extract text
  file_name = os.path.abspath('image_data/sample_id.png')


  # # Loads the image into memory
  with io.open(file_name, 'rb') as image_file:
      content = image_file.read()

  '''
  Tresholding and denoising feature has been removed for performance enhancement
  '''
  # Load the image in grayscale
  # image = cv.imread('sample_id.png', 0)
  
  # Apply denoising to the image
  # noiseless_image = cv.fastNlMeansDenoising(image, None, 20, 7, 21) 
  
  # Apply thresholding to the image
  # ret,thresh_image = cv.threshold(noiseless_image,150,255,cv.THRESH_BINARY)
 
  # Show Images
  # thresh_image = Image.fromarray(thresh_image)
  # thresh_image.show()
  
  
 
  # Display the thresholded image
  image = vision.Image(content=content)

  # Performs text detection on the image file
  response = client.document_text_detection(image=image)

  texts = response.text_annotations

  # Split the text by sentences
  texts = texts[0].description.split('\n')

  # Create a dictionary to arrange the extracted information
  id_dict = {}

  for i in range(len(texts)):
      if texts[i] == "HONG KONG IDENTITY CARD":
          id_dict["Name"] = texts[i+1] 
          id_dict['ID'] = texts[i+2]
          id_dict['Date of Birth'] = texts[i+4].split()[0]
          id_dict['Date of Issue'] = texts[i+8].split()[0]
  
  return id_dict
  # Save the extracted information into a JSON file
  
if __name__ == '__main__':
    extract_id()