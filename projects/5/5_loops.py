#          0  1  2  3  4
value_8 = [1, 4, 6, 8, 9]  # tuple, set

for i in value_8:
    if i < 7:
        # continue
        break
    else:
        print(i*i)
value7 = {
    "key_1": "value_1",
    "key_2": 10,
    "key_3": True
}

for key, value in value7.items():  # (key, value) #
    print(f"{key}:  {value} type - {type(value)}")

index = 0
while index < 100:
    index += 1
    if index % 2 != 0:
        continue
    print(index)
    # if index == 88:
    #     break