import os


def resave(fr, to):
    s = ""
    with open(fr, 'r', errors='ignore', encoding='utf-8') as f:
        s = f.read()
    with open(to, 'w', encoding='utf-8') as f:
        f.write(s)


for home, dirs, files in os.walk('./thu/train'):
    i = 1
    cat = home.split('\\')
    category = ''
    if len(cat) > 1:
        category = cat[1]
    print(category)
    for f in files:
        print(i, './thu/train/' + category + '/' + f)
        resave('./thu/train/' + category + '/' + f,
               './tmp_train/' + category + '_' + str(i) + '.txt')
        i += 1
