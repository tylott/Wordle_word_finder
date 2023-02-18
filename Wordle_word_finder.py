#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 22:37:14 2022

@author: tyler
"""

#from english_words import english_words_set

### This word set is limited ###

#print(english_words_set)

import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
file_path = open(os.path.expanduser(file_path))
english_words_set = []
for i in file_path:
    english_words_set.append(i)
    
english_words_set_stripped = []
data = []
### Cleaning up the text files
for i in english_words_set:
    i_stripped = i.strip('\n')
    english_words_set_stripped.append(i_stripped)

for i in english_words_set_stripped:
    i_stripped2 = str(i.strip("'"))
    data.append(i_stripped2)

english_words_set = data

total_words = english_words_set
#print(len(total_words))
five_letter_words = []
for i in english_words_set:
    if len(i) == 5:
            five_letter_words.append(i)
            
### Create your conditional of choice ###


solution_found = False
letters_not_present = []
letters_present = []
known_letters_position_known = []
known_letters_position_unknown = []
position_known_letter = []
position_known_letter_absent = []
num_of_attempts = 1
words_containing_condition_1 = []
words_containing_condition_2 = []


while solution_found == False:
    update_known_letters_list_prompt= input("Would you like to update the known letter list? ")
    new_known_letter_count = 0 
    if update_known_letters_list_prompt == "Y" or update_known_letters_list_prompt == "Yes" or update_known_letters_list_prompt == "yes" or update_known_letters_list_prompt == "y": 
        number_user_letters_present = int(input("How many new letters do you know that are certaintly in the word (number character)? "))
        while new_known_letter_count < number_user_letters_present:
            add_known_letter = str(input("Please input the letter which is present: "))
            position_known_letter_prompt = input("Do you know where the letter is (Y/N) ? ")
            if position_known_letter_prompt  == "Y" or position_known_letter_prompt  == "Yes" or position_known_letter_prompt == "yes" or position_known_letter_prompt == "y": 
                add_known_letter_position = int(input("Please input the position of the letter (1-5, left-right): "))   
                position_known_letter.append(add_known_letter_position)
                known_letters_position_known.append(add_known_letter)
            else:
                add_known_letter_absent_position = int(input("Please input the position which the letter is not present (1-5, left-right): "))   
                position_known_letter_absent.append(add_known_letter_absent_position)
                known_letters_position_unknown.append(add_known_letter)
            letters_present.append(add_known_letter)
            new_known_letter_count += 1
            
    for word in five_letter_words[:]:
        if len(position_known_letter) > 0:
            count_j = 0
            for letter in known_letters_position_known:
                if letter in word:
                    if word[position_known_letter[count_j]-1] == letter:
                        words_containing_condition_1.append(word)
                count_j += 1
        if len(position_known_letter_absent) > 0:
            count_j = 0
            for letter in known_letters_position_unknown:
                if letter in word:
                    if word[position_known_letter_absent[count_j]-1] == letter:
                        words_containing_condition_2.append(word)   
                count_j += 1
    
    new_missing_letter_count = 0 
    if num_of_attempts > 0:
        update_missing_letters_list_prompt = input("Would you like to update the missing letter list? ")
        if update_missing_letters_list_prompt == "Y" or update_missing_letters_list_prompt == "Yes" or update_missing_letters_list_prompt == "yes" or update_missing_letters_list_prompt == "y":   
            number_user_letters_not_present = int(input("How many new letters do you know that are certaintly missing from the word (number character)? "))
            while new_missing_letter_count < number_user_letters_not_present:
                add_missing_letter = str(input("Please input the letter which is missing: "))
                letters_not_present.append(add_missing_letter)
                new_missing_letter_count += 1
                
    new_letter_count = 0      
    
    if len(known_letters_position_known) == 1:
        known_possible_word_list = []
        for word in words_containing_condition_1:
            if word[0] == known_letters_position_known[0]:
                known_possible_word_list.append(word)  
        if len(known_letters_position_unknown) > 0:
            possible_word_list = []
            possible_word_list2 = []
            possible_word_list3 = []
            for word in known_possible_word_list:
                if word not in words_containing_condition_2:
                    possible_word_list.append(word)  
            for word in possible_word_list:
                for letter in known_letters_position_unknown:
                    if letter not in word:
                        possible_word_list2.append(word)
            for word in possible_word_list:
                if word not in possible_word_list2:
                    possible_word_list3.append(word)      
            possible_words = possible_word_list3        
        else:
            possible_words = known_possible_word_list
            
    elif len(known_letters_position_known) == 2:
        known_possible_word_list = []
        known_possible_word_list2 = []
        for word in words_containing_condition_1:
            if word[0] == known_letters_position_known[0]:
                known_possible_word_list.append(word)  
        for word in known_possible_word_list:
            if word[position_known_letter[1]-1] == known_letters_position_known[1]:
                known_possible_word_list2.append(word)  
        if len(known_letters_position_unknown) > 0:
            possible_word_list = []
            possible_word_list2 = []
            possible_word_list3 = []
            for word in known_possible_word_list2:
                if word not in words_containing_condition_2:
                    possible_word_list.append(word)  
            for word in possible_word_list:
                for letter in known_letters_position_unknown:
                    if letter not in word:
                        possible_word_list2.append(word)
            for word in possible_word_list:
                if word not in possible_word_list2:
                    possible_word_list3.append(word)      
            possible_words = possible_word_list3        
        else:
            possible_words = known_possible_word_list2

    elif len(known_letters_position_known) == 3:
        known_possible_word_list = []
        known_possible_word_list2 = []
        known_possible_word_list3 = []
        for word in words_containing_condition_1:
            if word[0] == known_letters_position_known[0]:
                known_possible_word_list.append(word)  
        for word in known_possible_word_list:
            if word[position_known_letter[1]-1]  == known_letters_position_known[1]:
                known_possible_word_list2.append(word)  
        for word in known_possible_word_list2:
            if word[position_known_letter[2]-1]  == known_letters_position_known[2]:
                known_possible_word_list3.append(word)  
        if len(known_letters_position_unknown) > 0:
            possible_word_list = []
            possible_word_list2 = []
            possible_word_list3 = []
            for word in known_possible_word_list3:
                if word not in words_containing_condition_2:
                    possible_word_list.append(word)  
            for word in possible_word_list:
                for letter in known_letters_position_unknown:
                    if letter not in word:
                        possible_word_list2.append(word)
            for word in possible_word_list:
                if word not in possible_word_list2:
                    possible_word_list3.append(word)      
            possible_words = possible_word_list3        
        else:
            possible_words = known_possible_word_list3
            
    elif len(known_letters_position_known) == 4:
        known_possible_word_list = []
        known_possible_word_list2 = []
        known_possible_word_list3 = []
        known_possible_word_list4 = []
        for word in words_containing_condition_1:
            if word[0] == known_letters_position_known[0]:
                known_possible_word_list.append(word)  
        for word in known_possible_word_list:
            if word[position_known_letter[1]-1]  == known_letters_position_known[1]:
                known_possible_word_list2.append(word)  
        for word in words_containing_condition_2:
            if word[position_known_letter[2]-1]  == known_letters_position_known[2]:
                known_possible_word_list3.append(word)  
        for word in words_containing_condition_2:
            if word[position_known_letter[3]-1] == known_letters_position_known[3]:
                known_possible_word_list4.append(word)  
        if len(known_letters_position_unknown) > 0:
            possible_word_list = []
            possible_word_list2 = []
            possible_word_list3 = []
            for word in known_possible_word_list4:
                if word not in words_containing_condition_2:
                    possible_word_list.append(word)  
            for word in possible_word_list:
                for letter in known_letters_position_unknown:
                    if letter not in word:
                        possible_word_list2.append(word)
            for word in possible_word_list:
                if word not in possible_word_list2:
                    possible_word_list3.append(word)      
            possible_words = possible_word_list3        
        else:
            possible_words = known_possible_word_list4
    else:
        possible_word_list = []
        possible_word_list2 = []
        possible_word_list3 = []
        for word in five_letter_words:
            if word not in words_containing_condition_2:
                possible_word_list.append(word)  
        for word in possible_word_list:
            for letter in known_letters_position_unknown:
                if letter not in word:
                    possible_word_list2.append(word)
        for word in possible_word_list:
            if word not in possible_word_list2:
                possible_word_list3.append(word)      
        possible_words = possible_word_list3
    count = 0
    removed_words = []
    for i in possible_words[:]: ### Don't modify a list while iterating over it!!!
        word = i
        # print(word)
        count = 0
        remove_word = False
        for j in letters_not_present:
            letter = j
            count +=1
            if remove_word == True and count == len(letters_not_present):
                remove_word = True
                possible_words.remove(i)
                removed_words.append(i)
            elif j in i and count == len(letters_not_present):
                possible_words.remove(i)
                removed_words.append(i)
            elif letter in word:
                remove_word = True
            
    possible_words_filtered = []
    for word in possible_words:
       if word not in possible_words_filtered:
          possible_words_filtered.append(word)
    print("Here is a list of possible words which satisfy the solution:" + str(possible_words_filtered))
    user_found_solution_prompt = str(input("Have you found the solution? "))
    if user_found_solution_prompt == "Y" or user_found_solution_prompt == "Yes" or user_found_solution_prompt == "yes" or user_found_solution_prompt == "y":
        solution_found = True
        print("Congratulations!")
    else:
        solution_found = False
        num_of_attempts += 1


           

        