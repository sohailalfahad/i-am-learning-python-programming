from itertools import permutations


person={"first_name":"sohail","last_name":"Ahmed","gender":"male","age":"30","place":"ballari"}
print(person)
print(len(person))
for dictionaryitems in person:
 print("the key name and items value pairs in the dictionary are:",)
person[dictionaryitems]
print(type(person))
firstname=person["first_name"]
lastname=person["last_name"]
gender=person["gender"]
age=person["age"]
place=person["place"]
print("the first name is:",firstname)
print("the last namis :", lastname)
print("the gerder:",gender)
print("age is :",age)
print("the place is:",place)
print(person.get("age"))
print(person.get("place"))
print(person.get("sohail"))#instead of raising an erros the get()
#will only return "none" if the specified key is not found
print(person.get(143))
print(person.get("first_name"))
print["hobby"]="playing chess"
print(person)
print(person.get("hobby"))
print["hobby"]="playing cricket"
print(person)
person.pop("age")
print(person)
del person ["hobby"]
print(person)
if "place"in person:
 print("the key name 'place' is exist")
else:
 print("the key name 'place' is not existed")
if "place" not in person:
    print("the key name 'place' is exist")
else:
    print("the key name 'place'is not existed")