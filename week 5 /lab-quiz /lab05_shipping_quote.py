# MIS 2. Sınıf - Lab 05: Shipping Quote Programı

# 1. Fonksiyon: Ara toplam hesaplama
def calculate_subtotal(unit_price, quantity):
    subtotal = unit_price * quantity
    return subtotal

# 2. Fonksiyon: Miktara göre indirim oranı belirleme
def determine_discount_rate(quantity):
    if quantity >= 50:
        return 0.10  # %10 indirim
    elif quantity >= 10:
        return 0.05  # %5 indirim
    else:
        return 0.0   # İndirim yok

# 3. Fonksiyon: Kargo ücreti hesaplama (İndirimli fiyata göre)
def calculate_shipping_fee(discounted_subtotal, shipping_method):
    # Kullanıcı büyük/küçük harf yazarsa diye küçültüyoruz
    method = shipping_method.lower()
    
    if method == "express":
        return 18.00
    elif method == "standard":
        # Eşik değeri: 100 TL/Dolar ve üzeri kargo bedava
        if discounted_subtotal >= 100.00:
            return 0.00
        else:
            return 7.50
    else:
        return 5.00

# 4. Fonksiyon: Genel toplamı hesaplama
def calculate_final_total(subtotal, discount_rate, shipping_fee):
    discount_amount = subtotal * discount_rate
    total = (subtotal - discount_amount) + shipping_fee
    return total

# Sipariş fişini ekrana basan yardımcı fonksiyon (Kod tekrarını önler)
def print_quote(order_id, unit_price, quantity, shipping_method):
    subtotal = calculate_subtotal(unit_price, quantity)
    discount_rate = determine_discount_rate(quantity)
    discount_amount = subtotal * discount_rate
    discounted_subtotal = subtotal - discount_amount
    shipping_fee = calculate_shipping_fee(discounted_subtotal, shipping_method)
    final_total = calculate_final_total(subtotal, discount_rate, shipping_fee)

    print(f"--- Sipariş Özeti: {order_id} ---")
    print(f"Ürün Adedi: {quantity} x {unit_price:.2f} TL")
    print(f"Ara Toplam: {subtotal:.2f} TL")
    print(f"İndirim Oranı: %{int(discount_rate * 100)} (-{discount_amount:.2f} TL)")
    print(f"Kargo Ücreti ({shipping_method}): {shipping_fee:.2f} TL")
    print(f"Ödenecek Tutar: {final_total:.2f} TL\n")


# --- ASSERT TESTLERİ ---
# 1. Matematik testi
assert calculate_subtotal(10.0, 5) == 50.0

# 2. Sınır testi: 9 adette indirim 0 olmalı, tam 10 adette %5 başlamalı
assert determine_discount_rate(9) == 0.0
assert determine_discount_rate(10) == 0.05

# 3. Kargo eşik testi: 99.99'da kargo çıkmalı, 100.00'da ücretsiz olmalı
assert calculate_shipping_fee(99.99, "standard") == 7.50
assert calculate_shipping_fee(100.00, "standard") == 0.00


# --- ÖRNEK SİPARİŞLER ---
# Sipariş 1: Küçük sipariş (indirim yok, kargo ücretli)
print_quote("ORD-01", 15.0, 4, "standard")

# Sipariş 2: 10 adet eşiğini geçen sipariş (indirimli ve ücretsiz kargo)
print_quote("ORD-02", 20.0, 10, "standard")

# Sipariş 3: Toptan sipariş (express kargo)
print_quote("ORD-03", 8.0, 60, "express")
