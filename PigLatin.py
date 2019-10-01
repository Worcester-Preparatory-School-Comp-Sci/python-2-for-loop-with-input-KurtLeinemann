## Kurt Leinamann Pig Latin September 26 2019

word=input("Pick a word")
vowelList=['a','e','i','o','u']
if word[0] in vowelList:
	print(word +"yay")  #yikes... print(print... also didn't need to select a slice of word.. just whole word
else:
	print(word[1:] + word[0] + "ay")
