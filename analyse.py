category_cnt = []
outcome_mat = {}
outcome_rate = {}

with open('category_cnt', 'r', encoding='utf-8') as f:
    s = f.read().split()
    for i in range(0, len(s), 2):
        category_cnt.append((s[i], int(s[i + 1])))


for i in range(0, len(category_cnt)):
    with open("./outcome/" + category_cnt[i][0] + ".txt", "r", encoding='utf-8') as f:
        s = f.read().split('\n')
        for l in s:
            info = l.split()
            if l[0] == 't':
                outcome_rate[category_cnt[i][0]] = info[5]
                break
            if info[3] in outcome_mat:
                if info[1] in outcome_mat[info[3]]:
                    outcome_mat[info[3]][info[1]] += 1
                else:
                    outcome_mat[info[3]][info[1]] = 1
            else:
                outcome_mat[info[3]] = {}
                outcome_mat[info[3]][info[1]] = 1

precision_cnt = {}

for k in outcome_mat.keys():
    for v in outcome_mat[k].keys():
        if v in precision_cnt:
            precision_cnt[v] += outcome_mat[k][v]
        else:
            precision_cnt[v] = outcome_mat[k][v]

precision = {}
for k in outcome_mat.keys():
    precision[k] = outcome_mat[k][k] / precision_cnt[k]


for k in outcome_mat.keys():
    print(k, 'recall', outcome_rate[k], 'precision', precision[k])
    s = ""
    for v in outcome_mat[k].keys():
        s += v + ": " + str(outcome_mat[k][v])+" "
    print(s)
