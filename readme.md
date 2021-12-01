# MemoryGameKivy

A MemoryGameKivy egy Python-ban és azon belül a Kivy framework-ben megírt memóriajáték.

## Előfeltételek

Az alábbi dolgok szüksésekes az alkalmazás futtatásához.

1. Python 3 telepítése
   * Windows 
     * <a href="https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe" target="_blank">Letöltés</a>
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
3. MySQL Connector telepítése
   * Windows terminálban (CMD):
     ```
     python -m pip install mysql-connector-python
     ```
   * Linux terminálban:
     ```
     python3 -m pip install mysql-connector-python
     ```
4. xampp telepítése
   * Windows-ra:
     * <a href="https://www.apachefriends.org/xampp-files/8.0.13/xampp-windows-x64-8.0.13-0-VS16-installer.exe" target="_blank">Letöltés</a>
   * Linux-ra:
     * <a href="https://www.apachefriends.org/xampp-files/8.0.13/xampp-linux-x64-8.0.13-0-installer.run" target="_blank">Letöltés</a>

## Futtatás

<h4>🔴 Az alább található parancsok/fájlok futtatása előtt el kell indítani a xampp control panelben a mysql-t!</h4>

Opciók:

1. Projekt megnyitása <a href="https://www.jetbrains.com/pycharm/" target="_blank">Pycharm</a>-ban.
   1. _create_db.py_ megnyitása és execute gomb
   2. _main.py_ megnyitása és execute gomb
2. Projekt megnyitása terminálból
   * Elnavigálunk a _create_db.py_ és _main.py_ fájl helyére, majd nyitunk egy terminált.
     * Windows terminálban (CMD):
       ```
       python create_db.py
       ```
       ```
       python main.py
       ```
     * Linux terminálban:
       ```
       python3 create_db.py
       ```
       ```
       python3 main.py
       ```
       
## Felhasznált képek
* <a href="https://www.flaticon.com/" target="_blank" title="Flaticon">Flaticon</a>
  * <a href="https://www.flaticon.com/free-icon/card-games_3813722" target="_blank">Alkalmazásikon</a>
  * <a href="https://www.flaticon.com/free-icon/banana_1135549" target="_blank">Banán</a>
  * <a href="https://www.flaticon.com/free-icon/cherry_1135550" target="_blank">Cseresznye</a>
  * <a href="https://www.flaticon.com/free-icon/cherry_1135550" target="_blank">Narancs</a>
  * <a href="https://www.flaticon.com/free-icon/coconut_1135557" target="_blank">Kókusz</a>
  * <a href="https://www.flaticon.com/free-icon/kiwi_1135602" target="_blank">Kiwi</a>
  * <a href="https://www.flaticon.com/free-icon/watermelon_1135553" target="_blank">Dinnye</a>

## Játék logikai alapja:
https://github.com/niavlys/memoryKivy
