### :( Başka ödevlerden dolayı projeyi yetiştiremedim o yüzden yarım bırakmak zorunda kaldım :(



class islemler:
    kayit=[]
    dersSayisi=0
    dersOrtalama=0
    dersNotlari={}


      

#İsim Modülü    
    count=0
    while (count < 3):
        name=input("İsim soyisim giriniz: ")
        if(name=="Hazar Demircan"):
            print(f"Merhaba, {name}")
            break
        else:
            print("Yanlış girdiniz, tekrar deneyin...")
            count+=1

#Ders giriş fonksiyonu        
def dersAlma(x):
  for i in range(x):
   islemler.kayit=input(f"{i+1}.Ders ismi giriniz: ")
   i+=1 
          
x=int(input("Kaç ders almak istiyorsunuz: "))       
dersAlma(x)

if(x<3):
    print("Yetersiz ders sayısı...")
    dersAlma(x)
    
    
secilen=int(input("secmek istediğiniz dersin numarası: "))
print(f"sectiğiniz ders: {islemler.kayit[secilen-1]}")



vize=int(input("Vize notu: "))
final=int(input("Final notu: "))
proje=int(input("Proje notu: "))


    
islemler.dersNotlar={islemler.kayit[0],islemler.kayit[1],islemler.kayit[2]} 



    




    
    
    

    

    


            
        
           

