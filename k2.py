category_cnt = []
doc_cnt = 0

with open('category_cnt', 'r', encoding='utf-8') as f:
    s = f.read().split()
    for i in range(0, len(s), 2):
        category_cnt.append((s[i], int(s[i + 1])))
        doc_cnt += int(s[i + 1])

word_dict = {}

for i in range(0, len(category_cnt)):
    cat = category_cnt[i]
    cnt = int(cat[1])
    print(cat[0])
    for j in range(1, cnt + 1):
        print('./tmp_train/' + cat[0] + '_'+str(j) + '.txt')
        with open('./tmp_train/' + cat[0] + '_'+str(j) + '.txt', encoding='utf-8') as f:
            s = f.read().split()
            for k in range(0, len(s), 2):
                if s[k] in word_dict:
                    word_dict[s[k]][i] += 1
                else:
                    word_dict[s[k]] = [0] * len(category_cnt)
                    word_dict[s[k]][i] += 1

tot_k2 = {}
for cat in category_cnt:
    tot_k2[cat[0]] = []

for key in word_dict.keys():
    print(key)
    val = word_dict[key]
    v_sum = sum(val)
    for i in range(0, len(val)):
        belong_include = val[i]
        nbelong_include = v_sum - belong_include
        belong_ninclude = category_cnt[i][1] - belong_include
        nbelong_ninclude = (doc_cnt - category_cnt[i][1]) - nbelong_include
        k2 = doc_cnt * (belong_include*nbelong_ninclude -
                        nbelong_include * belong_ninclude) ** 2
        k2 /= (belong_include+belong_ninclude)*(nbelong_include+nbelong_ninclude) * \
            (belong_include + nbelong_include) * \
            (belong_ninclude + nbelong_ninclude)
        tot_k2[category_cnt[i][0]].append((key, k2))

for i in range(0, len(category_cnt)):
    key = category_cnt[i][0]
    print(key)
    k2 = tot_k2[key][:]
    k2 = sorted(k2, key=lambda x: x[1], reverse=True)
    with open("./k2/"+key + ".txt", 'w', encoding='utf-8') as f:
        s = ""
        for j in range(0, 1000):
            s += str(j) + " " + k2[j][0] + " " + str(k2[j][1]) + " "
            for k in range(0, len(category_cnt)):
                s += str(word_dict[k2[j][0]][k]) + " "
            s += '\n'
        f.write(s)


# --------------------------------------------------------------------

final_dict = {}

with open('category_cnt', 'r', encoding='utf-8') as f:
    s = f.read().split()
    for i in range(0, len(s), 2):
        print('./k2/'+s[i]+'.txt')
        with open('./k2/'+s[i]+'.txt', 'r', encoding='utf-8') as f2:
            s2 = f2.read().split()
            for j in range(0, len(s2), 13):
                final_dict[s2[j+1]] = 1

with open('final_dict.txt', 'w', encoding='utf-8') as f:
    s = ""
    for word in final_dict.keys():
        s += word + '\n'
    f.write(s)
