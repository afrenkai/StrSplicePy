#split a sentence into words
sentence = "Hello, how are you doing today?"
words = sentence.split()
print(words)
# Output: ['Hello,', 'how', 'are', 'you', 'doing', 'today?']

#split a sentence by a delimiter (commas here)
data = "apple,banana,cherry,dates"
fruits = data.split(",")
print(words)
# Target output: ['apple', 'banana', 'cherry', 'dates']


#split only the first n instances of a delimiter (colons here)
data = "name:age:location:email"
split_data = data.split(":", 2)
print(split_data)
# Output: ['name', 'age', 'location:email']


#split a string by newlines
text = """Hello World
This is a sample text
With multiple lines"""
lines = text.splitlines()
print(lines)
# Output: ['Hello World', 'This is a sample text', 'With multiple lines']

#split a string, do something to the parts, then add it back together. Try making each word uppercase here

sentence = "welcome to python!"
# split with no delimiter
words = sentence.split()
#blank list to store the words we'll make uppercase
new_words = []
# for loop to go through each words in the list of words that we got from splitting
for word in words:
    #add each word uppercased to the list we just made
    new_words.append(word.upper())
    #exit the loop
#once we're done, join the new words list we made with a blank string. 
new_sentence = " ".join(new_words)
print(new_sentence)
# Output: "WELCOME TO PYTHON"