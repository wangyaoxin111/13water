import sys
import itertools
import requests
import re
import time
sys.setrecursionlimit(900000000)


class pai:
    kind = ''
    num = 0

    def __init__(self, k, n):
        self.kind = k
        self.num = n






def paixukey(elem):
    return elem.num

url = "https://api.shisanshui.rtxux.xyz/auth/login"
headers = {
    'content-type': 'application/json'
}
# data = {
#     "username": username,
#     "password": password
# }
payload = "{\"username\":\"wyx\",\"password\":\"12345678\"}"

response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
# p = re.compile(r'token":"(.+?)"')
aaa = str(response.text)
print(aaa)
# token = re.search('token": "(.+)"',aaa)
p = re.compile(r'token":"(.+?)"')
token = p.findall(aaa)[0]
# token = p.findall(response.text)[0]
header = {
    "x-auth-token": token
}
print(token)


def validate(header):
    url = 'https://api.shisanshui.rtxux.xyz/auth/validate'
    headers = {
        "x-auth-token": token111
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)


def zhizunqinglong(list):
    list1 = list.copy()
    for i in range(13):
        if list1[0].kind != list1[i].kind:
            return 0
    return 1


def yitiaolong(list):
    list1 = list.copy()
    list1.sort(key=paixukey)
    for i in range(13):
        if (list1[i].num - list1[0].num) != i:
            return 0
    return 1


def shierhuangzu(list):
    list1 = list.copy()
    list1.sort(key=paixukey)
    if list1[1].num >= 11:
        return 1
    return 0


def sanfentianxia(list):
    list1 = list.copy()
    list1.sort(key=paixukey)
    list2 = []
    list3 = []
    list4 = []
    for i in range(13):
        list2.append(list1[i].num)
    for i in range(13):
        list3.append(list2.count(i + 2))
    list4.append(0)
    for i in range(1, 5):
        list4.append(list3.count(i))
    if list4[4] == 3:
        return 1
    return 0


def quanda(list):
    list1 = list.copy()
    list1.sort(key=paixukey)
    if list1[0].num > 7:
        return 1
    return 0


def quanxiao(list):
    list1 = list.copy()
    list1.sort(key=paixukey)
    if list1[12].num < 9:
        return 1
    return 0


def couyise(list):
    list1 = list.copy()
    if list1[0].kind == "*" or list1[0].kind == "#":
        for i in range(1, 13):
            if list1[i].kind != "*" and list1[i].kind != "#":
                return 0
    else:
        for i in range(1, 13):
            if list1[i].kind != "$" and list1[i].kind != "&":
                return 0
    return 1


def shuangguaichongsan(list):
    list1 = list.copy()
    list1.sort(key=paixukey)
    list2 = []
    list3 = []
    list4 = []
    for i in range(13):
        list2.append(list1[i].num)
    for i in range(13):
        list3.append(list2.count(i+2))
    list4.append(0)
    for i in range(1, 5):
        list4.append(list3.count(i))
    if list4[3] == 2 and list4[2] == 3:
        return 1
    return 0


def sitaosantiao(list):
    list1 = list.copy()
    list1.sort(key=paixukey)
    list2 = []
    list3 = []
    list4 = []
    for i in range(13):
        list2.append(list1[i].num)
    for i in range(13):
        list3.append(list2.count(i + 2))
    list4.append(0)
    for i in range(1, 5):
        list4.append(list3.count(i))
    if list4[3] == 4:
        return 1
    return 0


def wuduisantiao(list):
    list1 = list.copy()
    list1.sort(key=paixukey)
    list2 = []
    list3 = []
    list4 = []
    for i in range(13):
        list2.append(list1[i].num)
    for i in range(13):
        list3.append(list2.count(i + 2))
    list4.append(0)
    for i in range(1, 5):
        list4.append(list3.count(i))
    if list4[3] == 1 and list4[2] == 5:
        return 1
    return 0


def liuduiban(list):
    list1 = list.copy()
    list1.sort(key=paixukey)
    list2 = []
    list3 = []
    list4 = []
    for i in range(13):
        list2.append(list1[i].num)
    for i in range(13):
        list3.append(list2.count(i + 2))
    list4.append(0)
    for i in range(1, 5):
        list4.append(list3.count(i))
    if list4[2] == 6:
        return 1
    return 0


def sanshunzi(list):
    list1 = list.copy()
    dict1 = {}
    for x in range(2, 15):
        dict1[x] = 0
    for r in list1:
        dict1[r.num] = dict1[r.num] + 1
    z = 0
    sumy = 0
    for vi in range(3):
        y = 0
        for r in list1:
            if dict1[r.num] > 1:
                for x in range(r.num, min(r.num + 5, 15)):
                    if dict1[x] > 0:
                        dict1[x] = dict1[x] - 1
                        y += 1
                        if y == 5:
                            sumy += 1
                            break
                        elif x == 14 and y == 3 :
                            z = 1
                            break
                    else:
                        if y == 3:
                            z = 1
                        break
                break
    for vi in range(3):
        y = 0
        for r in list1:
            if dict1[r.num] > 0:
                for x in range(r.num, min(r.num + 5, 15)):
                    if dict1[x] > 0:
                        dict1[x] = dict1[x] - 1
                        y += 1
                        if y == 5:
                            sumy += 1
                            break
                        elif x == 14 and y == 3:
                            z = 1
                            break
                    else:
                        if y == 3:
                            z = 1
                        break
                break
    if sumy+z == 3:
        return 1
    else:
        return 0


def santonghua(list):
    list1 = list.copy()
    dict1 = {}
    for i in range(4):
        dict1[i] = 0
    for x in list1:
        if x.kind == "$":
            dict1[0] += 1
        elif x.kind == "&":
            dict1[1] += 1
        elif x.kind == "*":
            dict1[2] += 1
        else:
            dict1[3] += 1
    s = 0
    for u in range(4):
        s += pow(2, dict1[u])
    if s == 73 or s == 1034 or s == 290:
        return 1
    else:
        return 0


def santonghuashun(list):
    if sanshunzi(list) and santonghua(list):
        return 1
    return 0


def sanpai(list1):
    list1.sort(key=paixukey)
    if len(list1) == 5:
        return (list1[4].num*100000000+list1[3].num*1000000+list1[2].num*10000+list1[1].num*100+list1[0].num)/100000000.0
    else:
        return (list1[2].num*10000+list1[1].num*100+list1[0].num)/10000.0


def duizi(list1):
    f = 1
    if len(list1) == 5:
        list2 = []
        list3 = []
        list4 = []
        for i in range(5):
            list2.append(list1[i].num)
        for i in range(2, 15):
            list3.append(list2.count(i))
            if list2.count(i) == 2:
                f = i
        list4.append(0)
        for i in range(1, 5):
            list4.append(list3.count(i))
        if list4[2] == 1 and list4[3] == 0:
            return f
        return 0
    else:
        list2 = []
        list3 = []
        list4 = []
        for i in range(3):
            list2.append(list1[i].num)
        for i in range(2, 15):
            list3.append(list2.count(i))
            if list2.count(i) == 2:
                f = i
        list4.append(0)
        for i in range(1, 4):
            list4.append(list3.count(i))
        if list4[2] == 1 and list4[3] == 0:
            return f
        return 0


def erdui(list1):
    list2 = []
    list3 = []
    list4 = []
    f1 = 1
    f2 = 1
    for i in range(5):
        list2.append(list1[i].num)
    for i in range(2, 15):
        list3.append(list2.count(i))
        if list2.count(i) == 2:
            if f1 == 1:
                f1 = i
            else:
                f2 = i
    list4.append(0)
    for i in range(1, 5):
        list4.append(list3.count(i))
    if list4[2] == 2:
        x = list3.index(2)
        list3[x] = 0
        y = list3.index(2)
        list3[x] = 2
        if y-x != 1:
            return f2*100+f1
    return 0


def liandui(list1):
    list2 = []
    list3 = []
    list4 = []
    f1 = 1
    f2 = 1
    for i in range(5):
        list2.append(list1[i].num)
    for i in range(2, 15):
        list3.append(list2.count(i))
        if list2.count(i) == 2:
            if f1 == 1:
                f1 = i
            else:
                f2 = i
    list4.append(0)
    for i in range(1, 5):
        list4.append(list3.count(i))
    if list4[2] == 2:
        x = list3.index(2)
        list3[x] = 0
        y = list3.index(2)
        list3[x] = 2
        if y - x == 1:
            return f2*100+f1
    return 0


def santiao(list1):
    f = 1
    if len(list1) == 5:
        list2 = []
        list3 = []
        list4 = []
        for i in range(5):
            list2.append(list1[i].num)
        for i in range(2, 15):
            list3.append(list2.count(i))
            if list2.count(i) == 3:
                f = i
        list4.append(0)
        for i in range(1, 5):
            list4.append(list3.count(i))
        if list4[3] == 1 and list4[2] == 0:
            return f
        return 0
    else:
        list2 = []
        list3 = []
        list4 = []
        for i in range(3):
            list2.append(list1[i].num)
        for i in range(2, 15):
            list3.append(list2.count(i))
            if list2.count(i) == 3:
                f = i
        list4.append(0)
        for i in range(1, 4):
            list4.append(list3.count(i))
        if list4[3] == 1:
            return f
        return 0


def shunzi(list1):
    list1.sort(key=paixukey)
    if len(list1) == 5:
        for i in range(5):
            if (list1[i].num - list1[0].num) != i:
                return 0
        return list1[4].num
    else:
        for i in range(3):
            if (list1[i].num - list1[0].num) != i:
                return 0
        return list1[2].num


def tonghua(list1):
    list1.sort(key=paixukey)
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    for x in list1:
        if x.kind == "$":
            list2.append(x)
        if x.kind == "&":
            list3.append(x)
        if x.kind == "*":
            list4.append(x)
        if x.kind == "#":
            list5.append(x)
    list6.append(len(list2))
    list6.append(len(list3))
    list6.append(len(list4))
    list6.append(len(list5))
    if len(list1) == 5:
        for x in list6:
            if x == 5:
                return list1[4].num*100000000+list1[3].num*1000000+list1[2].num*10000+list1[1].num*100+list1[0].num
        return 0
    else:
        for x in list6:
            if x == 3:
                return list1[2].num * 10000 + list1[1].num * 100 + list1[0].num
        return 0


def hulu(list1):
    list2 = []
    list3 = []
    list4 = []
    f = 1
    for i in range(5):
        list2.append(list1[i].num)
    for i in range(2, 15):
        list3.append(list2.count(i))
        if list2.count(i) == 3:
            f = i
    list4.append(0)
    for i in range(1, 5):
        list4.append(list3.count(i))
    if list4[2] == 1and list4[3] == 1:
        return f
    return 0


def zhadan(list1):
    list2 = []
    list3 = []
    list4 = []
    f = 1
    for i in range(5):
        list2.append(list1[i].num)
    for i in range(2, 15):
        list3.append(list2.count(i))
        if list2.count(i) == 4:
            f = i
    list4.append(0)
    for i in range(1, 5):
        list4.append(list3.count(i))
    if list4[4] == 1:
        return f
    return 0


def tonghuashun(list):
    f = shunzi(list)
    if tonghua(list) and f:
        return f
    return 0


def score(list, m):
    if m == 5:
        f = tonghuashun(list)
        if f:
            return 150000+f*700
        f = zhadan(list)
        if f:
            return 120000+f*700
        f = hulu(list)
        if f:
            return 90000+f*700
        f = tonghua(list)
        if f:
            return 70000+f*0.000007
        f = shunzi(list)
        if f:
            return 60000+f*700
        f = santiao(list)
        if f:
            return 50000+f*700
        f = liandui(list)
        if f:
            return 40000+f*7
        f = erdui(list)
        if f:
            return 30000+f*7
        f = duizi(list)
        if f:
            return 20000+f*100
        f = sanpai(list)
        if f:
            return 10000+f
    elif m == 3:
        """
        f = tonghuashun(list)
        if f:
            return 100000+f*0.07
        f = tonghua(list)
        if f:
            return 70000+f*0.07
        f = shunzi(list)
        if f:
            return 60000+f*700
        """
        f = santiao(list)
        if f:
            return 50000+f*700
        f = duizi(list)
        if f:
            return 20000+f*100
        f = sanpai(list)
        if f:
            return 10000+100*f


def cmb(list0):
    list1 = list0.copy()
    iter1 = itertools.combinations(list1, 5)
    for tup0 in iter1:
        listc = list(tup0)
        a = score(listc, 5)
        if a < 30000:
            continue;
        list1 = list0.copy()
        for i in range(5):
            list1.remove(listc[i])
        iter2 = itertools.combinations(list1, 5)
        for tup1 in iter2:
            liste = list(tup1)
            list2 = list0.copy()
            for i in range(5):
                list2.remove(listc[i])
            for i in range(5):
                list2.remove(liste[i])

            b = score(liste, 5)
            c = score(list2, 3)
            if (a > b) and (b > c):
                s[1] = a + 2 * b + 4 * c
                if s[1] > s[0]:
                    s[0] = s[1]
                    global result
                    result.clear()
                    for k in range(3):
                        result.append(list2[k])
                    for k in range(5):
                        result.append(liste[k])
                    for k in range(5):
                        result.append(listc[k])



def logout(header):
    url = 'https://api.shisanshui.rtxux.xyz/auth/logout'
    data = {}
    respond = requests.post(url, json=data).text
    print(respond)


def openn(header):
    url = 'https://api.shisanshui.rtxux.xyz/game/open'
    header = str(header)
    headers = {'x-auth-token': header}
    data = {}
    response = requests.request("POST", url, headers=headers)
    return response

def submit(idd, listt):
    url = "https://api.shisanshui.rtxux.xyz/game/submit"
    headers = {
        'content-type': "application/json",
        'x-auth-token': token
    }
    payload = "{\"id\":"
    payload = payload + str(idd)
    payload = payload + ",\"card\":[\""
    # payload = "{\"id\":"
    # payload=payload+str(idd)
    # payload=payload+"\",\"card\":[\""

    if len(listt) == 1:
        payload = payload + str(listt[0])
    else:
        payload = payload + str(listt[0])
        payload = payload + "\",\""
        payload = payload + str(listt[1])
        payload = payload + "\",\""
        payload = payload + str(listt[2])
    payload = payload + "\"]}"
    # print(payload)
    # dataa=str(data)
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    '''
    p = re.compile(r'token":"(.+?)"')
    token = p.findall(respond)[0]
    print(token)
    return token
    '''


def history(header):
    u = 'https://api.shisanshui.rtxux.xyz/history'
    header = {
        "x-auth-token": token
    }
    response = requests.get(url=u, headers=header).text
    print(response)


while 1:
    try:
        s = []
        s.append(0)
        s.append(0)
        result = []
        tok = openn(token)

        tok1 = str(tok.text)
        # tok1=json.loads(tok)
        # str0 = input()
        p1 = re.compile(r'card":"(.+?)"')
        str0 = p1.findall(tok1)[0]
        print("receive origin card:", end=' ')
        print(str0)
        # str0= re.search('card\': \'(.+)\'',tok1)
        # str0=tok1['data']['card']
        p2 = re.compile(r'id":(.+?),')
        idd = p2.findall(tok1)[0]
        print("number of game:", end=' ')
        print(idd)
        # idd=re.search('id\': \'(.+)\'',tok1)
        # idd=tok1['data']['id']
        str0 = str0.replace("10", "T")
        list0 = []
        for i in range(0, len(str0), 3):
            if str0[i + 1] == "T":
                a = pai(str0[i], 10)
            elif str0[i + 1] == "A":
                a = pai(str0[i], 14)
            elif str0[i + 1] == "J":
                a = pai(str0[i], 11)
            elif str0[i + 1] == "Q":
                a = pai(str0[i], 12)
            elif str0[i + 1] == "K":
                a = pai(str0[i], 13)
            else:
                a = pai(str0[i], int(str0[i + 1]))
            list0.append(a)
        list0.sort(key=paixukey)
        lans = []
        st = ""
        result = list0.copy()
        if zhizunqinglong(list0):
            pass
        elif yitiaolong(list0):
            pass
        elif shierhuangzu(list0):
            pass
        elif santonghuashun(list0):
            pass
        elif sanfentianxia(list0):
            pass
        elif quanda(list0):
            pass
        elif quanxiao(list0):
            pass
        elif couyise(list0):
            pass
        elif shuangguaichongsan(list0):
            pass
        elif sitaosantiao(list0):
            pass
        elif wuduisantiao(list0):
            pass
        elif liuduiban(list0):
            pass
        elif sanshunzi(list0):
            pass
        elif santonghua(list0):
            pass
        else:
            cmb(list0)
        for i in range(13):
            st = st + result[i].kind + str(result[i].num) + " "
        st = st.replace("10", "T")
        st = st.replace("11", "J")
        st = st.replace("12", "Q")
        st = st.replace("13", "K")
        st = st.replace("14", "A")
        st1 = ""
        st2 = ""
        st3 = ""
        for x in range(0, 8):
            st1 = st1 + st[x]
        for x in range(9, 23):
            st2 = st2 + st[x]
        for x in range(24, 38):
            st3 = st3 + st[x]
        st1 = st1.replace("T", "10")
        st2 = st2.replace("T", "10")
        st3 = st3.replace("T", "10")
        print(st1)
        print(st2)
        print(st3)
        lans.append(st1)
        lans.append(st2)
        lans.append(st3)
        submit(idd, lans)
        print("*************************************************************")
    except IndexError:
        time.sleep(10)

