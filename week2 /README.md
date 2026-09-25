AI Tool:Gemini
Prompt:Bir döngü yap. Döngüde isim iste (Enter student name (or q to quit):). 'q' girilirse break ile çık.Not iste (Enter score:). Not 0-100 aralığında değilse "Invalid score. Please enter a number between 0 and 100." yazdırıp continue ile başa dön. Not baremi (A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59) üzerinden formatı yazdır: Ali: 85 -> B
Çıkışta toplam öğrenci sayısı ve 2 basamak yuvarlanmış ortalamayı yazdır (Total students: X, Average score: Y.YY). Hiç öğrenci girilmediyse "No students entered." bas. hepsini İngilizce şekilde yap.  
What i changed:i changed the end part when the output is given it does a little table to make it look a little bit cool
break işlevi: input kısmında eğer q yazarsam programı bitiriyor ve çıktı olarak eğer öğrenci yazdıysan en sondaki kısma atıyor ve ortalama ile öğrenci sayısını çıkarıyor,öğrenci yazılmazsa da no students entered yazısı veren son kısma atıyor programı
