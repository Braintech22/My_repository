# Python3 code to demonstrate
# to count words in string
# using split()

# initializing string
init_sentence = input ("Enter your sentences    ")

# printing original string
print ("The original string is : " + init_sentence)

# using split()
# to count words in string
res = len(init_sentence.split())

# printing result
print ("The number of words in your sentence are : " + str(res))
