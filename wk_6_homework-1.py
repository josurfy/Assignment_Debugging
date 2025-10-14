# -*- coding: utf-8 -*-
"""
#%% the humble print statement
'''
1.a
Using the print() function only, get the wrong_add_function to print out where
it is making a mistake, given the expected output for ex, "we are making an error 
in the loop", which you would put near the loop. 
Structure the print() statement to show what the expected output ought to be
via f-strings: ie "The correct answer is supposed to be: [...]".
1.b
Then, changing as little as possible, modify the function, using the same 
general structure to output the correct answer. Call this new function 
correct_add_function() 
'''
"""
def wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [6,9,12]

   whereas the expected correct answer is, [2,3,4]

   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      print(f"We are making an error in the loop. The correct answer is supposed to be '{arg1[arg1_index] + arg2[arg1_index]}'") #print statement added to report what should be the correct value for every loop
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
      arg1[arg1_index]=arg_2_sum  
      arg1_index+=1
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

wrong_add_function(arg1, arg2)

one_a = print(f"1.a \n{wrong_add_function(arg1, arg2)}") #set one_a variable equal to a print statement with the problem number and the output of the malfunctioning wrong_add_function

def correct_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [6,9,12]

   whereas the expected correct answer is, [2,3,4]

   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      for arg2_elements in arg2:
          arg_2_sum = sum([arg1[arg1_index]+i if index == arg1_index else 0 for index, i in enumerate(arg2)]) #corrected loop which only adds indices of arg1 and arg2 when the index values are the same, otherwise the value is zero.
      arg1[arg1_index]=arg_2_sum  
      arg1_index+=1
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]


one_b = print(f"\n1.b \n{correct_add_function(arg1,arg2)}") #define variable one_b as a print operation giving the problem bumber and the execution of the correct_add_function.

#%% try, except
'''
2.a
Update the numeric section of the function with your changes from 1 for both 
2.b and 2.c

2.c
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
gets it to process via the string section. IE, do not, outside the function,
change the values of arg_str_1 or arg_str_2. Name this function 
correction_add_function(), i.e you will not be updating the wrong_add_function,
you will simply handle the error of wrong inputs in a seperate function, you want
the wrong_add_function to output its current result you are only bolstering the 
function for edge cases .
'''
def wrong_add_function2(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [4,5,6]
   
   If the lists are lists of strings, concatenate them
   Example:
      > wrong_add_function(['1','2','3'],['1','1','1'])
      > ['1111','2111','3111']
   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.

   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.

   '''
   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
               arg_2_sum = sum([arg1[arg1_index]+i if index == arg1_index else 0 for index, i in enumerate(arg2)]) #changed the arg_2_sum line per the instructions so that only indices with the same index number from arg1 and arg2 will sum, otherwise the value will be 0
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1

arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]

two_a = print(f"\n2.a\nBefore: arg_2_sum = sum([arg1[arg1_index]+i for index, i in enumerate(arg2)])\nAfter: arg_2_sum = sum([arg1[arg1_index]+i if index == arg1_index else 0 for index, i in enumerate(arg2)])") #defining variable two_a as a print statement showing what the arg_2_sum variable was set to before and after changing it according to the problem instructions.

'''
2.b
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
returns an error message to the user, in case users give invalid inputs,
(for example an input of ["5","2", 5])
: "Your input argument [1 or 2] at element [n]
is not of the expected type. Please change this and rerun. Name this function 
exception_add_function()'''

def exception_add_function(arg1, arg2): #define exception_add_function as a function with two arguments, arg1 and arg2
   t_list = arg1 + arg2 #define t_list as a variable that combines the lists arg1 and arg2
   arg_dict = {1: arg1, 2: arg2} #define arg_dict as a dictionary with key: 1 as value: arg1 and key: 2 as value: arg2
   s_list = [] #creates s_list as an empty list
   s_list.append(arg1) #appends arg1 to be the first element in s_list
   s_list.append(arg2) #appends arg2 to the second element in s_list
   
   try:
      sum(i for i in t_list) #try to sum the elements in t_list. will only work if elements in t_list are int, otherwise there will be a TypeError
   except TypeError: #TypeError exception 
      try: #nested try
         "".join(t_list) #try to join the elements in t_list. Will only work if elements in t_list are strings, otherwise there will be a TypeError.
      except TypeError: #nested TypeError exception
         try: #nested try
            j = 1 #set j as the iteration variable that keeps track of what argument is being evaluated
            for item in s_list: #initiate for loop for elements in s_list
               1/(len(set(type(i) for i in item))-2) #divides 1 by the length of the set of the types of elements in the elements in s_list and subtracts by 2. If there are int and str elements in the list, the value of the denominator will be 0 (ZeroDivisionError). Otherwise the value of the denominator will be -1.
               j += 1 #increase j by 1 before performing next for loop iteration
         except ZeroDivisionError: #ZeroDivisionError exception
            a = sum(type(i)==int for i in arg1) #set a equal to the sum of the integers in arg1
            b = sum(type(i)==str for i in arg1) #set b equal to the sum of the strings in arg1
            c = sum(type(i)==int for i in arg2) #set c equal to the sum of the integers in arg2
            d = sum(type(i)==str for i in arg2) #set d equal to the sum of the strings in arg2
            if a + c >= b + d: #more int elements than str
               try:
                  k = 0 #k is the element tracker
                  for i in arg_dict[j]: #initiate for loop for arg_dict at element j
                     1/(type(i)==int) #divide 1 by the boolean operation, if false then ZeroDivisionError
                     k += 1 #uptick k by 1
               except ZeroDivisionError: #ZeroDivisionError exception
                  print(f"Your input argument '{j}' at index '{k}' is not an integer. Please change this and rerun.") #print statement to alert user to change inputs to lists of integers
            if a + c < b + d: #more str elements than int
               try:
                  k = 0 #k is the element tracker
                  for i in arg_dict[j]: #initiate for loop for arg_dict at element j
                     1/(type(i)==str) #divide 1 by the boolean operation, if false then ZeroDivisionError
                     k += 1 #uptick k by 1
               except ZeroDivisionError: #ZeroDivisionError exception
                  print(f"Your input argument '{j}' at index '{k}' is not a string. Please change this and rerun.") #print statemetn to alert user to change inputs to lists of strings
   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
               arg_2_sum = sum([arg1[arg1_index]+i if index == arg1_index else 0 for index, i in enumerate(arg2)])
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1


arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]

two_b = print(f"\n2.b \n{exception_add_function(arg_str_1, arg_str_2)}") #two_b variable set to print the problem number and execute exception_add_function

