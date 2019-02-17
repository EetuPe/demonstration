import sys
import os
import glob
import gzip
import json
import shutil
print("This is the name of the script: ", sys.argv[0])
fnames = []
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))
files = []
files2 = []
for filename in glob.glob('testi.json.gz'):
   files2.append(filename)
for file in files2:
   with gzip.open(file, 'rb') as f_in:
         with open(file + ".csv", 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
for file in files2:
   print(file, ".csv", "created", "(TEMPORARY FILE)")
for filename in glob.glob('*.csv'):
   files.append(filename)
print(files)
print(files2)
result_name = input("Filename: ")
f= open(result_name,"w+")
for file in files:
    with open(file) as current_file:
        for line in current_file:
               f.write(str(line))
               print(line)
for file in files:
   os.remove(file)
   print(file + " " + "removed" + " "  + "(TEMPORARY FILE)")
print("You can find the result in " + result_name)
f.close()

#Tämä skripti purkaa pakatun json.gz tiedoston, lukee ja tallentaa uuteen tiedostoon ja printtaa uuden tiedoston sisällön, niin että voit lukea sisällön ilman että avaat tiedostoa.
#Sinun täytyy itse kertoa uuden tiedoston nimi ja tiedostotyyppi esim. testi.txt
#Ä ja Ö kirjaimet eivät välttämättä toimi
