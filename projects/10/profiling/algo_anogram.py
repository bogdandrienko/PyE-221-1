from typing import OrderedDict


# OrderedDict

def clear_method(src1: str, src2: str) -> bool:  # N(log(n)):   O(n) >  O(log(n)) < O(1)
    return sorted(src1) == sorted(src2)


def dirty_method(src1: str, src2: str) -> bool:
    if len(src1.split(" ")) != len(src2.split(" ")):  # пограничные условия (баги)
        return False

    # пограничные условия (баги)
    for i in src1:
        if i not in src2:  # если хоть один символ не такой как в другом слове, то это не аннограмма
            return False

    set1 = set(src1)
    print(set1, src1)  # {'t', 'e', 'a'} teaa
    set2 = set(src2)
    print(set2, src2)  # {'t', 'e', 'a'} eatt

    set1.intersection()
    set1.difference()

    return True


def middle_method(src1: str, src2: str) -> bool:
    if len(src1.split(" ")) != len(src2.split(" ")):  # пограничные условия (баги)
        return False

    dict1 = {}
    for i in src1:
        # if dict1.get(i, None) is None:
        #     dict1[i] = 1  # ЕСЛИ
        # else:
        #     dict1[i] += 1  # ЕСЛИ
        dict1[i] = dict1.get(i, 0) + 1

    for i in src2:
        elem = dict1.get(i, None)  # ЕСЛИ
        if elem is None or elem < 0:
            return False
        else:
            dict1[i] -= 1  # ЕСЛИ
            if dict1[i] == 0:
                del dict1[i]  # ЕСЛИ
    return dict1 == {}  # ЕСЛИ

    # dict2 = {"a": 3}
    # -= -= -=
    # dict2 = {}

    # dict2 = {}
    # for i in src2:
    #     dict2[i] = dict2.get(i, 2) + 1
    # print(dict2)

    # list1 = [1, 2, 3]
    # list2 = [3, 2, 1]

    # for k, v in dict1.items():
    #     elem = dict2.get(k, None)
    #     if elem is None or elem != v:
    #         return False
    #
    # return dict1 == dict2


if __name__ == "__main__":
    str1 = "aeta"
    str2 = "aeta"
    str3 = "ter"

    source = "австралопитек"
    equal1 = "ватерполистка"
    equal2 = "ватерпрлистка"

    # res = clear_method(str1, str2)
    # res = dirty_method(str1, str2)
    res = middle_method(str1, str2)
    # res = clear_method(source, equal2)
    if res:
        print("Аннограммы")
    else:
        print("Не аннограммы")

    # dict8 = {"name": "Alice", "age": 20}
    # dict9 = {"age": 20, "name": "Alice"}

    # print(dict9 == dict8)
