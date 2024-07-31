#Bismillah


#Butun sonlarni ham o'zgaruvchida saqlash, ularning ustida qo'shish (+), ayirish (-), ko'paytirish(*), bo'lish (/) kabi arifmetik amalarni bajarish mumkin:
a = 20  # Sonlar musbat yoko
b = -30 # manfiy bo'lishi mumkin
c = a + b
print(c)





#Python - operatorlar orasidagi bo'shliqlarni inobatga olmaydi. O'qishga qulay bo'lishi uchun yuqoridagi kabi (bo'shliqlar bilan) yozishingiz mumkin.

# Kvadratning yuzini hisoblaymiz
kvdrt_tmni = 20 # Kavdratning tomoni 20 ga teng
kvdrt_yuzi = kvdrt_tmni**2 # Kvadrat yuzini hisoblaymiz
print(kvdrt_yuzi)




#FLOATS — O'NLIK SONLAR
pi = 3.14159 # o'nlik son (float)
radius = 10  # butun son (integer)
diametr = 2*radius
print("Aylana uzunligi ", pi*diametr, " ga teng.")




 #sonni bo'lish (/) natijasida o'nlik son hosil bo'ladi (natija butun bo'lsa ham).
a = -20
b = 40
c = b/a
print(c) # natija o'nlik son bo'ladi


#Shuningdek butun va o'nlik sonlar o'rtasidagi har qanday arifmetik amallarning natijasi ham o'nlik son bo'ladi.

a = 2
b = 3.0

# Quyidagi arifmetik amallarning natijasi o'nlik son hosil qiladi
print(a+b) 
print(a*b)
print(a**b)
print(2*(a+b))





#UZUN SONLARNI KIRITISH
aholi_soni = 7_594_000_000 # o'zmizga qulay bo'lishi uchun shinday yozdik
print("Yer kurrasida", aholi_soni, " ga yaqin odam yashaydi")





#KONSTANTA
PI = 3.14159
raduis = 21.2





#BIR NECHTA O'ZGARUVCHIGA QIYMAT BERISH
x, y, z = 10, -7.25, -30



"""
=========O'ZGARUVCHI TURINI ALMASHTIRISH

Pythonda bir turdagi o'zgaruvchini boshqa turga o'tkazish mumkin, bu ingliz tilida typecasting detiladi. Buning uchun Pythonda mahsus funktsiyalar bor, keling ular bilan tanishamiz:

str()— int yoki float turidagi sonlarni matnga o'zgartiradi.
int()— matn yoki float ko'rinishidagi qiymatlarni butun songa o'zgartiradi. Bunda matn butun son ko'rinishida bo'lishi kerak.
float()— matn yoki int ko'rinishidagi qiymatlarni o'nlik songa o'zgartiradi.

"""

ism = 'Jobir'
yosh = 36
xabar = ism + ' ' + str(yosh) + ' yoshda'
print(xabar)





#O'ZGARUVCHI TURINI TEKSHIRISH
ism = 'Jobir'
yosh = 36
print(type(ism))  # ism degan o'zgaruvchining turini konsolga chiqaramiz
print(type(yosh)) # ismyosh degan o'zgaruvchining turini konsolga chiqaramiz





#========INPUT() VA SONLAR

#1 foydalanuvchining tug'ilgan yilini so'raymiz va qiymatni int ga aylantiramiz
t_yil = int(input("Tug'ilgan yilingizni kiriting: "))

#2 foydalanuvchi yoshini xisoblaymiz
yosh = 2020 - t_yil # 

#3 foydalanuvchi yoshini konsolga chiqaramiz
print("Siz " + str(yosh) + " yoshda ekansiz")







#######================-----------Amaliyot-----------=========################


#Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur yozing.

son = int(input("Istalgan sonni kiriting: "))
print(son, " ning kvadrati ", son**2, " ga teng")
print(son, " ning kubi ", son**3, " ga teng")




#Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur

yosh = int(input("Yoshingiz nechida? "))
t_yosh = 2024 - yosh
print(f"Siz {t_yosh} - yilda tug'ilgansiz")



#Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur

son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))

print(son1*son2)
print(son1/son2)
print(son1+son2)
print(son1-son2)

