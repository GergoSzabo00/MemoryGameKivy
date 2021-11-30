# MemoryGameKivy

A MemoryGameKivy egy Python-ban és azon belül a Kivy framework-ben megírt memóriajáték.

## Előfeltételek

Az alábbi dolgok szüksésekes az alkalmazás futtatásához.

1. Python 3 telepítése
   * Windows 
     * https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe
     * 🔴 Telepítésnél az Add Python 3.8 to PATH opciót be kell jelölni!
   * Linux
     * Elméletileg gyárilag kell, hogy legyen telepítve Python.
     * Ha mégsem, akkor terminálban az alábbi parancsot kell futtatni:
       ```
       sudo apt-get install python3.8
       ```
2. Kivy telepítése
   * Windows terminálban (CMD):
       ```
     python -m pip install --upgrade pip setuptools virtualenv
       ```
       ```
     python -m pip install kivy[full] kivy_examples
       ```
   * Linux terminálban:
      ```
      python3 -m pip install --upgrade pip setuptools virtualenv
      ```
      ```
      python3 -m pip install kivy[full] kivy_examples
      ```

## Futtatás

Opciók:

1. Projekt megnyitása <a href="https://www.jetbrains.com/pycharm/" target="_blank">Pycharm</a>-ban.
   * main.py fájl megnyitása és execute gomb
2. Projekt megnyitása terminálból
   * Elnavigálunk a _main.py_ fájl helyére, majd nyitunk egy terminált.
     * Windows terminálban (CMD):
       ```
       python main.py
       ```
     * Linux terminálban:
       ```
       python3 main.py
       ```
       
## Felhasznált képek
* <a href="https://www.flaticon.com/" target="_blank" title="Flaticon">Flaticon</a>
  * <a href="https://www.flaticon.com/free-icon/card-games_3813722" target="_blank">Alkalmazásikon</a>

