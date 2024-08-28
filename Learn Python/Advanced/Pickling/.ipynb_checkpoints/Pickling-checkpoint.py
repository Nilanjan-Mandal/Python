'''
Pickling : Python Object -> Binary Object(0 1 1 0 1 0) through a serialized way. 
Unpickling : Python Object -> Binary Object through a serialized way. 
Use - Machine Learning(Module), Save in Database
'''
import pickle
import seaborn as sns

df=sns.load_dataset('tips')
df.head()





# # Define a Python object
# person = {
# 	"name": "Alice",
# 	"age": 30,
# 	"gender": "female"
# }

# # Pickle the object to a binary file
# with open("person.pickle", "wb") as file:
# 	pickle.dump(person, file)

# print("Pickling completed")
