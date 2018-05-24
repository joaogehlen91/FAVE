# entrada:
# - arquivo com Working set(verificado por um humando, vai ser usado para criar o modelo de verificação)
#   formato de tupla(string, classe).
#   exemplo: ("a Survey of Multi-objective Sequential decision-making", "Title")
import re
import numpy

ws_name = '/home/joao/TCC_source/book-amazon-author.txt'

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

    return f

# funcao que gera o modelo de verificacao a partir da entrada de treinamento
def model_building(ts):
    vm = []
    soma = 0
    for x in range(21):
        for y in range(len(ts)):
            soma += ts[y][1][x]

        media = soma / len(ts)
        vm.append(media)
        soma = 0

    return vm


# funcao que recebe o modelo de verificacao e um slot não verificado e faz a verificacao
def verifier(vm, uws):
    uts = caracteriza(uws[2])
    print(uws)
    print(f'uts: {uts}')
    print(f'vm: {vm}')

    n_uts = numpy.array((uts))
    n_vm = numpy.array((vm))

    dist = numpy.linalg.norm(n_uts - n_vm)
    print(f'ditancia euclidiana: {dist}')



# main
for line in page[2:]:
    slot_ts = []
    slot_ws = line.replace('\n', '').split('\t')
    fts = caracteriza(slot_ws[2])
    slot_ts.append(slot_ws[0])
    slot_ts.append(fts)
    slot_ts.append("title")

    ts.append(slot_ts)


vm = model_building(ts)

#uws = [1500, 1, 'as565426354162534162534']
uws = [1500, 1, "Peter A. Lillback"]


verifier(vm, uws)
