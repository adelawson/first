import os 
def rename_files():
   x= os.listdir(r"C:\Users\Adesayo\Pictures")
   print (x)
   y=os.getcwd()
   print (y)
   os.chdir(r"C:\Users\Adesayo\Pictures")
   for file_name in x:
       os.rename(file_name,file_name.translate(None,"0123456789-"))
   os.chdir(y)
rename_files()
