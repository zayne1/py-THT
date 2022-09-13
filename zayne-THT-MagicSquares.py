# Magic Squares
##################

# Todo:
# Possibly refactor all of this into a Class, so that it can be imported
# as a module.

# Create multi dimensional representation of magic square box, to size
def create_list(box_size):
    x = [[] for y in range(box_size)]
    
    for y in range(box_size):
        for i in x:
            i.append('')

    return x


def check_is_top_row(cur_row):
    if cur_row == 0:
        return True


def check_top_right_field_empty(cur_row, cur_col,list,box_size):
    if check_is_top_row(cur_row) or check_at_right_border(cur_col, box_size):
        return False
    elif bool(list[max(0, cur_row-1)][min(box_size-1, cur_col+1)]):
        return False
    else:
        return True


def check_at_right_border(cur_col, box_size):
    if cur_col == (box_size - 1):
        return True


def check_bottom_field_empty(cur_row, cur_col, list, box_size):
    if not bool(list[min(box_size-1, cur_row+1)][cur_col]):
        return True

# display
def print_magic_square(list):
    print("\r\n\r\n\r\n")
    print('    ███╗░░░███╗░█████╗░░██████╗░██╗░█████╗░  ░██████╗░██████╗░██╗░░░██╗░█████╗░██████╗░███████╗░██████╗')
    print('    ████╗░████║██╔══██╗██╔════╝░██║██╔══██╗  ██╔════╝██╔═══██╗██║░░░██║██╔══██╗██╔══██╗██╔════╝██╔════╝')
    print('    ██╔████╔██║███████║██║░░██╗░██║██║░░╚═╝  ╚█████╗░██║██╗██║██║░░░██║███████║██████╔╝█████╗░░╚█████╗░')
    print('    ██║╚██╔╝██║██╔══██║██║░░╚██╗██║██║░░██╗  ░╚═══██╗╚██████╔╝██║░░░██║██╔══██║██╔══██╗██╔══╝░░░╚═══██╗')
    print('    ██║░╚═╝░██║██║░░██║╚██████╔╝██║╚█████╔╝  ██████╔╝░╚═██╔═╝░╚██████╔╝██║░░██║██║░░██║███████╗██████╔╝')
    print('    ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░╚════╝░  ╚═════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░')
    print("\r\n\r\n\r\n")
    

    strRow=''
    strDividers=''
    i=0

    for row in list:
        
        i+=1
        strRow=''
        strDividers=''

        for item in row:
            strItem = str(item).ljust(3)
            strRow+=' ' + strItem + '|'
            strDividers+= '____|'
        
        if i % 2:
            print('                                          |' + strDividers)
        print('                                          |' + strRow)
        if i % 2:
            print('                                          |' + strDividers)


def validate(magic_constant, list, box_size):
    counter=0
    colCount=0
    rowCount=0

    # Test if rows add up the magic_constant
    for row in list:
        counter=0
        for item in row:
            counter+=item

        if counter != magic_constant:
            return False

    
    # Test if cols add up the magic_constant
    counter=0
    for row in list:
        counter=0
        
        for item in row:            
            counter+=list[colCount][rowCount]

            if colCount == box_size-1: # hit the limit
                colCount=0
            else:
                colCount=min(box_size-1, colCount+1)
        
        if rowCount == box_size-1: # hit the limit
            rowCount = 0
        else:
            rowCount=min(box_size-1, rowCount+1)                

        if counter != magic_constant:
                return False            

    # print([sum(x) for x in zip(*list)]) # Shorter col addition method

    return True


def main():
    # We use a try block to capture the string input error, so that we can show a nicer err mesg
    try:
        box_size = int(input("Enter a positive, odd number: "))

        box_slots= box_size ** 2 # Tot num of 'slots' in our 'box' (array)
        last_row=box_size-1
        cur_col=int((box_size-1)/2) # start at middle index item of our odd number
        cur_row=0

        if box_size % 2 !=0 and box_size > 0: # validate number
            magic_constant = box_size * ((box_size*box_size) + 1)/2 # 15 for 3, 65 for 15
            list = create_list(box_size)

            # set first array item
            list[cur_row][cur_col]=1 # we always start with 1, in the center col of array/list

            for i in range(2, box_slots+1):

                # if top right field is empty..
                if check_top_right_field_empty(cur_row, cur_col,list,box_size):
                    
                    list[cur_row-1][cur_col+1]=i # enter num into top left field
                    
                    # move our current col/row pointer to where it we just worked
                    cur_row=max(0, cur_row-1)
                    cur_col=min(box_size-1, cur_col+1)

                # if we're at top row
                elif check_is_top_row(cur_row) and check_at_right_border(cur_col, box_size):
                    
                    # test if bottom field is emptu
                    if check_bottom_field_empty(cur_row, cur_col, list,box_size):

                        list[min(box_size-1, cur_row+1)][cur_col]=i # enter num into bottom field
                        
                        # move our current col/row pointer to where it we just worked
                        cur_row=min(box_size-1, cur_row+1)

                # if we're at top row
                elif check_is_top_row(cur_row):

                    # check if bottom row, next col has no val
                    if not bool(list[last_row][min(box_size-1, cur_col+1)]):
                        
                        list[last_row][cur_col+1]=i # enter num into last row, next col

                        # move our current col/row pointer to where it we just worked
                        cur_row=last_row
                        cur_col=min(box_size-1, cur_col+1)
                    else:
                        continue

                # if we're at right most col
                elif check_at_right_border(cur_col, box_size):
                    
                    # check if prev row, first col has no val
                    if not bool(list[cur_row-1][0]): 
                        
                        list[cur_row-1][0]=i # enter num into prev row, left most col

                        # move our current col/row pointer to where it we just worked
                        cur_row=max(0, cur_row-1)
                        cur_col=0
                    else:
                        continue

                #is bottom field empty?
                elif check_bottom_field_empty(cur_row, cur_col, list,box_size):
                    
                    list[min(box_size-1, cur_row+1)][cur_col]=i # enter num into bottom row of current col

                    # move our current col/row pointer to where it we just worked
                    cur_row=min(box_size-1, cur_row+1)

            # display graphic output
            print_magic_square(list)
            
            # validate if a true magic num
            if validate(magic_constant, list, box_size):
                print("correct \r\n\r\n\r\n")
            else:
                print('-- Magic Square is invalid --')

        else:
            print("\r\nInvalid entry, please enter a positive, odd number.")
            return main() ## recursive, to restart if bad entry given

    except ValueError as err: 
        print('The following exception was caught:')
        print('-> ' + str(err))

  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()
