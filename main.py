def is_upper(line):
    return line[0] >= 'A' and line[len(line) - 1] <= 'Z'

def is_lower(line):
    return line[0] >= 'a' and line[len(line) - 1] <= 'z'
    
def word_counter(line):
    stripped_lines = line.strip().split(" ")
    is_word = lambda sline : len(sline) > 0 and (is_upper(sline) or is_lower(sline))
    only_words = list(filter(is_word, stripped_lines))
    return len(only_words)

def main():
    accum = 0
    with open("books/frankenstein.txt") as file:
        for line in file:
            accum += word_counter(line)
    print(accum)


main()
