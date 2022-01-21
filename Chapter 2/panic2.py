phrase = "Don't panic!"
##Make it to an array 
plist =list(phrase)
print(phrase)
print(plist)

##slice the array 
cut_phrase = plist[1:3]
## copy the array
copy_phrase = (cut_phrase.copy())
# Add the array
new_phrase = ''.join(copy_phrase) +  ''.join([phrase[5],phrase[4],phrase[7],phrase[6]])

print(plist)
print(new_phrase)
