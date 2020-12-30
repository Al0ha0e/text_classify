import shutil
import os


for home, dirs, files in os.walk('./thu2'):
    i = 1
    cat = home.split('\\')
    category = ''
    if len(cat) > 1:
        category = cat[1]
    print(category)
    for f in files:
        if i > 12000:
            break
        print(i, './thu2/' + category + '/' + f)
        if i > 6000:
            shutil.move('./thu2/' + category + '/' + f,
                        './thu/test/' + category + '/' + f)
        else:
            shutil.move('./thu2/' + category + '/' + f,
                        './thu/train/' + category + '/' + f)

        i += 1
