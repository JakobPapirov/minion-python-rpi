# minion-python-rpi
This repo will host python3 scripts I've cooked up for my daughter, age 4, to play with on her RPI 1B (works on RPI 4 too)

# Important
For programmatical and "source of Truth" reasons English will be the default language in which scripts will be written in.

All programmes are to be translated into Swedish and Russian over time.

## Dev
* Python 3.9 dev
  * Python 3.7 on RPI 4, 8 Gb (Will be tested on the RPI 1)
  * On the RPI python version used needs to be changed from 2.x to latest
* Dev environment virtual (Cmder) environment Windows & PyCharm (and terminal)
* On RPI tested via Putty and locally
  * WinSCP

## 3rd party Dependencies
* NumPy - pip install numpy
* mpmath - pip install mpmath
* yachalk - pip install yachalk
* emoji - pip install emoji

## Structure [as per 2023-04-20]
* en\
  * math\
    1) math-numbers-all-en.py
    2) math-numbers-en.py
    basicMath\
     1) math-add-0-9-en.py
     2) math-add-0-13-en.py
     3) math-add-8-12-en.py
     4) math-add-10-20-en.py
     5) math-add-10s-0-100-en.py
     6) math-sub-0-9-en.py
  * lang\
   en\
    1. letters-all-en.py
    2. letters-bg-en.py
    3. letters-sm-en.py
    4. numbers-en.py
   sv\
    1. letters-all-en.py
    2. letters-bg-en.py
    3. letters-sm-en.py
    4. numbers-en.py
   Python\
    1. keywords-py-en.py
  * games\boutique\
    1. boutique.py (en)
  
* sv\
  * math\
    1) math-numbers-all-sv.py
    2) math-numbers-sv.py
    basicMath\
     1) math-add-0-9-sv.py
     2) math-add-0-13-sv.py
     3) math-add-8-12-sv.py
     4) math-add-10-20-sv.py
     5) math-add-10s-0-100-sv.py
     6) math-sub-0-9-sv.py
  * lang\
   en\
    1. letters-all-sv.py
    2. letters-bg-sv.py
    3. letters-sm-sv.py
   sv\
    1. letters-all-sv.py
    2. letters-bg-sv.py
    3. letters-sm-sv.py
  
* ru\
  * math\
     1) math-numbers-all-ru.py
    2) math-numbers-ru.py
    basicMath\
     1) math-add-0-9-ru.py
     2) math-add-0-13-ru.py
     3) math-add-8-12-ru.py
     4) math-add-10-20-ru.py
     5) math-add-10s-0-100-ru.py
     6) math-sub-0-9-ru.py
  * lang\
   en\
    1. letters-all-ru.py
    2. letters-bg-ru.py
    3. letters-sm-ru.py
   sv\
    1. letters-all-ru.py
    2. letters-bg-ru.py
    3. letters-sm-ru.py 

### Math
The names of the programmes should be explicit enough to explain their purpose and limitations.
* math = category of programme
* add = addition
* sub = subtraction
* x-y = range, least value -> highest value, including in both cases.
* Xs = numbers have an increment in the 10s or more.


### Languages
The main language folder dictates in which language the greeting and farewell messages will be written in and other interactive text. The sub-language folder specifies which language is being learned. So questions should be written in the target language.

## Python

### Games
a) Please see https://github.com/JakobPapirov/minion-python-rpi/commit/e7625c3b14cbedcc0ef09bfe9a9276ea84138988 for features and limitations
