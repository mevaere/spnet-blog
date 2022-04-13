---
orphan: true
---
# ⚔ Protect your python code 🇬🇧
## ℹ Introduction
Python scripts can be protected in order to avoid stealing of intellectual property, algorithms or anything else you want to hide from the final user. As using an interpreter (usually CPython), your code is translated easily from human readable language (python) in python bytecodes (stored
in `__pycache__`) ; with some modifications of CPython source code, you could extract all the code (even if it's obfuscated) without difficulties.
```{admonition} How to dump code object to disk ?
Compile Python from source. Modify the `_PyEval_EvalFrameDefault` function such that it dumps the code object to disk.
```
In this article, I propose two ways of protecting your python scripts. An easy one using a python tools named **PyArmor** which relies on an external unknown not open-source library and a solider one using a tool which I appreciate whose name is **Enigma Protector** (it protects executable on windows 💠).

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
|                            Can protect all the program                             |                                                                                                    | 

### 📜 Obfuscating a script

### 💾 Obfuscating a program

### 🔐 Hardware lock

### 📦 Packaging with PyInstaller


## 🔮 Using [EnigmaProtector](https://enigmaprotector.com/)

Protection level on Windows : ⭐⭐⭐⭐⭐ \
Difficulty to implement : ⭐⭐⭐ 

|               ✅ Pros                |                  ❌ Cons                  |
|:-----------------------------------:|:----------------------------------------:|
|        Very good protection         |               Only Windows               |
|            Trial control            | Using external program (not open-source) |
|        Registration manager         |    199 $ + 69 $ / year update by dev.    |
|          Licensing system           |     Need Cython and MSVC to compile      |
|       Wide range of check-up        |       Protect sensitive parts only       |
|          Hardware Lock ++           |                                          |
|          Message designer           |                                          |
|           Protect strings           |                                          |
| VirtualBox for file/registry hiding |                                          |
|       Virtual Machine (RISC)        |                                          |

## 🔧 Prerequisites
- Using windows (enigma protector works natively on windows, 🍷 wine is suitable for running EXE on 🐧 Linux )
- Cython
- [MSVC build-tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019)
- The [enigma protector software](https://enigmaprotector.com/) (199$), the trial version will obviously raise some alerts from antivirus cause some crackers & hackers use it to
  protect/hide their malwares.
## ⚙ Installing and using Cython
```{admonition} About Cython
Cython is a programming language that aims to be a superset of the Python programming language, designed to give C-like performance with code that is written mostly in Python with optional additional C-inspired syntax. Cython is a compiled language that is typically used to generate CPython extension modules.
```
Cython could generate with your Python code a **c++ file** which could be compiled in a dynamic link library (DLL) which could be directly called by your python code.
### 🔰 Setup
```bash
pip install cython
```
### 🔄 Convert our first program
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
Now convert in `c` and compile with `msvc` in `fib.cp38-win_amd64.pyd`
```bash
python setup.py build_ext --inplace
```
| ![Image 1](../../_medias/informatique/python/shareware1.png)
|:--:| | * **DLL Export Viewer** tells us this is a valid DLL* |
Calling the dll created is really easy from python. It's just treating it like a module.
```python
import fib
fib.fib(50000000)  # will give the expected result
```


## 🛡 Protecting your app
The goal is to protect your python app. In order to do this, you will need :
- some of your most important code in a .pyx file which will be converted in c++, only this code will be protected
- call the API of enigma protector to introduce the protection (RISC virtual machine etc.)
- packed the dll produced by cython with enigma protector
- Use it !
```{important}
As you know, C compilation is largely faster than python cause it doesn't deal with python object structure. C is also faster when it deals with loops, and cause it doesn't deal with the GIL, cython gives you the opportunity to use all your CPU cores.
```
```{warning}
Be carreful, GIL exists to avoid some complex problem with memory access to shared variables and handle correctly garbage collector.
```
### ⚒ Prepare the compilation
Here we are working with a `c++` file. It doesn't change a lot except `setup.py`.
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
### ➕ Add enigma headers files in working dir
In order to compile, you need to move two files from the sdk/VC path of *Enigma Protector*. You will need to use MSVC.
File 1 : `enigma_ide.h`
File 2 : `enigma_ide64.lib`
![Image 2](../../_medias/informatique/python/shareware2.png)
In `enigma_ide.h`, just insert the following line.
```cpp
#include <windows.h>
```
### ⚔ Protecting a script
File : `script_test.pyx`
```python
# distutils: language = c++
# cython: language_level=3
# Declare EP_Marker function in enigma_ide64.lib
cdef
extern
from
"enigma_ide.h":
void
EP_Marker(char * Name)
# Declare EP_RegHardwareID function in enigma_ide64.lib
cdef
extern
from
"enigma_ide.h":
char * EP_RegHardwareID()

# Declare a trivial function
def sum_it(number1, number2):
    return number1 + number2

# Call and print the EP_RegHardwareID
print(EP_RegHardwareID())
# Crypt this stuff which will only be decrypt with registration
EP_Marker("reg_crypt_begin1")
print("This part is totally crypted")
EP_Marker("reg_crypt_end1")
# Protect this with virtualization
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
Protect the DLL with *Enigma Protector*
![Image 3](../../_medias/informatique/python/shareware3.png)
Use-it like a normal module
```python
import test_it
```
![Image 4](../../_medias/informatique/python/shareware4.png)
## 🎇 BONUS : Using Widestring Char in Cython - **wchar_t***
```python
from cpython.ref cimport
PyObject
from libc.stddef cimport
wchar_t
cdef
extern
from
"Python.h":
PyObject * PyUnicode_FromWideChar(wchar_t * w, Py_ssize_t
size)
cdef
extern
from
"enigma_ide.h":
wchar_t * EP_RegHardwareIDW()
cdef
PyObject * pystr = PyUnicode_FromWideChar(EP_RegHardwareIDW(), -1)
print( < object > pystr)
```
