"""
Assignment1 ME369P/ME396P
Name: <David Zhang>
EID : <DZ4338>

Fill in the 4 functions below
"""

import random


def scifiAuthors(filename):
    #Put code for question 1 in this function
    fun = {}
    input = open(filename, "r")
    while input:
        line = input.readline()
        temp = line.split()
        try:
            num_nominations = int(temp[0])
            temp = line.split("--")
            temp2 = temp[1]
            last_name = temp2.split(",")
            key = last_name[0]
            check = fun.get(key,False)
            if not check:
                fun[key] = [1,num_nominations]
            else: 
                temp = fun.get(key)
                curr_nominations = temp[1]
                updated_nominations = curr_nominations + num_nominations
                num_books = temp[0] + 1
                fun[key] = [num_books, updated_nominations]
        except:
            alphabet_fun = dict(sorted(fun.items(), key = lambda x: x[0].lower()))
            descending_fun = dict(sorted(alphabet_fun.items(), key = lambda r: r[1][1], reverse = True))
            fun = descending_fun
            for key in fun:
                values = fun.get(key)
                if values[0] > 1:
                    output = "{}: {} books with {} total nominations".format(key, values[0], values[1])
                    print(output)
                else:
                    output = "{}: {} book with {} total nominations".format(key, values[0], values[1])
                    print(output)  
            break 


import re

def animalCollectives(filename):
    #Put code for question 2 in this function\
    fun = {}
    input_file = open(filename, "r")
    line = input_file.readline()
    line = input_file.readline()
    line = input_file.readline()
    while input_file:
        line = input_file.readline()
        line = line.split()
        try:
            group_name = line[0]
            animal_type = line[1]
            fun[animal_type] = group_name
        except:
            break 
    while True: 
        line = input("What type of animals are you running from ")
        def pluralize(noun):
            if re.search('[sxz]$', noun):
                return re.sub('$', 'es', noun)
            elif re.search('[^aeioudgkprt]h$', noun):
                return re.sub('$', 'es', noun)
            elif re.search('[aeiou]y$', noun):
                return re.sub('y$', 'ies', noun)
            else: 
                return noun + 's'
        if line == "Exit" or line == "Quit" or line == "exit" or line == "quit":
            random_animal = random.choice(list(fun.keys()))
            matching_random_group = fun.get(random_animal)
            output = "A " + matching_random_group + " of " + random_animal + " got you!"
            print(output)
            break
        check = fun.get(line, False)
        if not check:
            pluralline = pluralize(line)
            secondcheck = fun.get(pluralline, False)
            if not secondcheck:
                random_group = random.choice(list(fun.values())).lower() 
                output = "A " + random_group + " of " + line + " is coming to git you!"
                print(output)
            else: 
                group_name = fun.get(pluralline).lower()
                output = "A " + group_name + " of " + pluralline + " is coming to git you!"
                print(output)
        else:
            group_name = fun.get(line).lower()
            output = "A " + group_name + " of " + line + " is coming to git you!"
            print(output)



def myCalculator():
    #Put code for question 3 in this function
    while True:
        operation = input("Enter operation: ")
        if operation == "q":
            break
        first_num = input("Enter first number: ")
        if first_num == "":
            first_num = 0
        else:
            first_num = float(first_num)
        second_num = input("Enter second number: ")
        if second_num == "":
            second_num = 0
        else:
            second_num = float(second_num)
        if operation == "+":
            ans = first_num + second_num
            if ans == 0:
                print('0.0')
            else:
                print(round(ans,1))
        elif operation == "-":
            ans = first_num - second_num
            if ans == 0:
                print('0.0')
            else:            
                print(round(ans,1))
        elif operation == "*":
            ans = first_num * second_num
            if ans == 0:
                print('0.0')
            else:            
                print(round(ans,1))
        elif operation == "/":
            ans = first_num / second_num
            if ans == 0:
                print('0.0')
            else:            
                print(round(ans,1))
        else:
            ans = first_num ** second_num
            if ans == 0:
                print('0.0')
            else:            
                print(round(ans,1))

from wordcloud import WordCloud
from PIL import Image
import numpy as np


def wordCloud(filename):
    #Put code for question 4 in this function
    #Only required for graduate students
    dataset = open(filename, mode = 'r', encoding = 'utf-8').read()
    stopwords = ["The","the"]
    secondstopwords = ["a", "an", "the", "for", "and", "nor", "but", "or", "yet", "so", "at", "around", "by", "after", "along", "for", "from", "of", "on", "to", "with", "without"]
    mask = np.array(Image.open('C:\\Users\\David\\OneDrive\\Desktop\\CloudShape.jpg'))
    wc = WordCloud(background_color = 'white', mask = mask, stopwords = stopwords, height = mask.shape[0], width = mask.shape[1])
    wc2 = WordCloud(background_color = 'white', mask = mask, stopwords = secondstopwords, height = mask.shape[0], width = mask.shape[1])
    wc.generate(dataset)
    wc2.generate(dataset)
    wc.to_file("wordcloudone_output.jpg")
    wc2.to_file("wordcloudtwo_output.jpg")
    
if __name__ == '__main__':
    scifiAuthors("scifibookfavorites.txt")
    animalCollectives("collecti.txt")
    myCalculator()
    wordCloud("scifibookfavorites.txt")
    print("Done")
