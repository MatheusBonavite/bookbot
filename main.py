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
    # TODO: go back once the assignment is delivered
    #clean_word = clean_up_word(word)
    if len(word) == 0:
        return
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1

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

def count_characters(characters, words):
    for word, count in words.items():
        for character in word:
            if not character.isalpha():
                continue
            lower_case = character.lower()
            if lower_case in characters:
                characters[lower_case] += count
            else:
                characters[lower_case] = count

def report(amount_of_words, characters, words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{amount_of_words} words found in the document\n")
    sorted_by_characters = dict(sorted(characters.items(), key=lambda item : item[1], reverse=True))
    for character, count in sorted_by_characters.items():
        print(f"The '{character}' character was found {count} times")
    print("--- End report ---")

def main():
    words = {}
    with open("books/frankenstein.txt") as file:
        for line in file:
            word_counter(line.strip(), words)
    accum = 0
    for word, count in words.items():
        accum += count
    characters = {}
    count_characters(characters, words)
    report(accum, characters, words)

if __name__ == "__main__":
    main()
