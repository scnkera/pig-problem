def pig_latin(sentence):
    # Write your solution here!
    # word_list = []

    word_list = sentence.split()
    new_word_list = []

    for word in word_list:
        new_word_list.append(word_update(word))

    response = " ".join(new_word_list)

    return response


def word_update(word):
    if word[0] in 'aeiou':
        return word

    new_word = f'{word[1:]}{word[0]}ay'

    return new_word


# pig_latin("something")

# # Test cases
assert pig_latin("something") == "omethingsay"
assert pig_latin("awesome") == "awesome"
assert pig_latin("latin is a hard language") == "atinlay is a ardhay anguagelay"
assert pig_latin("y") == "yay"
assert pig_latin("e") == "e"

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")