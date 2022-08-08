# 6. Write a function that takes a string and returns a word that occurs least number of times in the string. if there are multiple words that occurs least number of times then return a list of words
# Input: Immigrants are good and citizens like immigrants are good too
# Output: [and, citizens, like, too]

def least_words(string):
    words = string.split(" ")
    duplication = {}

    for word in words:
        if word.strip().lower() in duplication.keys():
            duplication[word.strip().lower()] += 1
        else:
            duplication[word.strip().lower()] = 1

    for key,value in duplication.items():
    
    


print(least_words("Immigrants are good and citizens like immigrants are good too"))