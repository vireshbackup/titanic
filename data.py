#This file will hold the class that will manipulate the data on the titanic.


#Importing files that will be used for the project
import pandas as pd
import numpy as np

#This class is what will deal with all of the data about the titanic.
class Data():

    #The following method will show the user the total amount of people on the
    #Titanic.
    def amount_who_lived(self):
        self.__data = pd.read_csv('train.csv')
        total_passengers = len(self.__data)
        return total_passengers

    #This method will show the user who survived the sinking of the titanic by
    #sex.
    def who_lived_by_sex(self, sex):
        self.__data = pd.read_csv('train.csv')
        total_passengers = len(self.__data)
        survived_passengers = len(self.__data[self.__data.Survived == 1])
        sex_type = len(self.__data[(self.__data.Sex == sex) & (self.__data.Survived == 1)])
        return survived_passengers, total_passengers, sex_type

    #This method will show the user who survived the sinking of the titanic by
    #class.
    def who_lived_by_class(self, class_type):
        self.__data = pd.read_csv('train.csv')
        total_passengers = len(self.__data)
        survived_passengers = len(self.__data[self.__data.Survived == 1])
        class_type = len(self.__data[(self.__data.Pclass == class_type) & (self.__data.Survived == 1)])
        return survived_passengers, total_passengers, class_type

    #This method will simply convert the class selected, which is an integer, to a string
    #of either first, second or third.
    def convert_class(self, class_selected):
        if class_selected == 1:
            return 'first'
        elif class_selected == 2:
            return 'second'
        elif class_selected == 3:
            return 'third'

    #This method will show the user the amount of people who survived by age.
    def age_lived(self, age_entered):
        self.__data = pd.read_csv('train.csv')
        total_passengers = len(self.__data)
        age_survived = len(self.__data[(self.__data.Age >= age_entered)])
        return total_passengers, age_survived

    #This method will show the user the amount of people who survived by sex and class
    def survived_sex_class(self, sex_entered, class_entered):
        self.__data = pd.read_csv('train.csv')
        total_passengers = len(self.__data)
        class_sex_survived = len(self.__data[(self.__data.Pclass == class_entered) & (self.__data.Sex == sex_entered)])
        return total_passengers, class_sex_survived
