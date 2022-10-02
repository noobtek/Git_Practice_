str_ = "sony india"
for index, char in enumerate (str_):
    if char == "n":
        print(str_[index::], end=" ")

l_ = [str_[index::] for index, char in enumerate(str_) if char == "n"]
print(l_)
