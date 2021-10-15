def swap_last_item(list_input):
    '''
    Takes in a list input and switches the first and last item in the list.
    The modified list is then outputed.
    '''
    size = len(list_input)
    temp = list_input[size - 1]
    list_input[size - 1] = list_input[0]
    list_input[0] = temp
    return list_input
    