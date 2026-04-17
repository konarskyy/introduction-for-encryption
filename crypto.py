# =======================================
# Crypto 101 - szyfry podstawowe
# Szyfr Cezara + szyfr Vigenere'a: szyfrowanie i łamanie
# =======================================

# Szyfr Cezara
def caesar_encrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            # przesuniecie litery o określoną wartość shift
            # ord() zamienia litere na liczbe
            # %26 zapewnia, że przesunięcie będzie w zakresie alfabetu
            # chr() zamienia liczbę z powrotem na literę
            shifted = (ord(char) - ord('A') + shift) % 26
            result += chr(shifted + ord('A'))
        else:
            # znaki białe pozostają bez zmian
            result += char
    return result

def caesar_decrypt(text, shift):
    #deszyfrowanie szyfru cezara to wywołanie metody jeszcze raz z odwornym shiftem
    return caesar_encrypt(text, -shift)

# Szyfr Cezara za pomocą bruteforce
def caesar_bruteforce(ciphertext):
    #sprawdzenie wszystkich możliwych przesunięć od 0 do 25
    print("\n[Brute force Cezara - wszystkie mozliwosci: ]")
    print("-" * 45)
    for shift in range(1, 26):
        decrypted = caesar_decrypt(ciphertext, shift)
        print(f" Klucz {shift:2d}: {decrypted}")

#szyfr Vigenere'a
def vigenere_encrypt(text, key):
    result = ""
    text = text.upper()
    key = key.upper()
    key_index = 0 #osobny licznik klucza, zeby pomijac znaki biale
    for char in text:
        if char.isalpha():
            #przesuniecie litery o wartosc klucza
            shift = ord(key[key_index % len(key)] - ord('A'))
            shifted = (ord(char) - ord('A') + shift) % 26
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    text = text.upper()
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            #odejmowanie przesuniecia klucza zamiast dodawania
            shift = ord(key[key_index % len(key)] - ord('A'))
            shifted = (ord(char) - ord('A') - shift) % 26
            result += chr(shifted + ord('A'))
            key_index += 1
        else:
            result += char
    return result

#analiza czestotliwosci dla szyfru Vigenere'a
def frequency_analysis(ciphertext, lang="pl"):
    frequency_tables = {
        "en": "ETAOINSHRDLCUMWFGYPBVKJXQZ",
        "pl": "AIOWEZNSRWTDMYKLPJCHGBFUQXVZ"
        #w tym przypadku ignoruje polskie znaki diakrytyczne, gdyz szyfr Cezara i Vigenere'a działają tylko na podstawowym alfabecie łacińskim
    }

    if lang not in frequency_tables:
        print(f"Nieznany język: {lang}. Dostępne opcje: {', '.join(frequency_tables.keys())}")
        return
    expected_frequency = frequency_tables[lang]
    lang_name = "polski" if lang == "pl" else "angielski"

    #zliczanie wystapien liter w szyfrogramie
    counts = {}
    total = 0
    for char in ciphertext.upper():
        if char.isalpha():
            counts[char] = counts.get(char, 0) + 1
            total += 1
    if total == 0:
        print("brak liter do analizy")
        return
    #sortowanie
    sorted_letters = sorted(counts, key=counts.get, reverse=True)
    print(f"\n[Analiza częstotliwości — język: {lang_name}]")
    print("-" * 55)
    print(f"  {'Litera':6} | {'Wystąpienia':11} | {'%':5} | Prawdopodobna oryginalna")
    print("  " + "-" * 51)
    for i, letter in enumerate(sorted_letters[:8]):
        percent = (counts[letter] / total) * 100
        original_guess = expected_frequency[i] if i < len(expected_frequency) else "?"
        print(f"  {letter:6} | {counts[letter]:11} | {percent:4.1f}% | {original_guess}")

    # Zakładamy że najczęstsza litera w szyfrogramie odpowiada
    # najczęstszej literze w danym języku
    most_common = sorted_letters[0]
    most_common_in_lang = expected_frequency[0]
    guessed_shift = (ord(most_common) - ord(most_common_in_lang)) % 26

    print(f"\n  Najczęstsza litera w szyfrogramie: {most_common}")
    print(f"  Najczęstsza litera w języku {lang_name}: {most_common_in_lang}")
    print(f"  Prawdopodobny klucz: {guessed_shift}")
    print(f"  Odszyfrowany tekst: {caesar_decrypt(ciphertext, guessed_shift)}")

#menu działania programu
def main():
    print("=" * 50)
    print("  Crypto 101 — szyfry klasyczne")
    print("=" * 50)
    print("\n  1. Szyfruj   — Cezar")
    print("  2. Deszyfruj — Cezar")
    print("  3. Łam       — Cezar (brute force)")
    print("  4. Szyfruj   — Vigenere")
    print("  5. Deszyfruj — Vigenere")
    print("  6. Analiza częstotliwości (łamanie Cezara)")
    print("  0. Wyjście")

    while True:
        print()
        choice = input("Wybierz opcję: ").strip()

        if choice == "1":
            text = input("Tekst: ")
            shift = int(input("Przesunięcie (1-25): "))
            print(f"Zaszyfrowany: {caesar_encrypt(text, shift)}")

        elif choice == "2":
            text = input("Szyfrogram: ")
            shift = int(input("Przesunięcie (1-25): "))
            print(f"Odszyfrowany: {caesar_decrypt(text, shift)}")

        elif choice == "3":
            text = input("Szyfrogram do złamania: ")
            caesar_bruteforce(text)

        elif choice == "4":
            text = input("Tekst: ")
            key = input("Klucz (słowo): ")
            print(f"Zaszyfrowany: {vigenere_encrypt(text, key)}")

        elif choice == "5":
            text = input("Szyfrogram: ")
            key = input("Klucz (słowo): ")
            print(f"Odszyfrowany: {vigenere_decrypt(text, key)}")

        elif choice == "6":
            text = input("Szyfrogram do analizy: ")
            print("  Język: 1. Polski  2. Angielski")
            lang_choice = input("  Wybierz język (1/2): ").strip()
            lang = "pl" if lang_choice == "1" else "en"
            frequency_analysis(text, lang)

        elif choice == "0":
            print("Koniec.")
            break

        else:
            print("Nieznana opcja.")

if __name__ == "__main__":
    main()