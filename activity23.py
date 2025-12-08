snack1 = "Banana cue"
snack2 = "Bibingka"
#List with default values

snack = ['Banana cue', 'Bibingka', 'Puto', 'Kutsinta', 'Halo-Halo', 'Ensaymada', 'Kamote cue']
            #0        1          2           3          4            5           6
print(snack)

#Every list has an index value / address
print(snack[3])
print(snack[2 : 5]) #List slicing

#Appending or adding items on the end of the list
snack.append("Maruya")
print(snack)

snack.append("Siomai")
print(snack)

#Inserts item at specified index
snack.insert(4, "Taho")
print(snack)

#Remove first occurence of item
snack.remove("Banana cue")
print(snack)

#Removes and returns item at index
snack.pop()
print(snack)

#Returns number of elements
print(len(snack))


#Sorts the list(ascending by default)
snack.sort()
print(snack)

#Reverses the list order
snack.reverse()
print(snack)
