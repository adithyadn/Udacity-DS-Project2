import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    output = list()
    find_files_rec(suffix, path, [], output)
    return output

def find_files_rec(suffix, path, stack, output):
    #print("called for " + path + " :: " + str(stack))

    #print(os.path.isfile(path))
    if os.path.isfile(path) and path.endswith(suffix):
        #print("returning path " + path)
        output.append(path)

    if os.path.isdir(path):
        stack.extend([path + "/" +file for file in os.listdir(path)])
        #print("stack has :: " + str(stack))

    if len(stack) == 0:
        return output

    find_files_rec(suffix, stack.pop(), stack, output)





print(find_files(".c", "./testdir"))
# Let us print the files in the directory in which you are running this script
print(str(os.walk("testdir", True)))
# Let us check if this file is indeed a file!
print (os.path.isfile("./testdir/t1.c"))

# Does the file end with .py?
print ("./ex.py".endswith(".py"))

assert find_files(".c", "./testdir/subdir1") == ['./testdir/subdir1/a.c']
assert find_files(".h", "./testdir/subdir1") == ['./testdir/subdir1/a.h']
assert len(find_files(".c", "./testdir")) == 4
assert len(find_files(".c", "./testdir/subdir4")) == 0