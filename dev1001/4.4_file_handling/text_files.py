# Default mode is '(r)ead' and 'w' for write, 'a' for append.
file = open('my_first_file.txt', 'a') 
file.write('Hello\n')
file.close()

# Read (sequential access)
# 'with' automatically closes the file when it ends.
with open('my_first_file.txt') as f:
    # Read the whole file into a variable.
    # Files internally track their current position.
    # all_content = f.read(20) # Read the first 20 characters.
    # new_content = f.read(10) # Read the next 10 characters after the first 20.
    # print(all_content)
    # print(new_content)
    first_line = f.readline()
    print(first_line.strip())
    second_line = f.readline()
    print(second_line)
