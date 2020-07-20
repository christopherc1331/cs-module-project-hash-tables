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


def indicate(word):
    if len(word) < 2:
        if word[0] in upper_chars:
            return 0    # ===Start===
    else:
        if (word[0] == '"' or word[0] == '"') and word[1] in upper_chars:
            return 0    # ===Start===

        elif word[-1] == "." or word[-1] == "?" or word[-1] == "!":
            return 1    # ===Stop===

        elif (word[-2] == "." or word[-2] == "?" or word[-2] == "!") and (word[-1] == '"' or word[-1] == "'"):
            return 1    # ===Stop===

        else:
            return 2  # ===Middle===


my_dict = {}


for i in range(len(word_list)):
    curr_word = word_list[i]
    if i < len(word_list) - 1:
        next_word = word_list[i + 1]

    if i > 0:
        prev_word = word_list[i - 1]
        if curr_word not in my_dict[prev_word]["word_after_list"]:
            my_dict[prev_word]["word_after_list"].append(curr_word)

    if curr_word not in my_dict:
        new_word_obj = {}
        new_word_obj["word_after_list"] = []
        new_word_obj["indicator"] = indicate(curr_word)
        my_dict[curr_word] = new_word_obj

    else:
        if next_word:
            if next_word not in my_dict[curr_word]["word_after_list"]:
                my_dict[curr_word]["word_after_list"].append(next_word)


def get_rand_start():
    all_keys = []
    for i in my_dict.items():
        all_keys.append(i[0])
    indicator = 2
    while indicator != 0:
        rand_word = random.choice(all_keys)
        indicator = my_dict[rand_word]["indicator"]

    return rand_word


# print(my_dict)


def generate_sentences(num):

    sentence_count = 0
    sentence = ""

    while sentence_count < num:
        sentence_stopped = False
        curr_word = get_rand_start()
        sentence += curr_word + " "

        while sentence_stopped == False:
            curr_word = my_dict.get(curr_word)
            if len(curr_word["word_after_list"]) > 0:
                curr_word = random.choice(
                    curr_word["word_after_list"])
                sentence += curr_word + " "

                if my_dict[curr_word]["indicator"] == 1:
                    sentence_stopped = True

            else:
                sentence_stopped = True
        sentence_count += 1
        sentence += "\n"
    return sentence


print(generate_sentences(100))

# TODO: construct 5 random sentences
# Your code here
