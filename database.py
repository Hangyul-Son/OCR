import mysql.connector
from mysql.connector import errorcode


def connect_db():
  try:
    cnx = mysql.connector.connect(user='hson', password='1234',
                                host='127.0.0.1', database = 'OCR')
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)

  
  return cnx

def insert_to_table(db_instance, table_name, dict=None):
  mycursor = db_instance.cursor()
  if table_name == 'HKID':
    sql = "INSERT INTO HKID (Name, ID, DOB, DOI) VALUES (%s, %s, %s, %s)"
    val = (dict['Name'], dict['ID'], dict['Date of Birth'], dict['Date of Issue'])
    mycursor.execute(sql, val)
  
  if table_name == 'ADDRESS':
    sql = "INSERT INTO ADDRESS (line1, line2, line3, line4) VALUES (%s, %s, %s, %s)"
    val = (dict['Address Line 1'], dict['Address Line 2'], dict['Address Line 3'], dict['Address Line 4'])
    mycursor.execute(sql, val)
    
  print(mycursor.rowcount, "record inserted.")    
  db_instance.commit()
  db_instance.close()
  
if __name__ == '__main__':
  cnx = connect_db()
  insert_to_table(cnx, 'HKID')
  cnx.close()
  
 
