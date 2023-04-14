# Part 2, with tasks and TODOs

'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members

    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''

    # TODO: Open the currentMem file as in r+ mode
    # TODO: Open the exMem file in a+ mode
    # TODO: Read each member in the currentMem (1 member per row) file into a list.
    # Hint: Recall that the first line in the file is the header.

    # TODO: iterate through the members and create a new list of the innactive members

    # Go to the beginning of the currentMem file
    # TODO: Iterate through the members list.
    # If a member is inactive, add them to exMem, otherwise write them into currentMem

def cleanFiles(memReg, exMem):
    with open(memReg, 'r+') as currentMem:
        with open(exMem, 'a+') as ex:
            header = "Membership No  Date Joined  Active  \n"

            members = currentMem.readlines()
            currentMem.seek(0, 0)
            currentMem.write(header)
            for mem in members:
                if 'no' in mem:
                    ex.write(mem)
                else:
                    currentMem.write(mem)
            currentMem.truncate()


# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg, exReg)


with open(memReg, 'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg, 'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())



