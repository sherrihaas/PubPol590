from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "\Users\Sherri\Documents\Duke MPP Year 2\Big Data\Data files"
git_dir = "\Users\Sherri\Documents\GitHub\PubPol590"
csv_file = "sample_data_clean_csv.csv"

#OS Module
df = pd.read_csv(os.path.join(main_dir, csv_file))

# PYTHON Data Types -----------------------

## strings
str1 = "hello, computer" 
str2 = 'hello, human'
str3 = u'eep'

type(str1) #type str
type(str2) #type str
type(str3) #type unicode

## numeric
int1 = 88 #any integer
float1 = 20.25 #any number with a decimal
long1 = 89999999998888888999999  #really long numbers

## logical
bool1 = True
notbool1 = 0
bool2 = bool(notbool1)


# Creating Lists and Tuples ---------------------

## in brief, lists can be changed, tuples cannot
## we will almost exclusively use lists

list1 = []
list1
list2 = [7,8,'a']
list2[2] # the output of this is 'a'
list2[2] = 5  #this changes the value to 5 


## tuples, can't change. basically thinks you don't want to use
tup1 = (8,3,19)
tup1[2] # output is 19

## convert
list2 = list(tup1)
tup2 = tuple(list1)

## list can be appended and extended
list2 = [8,3,19]
list2.append([3, 90])
len(list2)  
list3 = [8,3,19],
list2.extend([6, 88])  # output: [8,3,19,6,88]
len(list3)

# Converting Lists to Series and Dataframes ------------
list4 = range(5,10) # range (n,m) gives a list from n to m-1
list4  # output: [5,6,7,8,9]
list8 = range(5) # range(m) gives list from 0 to m-1
list8  #output: [0,1,2,3,4]
list5 = ['q', 'r', 's', 't', 'u']



## list to series
s1 = Series(list4)
s2 = Series(list5)  #its case sensitive, lower and upper case matters

## lists to DataFrame



