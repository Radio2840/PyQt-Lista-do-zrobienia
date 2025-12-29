**Autor: Kinga Smolarek. Aplikacja do robienia notatek**

# Opis
Aplikacja na system Windows 10 do tworzenia list rzeczy do zrobienia wraz z kalkulatorem bmi.
Aplikacja zawiera 3 listy, Główna, robocza i zakończone.
Do każdej listy można dodawać i usuwać elementy.
**Po każdych zmianach nalerzy zapisać przyciskiem zapisz**

## Przygotowanie do uruchomienia
### **UWAGA! Komendy działają na nowszej wersji pythona (3.13)**
### bez odpowiedniej wersji mogą pojawić się problemy takie jak nie znalezienie paczek.
1. Ściągnij wszystkie pliki do jednego folderu
2. Odpal ten folder w środowisku programistycznym np. visual studio code
    - W przypadku visual studio code musimy zainstalować wstyczkę python do kompilacji kodu
3. W terminalu środowiska wpisz komendę `pip install -r requariaments.txt` lub `python pip install -r requariaments.txt`
    - W razie dalszych problemów `py -m pip install -r requariaments.txt` lub `python -m pip install -r requariaments.txt`
4. Przejdź do pliku main.py
5. za pomocą środowiska uruchom ten plik

## Uruchomienie testów
1. W terminalu wpisz komendę `pytest tests.py`
2. Dokładniejszy widok testów `pytest -v tests.py`
    - Podobnie jak z instalacją w razie problemów proszę spróbować następujących komend
        - `py -m pytest -v tests.py`
        - `python -m pytest -v tests.py`

# Wnioski

Projekt można o wiele bardziej rozwinąć np. dodać: zaznaczanie wiele elementów na raz,
drag and drop, ładniejsze rozłożenie elementów lub dodawanie treści po wciśnięciu enter.
Użyłam prostych rozwiązań dla ułatwienia i przyspieszenia pisania takich jak zapis do pliku.

Aplikacja jest moim zdaniem trochę toporna, i trzeba by było nad nią dużo popracować, poszukać lepszych rozwiązań.

