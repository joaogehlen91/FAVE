# entrada:
# - arquivo com Working set(verificado por um humando, vai ser usado para criar o modelo de verificação)
#   formato de tupla(string, classe).
#   exemplo: ("a Survey of Multi-objective Sequential decision-making", "Title")
import re


ws_name = '/home/joao/TCC_source/book-amazon-title.txt'

file = open(ws_name, 'r')
page = file.readlines()

f = []
label = ''
ts = []

# funcao que caracteriza o Workign-set(WS) e transforma em um Training-Set(TS)
def caracteriza(data):
    f = []
    dots = re.compile(r'[.,;:?!]')
    if dots.findall(data):
        f.append(True)
    else:
        f.append(False)

    f.append(data[0].isupper())
    f.append(data.istitle())

    f.append('.' in data)
    f.append(',' in data)
    f.append(';' in data)
    f.append(':' in data)
    f.append('?' in data)
    f.append('!' in data)

    cm = re.compile(r'[A-Z]')
    f.append(True if cm.findall(data) else False)

    num = re.compile(r'\d')
    f.append(True if num.findall(data) else False)

    not_num = re.compile(r'\D')
    f.append(True if not_num.findall(data) else False)


    # numerical features
    f.append(len(num.findall(data)))
    f.append(len(not_num.findall(data)))
    f.append(len(data))
    f.append(len(data.split(' ')))

    return f



for line in page[2:]:
    slot_ts = []
    slot_ws = line.replace('\n', '').split('\t')
    fts = caracteriza(slot_ws[2])
    # print(fts)
    slot_ts.append(slot_ws[0])
    slot_ts.append(fts)
    slot_ts.append("title")

    print(slot_ts)

    ts.append(slot_ts)


# print(ts)








#funcao que gera o modelo de verificação(VM)
