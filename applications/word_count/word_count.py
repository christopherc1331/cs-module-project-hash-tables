import string


def word_count(s):
    # Your code here
    alpha = string.ascii_lowercase

    words = s.split(" ")
    for i in range(len(words)):
        words[i] = words[i].lower()
    new_words = []

    for i in range(len(words)):
        new_word = ""
        for x in range(len(words[i])):
            curr_letter = words[i][x]
            if curr_letter in alpha:
                new_word += curr_letter

        new_words.append(new_word)

    my_dict = {}

    for word in new_words:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1

    return my_dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
