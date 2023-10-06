import heapq
import time


# Generates a list of n list sizes.
def generate_list_of_lists(n):
    king = []
    for prince in range(1, n+1):
        king.append(prince)
    return king


# list_sizes is the list of the sizes of the list.
def calc_total_cost(list_sizes):
    total_cost = 0

    # Heapify will convert the regular list into a minimum heap. This will run in O(n).
    heapq.heapify(list_sizes)

    # Check heap has more than one value, amount of lists gets smaller.
    while len(list_sizes) > 1:

        # Remove smallest list sizes from minimum_heap (This is O(log(n))).
        list1_size = heapq.heappop(list_sizes)
        list2_size = heapq.heappop(list_sizes)

        # Calculate current cost of list1_size and list2_size and add to existing total cost.
        current_cost = list1_size + list2_size
        total_cost += current_cost

        # Insert cost to minimum heap as a new element.
        heapq.heappush(list_sizes, current_cost)

    # Value that’s left in minimum heap is the size of the lists.
    return total_cost


if __name__ == "__main__":

    # Gives the user the option to enter how many list sizes they want.
    n_list = int(input("Enter n lists: "))

    # Generates n number list sizes
    list_of_lists = generate_list_of_lists(n=n_list)

    # Start time (in ns) of when the merge total cost function runs.
    start = time.perf_counter_ns()

    # Invokes the merge total cost function and passes the list of lists to it.
    merge_total_cost = calc_total_cost(list_of_lists)

    # End time (in ns) of when the merge total cost function runs.
    end = time.perf_counter_ns()

    # Calculates how long the function ran for in nanoseconds.
    print("Time run of merge total cost function: ")
    print(end - start)

    # Outputs the total cost for merging n number lists of 1 to n sizes.
    print("Merge total cost: ")
    print(merge_total_cost)
