import random
import string

lower_chars = string.ascii_lowercase
upper_chars = string.ascii_uppercase

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
word_list = words.split()
first_word = random.choice(word_list)
print(first_word)


def indicate(word):
    if len(word) < 2:
        if word[0] in upper_chars:
            return 0    # ===Start===
    else:
        if word[0] == '"' and word[1] in upper_chars:
            return 0    # ===Start===

        elif word[-1] == "." or word[-1] == "?" or word[-1] == "!":
            return 1    # ===Stop===

        elif (word[-2] == "." or word[-2] == "?" or word[-2] == "!") and word[-1] == '"':
            return 1    # ===Stop===

        else:
            return 2  # ===Middle===


my_dict = {}


for i in range(len(word_list)):
    curr_word = word_list[i]
    if i < len(word_list) - 1:
        next_word = word_list[i + 1]

    if curr_word not in my_dict:
        new_word_obj = {}
        new_word_obj["word_after_list"] = []
        new_word_obj["indicator"] = indicate(curr_word)
        my_dict[curr_word] = new_word_obj

    else:
        if next_word:
            if next_word not in my_dict[curr_word]["word_after_list"]:
                my_dict[curr_word]["word_after_list"].append(next_word)

print(my_dict)


# TODO: construct 5 random sentences
# Your code here
