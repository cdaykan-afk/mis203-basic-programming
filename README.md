# mis203-basic-programming
Name:Çağan Deniz Aykan
Student number:2504109002 
Department name:Management Information System
Course Name: MIS203 Basic Programming
Week1:
Name:Çağan Deniz Aykan Student number:2504109002
Department name:Management Information System 
Course Name: MIS203 Basic Programming
AI Tool Used:gemini
prompt:Basit bir python programı oluştur, program ismimi ,yaşımı, departmanımı ve carrer goalımı sorsun
output olarak da küçük bir öğrenci profili versin,i changed the output part by mainly putting some different codes with the help of AI to make it more beautiful
Week2:
AI Tool:Gemini
Prompt:Bir döngü yap. Döngüde isim iste (Enter student name (or q to quit):). 'q' girilirse break ile çık.Not iste (Enter score:). Not 0-100 aralığında değilse "Invalid score. Please enter a number between 0 and 100." yazdırıp continue ile başa dön. Not baremi (A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: 0-59) üzerinden formatı yazdır: Ali: 85 -> B
Çıkışta toplam öğrenci sayısı ve 2 basamak yuvarlanmış ortalamayı yazdır (Total students: X, Average score: Y.YY). Hiç öğrenci girilmediyse "No students entered." bas. hepsini İngilizce şekilde yap.  
What i changed:i changed the end part when the output is given it does a little table to make it look a little bit cool
break işlevi: input kısmında eğer q yazarsam programı bitiriyor ve çıktı olarak eğer öğrenci yazdıysan en sondaki kısma atıyor ve ortalama ile öğrenci sayısını çıkarıyor,öğrenci yazılmazsa da no students entered yazısı veren son kısma atıyor programı
Week3:
AI Tool:Gemini
Prompt:Kullanıcıdan "q" girilene kadar isim, yaş (0–120 arası tam sayı), gün (hafta içi/hafta sonu) ve öğrencilik (evet/hayır) bilgilerini input ile alan bir Python programı yaz, geçersiz girişlerde uygun uyarıyı verip continue, çıkışta ise break kullanarak döngüyü yönet bilet taban fiyatını hafta içi 200 TL, hafta sonu 250 TL kabul edip sırasıyla 6 yaş altı (%100, Free), 65 yaş ve üzeri (%50, Senior), 6–12 yaş (%40, Child), 25 yaş ve altı öğrenci (%30, Student) ve diğerleri (%0, Standard) öncelik sırasına göre tek bir indirim uygula her satışı İsim: Fiyat TRY (Kategori) formatında 2 ondalık basamakla yazdır ve döngü bittiğinde toplam satılan bilet, toplam gelir, ortalama bilet fiyatı (2 ondalıklı) ile ücretsiz bilet sayısını özetle (hiç bilet satılmadıysa yalnızca "No tickets sold." bas) , programı ingilizce şekilde yap
What i changed: i changed the output of the program with the code print( "=" * 36) so it looks good 
test: first i write q and it give me No tickets sold, then i wrote one 13 year old boy and he is not a student so he does not get any discount , thirdly i wrote 3 4 names with each of them with different age area one 6 , one 14,one 26, one 66 it give me different outcomes even tho i did say every one of them are students
 conditional statements stop evaluating at the very first matching condition, placing the Student rule first would incorrectly give a 10-year-old student only the 30% Student discount instead of their rightful 40% Child discount. Maintaining the proper hierarchy ensures overlapping qualifications always resolve in favor of the more generous benefit.
