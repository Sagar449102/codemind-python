a=input()
s=[';', ':', '!', "*", " "]
for i in s:
    if i in a:
        a=a.replace(i,"")
print(min(a),a.count(min(a)),max(a),a.count(max(a)))
