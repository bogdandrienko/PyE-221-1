value1 = 10  # - 100
value2 = 10.0  # -10.6
value3 = True  # False
value4 = ""
value5 = "10"
value6 = "Hello"
str1 = b'\x01\x02\x03\x04\x05'
str2 = "\n \t  I'am "
str3 = """\n \t  I'am """
str4 = '''\n \t  I'am '''
str5 = '\n \t \\ I\'am '
str6 = r"\n\tC:\Users\bogdan\Desktop\Django\Курс лекций Django1\Python"



value7 = {
    10: "value_1",
    11.0: "value_1",
    True: "value_1",
    False: "value_1",
    (True, "value_1",): "value_1",
    "key_1": "value_1",
    "key_2": value2,
    "key_3": True,
    "key_4": {
        "key_1": "value_1",
        "key_2": value2,
        "key_3": "Bogdan",
        "key_4": True,
    },
}

tup1 = (True, "value_1",)
# tup1 = (*tup1, "12",)

str55 = "key_1"
# str55[3]= 12

print(value7["key_4"]["key_3"])

value_8 = [True, "value_1", [True, "value_1", False, ], True]
value_8[1] = "value_2"
# value_8.
value_9 = (True, "value_1",)
value_10 = {"key_1",
            "key_2",
            "key_2",
            "key_3"}
print(value_10)

value_8_unique = []
for i in value_8:
    if i not in value_8_unique:
        value_8_unique.append(i)

    # else:
    #     print("такое значение уже есть")
#