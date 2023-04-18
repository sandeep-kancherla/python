names1=('sandy','candy','randy')
names2=names1

#print(names1)
#print(names2)

names1[1]='nandy'

print(names1)
print(names2)

# we encounter an error because replacing data is not allowed/possible in Tuples
# whereas it is allowed in lists only.