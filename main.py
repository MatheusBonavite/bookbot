def is_upper(character):
    return character >= 'A' and character <= 'Z'

def is_lower(character):
    return character >= 'a' and character <= 'z'

def is_word(word):
    if len(word) <= 0:
        return False
    if is_upper(word[0])  and is_upper(word[len(word) - 1]):
        return True
    if is_upper(word[0])  and is_lower(word[len(word) - 1]):
        return True
    if is_lower(word[0])  and is_upper(word[len(word) - 1]):
        return True
    if is_lower(word[0])  and is_lower(word[len(word) - 1]):
        return True
    return False

def word_counter(line):
    stripped_lines = line.strip().split(" ")
    only_words = list(filter(is_word, stripped_lines))
    return len(only_words)

def main():
    accum = 0
    with open("books/frankenstein.txt") as file:
        for line in file:
            accum += word_counter(line)
    print(accum)


main()
