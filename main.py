def test_space_ascii(character):
    return ord(character) != 32

def clean_up_word(word):
    upper_valid_characters = tuple([65,90])
    lower_valid_characters = tuple([97,122])
    valid_punctuation_characters = ['.', '-', '/', '\'']
    valid_word = ""
    for character in word:
        if ord(character) >= upper_valid_characters[0] and ord(character) <= upper_valid_characters[1]:
            valid_word += character
        if ord(character) >= lower_valid_characters[0] and ord(character) <= lower_valid_characters[1]:
            valid_word += character
        if character in valid_punctuation_characters:
            valid_word += character
    return valid_word

def add_word_in_dict(word, words_dict):
    clean_word = clean_up_word(word)
    if len(clean_word) == 0:
        return
    if clean_word in words_dict:
        words_dict[clean_word] += 1
    else:
        words_dict[clean_word] = 1

def word_counter(line, words):
    # Temporary variable to keep the current word until next punctuation, special character, etc...
    current_word = ""
    # Iterating over each character in the line
    for character in line:
        if (test_space_ascii(character)):
            current_word += character
        else:
            add_word_in_dict(current_word, words)
            current_word = ""
    # The last valid word was not accounted before
    add_word_in_dict(current_word, words)
    return words

def main():
    words = {}
    with open("books/frankenstein.txt") as file:
        for line in file:
            word_counter(line.strip(), words)
    accum = 0
    for word, count in words.items():
        accum += count

if __name__ == "__main__":
    main()
