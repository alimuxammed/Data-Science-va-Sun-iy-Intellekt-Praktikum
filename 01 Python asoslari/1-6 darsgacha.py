#Bismillah

######################print(), arfimetik amllar va sintaks####################

#shunchaki hello world
print("hello world")


#\n matinni yangi qatorga chiqaradi.
print("Odami ersang, demagil odami,\nOniki, yo'q xalq g'amidin g'ami")


#""" """ matinni yangi qatorlardan bemalol shunga o'hashb yozib ketsangiz bo'ladi. \n-ga o'hshab. 
print("""Odami ersang, demagil odami,
Oniki, yo'q xalq g'amidin g'ami""")


#kerakli so'zlarni qo'shtirnoq ichiga olish uchun butun matinni bir tirnoqga olib kerakli so'zni qo'shtirnoq ichiga olib ketsangiz bo'ladi.
print('Men "Dell" markasidagi noutbuk sotib oldim')


#matin bir tirnoqga olinib ichida yana bir tirnoqlar bo'lsa yani o' ,g' hariflarga o'hshagan u holda \ belgisini qo'yib ishlatsa bo'ladi. 
print('Odami ersang, demagil odami, \nOniki, yo\'q xalq g\'amidin g\'ami')


#Bo'lish va butun qismini olish	
print(16//2)

#Exponenta (daraja/ildiz)
print(2**4)

#ko'paytirish
print(2*4)

#Bo'lish
print(4/2)

#Bo'linmaning qoldig'ini olish	
print(15%6)

#Qo'shish
print(15+6)

#Ayirish
print(15-6)


#----------AMALIYOT-------------#

#####ko'nsolga shunday matin chiqsin: "Nexia", "Tico", 'Damas' ko'rganlar qilar havas
print("\"Nexia\", \"Tico\", 'Damas' ko'rganlar qilar havas")


#5 ning 4-darajasini toping
print(5**4)


#22 ni 4 ga bo'lganda qancha qoldiq qoladi?
print(22%4)


#Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
print("Tomonlari 125 ga teng kvadratning yuzi", 125*125, "ga teng, perimetri", 4*125, "ga teng")


#Diametri 12 ga teng bo'lgan doiraning yuzini toping ( π=3.14 deb oling)
print("Diametri 12 ga teng bo'lgan doiraning yuzi", 3.14*(12/2)**2, "ga teng")


#Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping (Pifagor teoremasidan foydalaning)
print("Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburakning gipotenuzasi", (6**2+7**2)**(1/2), "ga teng")





##################################O'zgaruvchilar#########################

"""
O'ZGARUVCHILARNI NOMLASH
O'zgaruvchilarga nom berishda quyidagi qoidalarga amal qiling:

O'zgaruvchi nomi harf yoki pastki chiziq (_) bilan boshlanishi kerak
O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas
O'zgaruvchi nomida faqatgina lotin alifbosi harflari (A-z), raqamlar (0-9) va pastki chiziq (_) qatnashishi mumkin
O'zgaruvchi nomida bo'shliq (пробел) bo'lishi mumkin emas
O'zgaruvchi nomida katta-kichik harflar turlicha talqin qilinadi (ism, ISM, va Ism uchta turli o'zgaruvchi)
Qo'shimcha qoida sifatida:

O'zgaruvchi nomini kichik harflar bilan yozing.
O'zgaruvchi nomida 2 va undan ortiq so'z qatnashsa ularning orasini pastki chiziq (_) bilan ajrating (ism_sharif="Anvar Narzullaev")
O'zgaruvchiga tushunarli nom bering (y=20 emas yosh=20, d="Korea" emas davlat = "Korea" va hokazo)
Shuningdek o'zgaruvchilarga Pythonda ishlatiladigan funktsiyalar va maxsus kalit so'zlarning (keywords) nomini bermang. Kalit so'zlar ro'yhatini ko'rish uchun Spyder konsolida avval help() deb yozing va Enter tugmasini bosing. Keyin esa keywords deb kiritib, yana Enter bosing. Marhamat, ekraningizda Pythondagi maxsus kalit so'zlar ro'yhatini ko'ryapsiz:

"""
#----------AMALIYOT-------------#

# "Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida konsolga chiqaring
matn = "Hello World!"
print(matn)

# xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring, keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.
xabar = "Assalom alaykum"
print(xabar)

# class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering va konsolga chiqaring (siz kutgan natija chiqdimi?)
# O'zgaruvchini class deb nomlash mumkin emas, sababi class bu maxsus kalit so'z.
"""
class = 5
print(class)
"""

#Quyidagi kodni bajaring
radius = 5
pi = 3.14159
aylana_yuzi = pi * radius**2
print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)













