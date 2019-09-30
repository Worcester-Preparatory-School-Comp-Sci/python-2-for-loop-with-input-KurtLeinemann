## Kurt Leinamann Pig Latin September 26 2019

word=input("Pick a word")
vowelList=['a','e','i','o','u']
if word[0] in vowelList:
	print(print(word[0:]+"yay"))
else:
	print(word[1:]+word[0]+"ay")
