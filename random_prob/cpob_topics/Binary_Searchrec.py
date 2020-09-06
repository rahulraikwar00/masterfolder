# n = number we are searching for
# lst = the sorted list we are searching in
# sp = list start position
# ep = list end postion
def binary_search_recursion(n: int, lst: list, sp: int = 0, ep: int = None):
    # first time searching, start position will be 0
    # and end position will be None
    if ep is None:
        # End position equals total length minus 1 since 0 indexed
        ep = len(lst) - 1

    # get the midpoint of the list (lst)
    mid = (sp + ep) // 2
    mid_item = lst[mid]
    print(f"Start: lst[{sp}] = {lst[sp]}\nMid: lst[{mid}] = {mid_item}\nEnd: lst[{ep}] = {lst[ep]}")
    # If mid item matches the searching number then success
    if mid_item == n:
        print(f"Success!!! Number {n} found in lst[{mid}]")
        return True
    # Else if mid item is greater than number, we eliminate everything to the left and move right
    elif mid_item > n:
        new_ep = mid - 1  
        if new_ep < 0: 
            print(f"Number {n} is too low. Lowest number found is {lst[sp]}")
            return False
        else:
            print(f"Number {n} is less than mid item {mid_item}, change ep {ep} to {new_ep}.\n")
            binary_search_recursion(n, lst, sp, new_ep)
    # Else if mid item is lower than number, we eliminate everything to the right and move left
    elif mid_item < n:
        new_sp = mid + 1
        if new_sp > ep:
            print(f"Number {n} is too High. Highest number found is {lst[ep]}")
            return False
        else:
            print(f"Number {n} is greater than mid item {mid_item}, change sp {sp} to {new_sp}.\n")
            binary_search_recursion(n, lst, new_sp, ep)
num_list = [10,20,30,40,50,60,70,80,90,100,110]
binary_search_recursion(10, num_list)