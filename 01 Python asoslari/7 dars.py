#Bismillah

#Matnlarni qo'shish uchun + operatoridan foydalanmiz
ism = 'Ahmad'
print("Mening ismim " + ism)

#kodda ism va familiya orasiga bo'shliq belgisini qo'shmaganimiz uchun ikki matn qo'shilib yozildi.
ism = 'Ahad'
familiya = 'Qayum'
print(ism + familiya)



#Tepadagu codni to'g'irlanga varianti.
ism = 'Ahad'
familiya = 'Qayum'
print(ism + ' ' + familiya) # ikki o'zgaruvchi orasiga bo'sh joy qo'shamiz



#Ikki (va undan ko'p) matn ko'rinishidagi o'zgaruvchilarni birlashtirish uchun f-string usulidan  `f"{matn1} {matn2}"` ham foydalansak bo'ladi:
ism = "Ahad"
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)


#Bu usul yordamida uzun matnlarni ham yasash mumkin: f string
ism = "James"
familiya = 'Bond'
print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")




#Matnga bo'shliq qo'shish uchun `\t` belgisidan, yangi qatordan boshlash uchun `\n` belgisidan foydalanamiz:
print('Hello World!')
print('Hello \tWorld!')
print('Hello \nWorld!')



#upper() metodi matndagi har bir harfni katta harfga o'zgartiradi.
ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())



#lower() metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi.
ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.lower())




#title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi.
ism_sharif = 'james bond'
print(ism_sharif.title())




#capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.
ism_sharif = 'james bond'
print(ism_sharif.capitalize())


"""
strip(), rstrip() va lstrip() metodlari
Bu metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.

lstrip() — matn boshidagi bo'shliqni,
rstrip() – matn oxiridagi bo'shliqni,
strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi
"""

meva = "     olma     "
print("Men " + meva.lstrip() + " yaxshi ko'raman")
print("Men " + meva.rstrip() + " yaxshi ko'raman")
print("Men " + meva.strip() + " yaxshi ko'raman")
print("Men " + meva + " yaxshi ko'raman")




#Buning uchun input() funktsyasidan foydalanamiz.                             
#Shu paytgacha biz o'zgaruvchilarning qiymatini dasturning ichida berayotgan edik. Keling endi qiymatni o'zimiz emas, balki dastur foydalanuvchilariga kiritish imkonini beramiz. 

ism = input("Ismingiz nima?")
print("Assalom alaykum, " + ism)


#############-----------------Amaliyot-------------##################

# 1  Quyidagi o'zgaruvchilarni yarating:
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"

# 2 Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring
print("Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati")


# 3 Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
kocha = input("Ko'changiz nomi?\n>>>")
mahalla = input("Mahallangiz nomi?\n>>>")
tuman = input("Tumaningiz nomi?\n>>>")
viloyat = input("Viloyatingiz nomi?\n>>>")
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")



# 4 Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing.
print(f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati")


# 5 Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.

manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil.title())
print(manzil.upper())
print(manzil.lower())
print(manzil.capitalize())
















