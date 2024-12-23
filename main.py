
def word_counter(line):
    stripped_lines = line.strip().split(" ")
    is_word = lambda sline : len(sline) > 0 and ((sline[0] >= 'A' and sline[len(sline) - 1] <= 'Z') or (sline[0] >= 'a' and sline[len(sline) - 1] <= 'z'))
    only_words = list(filter(is_word, stripped_lines))
    return len(only_words)

def main():
    accum = 0
    with open("books/frankenstein.txt") as file:
        for line in file:
            accum += word_counter(line)
    print(accum)


main()
