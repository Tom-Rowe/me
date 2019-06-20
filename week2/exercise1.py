"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

some_words = ['what', 'does', 'this', 'line', 'do', '?']
# I think that this will print each word in the list
for word in some_words: #It printed each word in the list
    print(word)

for x in some_words: #the function says x:'what', so it will print "what"
    print(x) #It printed "what does this line do? x must be each word in some_words"

# I think this will print "what does this line do?" in one line of code
print(some_words) # It printed in a list with each word

#I think that this means if there are more words than 3, then it will print all the words
if len(some_words) > 3:
    print('some_words contains more than 3 words') # That makes sense lol, because there are more than three words, it printed "some_words contains more than 3 words"

# I think this tells me about the computer i have and its specs: system, node, release, version, machine and processor
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) # Yay it told me about my computer - no idea what it means but thats cool

usefulFunction()
