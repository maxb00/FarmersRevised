# Call from functions file
from Functions import index_markets, townresults, zipresults, printresults

# Open loops for later
FindFile = True
Running = True

# Finding the chosen list of markets
while FindFile:
    try:
        # Calling first function, assinging results to two variables for later
        zips, towns = index_markets(input("File Name? "))

        # for quick use in debugging
        # zips, towns = index_markets('markets-updated.csv')

        # If file was found, end the loop
        FindFile = False

    # FileNotFoundError for making sure file is readable and exists in specified place
    except FileNotFoundError:
        print("File not found, or it is not in the right directory.")

# Welcome statement
print("Welcome to the Farmers Market Finder; Find your local fresh foods!")
print("Type quit at any time to exit the program.")

# Main loop
while Running:
    # Query user for zip or town
    query = str(input("What is the name of your zip code or town? "))

    # Check if they want to quit
    if query == "quit":
        print("Thank you for using this Farmers Market Finder!")
        Running = False

    # Was the entry blank?
    elif query == "":
        print("No Entry.")

    # If none of the above search starts
    else:

        # Checking for int, and therefor zip
        try:
            int(query)
            results = zipresults(query, zips)

            # Print and format results of zip search
            printresults(results)

        # If entry was not castable to an int, it must be a town
        except ValueError:
            results = townresults(query, zips, towns)

            # Print and format results of town search
            printresults(results)
