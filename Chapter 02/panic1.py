phrase = "Don't panic!"
##Make it to an array 
plist =list(phrase)
print(phrase)
print(plist)

for i in range(4):
  plist.pop()

plist.pop(0)
plist.remove("'")
##Swap between value
## Pop first , pop the last array than the second last array , and than add the pop value to the array
plist.extend([plist.pop(), plist.pop()])
## Swap value
plist.insert(2, plist.pop(3))


new_phrase = ''.join(plist)
print(plist)
print(new_phrase)