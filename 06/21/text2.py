def count_words(filename):
    try:
        with open(filename,encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"sorry,the file{filename} not found")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words")

filename = 'D:\\file2.txt'
count_words(filename)
