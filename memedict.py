meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şeydir.",
            "LOL": "Yüksek bir sesle etrafa doğru gülmektir.",
            "AURA":"Havalı veya saygın sayılabilecek hareketleriyle kendilerine özgü bir atmosfer veya nitelik yaymasıdır.",
            "RIZZ":"'Karizma' kelimesinden türetilen rizz, basitçe birini büyüleme anlamına gelir.",
            "CAP" :"Birinin yalan söylediğini düşünüyorsanız 'O yalan söylüyor' yerine 'O cap yapıyor' diyebilirsiniz.(Bunu Ingilizce'de kullanmanızı daha çok tercih ederim.)"
        }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!)(cap,lol,cringe,rizz,aura): ")

if word in meme_dict.keys():
    print("Anlamı:", meme_dict[word])
    # Kelime eşleşiyorsa ne yapmalıyız?
else:
    print("Üzgünüm, bu kelime sözlükte yok.")
    # Kelime eşleşmiyorsa ne yapmalıyız?
