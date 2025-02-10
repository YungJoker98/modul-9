import pickle

# Tworzenie różnych obiektów
int_obj = 42
float_obj = 3.14
string_obj = "Hello, pickle!"
list_obj = [1, 2, 3, 4, 5]
dict_obj = {"a": 1, "b": 2, "c": 3}

def sample_function():
    return "I'm a function!"

class SampleClass:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, my name is {self.name}!"

class_instance = SampleClass("Alice")

# Zapisywanie obiektów do pliku
with open("data.pkl", "wb") as file:
    pickle.dump(int_obj, file)
    pickle.dump(float_obj, file)
    pickle.dump(string_obj, file)
    pickle.dump(list_obj, file)
    pickle.dump(dict_obj, file)
    pickle.dump(sample_function, file)
    pickle.dump(class_instance, file)

# Odczytywanie obiektów z pliku
with open("data.pkl", "rb") as file:
    int_loaded = pickle.load(file)
    float_loaded = pickle.load(file)
    string_loaded = pickle.load(file)
    list_loaded = pickle.load(file)
    dict_loaded = pickle.load(file)
    function_loaded = pickle.load(file)
    class_instance_loaded = pickle.load(file)

# Testowanie
print(int_loaded)
print(float_loaded)
print(string_loaded)
print(list_loaded)
print(dict_loaded)
print(function_loaded())  # Powinno wywołać funkcję
print(class_instance_loaded.greet())  # Powinno wywołać metodę klasy

# Odpowiedzi na pytania:
# 1. Można zapisać wiele obiektów do pliku bez opakowania ich w kontener, zapisując je kolejno.
# 2. Można zapisać instancję klasy i poprawnie ją odczytać.
# 3. Pickle nie jest bezpieczne, jeśli plik pochodzi z niezaufanego źródła, ponieważ może zawierać złośliwy kod.
