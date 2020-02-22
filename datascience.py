#lst=['a','b','o' ,'s','o','p','b','b','a']
import matplotlib.pyplot as plt
file=open("file_example_CSV_5000(1).txt",'r')
word=file.read()
file.close()
alpha="abcdefghijklmnopqrstuvwxyz"
for w in word:
	if w  in alpha:
		pass
	else:
		word=word.replace(w,"")
word=word.replace(' ','')
#word=word.replace(',','')
#converts to list so it can be sorted alphabetically 
word=list(word)
word=sorted(word)
lst=list(word)
alph=list(alpha)
dict=dict.fromkeys(lst , 0)
for i in range(len(lst)):
	for j in range(len(alph)):
		if	lst[i] == alph[j]:
			dict[lst[i]]+=1
			

alphabets=[*dict]
#print(alphabets)
fre=list(dict.values())


plt.bar(alphabets,fre,label='Bar',color='Black')
fre=sum(fre)
plt.xlabel(fre)
plt.title("Alphabets")
plt.legend()
plt.show()