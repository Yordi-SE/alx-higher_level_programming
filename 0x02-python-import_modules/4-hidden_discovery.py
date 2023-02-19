#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list1 = dir(hidden_4)
    for i in range(0, len(list1)):
        if list1[i][0] == "_" and list1[i][1] == "_":
            continue
        else:
            print(list1[i])
