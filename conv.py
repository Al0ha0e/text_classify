import os


def resave(fr, to):
    s = ""
    with open(fr, 'r', errors='ignore') as f:
        s = f.read()
    with open(to, 'w', encoding='utf-8') as f:
        f.write(s)


for home, dirs, files in os.walk('./fudan/train'):
    i = 1
    cat = home.split('\\')
    category = ''
    if len(cat) > 1:
        category = cat[1]
    print(category)
    for f in files:
        print(i, './fudan/train/' + category + '/' + f)
        resave('./fudan/train/' + category + '/' + f,
               './tmp_train/' + category + '_' + str(i) + '.txt')
        i += 1
