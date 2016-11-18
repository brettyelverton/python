# CADET BRETT YELVERTON
# X97226
def index_div(string,integer):
    """
    >>> index_div('abcdefgh', 4)
    'c'
    >>> index_div('ab', 2)
    'b'
    >>> index_div('', 3)
    Traceback (most recent call last):
     ...
    ValueError: empty text string not allowed
    >>> index_div('a', 2)
    Traceback (most recent call last):
     ...
    ValueError: string length not divisible by index
    >>> index_div('abc', 2)
    Traceback (most recent call last):
     ...
    ValueError: string length not divisible by index
    >>> index_div('a', 0)
    'a'
    >>> index_div('a', 1)
    'a'
    >>> index_div('abcde', 1)
    'e'
    >>> index_div('abcd', 4.0)
    Traceback (most recent call last):
     ...
    TypeError: string indices must be integers
    >>> index_div('abcd', 3.0)
    Traceback (most recent call last):
     ...
    ValueError: string length not divisible by index
    >>> index_div('abcd', 'efg')
    Traceback (most recent call last):
     ...
    TypeError: unsupported operand type(s) for %: 'int' and 'str'
    """
    maxChar = len(string) - 1
    if len(string) <= 0:
        raise ValueError("empty text string not allowed")
    else:
        if len(string) % integer != 0:
            raise ValueError("string length not divisible by index")
        else:
            try:
                indexLocation = len(string) / integer
                return string[indexLocation]
            except ZeroDivisionError:
                return string[0]

            except IndexError:
                return string[maxChar]

def file_mangle(input,output):
    """
    >>> file_mangle('eecummings.txt','output.txt')
    >>> open('output.txt').read() == open('expected.txt').read()
    True
    """
    # CDT Russell, Conner D1, 2019. Helped me figure out the the string methods
    # needed in order to fill out the padding of zeroes in the digit only lines
    # by showing me the zfill string method.
    # Showed me the string method isdigits which helped me to identify digits only
    # lines. He also assisted me by showing me a method of getting the program to
    # identify the appropriate strings to make changes to in the input file. West
    # Point, NY. 20SEP16
    input_text = file.open(input,'r')
    output_text = file.open(output,'w')
    linecount = 0
    import string
    for line in input_text.readlines():
        linecount += 1
        #digit only
        stripIndent = line.strip()
        stripHyphen = stripIndent.strip('-')
        if stripIndent.isdigits() == True:
            line = line.strip()
            line = line.zfill(10)
            line += "\n"
            output_text.write(line)
            continue

    #for changing digits to pound signs
        for char in line:
            if char in string.digits:
                line = line.replace(char,'#')
                continue

    #Letter line methods
        if linecount % 3 == 0 and linecount % 2 == 0:
            line = line[::-1] 
            line = line.swapcase()
            line = line.strip()
            line += '\n'
            output_text.write(line)
            continue

        if linecount % 2 == 0:
            line = line[::-1]
            line = line.strip()
            line += '\n'
            output_text.write(line)
            continue

        if linecount % 3 == 0:
            line = line.swapcase()
            line = line.strip()
            line += '\n'
            output_text.write(line)
            continue

    #if no change is made to line
        else:
            output_text.write(line)
            continue

    output_text.close()
    input_text.close()

                    
        

if __name__=='__main__':
    import doctest
    doctest.testmod()


    
