import datetime
import random
import sys
import webbrowser

print("Today's date is :", datetime.date.today())
print()
print()
print(sys.path)
# This basically the path where python will look in order to import the module. 
print()
#sys.exit() 
# After this command nothing will execute. 
print("Random number is :", random.randint(1,100))
webbrowser.open('www.facebook.com')




