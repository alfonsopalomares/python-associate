try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except FileNotFoundError as e:
  print("Something went wrong when opening the file")
except NameError as e1:
  print ("error de name error" )
except:
  print ("agarro TODAS las exceptions que no puse antes")

  


print ("linea siguiente")


class MyException(Exception):
  pass

raise MyException("esta es mi exception") 


