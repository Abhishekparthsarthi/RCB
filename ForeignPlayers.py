import os
import json

def rename_files():
     count =0
     file_to_open = os.path.expanduser('~/Desktop/TeamRCB.json')
     f = open(file_to_open)
     data = json.load(f)
     for i in data['player']:
        if (i['country']) != 'India':
           count +=1
     if count == int(4):
        print ("This test validates that the team has only 4 foreign players")
     else:
          print("This test validates that the team doesn't 4 foreign players")   
     f.close()
rename_files()
