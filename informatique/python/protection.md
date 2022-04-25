---
orphan: true
---

# ⚔ Protect your python code 🇬🇧

## ℹ Introduction

Python scripts can be protected in order to avoid stealing of intellectual property, algorithms or anything else you want to hide from the final user. As using an interpreter (usually CPython), your code is translated from human readable language (python) in python bytecodes (stored in `__pycache__`) ; with some modifications of CPython source code, you
could extract all the code (even if it's obfuscated) without difficulties.

```{admonition} How to dump code object to disk ?
Compile Python from source. Modify the `_PyEval_EvalFrameDefault` function such that it dumps the code object to disk.
```

In this article, I propose two ways of protecting your python scripts. An easy one using a python tool named **PyArmor** which relies on an external unknown not open-source
library and a solider one using a tool which I appreciate whose name is **Enigma Protector** (it protects executable on windows 💠).

## 🛡 Using [PyArmor](https://github.com/dashingsoft/pyarmor)

Protection level : ⭐⭐ \
Protection level on Windows : ⭐⭐⭐ \
Difficulty to implement : ⭐

|                                       ✅ Pros                                       |                                               ❌ Cons                                               |
|:----------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------:|
|                                 Multiple platforms                                 | Using external C compiled [Library](https://github.com/dashingsoft/pyarmor-core) (not open-source) |
| Full [python](https://github.com/dashingsoft/pyarmor) implementation (open-source) |                                  Virtual Machine only for Windows                                  |
|                                  52 $ by project                                   |                             Runtime obfuscation of python script only                              |
|                                   Hardware lock                                    |                             More weak protection than Enigma Protector                             |
|                                Seamless Replacement                                |                               No trial (need a double distribution)                                |
|                           Easy packing with PyInstaller                            |                          Need to have a licence file for each final user                           |
|                          Can protect the complete program                          |                 PyArmor Core need an update for each new plateform/python version                  | 

### 🔧 Prerequisites

After buying a capsule on the [website](https://github.com/dashingsoft/pyarmor), register the program.

```bash
pyarmor register pyarmor-regfile-1.zip
```

```bash
pyarmor register
> INFO     PyArmor Version 7.4.1
> INFO     Python 3.10.4
> PyArmor Version 7.4.1
> Registration Code: pyarmor-vax-000****
> This code is authorized to "Rémi MEVAERE (Personal) <****@*****.fr>"
```

The program we want to protect is composed of two scripts :

File : `main.py`

```python
from fibonacci import fibonacci

print("Welcome to the test program")
nbr = input("Please enter an integer : ")
if None != (fib_list := fibonacci(nbr)):
    print("Sequence of Fibonacci : ")
    print(fib_list)
input("Press key to stop")
```

File : `fibonacci.py`

```python
def fibonacci(n):
    try:
        nbr = int(n)
        if nbr <= 0:
            raise ValueError

        FibArray = [0, 1]

        for i in range(nbr - 2):
            FibArray.append(FibArray[-1] + FibArray[-2])

        return FibArray

    except:
        print("Incorrect input")
        return None
```

### 📜 Obfuscating a script

First we want to protect the script `fibonacci.py`. It's recommended to use `--advanced` parameter to improve the protection but it doesn't change anything for this demonstration. To protect seriously your script/program you need to use this parameter, see the manual.

```bash
pyarmor obfuscate --exact fibonacci.py  --output protected_script
```

| ![Image 1](../../_medias/informatique/python/protected_script.png)
|:--:| 
| The new directory contains the protected script `fibonnaci.py` and the library `_pytransform.dll`|

We don't know what contains `_pytransform.dll`, it's an executable from PyArmor. Not open-source.

| ![Image 1](../../_medias/informatique/python/pytransform.png)
|:--:| 
| Exported functions from `_pytransform.dll` |

File : `protected_script\fibonacci.py` is now obfuscated and unreadable.

```python
from pytransform import pyarmor_runtime
pyarmor_runtime()
__pyarmor__(__name__, __file__, b'\x50\x59\x41\x52\x4d\x4f\x52\x00\x00\x03\x0a\x00\x6f\x40\x5f\x0c\x21\x4f\xb4\xa5\x99\xa3\x7f\x6d\xe2\xb8\xa7\xf5\x32\x1c\x5a\xf7\xb2\x6d\xbd\xa5\x72\x57\x6c\xd2\x94\x4a\x38\x8d\xce\xd2\xac\x3f\x29\x2b\x26\x8f\x99\xde\xc2\xff\xb3\xa3\xa1\xbb\xcc\x1c\x83\x03\xc4\x5b\x80\x63\xb8\xef\x8a\x9d\x7f\x03\x8e\x79\x96\x14\x87\x22\xb7\x7f\x6d\x43\xf\xb1\x1c\x8b\xda\x7\xcc\x8f\x89\xbf\xa5\x74\x0a\x1e\x61\x78\x46\x37\xc1\x99\x35\xec\xe0\xfc\x33\xa9\xb\x90\x89\x36\xc7\x25\x3x37\xd8', 2)
```

The program `main.py` works as expected :

```bash
C:\Users\remi\AppData\Local\pypoetry\Cache\virtualenvs\protect-python-knxkg4Ko-py3.10\Scripts\python.exe C:/Users/remi/Documents/PyCharmProjects/protect-python/protected_script/main.py
Welcome to the test program
Please enter an integer : 55
Sequence of Fibonacci : 
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272]
Press key to stop
```

### 💾 Obfuscating a program

We want to protect the program and not only the script.

```bash
pyarmor obfuscate main.py  --output protected_program
```

The two scripts are now obfuscated in `protected_program` directory.

### 🔐 Hardware lock (protect)

Our program is not protected, it can be run by anyone. In order to protect-it we need to obfuscate it without the licence file, which will be sent to the final user.

```bash
pyarmor obfuscate main.py  --with-license outer --output register_program
```

Running the program gives us :

```bash
C:\Users\remi\AppData\Local\pypoetry\Cache\virtualenvs\protect-python-knxkg4Ko-py3.10\Scripts\python.exe C:/Users/remi/Documents/PyCharmProjects/protect-python/register_program/main.py
Read file license.lic failed, No such file or directory
```

We want to generate some licence files for decryption. Here are the options :

```{eval-rst}
-e, --expired YYYY-MM-DD       Expired date for this license
-d, --bind-disk SN        	   Bind license to serial number of harddisk
-4, --bind-ipv4 IPV4  		   Bind license to ipv4 addr
-m, --bind-mac MACADDR         Bind license to mac addr
-x, --bind-data DATA           Pass extra data to license, used to extend license type
```

We are changing our program `main.py` to `main_pyarmor.py` to extract some data bind when generating the licence.

```python
from fibonacci import fibonacci
from pytransform import get_license_info
info = get_license_info()

print("Welcome to the test program")
print("Data from licence : ",info['DATA'])
nbr = input("Please enter an integer : ")
if None != (fib_list := fibonacci(nbr)):
    print("Sequence of Fibonacci : ")
    print(fib_list)
input("Press key to stop")
```

```bash
pyarmor obfuscate main_pyarmor.py  --with-license outer --output register_program
```

In order to bind to specific material we need to get hardware info with `hdinfo` command.

```bash
pyarmor hdinfo
> Hardware informations got by PyArmor:
> Serial number of first harddisk: "FV994730S6LLF07AY"
> Default Mac address: "f8:ff:c2:27:00:7f"
> Ip address: "192.168.121.100"
```

Create a licence and copy it to the same folder of the script :

```bash
pyarmor licenses --expired 2019-10-10 --bind-data "MY_PROGRAM_V2" lic001
```

| ![Image 1](../../_medias/informatique/python/protected_program.png)
|:--:| 
| The licence file is generated in the `lic001` folder |

Running the program failed logically cause the licence is expired :

```bash
C:\Users\remi\AppData\Local\pypoetry\Cache\virtualenvs\protect-python-knxkg4Ko-py3.10\Scripts\python.exe C:/Users/remi/Documents/PyCharmProjects/protect-python/register_program/main_pyarmor.py
> License is expired
```

Generation of a new licence :

```bash
pyarmor licenses --expired 2025-10-10 --bind-disk "FV994730S6LLF07AY" --bind-data "MY_PROGRAM_V2" lic002
```

Everything works as excepted :

```bash
C:\Users\remi\AppData\Local\pypoetry\Cache\virtualenvs\protect-python-knxkg4Ko-py3.10\Scripts\python.exe C:/Users/remi/Documents/PyCharmProjects/protect-python/register_program/main_pyarmor.py
> Welcome to the test program
> Data from licence :  MY_PROGRAM_V2
> Please enter an integer : 6
> Sequence of Fibonacci : 
> [0, 1, 1, 2, 3, 5]
> Press key to stop
```

### 📦 Packaging with PyInstaller

Sometimes it's useful to pack the program in a standalone executable, in order to do that **PyArmor** provides some facilities. 

```bash
pyarmor pack main_pyarmor.py --with-license outer
```

A `dist` folder is created and the **protected executable** is inside. Copy the **licence.lic** file and run the program, that's all ! If you want to customize the executable please read the manual.

## 🔮 Using [EnigmaProtector](https://enigmaprotector.com/)

Protection level on Windows : ⭐⭐⭐⭐⭐ \
Difficulty to implement : ⭐⭐⭐

|               ✅ Pros                |                  ❌ Cons                  |
|:-----------------------------------:|:----------------------------------------:|
|        Very good protection         |               Only Windows               |
|            Trial control            | Using external program (not open-source) |
|        Registration manager         |   199 \$ + 69 \$ / year update by dev.   |
|          Licensing system           |     Need Cython and MSVC to compile      |
|       Wide range of check-up        |       Protect sensitive parts only       |
|          Hardware Lock ++           |                                          |
|          Message designer           |                                          |
|          Protected strings          |                                          |
| VirtualBox for file/registry hiding |                                          |
|       Virtual Machine (RISC)        |                                          |
|  Independant of new python version  |                                          |

### 🔧 Prerequisites

- **Microsoft windows** (enigma protector works natively on windows, 🍷 wine is suitable for running EXE on 🐧 Linux )
- Cython
- [MSVC build-tools](https://visualstudio.microsoft.com/downloads/)
- The [enigma protector software](https://enigmaprotector.com/) (199$), the trial version will raise some alerts from antivirus, cause some crackers & hackers use it to
  protect/hide their malwares.

### ⚙ Installing and using Cython

```{admonition} About Cython
Cython is a programming language that aims to be a superset of the Python programming language, designed to give C-like performance with code that is written mostly in Python with optional additional C-inspired syntax. Cython is a compiled language that is typically used to generate CPython extension modules.
```

Cython could generate with your Python code a **c++ file** which could be compiled in a dynamic link library (DLL) which could be directly called by your python code.

#### 🔰 Install Cython

```bash
pip install cython
```

#### 🔄 Convert our first program

The first file is the python file script you want to convert in C. Please note the extension **.pyx**.
File : `fib.pyx`

```python
# cython: language_level=3
def fib(n):
    """Print the Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()
```

Now we need to create the `setup.py`, which is a python Makefile (for more information
see [Source Files and Compilation](https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html)
File : `setup.py`

```python
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("fib.pyx"),
)
```

Run the following command :

```bash
python setup.py build_ext --inplace
```

It converts it in `c` and compile with `msvc` in `fib.cp38-win_amd64.pyd`

| ![Image 1](../../_medias/informatique/python/shareware1.png)
|:--:| 
| **DLL Export Viewer** tells us this is a valid DLL |

Calling the DLL created is really easy from python. Python treats it like a module :

```python
import fib

fib.fib(50000000)  # will give the expected result
```

### 🛡 Protecting your app

The goal is to protect your python app. In order to do this, you will need :

- some of your most important code in a `.pyx file` which will be converted in `c++`, this code will be protected
- call the API of enigma protector to introduce the protection (RISC virtual machine etc.)
- packed the DLL produced by cython with enigma protector
- Use it !

```{important}
C compiled file are faster than python cause they doesn't deal with python object structure. C files are also faster when they deals with loops, and cause they doesn't deal with the GIL, cython gives you the opportunity to use all your CPU cores.
```

```{warning}
Be carreful, GIL exists to avoid some complex problem with memory access to shared variables and handle correctly garbage collector.
```

### ⚒ Prepare the compilation

Here we are working with a `c++` file. It doesn't change a lot except in `setup.py`.
File : `setup.py`

```python
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    name='Test app',
    ext_modules=[
        Extension('test_it',
                  sources=['script_test.pyx'],
                  extra_link_args=['/MAP'],
                  libraries=["enigma_ide64"],
                  language="c++")
    ],
    cmdclass={'build_ext': build_ext}
)
```

### 👓 Watch the API

````{admonition} Enigma Protector API
A Marker is a set of bytes placed into the source code and helping Enigma Protector find the code inside markers for processing. A marker consists of two parts: begin marker and end marker.
```cpp
// Markers API
void __declspec(dllimport) __stdcall EP_Marker(char* Name);
```
EP_RegHardware function serves for retrieving unique user PC information. The function does not have parameters. If the function succeeds, the return value is a pointer to the null terminated ANSI string. If the function fails, the return value is 0.

```cpp
// Registration API
LPCWSTR __declspec(dllimport) __stdcall EP_RegHardwareIDW();
```
````

I will not copy all the manual in this article, if you want more infos about the API please read the manual.

### ➕ Add enigma headers files in working dir

In order to compile, you need to move two files from the sdk/VC path of *Enigma Protector*. You will need to use MSVC.
File 1 : `enigma_ide.h`
File 2 : `enigma_ide64.lib`

| ![Image 1](../../_medias/informatique/python/shareware2.png)
|:--:| 
| Copy two files in the project folder |

In `enigma_ide.h`, just insert the following line.

```cpp
#include <windows.h>
```

### ⚔ Protecting a script

File : `script_test.pyx`

```python
# distutils: language = c++
# cython: language_level=3

# import functions from enigma_ide64.lib
cdef extern from "enigma_ide.h":
    void EP_Marker(char* Name)
    char* EP_RegHardwareID()


# Declare a trivial function
def sum_it(number1, number2):
    return number1 + number2

# Call and print the EP_RegHardwareID
ansi_str_hid = str(EP_RegHardwareID(), 'cp1252')
print('ANSI :', ansi_str_hid)


# Protect this with RISC virtualization
EP_Marker("vm_risc_begin")
a = 4
b = 7
c = a + b
print('Virtualized :', c)
EP_Marker("vm_risc_end")

# Classic python code
print("Give me the sum :", sum_it(1, 2))
input("End, press key")
```

Convert and build with `msvc`

```bash
python setup.py build_ext --inplace
```

| ![Image 1](../../_medias/informatique/python/shareware3.png)
|:--:| 
| Use-it like a normal module |

```python
import test_it
```

| ![Image 1](../../_medias/informatique/python/shareware4.png)
|:--:| 
| **Output** |

### 🎇 Using Widestring Char (unicode) in Cython - **wchar_t***

Sometimes it's necessary to use more than ANSI characters, in order to use WideChar it's necessary to adapt the code.

```python
# distutils: language = c++
# cython: language_level=3

# Imports and declaration to work fromWideChar
from cpython.ref cimport PyObject
from libc.stddef cimport wchar_t

cdef extern from "Python.h":
    PyObject * PyUnicode_FromWideChar(wchar_t *w, Py_ssize_t size)

# import functions from enigma_ide64.lib
cdef extern from "enigma_ide.h":
    void EP_Marker(char* Name)
    char* EP_RegHardwareID()
    wchar_t * EP_RegHardwareIDW()

# Declare a trivial function

def sum_it(number1, number2):
    return number1 + number2

# Call and print the EP_RegHardwareID
ansi_str_hid = str(EP_RegHardwareID(), 'cp1252')
print('ANSI :', ansi_str_hid)

cdef PyObject * pystr = PyUnicode_FromWideChar(EP_RegHardwareIDW(), -1)
wide_str_hid = str(<object> pystr)
print('WideChar :', wide_str_hid)


# Protect this with RISC virtualization
EP_Marker("vm_risc_begin")
a = 4
b = 7
c = a + b
print('Virtualized :', c)
EP_Marker("vm_risc_end")

# Classic python code
print("Give me the sum :", sum_it(1, 2))
input("End, press key")

```

```bash
python setup.py build_ext --inplace
```

```bash
🛡️ Protect with Enigma ⚔️
```

```python
import test_it
> ANSI : 02EF34-F57F02
> WideChar : 02EF34-F57F02
> Virtualized : 11
> Give me the sum : 3
> End, press key
```

### 🔏 Registration feature

In order to test registration features we need to add to our program some code which will only be executed if the user is registered :

```python
# Crypt this stuff which will only be decrypted with registration
EP_Marker("reg_crypt_begin1")
print("This is an encrypted section")
nbr = input("Enter a number : ")
print(nbr + " + 5 = ", str(int(nbr) + 5))
EP_Marker("reg_crypt_end1")
```

First you need to generate a key, please note that in this article I will use WideChar (Unicode in configuration). It's more complex than ANSI, if you understand with unicode, it will be straightforward for ANSI.

| ![Image 1](../../_medias/informatique/python/shareware6.png)
|:--:| 
| **Generate** a new key for testing |

#### Registration dialog

If you want to use the registration dialog just use the dedicated API

```python
cdef extern from "enigma_ide.h":
    void EP_RegShowDialog()

if not registered:
    EP_RegShowDialog()
```

After registering the software it will **decrypt** the first section ahead. 


#### Manual registration

I prefer handle myself the registration

```python
cdef extern from "Python.h":
    wchar_t * PyUnicode_AsWideCharString(object, Py_ssize_t *)

# Declare function in enigma_ide64.lib
cdef extern from "enigma_ide.h":
    bool EP_RegCheckAndSaveKeyW(wchar_t * Name, wchar_t * Key);
```

As an example I will try with two keys, one legit and one false.

```python

reg_name = u"Test-WrongUSER"
reg_key = u"CKML369-XGSH5DW-RVG2ANU-W4FG4K4-J2RQYHM-32SD3LD-XJPKSYB-S5RPPPE-SEURZXQ"
reg_name_2 = "Rémi MEVAERE"
reg_key_2 = "CKML369-XGSH5DW-RVG2ANU-W4FG4K4-J2RQYHM-32SD3LD-XJPKSYB-S5RPPPE-SEURZXQ"
cdef Py_ssize_t length
cdef wchar_t *reg_name_wchar = PyUnicode_AsWideCharString(reg_name, &length)
cdef wchar_t *reg_key_wchar = PyUnicode_AsWideCharString(reg_key, &length)
cdef wchar_t *reg_name_wchar_2 = PyUnicode_AsWideCharString(reg_name_2, &length)
cdef wchar_t *reg_key_wchar_2 = PyUnicode_AsWideCharString(reg_key_2, &length)

print("Registration to : ", reg_name)
if EP_RegCheckAndSaveKeyW(reg_name_wchar, reg_key_wchar):
    print("Registration OK, please restart APP")
    quit()
else:
    print("Registration ERROR")

print("Registration to : ", reg_name_2)
if EP_RegCheckAndSaveKeyW(reg_name_wchar_2, reg_key_wchar_2):
    print("Registration OK, please restart APP")
    quit()
else:
    print("Registration ERROR")
```

#### Test registration

You can use the encrypted section (EP_Marker) to know if the registration succeed. But I prefer using this function in the API :

```python
cdef extern from "enigma_ide.h":
    int EP_RegKeyStatus();

registered = False
if EP_RegKeyStatus() == 1:
    registered = True

if registered:
    print("You are registered")
else:
    print("You are NOT registered")
```

### 🗃️ File virtualization

It's possible to hide some files inside the executable. You will access to these files directly from your script.

| ![Image 1](../../_medias/informatique/python/shareware5.png)
|:--:| 
| **Add** a file `virtual_file.txt` with some text |

You could read the file with python easily :

```python
with open('virtual_file.txt') as f:
    lines = f.readlines()

print("------- virtual_file.txt -------")
print(lines)
print("--------------------------------")
```

### 🧵 Protected strings

You can add some sensible protected strings in your code. We will see in this section how to retrieve them :

| ![Image 1](../../_medias/informatique/python/shareware7.png)
|:--:| 
| **Add** some strings in Enigma Protector |

#### API : Extract AnsiString or binary file

No problem in this case, cause enigma.h expose a function accepting **char*** string.

```python
from libcpp cimport bool
from libc.stdlib cimport malloc, free

cdef extern from "enigma_ide.h":
    int EP_ProtectedStringByID(int ID, char * Buffer, int Len);
```

Extract the string :

```python
buf_size = EP_ProtectedStringByID(2, b'', 0)
print("Size of the string #2: ", buf_size)

cdef char * buf_string_2 = <char *> malloc((buf_size + 1) * sizeof(char))

if EP_ProtectedStringByID(2, buf_string_2, buf_size) != 0:
    print(str(buf_string_2, 'cp1252'))
else:
    print("Error can't extract #2")

free(buf_string_2)
```

Extract the binary data :

```python

buf_size = EP_ProtectedStringByID(3, b'', 0)
print("Size of the string #3: ", buf_size)

cdef char * buf_string_3 = <char *> malloc((buf_size + 1) * sizeof(char))

if EP_ProtectedStringByID(3, buf_string_3, buf_size) != 0:
    print(buf_string_3)
else:
    print("Error can't extract #3")
    
free(buf_string_3)
```

#### API : Extract WideString

There is a problem with the API provided by Enigma, first you need to change the signature of **EP_ProtectedStringByID** in `enigma.h`

```C
// Protection API
//int __declspec(dllimport) __stdcall EP_ProtectedStringByID( int ID, const char* Str, int Len);
int __declspec(dllimport) __stdcall EP_ProtectedStringByID( int ID, const wchar_t* Str, int Len);
int __declspec(dllimport) __stdcall EP_ProtectedStringByKey( const char* Key, const char* Str, int Len);
```

```python

empty = ''
cdef wchar_t *empty_wchar = PyUnicode_AsWideCharString(empty, &length)

buf_size = EP_ProtectedStringByID(1, empty_wchar, 0) 
print("Size of the string #1: ", buf_size)

cdef wchar_t * buf_string = <wchar_t *> malloc((buf_size // sizeof(wchar_t) + 1) * sizeof(wchar_t))
cdef PyObject * pystr_2

if EP_ProtectedStringByID(1, buf_string, buf_size) != 0:
    pystr_2 = PyUnicode_FromWideChar(buf_string, -1)
    wide_string = str(<object> pystr_2)
    print('WideString :', wide_string)
else:
    print("Error can't extract #1")
```

# 💁🏻‍♂️Conclusion

In this article, we have seen how to protect our python program or some sensitive parts that we don't want to share. Each time, we have to trust an external program (not open-source). The performance will be degraded.
