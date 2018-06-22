from lxml import html
import glob
import re


out = open('saida_generator.csv', 'w')


def caracteriza(data):
    f = []
    dots = re.compile(r'[.,;:?!]')
    if dots.findall(data):
        f.append(1)
    else:
        f.append(0)

    f.append(int(data[0].isupper()))
    f.append(int(data.istitle()))

    f.append(int('.' in data))
    f.append(int(',' in data))
    f.append(int(';' in data))
    f.append(int(':' in data))
    f.append(int('?' in data))
    f.append(int('!' in data))

    cm = re.compile(r'[A-Z]')
    f.append(1 if cm.findall(data) else 0)

    num = re.compile(r'\d')
    f.append(1 if num.findall(data) else 0)

    not_num = re.compile(r'\D')
    f.append(1 if not_num.findall(data) else 0)

    only_let = re.compile(r'[A-Za-z]')


    # numerical features
    f.append(len(num.findall(data)))
    f.append(len(not_num.findall(data)))
    f.append(len(data))

    words = data.split()

    f.append(len(words))
    f.append([1 if w[0].isupper() else 0 for w in words].count(1))

    f.append(len(words)/len(data))

    f.append(len(num.findall(data)) / len(data))
    f.append(len(dots.findall(data)) / len(data))
    f.append(len(only_let.findall(data)) / len(data))

    f.append([1 if l.isupper() else 0 for l in data].count(1) / len(data))
    f.append([1 if l.islower() else 0 for l in data].count(1) / len(data))
    f.append(sum(len(w) for w in words) / len(words))

    return f


for filename in glob.glob('/home/joao/TCC_source/groundtruth/auto/*price.txt'):
    print(filename)
    file = open(filename, 'r')
    page = file.readlines()

    for line in page[2:]:

	    slot_ws = line.replace('\n', '').split('\t')
	    fts = caracteriza(slot_ws[2])

	    fts.append(0) # 1 para target class e 0 para outlier
	    out.write(', '.join(str(i) for i in fts))
	    out.write('\n')
	    # print(fts)
	    # ts.append(slot_ts)

out.close()
