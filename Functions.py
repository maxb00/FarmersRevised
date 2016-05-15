# Indexing markets in chosen file
def index_markets(location):

    # Creating blank dictionaries
    ziplist = {}
    townlist = {}

    # Open file and skip info line
    m = open(location, 'r')
    m.readline()

    # Splitting output into dictionary
    for entry in m:
        info = entry.strip().split(',')
        town = str(info[4])
        localzip = str(info[7])
        # Checking to make sure a town is present
        if town == '':
            continue
        # Checking if entry already exists, then adding.
        if town not in townlist:
            townlist[town] = []
            townlist[town].append(localzip)
        else:
            townlist[town].append(localzip)
        # Checking if localzip entry exists, then adding all market info.
        if localzip not in ziplist:
            ziplist[localzip] = []
            ziplist[localzip].append((info[1], info[2], info[3], info[4], info[6], info[7]))
        else:
            ziplist[localzip].append((info[1], info[2], info[3], info[4], info[6], info[7]))
    return ziplist, townlist


# Searching zip dictionary
def zipresults(query, markets):
    # Create blank list for results
    results = []

    # Sift through list of all markets and index them into tuples
    try:
        for i in markets[query]:
            results.append((i[0],  i[1], i[2], i[3], i[4], i[5]))

    # Handling a Zip not found or incorrect
    except KeyError:
        return "Zip Code not found. Maybe your local market is not listed?"

    # Returning results of zip search to main functions
    return results


# Searching town dictionary
def townresults(query, zips, towns):

    # Create blank list for results
    results = []

    # Sift through list of all markets and index them into tuples
    try:
        for i in towns[query]:
            x = zips[i][0]
            results.append((x[0],  x[1], x[2], x[3], x[4], x[5]))

    # Handling a town that is not there or is spelled incorrectly.
    except KeyError:
        return "Town could not be found. Maybe your local market is not listed?"

    # Returning results of town search to main functions
    return results


# Format and print results
def printresults(results):

    # Iterate through tuples, format them to be presentable and READABLE
    for i in results:
        print("Market name:", i[0])
        print("Website:", i[1])
        print("Street Address:", i[2], i[3], i[4], i[5])
        print("-")
