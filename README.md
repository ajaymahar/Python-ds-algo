# Python Data-Strucute And Algorithm
---
>Solving data-structure and algorithm problems using python language.

#Test
For running some specific tests you can do this as following (Ex: sort):
```bash
 mkdir <directory name>
 cd  <directory name>
 git clone https://github.com/ajaykmahar/python-datastrucute-algo.git
 cd  python-datastrucute-algo
 ```
 However, it is a good practice to isolate Python environments by creating a virtual environment. In order to install pytest in an isolated virtual environment:
 ```bash
 Python 3

$ pip3 install -U virtualenv
$ python3 -m virtualenv venv
$ source venv/bin/activate # in Windows -> $ venv\Scripts\activate.bat
$ pip install pytest
$ pip install pytest-cov
_________________________________________

Python 3.6+

$ python3 -m venv venv
$ source venv/bin/activate # in Windows -> $ venv\Scripts\activate.bat
$ pip install pytest
``` 
Check pytest version.

 ```bash 
  pytest --version
 ```
How to run test cases ?
```bash 
python -m pytest -v
 OR
py.test -v

```

How to run code coverage for test cases ?
```bash 
pyton -m pytest --cov=solutions -v
 OR
py.test --cov=solutions -v

```
List of Implementations
---
* [Solutions](https://github.com/ajaykmahar/python-datastrucute-algo/tree/master/solutions)
    * [Arrays](https://github.com/ajaykmahar/python-datastrucute-algo/tree/master/solutions/Arrays)
        * [anagrams.py](https://github.com/ajaykmahar/python-datastrucute-algo/blob/master/solutions/Arrays/anagrams.py)
        * [pair_sum.py](https://github.com/ajaykmahar/python-datastrucute-algo/blob/master/solutions/Arrays/pair_sum.py)
        * [move_all_zeroes.py](https://github.com/ajaykmahar/Python-datastructure-and-algorithm/blob/master/solutions/Arrays/move_all_zeroes.py)

---

* [Tests](https://github.com/ajaykmahar/python-datastrucute-algo/tree/master/tests)
    * [test_anagrams.py](https://github.com/ajaykmahar/python-datastrucute-algo/blob/master/tests/test_anagrams.py)
    * [test_pair_sum.py](https://github.com/ajaykmahar/python-datastrucute-algo/blob/master/tests/test_pair_sum.py)
    * [test_move_all_zeroes.py](https://github.com/ajaykmahar/Python-datastructure-and-algorithm/blob/master/tests/test_move_all_zeroes.py)

