import os
import json

def rename_files():
     count =0
     file_to_open = os.path.expanduser('~/Desktop/TeamRCB.json')
     f = open(file_to_open)
     data = json.load(f)
     for i in data['player']:
        if (i['role']) == 'Wicket-keeper':
           count +=1
     if count == int(1):
        print ("This test validates that there is at least one wicket keeper")
     else:
          print("This test validates that there is not one wicket keeper")
     print(count)
     f.close()
rename_files()
