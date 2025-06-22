diary_file = "diary_entry.txt"

# 1. Write two lines about your day (use 'w' mode)
with open(diary_file, 'w') as f:
    f.write('I worked from home today.\n')
    f.write('I have Coder Academy this evening.\n')

# 2. Read and print content (use 'r' mode)
with open(diary_file) as f:
    # print(f.read())
    for line in f:
        print(line.strip())