#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden
str = dir(hidden)
for i in str:
    if i.startswith("__"):
        continue
    else:
        print("{}".format(i))
