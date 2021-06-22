set1 = []
set2 = []


first = input("")
second = input("")


for a in first:
    if a == " ":
        continue
    set1.append(a)
for w in second:
    if w == " ":
        continue
    set2.append(w)

set1.sort()
set2.sort()

if set1 == set2:
    print("Is an anagram.")
else:
    print("Is not an anagram.")
