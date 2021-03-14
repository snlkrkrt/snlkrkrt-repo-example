questions = {}
correct_answer = 0
questions["Ankara"] = "Türkiye'nin başkenti neresidir?:\n"
questions["Denizli"] = "Türkiye'nin horozuyla meşhur şehri neresidir?:\n"
questions["Konya"] = "Türkiye'nin en büyük yüz ölçümüne sahip şehri neresidir?:\n"
questions["Trabzon"] = "Türkiye'de sümela manastırı hangi şehirde bulunur?:\n"
questions["Galatasaray"] = "Türkiye Süper Ligi'nde en çok şampiyon olan takım hangisidir?:\n"
questions["Çin"] = "Dünya'nın en kalabalık ülkesi hangisidir?:\n"
questions["Rusya"] = "Dünya'nın en büyük yüz ölçümüne sahip ülkesi hangisidir?:\n"
questions["Madrid"] = "İspanya'nın başkenti neresidir?:\n"
questions["Roma"] = "İtalya'nın başkenti neresidir?:\n"
questions["Berlin"] = "Almanya'nın başkenti neresidir?:\n"
for k,m in questions.items():
    answer = input(m)
    if answer.title() == k:
        correct_answer += 1
print("\nDoğru Cevap Sayısı: ",correct_answer,"\nPuanınız: ",(correct_answer*10))
if correct_answer <= 5:
    print("Sonuç: Başarısız")
else:
    print("Sonuç: Başarılı")
