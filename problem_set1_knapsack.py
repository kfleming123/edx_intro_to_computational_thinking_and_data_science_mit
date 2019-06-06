###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips = []
    # Transform the dictionary to sorted list
    cow_list = [[k, cows[k]] for k in sorted(cows, key=cows.get, reverse=True)]
    while len(cow_list) > 0:
        totalWeight = 0
        temp = []
        temp_list = cow_list.copy()
        for cow in temp_list:
            if totalWeight + cow[1] <= limit:
                temp.append(cow[0])
                cow_list.remove(cow)
                totalWeight += cow[1]
        trips.append(temp)
    return trips

# Problem 2
# Helper to calculate weight of trip
def calc_weight(lst, dic):
    total_weight = 0
    for i in lst:
        total_weight += dic[i]
    return total_weight
    
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Transform the dictionary to sorted list
    cow_list = [k for k in cows]
    list_of_combos = []
    for partition in get_partitions(cow_list):
        list_of_combos.append(partition)
    list_of_combos.sort(key=len)
    for combo in list_of_combos:
        greater = 0
        for i in range(len(combo)):
            weight = calc_weight(combo[i], cows)
            if weight > limit:
                greater += 1
        if greater == 0:
            return combo
            
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    limit=10
    #print(cows)
    
    start1 = time.time()
    greedy = greedy_cow_transport(cows, limit)
    end1 = time.time()
    print('Greedy trips: ', len(greedy),'Greedy time:', end1 - start1)
    start2 = time.time()
    brute = brute_force_cow_transport(cows, limit)
    end2 = time.time()
    print('Brute trips: ', len(brute), 'Brute time:', end2 - start2)

"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

#cows = load_cows("ps1_cow_data.txt")
#limit=10
#print(cows)

#greedy_cow_transport(cows, limit)
#brute_force_cow_transport(cows, limit)
#print(brute_force_cow_transport({'Milkshake': 40, 'Miss Bella': 25, 'Lotus': 40, 'Horns': 25, 'Boo': 20, 'MooMoo': 50}, 100))
compare_cow_transport_algorithms()