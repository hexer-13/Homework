string = ("one word two word three word four word five word twenty words already "
          "one two three four five six seven eight ten more wait did you just say "
          "SIX SEVEN ok that's enough words already I'm not supposed to actualy put 1000 words here yea?"
          "the best I can do is a a a a a a a a a a a a a aa  a a aaa aaa a")


str_list = list(string.lower().split())
word_dict = dict()


for word in str_list:
    word_dict[word] = word_dict.get(word, 0) + 1


print(word_dict)
