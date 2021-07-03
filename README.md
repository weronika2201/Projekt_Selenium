Automatyzacja przypadku testowego za pomoca Selenium WebDriver

Przypadek testowy

ID: TC_01
Tytuł: Rejestracja nowego użytkownika niepoprawnym adresem e-mail
Dane: - adres email: xxxxx
 - hasło: Abcdef123!
-             data urodzenia: 05.07.1996
Środowisko: Google Chrome Version 88.0.4324.182 (Official Build) (64-bit)
Warunek wstępny: Użytkownik nie jest zalogowany na stronie
Kroki: 1. Wejść na stronę: https://www2.hm.com/pl_pl/index.html
 2. Kliknąć przycisk „Zaloguj się”
 3. Kliknąć przycisk „Dołącz do nas”
 4. Wpisać adres email
 5. Wpisać hasło
 6. Wprowadzić datę urodzenia
 7. Kliknąć przycisk „Dołącz do nas”
Rezultat oczekiwany: Wyświetla się komunikat o niepoprawnym adresie email
Rezultat rzeczywisty: Jak oczekiwany
