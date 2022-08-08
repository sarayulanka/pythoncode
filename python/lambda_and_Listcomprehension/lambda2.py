# Using Lambda - 1st way
# Here filtering is happening in the Lambda function
# Here you need both if and else
# In else, if you don't want to do anything, use "None"
# In python, if variable means if variable != "None"

friends = ["Sruthi", "Shloka", "Adhya", "Sharu", "Charlotte"]
friend_filter = lambda x: x if x[:2].lower() == "sh" else None
preferred_friends1 = [friend_filter(x) for x in friends]
# preferred_friends1 contains [None, "Shloka", None, "Sharu", None]
# Below list  comprehension filters None values
preferred_friends2 = [a for a in preferred_friends1 if a]
print(preferred_friends2)

# Using Lambda - 2nd way
# here Lambda returns a boolean value after checking for
# first two characters to equal "sh"
friend_filter1 = lambda x: x[:2].lower() == "sh"
# LC syntax [expression for variable in list filter]
# Here lambda is applied in filter rather than expression
# Here friend_filter1(x) is an expression which evaluates to True/False
# This is not the same as if variablename because this is if expression
preferred_friends3 = [x for x in friends if friend_filter1(x)]
print(preferred_friends3)

# Line 22 is the same as lines 26-28
for x in friends:
    if friend_filter1(x):
        print(x)

# decision operator
# In javascript decision (ternary) operator is ?
# In python it is
# value_if_true if expression else value_if_false
# But in List comprehension there will be only if and no else
# Because in LC the filter criteria is decided by the if
# followed by expression or variablename
# if the filter in LC evaluates to true,
# then the list value is sent to expression
# if the filter in LC evaulates to false, then the list value will be ignored


words = ["World", "Universe", "Galaxy", "Planets", "Stars", "Java", "Python"]
vowels = ["a", "e", "i", "o", "u"]
counter = 0
moreor2 = []
# make another list of all the words that have 2 or more vowels in them
# Not using List Comprehension

for word in words:
    counter = 0
    for vowel in vowels:
        for letter in word:
            if vowel.lower() == letter.lower():
                counter = counter + 1

    if counter >= 2:
        moreor2.append(word)

print(moreor2)
