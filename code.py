import pandas as pd
import numpy as np
import datetime

 
def set_index_to_datetime(data): #this function is used to set indices of the dataset as datatime which corresponds to Date column
    data["Time"]=pd.to_datetime(data["Date"])
    data.set_index("Time")
    data=data.set_index("Time")
    return data


def get_value_by_idx(idx="12:00:00" , MINS=0): 
    # FOR THIS FUNCTION TO WORK CORRECTLY THE VALUE OF THE IDX SHOULD BE PASSED IN THE SAME FORMATE AS THAT OF INDEICES OF THE DATASET , LIKE 01:03:00 TO WORK CORRECTLY
    # THIS FUNCTION IS NOW MORE DYNAMIC , YOU CAN PASS IN ANY TIME AND IT WILL GET YOU THE ROW PLUS/MINUS THE MINTS YOU PASS ,
    DATE=datetime.datetime.now().strftime("%Y-%m-%d")
    TIME=DATE + " "  +idx
    row= data.loc[TIME]
    return data.loc[(row.index[0]+datetime.timedelta(minutes=MINS))]
    
def get_bmo_high(startTime, stopTime):
    # this function will return the value of High column from startTime to stopTime , 
    # Note : the startTime and stopTime must be passed in the same formate as in index of dataset e.g 12:00:00 or 03:43:00 
    # These values must be passed without any space !!!
    DATE=datetime.datetime.now().strftime("%Y-%m-%d")
    startTime=DATE + " "  +startTime
    stopTime=DATE + " "  +stopTime
    start_and_stop_value=[]    
    for i in range(len(data.index)):
        if startTime==str(data.index[i]) or stopTime==str(data.index[i]):
            start_and_stop_value.append(i)      
    return data.loc[data.index[start_and_stop_value[0]:start_and_stop_value[1]]]["High"].max()


       
def get_time(startTime="02:30:00" , num=178):
    #THIS FUNCION WILL GIVE THE  FIRST ROW WHERE THE VALUE OF HGIH IS LESS THAN 178 
    #YOU CAN PASS IN ANY TIME AND AND ANY VALUE FOR THE ARGUMENT 'NUM' TO CHECK FOR THE HIGH AND IT WILL WORK
    #YOU'VE TO KEEP IN MIND THAT THE TIME SHOULD BE PASSED THE SAME FORMATE AS THAT IN THE INDEX OF DATASET
    DATE=datetime.datetime.now().strftime("%Y-%m-%d")
    startTime=DATE + " "  +startTime
    for i in range(len(data.index)):
        if startTime==str(data.index[i]):
            #index=i
            break
    for j in range(i , len(data.index)):
        if data.loc[data.index[j]]["High"]< num:
            return data.loc[data.index[j]]

 

 #I'VE TESTED TO CODE MULTIPLE TIMES AND IT IS WORKING PERFECTLY NOW , IT IS DYNAMIC AND ROBUST AS YOU REQUIRED.
 # i'VE CHEKCED IT MANUALLY WITH THE DATASET AND ITS GIVING ME CORRECT VALUES.
 #NOTE THAT , THIS CODE WILL WORK FOR CURRENT DAY DATE ONLY.
 #  
 
 
 
data=pd.read_csv("out.csv")
#dropping the indices which were named 'Unnamed: 0' in dataframe
data.drop('Unnamed: 0' , axis=1 , inplace=True)

data = set_index_to_datetime(data)
#rint(data)

row=get_value_by_idx("02:34:00",-4)

print(row)

high=get_bmo_high("04:00:00" , "05:00:00")
print(high)

time=get_time("12:43:00" , 178)
print(time )