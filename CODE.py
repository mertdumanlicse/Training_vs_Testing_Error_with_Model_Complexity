import csv
import codecs
import random
import math
#import pdb; pdb.set_trace()
# open file
data_world_rank=[]
data_quality_of_education=[]
test_data_world_rank=[]
test_data_quality_of_education=[]
# Datayı çekme
with open('cwurData - Kopya.csv', "rb") as f:
    reader = csv.reader(codecs.iterdecode(f, 'utf-8'))

    # read file row by row
    for row in reader:
       
        data_world_rank.append(int(row[0]))
        data_quality_of_education.append(int(row[4]))

# Data'nın %20 sini test, %80 ini Training olarak alma
count= int(len(data_world_rank)/5)
for i in range(0,count):
    randnum=random.randint(0,len(data_world_rank))
    test_data_world_rank.append(data_world_rank[randnum])
    test_data_quality_of_education.append(data_quality_of_education[randnum])
    data_world_rank.pop(randnum)
    data_quality_of_education.pop(randnum)
    count=count-1
datas_world_rank = []
datas_quality_of_education = []
test_datas_world_rank = []
test_datas_quality_of_education = []
#______________________________________________________________________________
#x'lerin ve bilinen y'lerin 1000e bölünerekten 0.000 ile 1.000 arasına alınmaları.
a = 0 
b = 0.0
c = 0.0
d = 0.0
e = 0.0
while(a < 1760):
    b = data_world_rank[a] / 1000
    c = data_quality_of_education[a] / 1000
    datas_world_rank.append(b)
    datas_quality_of_education.append(c)
    a  = a + 1
a = 0
while(a < 440):
    d = test_data_world_rank[a] / 440
    e = test_data_quality_of_education[a] / 440
    test_datas_world_rank.append(d)
    test_datas_quality_of_education.append(e)
    a  = a + 1
#______________________________________________________________________________
#input alınması
girdi = int(input("Kaçıncı dereceden bir grafik çizdirme işlemi yapmak istersiniz? ")) # kullandım
derece = girdi
r1 = girdi # kullandım
η = 0.5   
#______________________________________________________________________________
#tahmini y lerin bulunması ve geri değer olarak verilmesi.
def predicted_y0(w0):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0
        a = a + 1
        return round(ê,4)
def predicted_y1(w0,w1,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x
        a = a + 1
        return round(ê,4)
def predicted_y2(w0,w1,w2,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2
        a = a + 1
        return round(ê,4)
def predicted_y3(w0,w1,w2,w3,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3
        a = a + 1
        return round(ê,4)
def predicted_y4(w0,w1,w2,w3,w4,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4
        a = a + 1
        return round(ê,4)
def predicted_y5(w0,w1,w2,w3,w4,w5,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5
        a = a + 1
        return round(ê,4)
def predicted_y6(w0,w1,w2,w3,w4,w5,w6,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6
        a = a + 1
        return round(ê,4)
def predicted_y7(w0,w1,w2,w3,w4,w5,w6,w7,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7
        a = a + 1
        return round(ê,4)
def predicted_y8(w0,w1,w2,w3,w4,w5,w6,w7,w8,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8
        a = a + 1
        return round(ê,4)
def predicted_y9(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9
        a = a + 1
        return round(ê,4)
def predicted_y10(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10
        a = a + 1
        return round(ê,4)
def predicted_y11(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11
        a = a + 1
        return round(ê,4)
def predicted_y12(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12
        a = a + 1
        return round(ê,4)
def predicted_y13(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13
        a = a + 1
        return round(ê,4)
def predicted_y14(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14
        a = a + 1
        return round(ê,4)
def predicted_y15(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15
        a = a + 1
        return round(ê,4)
def predicted_y16(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16
        a = a + 1
        return round(ê,4)
def predicted_y17(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17
        a = a + 1
        return round(ê,4)
def predicted_y18(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18
        a = a + 1
        return round(ê,4)
def predicted_y19(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19
        a = a + 1
        return round(ê,4)
def predicted_y20(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 + x**20
        a = a + 1
        return round(ê,4)
def predicted_y21(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 * x**20 + w21 * x**21
        a = a + 1
        return round(ê,4)
def predicted_y22(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 * x**20 + w21 * x**21 + w22 * x**22
        a = a + 1
        return round(ê,4)
def predicted_y23(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 * x**20 + w21 * x**21 + w22 * x**22 + w23 * x**23
        a = a + 1
        return round(ê,4)
def predicted_y24(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 * x**20 + w21 * x**21 + w22 * x**22 + w23 * x**23 + w24 * x**24
        a = a + 1
        return round(ê,4)
def predicted_y25(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,w25,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 * x**20 + w21 * x**21 + w22 * x**22 + w23 * x**23 + w24 * x**24 + w25 * x**25
        a = a + 1
        return round(ê,4)
def predicted_y26(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,w25,w26,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 * x**20 + w21 * x**21 + w22 * x**22 + w23 * x**23 + w24 * x**24 + w25 * x**25 + w26 * x**26
        a = a + 1
        return round(ê,4)
def predicted_y27(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,w25,w26,w27,x):
    a = 0
    ê = 0.0
    while(a < 1760):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 * x**20 + w21 * x**21 + w22 * x**22 + w23 * x**23 + w24 * x**24 + w25 * x**25 + w26 * x**26 + w27 + x**27
        a = a + 1
        return round(ê,4)
#tahmini y lerin bulunması ve geri değer olarak verilmesi.
def predicted_y0rmse(w0):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0
        a = a + 1
        return round(ê,4)
def predicted_y1rmse(w0,w1,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x
        a = a + 1
        return round(ê,4)
def predicted_y2rmse(w0,w1,w2,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2
        a = a + 1
        return round(ê,4)
def predicted_y3rmse(w0,w1,w2,w3,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3
        a = a + 1
        return round(ê,4)
def predicted_y4rmse(w0,w1,w2,w3,w4,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4
        a = a + 1
        return round(ê,4)
def predicted_y5rmse(w0,w1,w2,w3,w4,w5,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5
        a = a + 1
        return round(ê,4)
def predicted_y6rmse(w0,w1,w2,w3,w4,w5,w6,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6
        a = a + 1
        return round(ê,4)
def predicted_y7rmse(w0,w1,w2,w3,w4,w5,w6,w7,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7
        a = a + 1
        return round(ê,4)
def predicted_y8rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8
        a = a + 1
        return round(ê,4)
def predicted_y9rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9
        a = a + 1
        return round(ê,4)
def predicted_y10rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10
        a = a + 1
        return round(ê,4)
def predicted_y11rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11
        a = a + 1
        return round(ê,4)
def predicted_y12rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12
        a = a + 1
        return round(ê,4)
def predicted_y13rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13
        a = a + 1
        return round(ê,4)
def predicted_y14rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14
        a = a + 1
        return round(ê,4)
def predicted_y15rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15
        a = a + 1
        return round(ê,4)
def predicted_y16rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16
        a = a + 1
        return round(ê,4)
def predicted_y17rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17
        a = a + 1
        return round(ê,4)
def predicted_y18rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18
        a = a + 1
        return round(ê,4)
def predicted_y19rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19
        a = a + 1
        return round(ê,4)
def predicted_y20rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 + x**20
        a = a + 1
        return round(ê,4)
def predicted_y21rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 * x**20 + w21 * x**21
        a = a + 1
        return round(ê,4)
def predicted_y22rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 * x**20 + w21 * x**21 + w22 * x**22
        a = a + 1
        return round(ê,4)
def predicted_y23rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 * x**20 + w21 * x**21 + w22 * x**22 + w23 * x**23
        a = a + 1
        return round(ê,4)
def predicted_y24rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 * x**20 + w21 * x**21 + w22 * x**22 + w23 * x**23 + w24 * x**24
        a = a + 1
        return round(ê,4)
def predicted_y25rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,w25,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 * x**20 + w21 * x**21 + w22 * x**22 + w23 * x**23 + w24 * x**24 + w25 * x**25
        a = a + 1
        return round(ê,4)
def predicted_y26rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,w25,w26,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 * x**20 + w21 * x**21 + w22 * x**22 + w23 * x**23 + w24 * x**24 + w25 * x**25 + w26 * x**26
        a = a + 1
        return round(ê,4)
def predicted_y27rmse(w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10,w11,w12,w13,w14,w15,w16,w17,w18,w19,w20,w21,w22,w23,w24,w25,w26,w27,x):
    a = 0
    ê = 0.0
    while(a < 440):
        ê = w0 + w1 * x + w2 * x**2 + w3 * x**3 + w4 * x**4 + w5 * x**5 + w6 * x**6 + w7 * x**7 + w8 * x**8 + w9 * x**9 + w10 * x**10 + w11 * x**11 + w12 * x**12 + w13 * x**13 + w14 * x**14 + w15 * x**15 + w16 * x**16 + w17 * x**17 + w18 * x**18 + w19 * x**19 + w20 * x**20 + w21 * x**21 + w22 * x**22 + w23 * x**23 + w24 * x**24 + w25 * x**25 + w26 * x**26 + w27 + x**27
        a = a + 1
        return round(ê,4)
#______________________________________________________________________________
def brackets(y,y_predicted):
    return round(y - y_predicted,4)
#______________________________________________________________________________
def RSS(y,y_predicted):
    #print(y,y_predicted)
    return round((y - y_predicted)**2,4)
#______________________________________________________________________________
def gradient_descent(q,u,x):
    r = u * (x ** q) # u * x^q
    return round(r,4)
#______________________________________________________________________________
def arbiter(w,η,gd,direction): #gd = gd[final]♦
    if direction == 1:
        r2 = 2.0 * η * gd
        w = w - r2
        return round(w,4)
    if direction == 0:
        r2 = 2.0 * η * gd
        w = w + r2
        return round(w,4)
#______________________________________________________________________________
#predicted_y0 fonksiyonunu çağırıp tahmini y leri alıp predicted_ê dizisine atamak.
predicted_ê = []
predicted_ê2 = []
wler=[]
r1=r1+1
for ı in range(r1):
    wler.append(1.0)
#wler = [1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1,0]
# b = ê
yeni_rss = []
for j in range(70):
    q = girdi
    r = girdi #kullandım
    final = girdi #kullandım
    final2 = girdi #kullandım
    a = 0
    b = 0.0
    if r == 0:
        while(a < 1760):
            b = predicted_y0(wler[0])
            predicted_ê.append(b)
            a = a + 1
    if r == 1:
        while(a < 1760):
            b = predicted_y1(wler[0],wler[1],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 2:
        while(a < 1760):
            b = predicted_y2(wler[0],wler[1],wler[2],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 3:
        while(a < 1760):
            b = predicted_y3(wler[0],wler[1],wler[2],wler[3],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 4:
        while(a < 1760):
            b = predicted_y4(wler[0],wler[1],wler[2],wler[3],wler[4],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 5:
        while(a < 1760):
            b = predicted_y5(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 6:
        while(a < 1760):
            b = predicted_y6(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 7:
        while(a < 1760):
            b = predicted_y7(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 8:
        while(a < 1760):
            b = predicted_y8(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 9:
        while(a < 1760):
            b = predicted_y9(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 10:
        while(a < 1760):
            b = predicted_y10(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 11:
        while(a < 1760):
            b = predicted_y11(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 12:
        while(a < 1760):
            b = predicted_y12(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 13:
        while(a < 1760):
            b = predicted_y13(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 14:
        while(a < 1760):
            b = predicted_y14(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 15:
        while(a < 1760):
            b = predicted_y15(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 16:
        while(a < 1760):
            b = predicted_y16(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 17:
        while(a < 1760):
            b = predicted_y17(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 18:
        while(a < 1760):
            b = predicted_y18(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 19:
        while(a < 1760):
            b = predicted_y19(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 20:
        while(a < 1760):
            b = predicted_y20(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 21:
        while(a < 1760):
            b = predicted_y21(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],wler[21],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 22:
        while(a < 1760):
            b = predicted_y22(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],wler[21],wler[22],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 23:
        while(a < 1760):
            b = predicted_y23(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],wler[21],wler[22],wler[23],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 24:
        while(a < 1760):
            b = predicted_y24(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],wler[21],wler[22],wler[23],wler[24],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 25:
        while(a < 1760):
            b = predicted_y25(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],wler[21],wler[22],wler[23],wler[24],wler[25],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 26:
        while(a < 1760):
            b = predicted_y26(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],wler[21],wler[22],wler[23],wler[24],wler[25],wler[26],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1
    if r == 27:
        while(a < 1760):
            b = predicted_y27(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],wler[21],wler[22],wler[23],wler[24],wler[25],wler[26],wler[27],datas_world_rank[a])
            predicted_ê.append(b)
            a = a + 1        
    #______________________________________________________________________________
    #tahmini y = ê => tahmini ylerin dizisi "predicted_ê" ve gerçek yler "datas_quality_of_education"   
    #tahmini y ile gerçek yler arasındaki farkın brackets fonk ile bulunması ve u dizisine atılması
    a = 0
    b = 0.0
    u = []
    while(a < 1760):
        b = brackets(predicted_ê[a],datas_quality_of_education[a])
        u.append(b)
        a = a + 1
    #______________________________________________________________________________
    #x üstü kaça kadar seçileceği bilgisinin verildiği ve gradient desent'inde yapıldığı fonksiyon
    # u * u'
    a = 0
    b = 0.0
    toplamfark_gd = []
    p = 0.0
    gd = []
    while(q >= 0):
        while(a < 1760):
            b = gradient_descent(q,u[a],datas_world_rank[a]) # q ; kaçıncı dereceden denklem olacağı
            toplamfark_gd.append(b)
            p = p + toplamfark_gd[a]
            #p = round(p,10)
            a = a + 1
        gd.append(p)
        p = 0.0
        toplamfark_gd.clear()
        q = q - 1
        a = 0
    gd.reverse() 
    #print(gd)
    #______________________________________________________________________________
    #1 defa tüm işlemin sonuçlandığı ve w0 w1 w2 gibi değerlerin ilk iterasyon sonucu oluşan sonuçları
    #finals dizisine atılıyor. w0 w1 w2    w18 şeklinde
    #RSS hesaplama
    a = 0
    b = 0.0
    rss = [] #predic ve real y ler arasınki farkların karelerinin dizisi
    while(a < 1760):
        b = RSS(predicted_ê[a],datas_quality_of_education[a])
        rss.append(b)
        a = a + 1
    top = sum(rss)
    yeni_rss.append(top)
    direction = 1#(çıkarmak)
    if j != 0:
        if yeni_rss[j] < yeni_rss[j-1]:
            direction = 1
        if yeni_rss[j] > yeni_rss[j-1]:
            direction = 0
    #print(direction)
    #print(round((yeni_rss[j]),4))
    #______________________________________________________________________________
    finals = []
    while(final >= 0):
        sonuc = arbiter(wler[final],η,gd[final],direction)
        final = final - 1
        finals.append(sonuc)
    finals.reverse()
    wler.clear()
    while(final2 >= 0):
        wler.append(finals[final2])
        final2 = final2 -1
    wler.reverse()
    finals.clear()
    gd.clear()
    predicted_ê.clear()
    u.clear()
    rss.clear()
print("En son hesaplanan değerlere göre RSS'im.(TRAINING DEGIL)")
print(top)#son rss
print("Denklem derecesi: ",derece)
print("En son buldugum w degerleri")
print(wler)
a = 0
c = 0.0
if r == 0:
    while(a < 440):
        c = predicted_y0rmse(wler[0])
        predicted_ê2.append(c)
        a = a + 1
if r == 1:
    while(a < 440):
        c = predicted_y1rmse(wler[0],wler[1],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 2:
    while(a < 440):
        c = predicted_y2rmse(wler[0],wler[1],wler[2],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 3:
    while(a < 440):
        c = predicted_y3rmse(wler[0],wler[1],wler[2],wler[3],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 4:
    while(a < 440):
        c = predicted_y4rmse(wler[0],wler[1],wler[2],wler[3],wler[4],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 5:
    while(a < 440):
        c = predicted_y5rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 6:
    while(a < 440):
        c = predicted_y6rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 7:
    while(a < 440):
        c = predicted_y7rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 8:
    while(a < 440):
        c = predicted_y8rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 9:
    while(a < 440):
        c = predicted_y9rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 10:
    while(a < 440):
        c = predicted_y10rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 11:
    while(a < 440):
        c = predicted_y11rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 12:
    while(a < 440):
        c = predicted_y12rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 13:
    while(a < 440):
        c = predicted_y13rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],test_datas_world_rank[a])            
        predicted_ê2.append(c)
        a = a + 1
if r == 14:
    while(a < 440):
        c = predicted_y14rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 15:
    while(a < 440):
        c = predicted_y15rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 16:
    while(a < 440):
        c = predicted_y16rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 17:
    while(a < 440):
        c = predicted_y17rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 18:
    while(a < 440):
        c = predicted_y18rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 19:
    while(a < 440):
        c = predicted_y19rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 20:
    while(a < 440):
        c = predicted_y20rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 21:
    while(a < 440):
        c = predicted_y21rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],wler[21],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 22:
    while(a < 440):
        c = predicted_y22rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],wler[21],wler[22],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 23:
    while(a < 440):
        c = predicted_y23rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],wler[21],wler[22],wler[23],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 24:
    while(a < 440):
        c = predicted_y24rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],wler[21],wler[22],wler[23],wler[24],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 25:
    while(a < 440):
        c = predicted_y25rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],wler[21],wler[22],wler[23],wler[24],wler[25],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 26:
    while(a < 440):
        c = predicted_y26rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],wler[21],wler[22],wler[23],wler[24],wler[25],wler[26],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
if r == 27:
    while(a < 440):
        c = predicted_y27rmse(wler[0],wler[1],wler[2],wler[3],wler[4],wler[5],wler[6],wler[7],wler[8],wler[9],wler[10],wler[11],wler[12],wler[13],wler[14],wler[15],wler[16],wler[17],wler[18],wler[19],wler[20],wler[21],wler[22],wler[23],wler[24],wler[25],wler[26],wler[27],test_datas_world_rank[a])
        predicted_ê2.append(c)
        a = a + 1
#rmse kök içinde 1/n toplam (rss) ama bu sefer x ler ve y ler training data
#wler[] var
a = 0
b = 0.0
rmse = []
while(a < 440):
    b = RSS(predicted_ê2[a],test_datas_quality_of_education[a])
    rmse.append(b)
    a = a + 1
top2 = sum(rmse)
top2 = top2 / 440
print("RMSE: ")
print(math.sqrt(top2))