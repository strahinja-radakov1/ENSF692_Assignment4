# calgary_dogs.py
# AUTHOR NAME: Strahinja Radakovic
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 README file.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import pandas as pd

def years_popular (dog_breed_input, data):
    """
    Creates an incomplete string that prints which years an inputted breed was popular in, and prints the result.

    The program checks if the data for a given breed contains a year value (if it does that means that the breed was popular in said year).
    If true, the year is appended to the aforementioned string.

    Args:
        dog_breed_input: dog breed inputted by the user.
        data: DataFrame containing all data from CalgaryDogBreeds.xlsx formatted

    Returns:
        nothing, it just prints to the console.
    """
    years_popular = "The " + dog_breed_input + " was found in the top breeds for years: " #creating the incomplete string
    #checks if the dogbreed was popular in 2021
    if (2021 in data.loc[dog_breed_input].index.get_level_values('Year')):
        years_popular += "2021 " #appends the year to above incomplete string
    #checks if the dogbreed was popular in 2022
    if (2022 in data.loc[dog_breed_input].index.get_level_values('Year')):
        years_popular += "2022 " #appends the year to above incomplete string
    #checks if the dogbreed was popular in 2023
    if (2023 in data.loc[dog_breed_input].index.get_level_values('Year')):
        years_popular += "2023 " #appends the year to above incomplete string
    
    print(years_popular) #prints now completed string to console


def get_total (dog_breed, data):
    """
    Finds the total number of dogs registered that are a specific (user inputted) breed. Then prints the information.
    The program sums the Total column for a specific breed of dog for all years and prints a string to the console informing the user.

    Args:
        dog_breed_input: dog breed inputted by the user.
        data: DataFrame containing all data from CalgaryDogBreeds.xlsx formatted

    Returns:
        nothing, it just prints to the console.
    """
    total = str(data.loc[dog_breed].sum().iloc[0]) #sums the total registrations for a given breed of dogs, turns it into a string and assigns it to 'total'
    print("There have been "  + total +  " " + dog_breed + " dogs registered in total.") #prints the total number of registered dogs of given breed to the console.


def breed_portion_of_year (dog_breed, data, year):
    """
    Finds which percentage of all dogs registered were of the user inputted breed for a given year.
    The program sums the total number of dogs registered for the user's selected breed, and divides it by the sum of all dogs registered in a given year.
    It then multiplies that by 100, converts it into a string, and assigns it to a variable.
    The function then prints a string informing the user.

    Args:
        dog_breed_input: dog breed inputted by the user.
        data: DataFrame containing all data from CalgaryDogBreeds.xlsx formatted
        year: the year the user wants the data for

    Returns:
        nothing, it just prints to the console.
    """
    percentage_of_top = str((data.loc[dog_breed,year].sum().iloc[0])/(data.loc[:,year,:].sum().iloc[0])*100) #finding the percentage of dogs registered that are of the user inputted breed for a given year
    print("The " + dog_breed + " was " + percentage_of_top + "% of top breeds in " + str(year) + ".") # string creation and printing

def percentage_of_all (dog_breed, data):
    """
    Finds the percentage of all dog breeds registered in the data that are of the user inputted breed.
    The program sums the total number of dogs registered that are of the user inputted breed for the whole data timeframe, and divides it by the total number of gods registered in that time frame.
    It then multipies the above number by 100 to get the percentage, and assigned it as a string to a value 'percantage_of_top_total'
    The function then prints a string informing the user.


    Args:
        dog_breed_input: dog breed inputted by the user.
        data: DataFrame containing all data from CalgaryDogBreeds.xlsx formatted

    Returns:
        nothing, it just prints to the console.
    """
    percentage_of_top_total = str((data.loc[dog_breed,:].sum().iloc[0])/(data.loc[:,:,:].sum().iloc[0])*100) #finding the percentage of dogs registered that are of the user inputted breed total
    print("The " + dog_breed + " was " + percentage_of_top_total + "% of top breeds accorss all years.") #informing the user

def popular_months(dog_breed, data):
    """
    Finds the months for which the user selected dog breed is most popular and informs the user. 
    The function creates an array of how many times the selcted breed was considered popular for a given month (since we have 3 years of data, minimum can be 0, maximum can be 3)
    It then creates and applies a mask to the array, filtering all months that don't occur as many times as the most popular month(s).
    Then it drops all NaN values, and finds the indices (months) that are left.
    Lastly it creates a string that contains all months for which the dog was most popular, which is printed, informing the user.

    Args:
        dog_breed_input: dog breed inputted by the user.
        data: DataFrame containing all data from CalgaryDogBreeds.xlsx formatted

    Returns:
        nothing, it just prints to the console.
    """
    monthly_counts = data.loc[dog_breed].groupby('Month').count() #creates a dataframe that contains months, and the number of their occurances for the given breed within 'data'
    popular_months = monthly_counts[monthly_counts == monthly_counts.max()] #creates a dataframe that removes months that dont tie with the maximum value of occurances
    popular_months = popular_months.dropna().index # gives an array of months that have a non NaN value (this corresponds with months that have the highest popularift for specific breed)

    popular_months_output = " ".join(popular_months) # creates a string of popular_months separted by a space
    #below 2 lines just handle the printing/output
    popular_months_output_string = f" dogs: {popular_months_output}" 
    print("Most popular month(s) for " + dog_breed + popular_months_output_string)

def main():

    # Import data here
    data = pd.read_excel('CalgaryDogBreeds.xlsx') #importing data from excel
    data.set_index(keys=['Breed', 'Year', 'Month'], inplace=True) #sets index for the data, formatting the dataframe, first by breed, then year, then month
    data.sort_index(inplace=True) #sorts the data

    print("ENSF 692 Dogs of Calgary")


    # User input stage

    #while true makes the loop permanent unless broken out of. this allows to propmt the user for a valid input
    while True:
        try:
            dog_breed_input = input("Please enter a dog breed: ").upper() #prompts the user for input, assigns their input (uppercased) to a variable
            if (dog_breed_input in data.index.get_level_values('Breed')): #if the input is contained in the 'Breed' column, then proceed

               
                # Data anaylsis stage

                #prints the years for which the user inputter dog breed was popular
                years_popular(dog_breed_input,data)    

                #prints the total number of user inputted dogs registered
                get_total(dog_breed_input, data)

                #prints the portion of all dogs registered that are of the user inputted breed as a percentage for a given year. one line for each year (see below)
                breed_portion_of_year(dog_breed_input, data, 2021)
                breed_portion_of_year(dog_breed_input, data, 2022)
                breed_portion_of_year(dog_breed_input, data, 2023)

                #prints the portion of all dogs registered that are of the user inputted breed as a percentage for the whole dataset timeframe.
                percentage_of_all(dog_breed_input, data)
                
                #prints the list of months for which the dog breed was most popular
                popular_months(dog_breed_input, data)

                quit() #ends the program
            else:
                raise KeyError #if user input is invalid, raise KeyError
        except KeyError as e:
            print("Dog breed not found in the data. Please try again.")


if __name__ == '__main__':
    main()
