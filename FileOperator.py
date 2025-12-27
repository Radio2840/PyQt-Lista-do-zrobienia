"""
Nazwa klasy: FileOperator
Opis: Klasa obsługuje pliki z rozszerzeniem .json 
Pola klasy: prywatne pole data_filename przechowującą nazwe pliku
Metoda i działanie: 
    get_project_file_path - jest statyczną metodą która tworzy ścieżkę
        do folderu w którym znajduje się aplikacja
    save_data - zapisuje dane do pliku nadpisując poprzednie wartości w pliku
    read_data - zwraca wartość z pliku
    delete_file - usuwa plik

"""



import json
import pathlib
import os

class FileOperator:
    
    def __init__(self, data_filename="shopping_data.json"):
        self.__data_filename = data_filename
    
    @staticmethod
    def get_project_file_path(filename):
        try:
            base_dir = pathlib.Path(__file__).resolve().parent
            file_path = base_dir / filename
            return file_path
        
        except NameError:
            return pathlib.Path(filename)
            


    def save_data(self, data):
        
        file_path = FileOperator.get_project_file_path(self.__data_filename)
        
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                print(f"Dane zapisano pomyślnie do: {file_path}")
                
        except IOError as e:
            print(f"Błąd zapisu do pliku {file_path}: {e}")

    def read_data(self):
                
        file_path = FileOperator.get_project_file_path(self.__data_filename)
        
        if not os.path.exists(file_path):
            print(f"Plik danych '{self.__data_filename}' nie istnieje. Zwracam pusty słownik.")
            return {}
            
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
                
        except json.JSONDecodeError:
            print(f"Błąd dekodowania JSON w pliku {self.__data_filename}. Plik jest uszkodzony.")
            return {}
        except IOError as e:
            print(f"Błąd odczytu pliku {file_path}: {e}")
            return {}

    def delete_file(self):
        
        file_path = FileOperator.get_project_file_path(self.__data_filename)
        
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"Plik {self.__data_filename} został usunięty.")
            except OSError as e:
                print(f"Błąd podczas usuwania pliku {self.__data_filename}: {e}")
        else:
            print(f"Plik {self.__data_filename} nie istnieje.")