import math
p = 180718077438230903088259404111109902408788792269321330228788417121936218680586291654359263875245636462136207209710898717518264476296827582787086600239059519068433796629738538852356045657226501395958857117045844014840556289597049728294079022228344144539320766265843349301546678380996159414467575746621210920423
g = 148562849017582886502129219523432650901081631900741560012762835434015656773556269782905534265944075561636258160863206515085291553869598240487034610794200885273152222081492113284851158683855136518571914511822896099073090699807696571184817585394507199795945943920222050123262795505014896679793579211466902946995
b = 75337134373468677459713939634802862691470341773066458614574066819647459020487750490202144046452588384708930610179602139487532673534203078979696419388988870994184370891249539676216423943616529431914408811209682976803824660304450002642226617625722930116228410432796827727307749819724459891017724486329134221472
a = 112056038587035895317250171945674225645902441664302973282760161832925706696542846782381121110814421016601515921677544903226525276262004999141397632527882964262050024956771856974128817372037021665514819893195144255428098900932679074130926430651208651800336526083527384178049022080681607153985681018865077909225

f = open('a3.cipher.txt')
l = list(f)
mask = []
cipher = []

for x in l:
    m = x.split(',')
    mask.append(long(m[0]))
    cipher.append(long(m[1]))


def inverse(e):
    one = p
    two = e
    q = long(math.floor(one/two))
    r = one % two
    x1 = 1
    y1 = 0
    x2 = 0
    y2 = 1
    while(two !=1):
        tmp1 = x2
        tmp2 = y2
        x2 = x1 - (q * x2)
        y2 = y1 - (q * y2)
        x1 = tmp1
        y1 = tmp2
        one = two
        two = r
        q = long(math.floor(one/two))
        r = one % two
    return long(y2 % p)


z = open('a3decrypt.txt', 'w')
text = ''

for i in range(len(mask)):
    print 'printing ' + str(i)
    z.write(str(chr((cipher[i] * inverse(long(pow(mask[i],a,p)))) % p)))