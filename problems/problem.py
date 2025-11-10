
import doctest 

def max_combo_string_freq(l1: list[str], l2: list[str]) -> str: 
    """
    Given two lists of strings, return the string that appears the most often when 
    combining the strings of each element in the same position.  

    The lists will be of the same size and will not be empty. 
    Assume there will be no ties 

    >>> max_combo_string_freq(["blue", "snow", "bl"], ["jay", "man", "uejay"])
    'bluejay'

    index 0 creates "bluejay"
    index 1 creates "snowman"
    index 2 creates "bluejay"
    "bluejay" appears the most

    >>> max_combo_string_freq(["com", "co", "computer"], ["puter", "mputer", "laptop"])
    'computer'

    """
    pass




def search_cave(cave: list[list[str]], start_row: int, start_col: int, visited=None) -> bool: 
    """
    Given 2d array cave and a starting row and column, determine if there exists 
    a path to the exit, i.e. no walls are blocking an empty path to the edges of the grid  
    Diagonal moves are not aloud  
    Assume the cave is not empty and has the same number of rows as columns. 

    Hint: keep track of what squares you have visited 

    >>> search_cave([
    ...     ['x', 'x', 'x', 'x', 'x', 'x'],
    ...     ['x', 'x', 'x', 'x', 'x', 'x'],
    ...     ['x', 'x', 'x', 'x', 'x', 'x'],
    ...     ['x', 'x', ' ', 'x', ' ', ' '],
    ...     ['x', 'x', ' ', 'x', ' ', 'x'],
    ...     ['x', 'x', ' ', ' ', ' ', 'x'],
    ...     ['x', 'x', 'x', 'x', 'x', 'x']], 3, 2)
    True

    >>> search_cave([
    ...     ['x', 'x', 'x', 'x', 'x', 'x'],
    ...     ['x', 'x', 'x', 'x', 'x', 'x'],
    ...     ['x', 'x', 'x', 'x', 'x', 'x'],
    ...     ['x', 'x', ' ', 'x', ' ', ' '],
    ...     ['x', 'x', ' ', 'x', 'x', 'x'],
    ...     ['x', 'x', ' ', ' ', ' ', 'x'],
    ...     ['x', 'x', 'x', 'x', 'x', 'x']], 3, 2)
    False


    """
    WALL = 'x'
    EMPTY = ' '

    pass 




if __name__ == "__main__": 
    doctest.testmod()

        

