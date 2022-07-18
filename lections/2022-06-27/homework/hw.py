import time

text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eu magna sit amet neque lobortis dignissim. 
Mauris vehicula lacinia bibendum. Phasellus elementum ipsum et mi mollis, sed eleifend elit pharetra. Donec interdum 
tempus ligula non vulputate. Cras mollis rhoncus facilisis. Fusce at viverra magna, id tempor nulla. Quisque at felis 
eget arcu gravida efficitur eget ac enim. Etiam quisque efficitur lorem at lorem dictum, a sagittis ipsum pulvinar. 
Maecenas elit nisi, iaculis a dolor id, tempor molestie dolor. Pellentesque aliquet non orci at convallis. Donec 
laoreet nisl quam. Ut accumsan, dui ut mattis ultricies, est nulla semper est, eget pulvinar magna lacus ut risus. 
Duis sed hendrerit odio. Etiam scelerisque nunc quis placerat interdum. Nam condimentum enim ac justo fermentum, 
et imperdiet purus finibus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Mauris bibendum urna vitae 
ullamcorper pellentesque. Aenean in est vitae felis semper vulputate convallis eu quam. Nullam feugiat elementum 
libero. Donec scelerisque finibus laoreet. Nam eu risus facilisis, iaculis urna vitae, aliquam neque. Donec elementum 
ipsum in pretium maximus. Integer id nulla commodo elit ultricies sollicitudin vel vitae augue. Proin commodo, 
magna at bibendum rutrum, odio risus dictum nisi, ac commodo ipsum dolor vitae purus. Maecenas posuere, 
est id vulputate porta, erat lacus efficitur purus, a mattis justo ligula eu felis. Suspendisse potenti. Mauris 
commodo libero ut dui efficitur malesuada. Donec ultricies vel purus vel pellentesque. Etiam fusce a ex in libero 
rutrum placerat suscipit ac tellus. Etiam dignissim ullamcorper tincidunt. Proin tempor lorem eu nulla euismod, 
id sollicitudin massa ultricies."""

txt = "Python"
txt1 = 'Python'
txt2 = 'I\'m a Python'
txt3 = "I\"m a Python"
txt4 = "I'm a Python"
txt5 = '''I'm"''""' a Python'''

# text1 = text.lower().split('.')
# text2 = [x.strip().capitalize() for x in text1]
# text3 = ". ".join(text2)
#
# print(text)
# print('\n\n\t****************\n\n')
# print(text1)
# print(text2)
# print(text3)

text1 = text.lower()
print(text1)
substr = 'etiam'

# def fin(text1: str, substr: str):
#     text1.find(substr)
count = 0
index = 0

# print([x for x in text1])
# print([ord(x) for x in text1])

# def get_value(text5: str):
#     # time.sleep(0.1)
#     if index < 0:
#         print("!")
#     else:
#         text5 += "!"
#         get_value(text5)
#
#
# get_value("111")

while True:  # ошибка логики, когда цикл никогда не заканчивается
    index = text1.find(substr, index + 1)  # 388
    if index < 0:
        break  # выходит из цикла
    else:
        count += 1  # count = count + 1 | count *= 2 | count -= 2 | count /= 2
        print(f"index: {index}")
        print(f"count: {count}")
        continue  # идёт к следующей итерации цикла
    index = "!!!!!!!"

print(f"index: {index}")
print(f"count: {count}")
# for x in a:  # сложность алгоритма
#     for b in x:
#         for c in b:
#             pass

# print([ord(x) for x in text1])

str0 = []
for i in text1:
    str0.append(ord(i))
print(str0)

index = 0
str10 = []
while True:
    try:  # попытка
        str10.append(text1[index])
        index += 1
    except Exception as error:
        print(f"error: {error}")
        break

#       -5   -4   -3   -2   -1
#        0    1    2    3    4
val1 = [108, 111, 114, 101, 109]
val1.sort(reverse=False)
print(val1)
# print(val1.sort(reverse=True)[-1])
