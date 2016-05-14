from Functions import index_markets, townresults, zipresults

FindFile = True
Running = True
while FindFile:
    try:
        zips, towns = index_markets(input("File Name? "))
        FindFile = False
    except FileNotFoundError:
        print("File not found, or it is not in the right directory.")

print("Welcome to the Farmers Market Finder; Find your local fresh foods!")
print("Type quit at any time to exit the program.")

while Running:
    query = str(input("What is the name of your zip code or town? "))
    if query == "quit":
        print("Thank you for using this Farmers Market Finder!")
        Running = False
    # Was the entry blank?
    elif query == "":
        print("No Entry.")
    else:
        try:
            int(query)
            zipresults(query, zips)
        except ValueError:
            townresults(query, zips, towns)
