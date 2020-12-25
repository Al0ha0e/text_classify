import math

category_cnt = []

with open('category_cnt', 'r', encoding='utf-8') as f:
    s = f.read().split()
    for i in range(0, len(s), 2):
        category_cnt.append((s[i], s[i + 1]))

final_dict = {}

with open('final_dict.txt', 'r', encoding='utf-8') as f:
    s = f.read().split()
    for word in s:
        final_dict[word] = [1] * len(category_cnt)

word_category_cnt = [0] * len(category_cnt)

for i in range(0, len(category_cnt)):
    cat = category_cnt[i]
    cnt = int(cat[1])
    print(cat)
    for j in range(1, cnt + 1):
        print('./tmp_train/' + cat[0] + '_'+str(j) + '.txt')
        with open('./tmp_train/' + cat[0] + '_' + str(j) + '.txt', encoding='utf-8') as f:
            s = f.read().split()
            for k in range(0, len(s), 2):
                if s[k] in final_dict:
                    word_category_cnt[i] += int(s[k + 1])
                    final_dict[s[k]][i] += int(s[k + 1])

    with open('./possib/' + cat[0] + '.txt', 'w', encoding='utf-8') as f:
        s = ""
        for word in final_dict.keys():
            s += word + ' '
            s += str(math.log10(final_dict[word][i]) -
                     math.log10(word_category_cnt[i] + len(final_dict))) + ' '
            s += '\n'
        f.write(s)
