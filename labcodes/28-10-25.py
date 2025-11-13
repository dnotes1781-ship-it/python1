{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# unit 4 (immutable data structure)- 10 marks\n",
    "# unit 5 - 15 marks\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# string:\n",
    "- An immutable data structure\n",
    "- it is an iterable & can be indexed. sliced or looped through "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# creating string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "S = \"H\"\n",
    "t = \"hi\"\n",
    "u = \"hello\"\n",
    "v = \" this is python tutorial \""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'> <class 'str'> <class 'str'> <class 'str'>\n"
     ]
    }
   ],
   "source": [
    "print(type(S),type(t),type(u),type(v))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "h\n",
      "l\n",
      "d\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'hello world'"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = \"hello world\"\n",
    "print(s[0])\n",
    "print(s[2])\n",
    "print(s[-1])\n",
    "# print(s[100])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'world'"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = \"hello world\"\n",
    "s[:]\n",
    "s[: :]\n",
    "s[: :2]\n",
    "# reverseing string\n",
    "s[: :-1]\n",
    "s[1:3]\n",
    "s[1:]\n",
    "s[1:-1]\n",
    "s[1:-1:-1]\n",
    "s[-1:1:-1]\n",
    "s[-5:-2:1]\n",
    "s[-2:-5:1]\n",
    "s[-2:-5:-1]\n",
    "s[-5:]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# universal methods \n",
    "- len, min , max , sorted"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "11\n"
     ]
    }
   ],
   "source": [
    "s = 'hello world'\n",
    "print(len(s))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " \n"
     ]
    }
   ],
   "source": [
    "print(min(s))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "w\n"
     ]
    }
   ],
   "source": [
    "print(max(s))\n",
    "# ans: from ascii value"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "119"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#for ascii value\n",
    "ord('w')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[' ', 'd', 'e', 'h', 'l', 'l', 'l', 'o', 'o', 'r', 'w']"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['w', 'r', 'o', 'o', 'l', 'l', 'l', 'h', 'e', 'd', ' ']"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sorted(s,reverse = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world\n"
     ]
    }
   ],
   "source": [
    "print(s)\n",
    "# bcz string is immutable so its can't change"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "sorted?? \n",
    "# formula chacking in exam "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# comparison operator "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'hi' == 'hi'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"hi\" < \"Hi\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "104 72\n"
     ]
    }
   ],
   "source": [
    "print(ord(\"h\") ,ord(\"H\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"hEllo\" < \"hello\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# logical operator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello'"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'hello' or 'python'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'python'"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\" or 'python'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "' '"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\" \" or 'python'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'python'"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'hello' and 'python'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "''"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\" and 'python'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'python'"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\" \" and 'python'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not ''"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# membership operator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'p' in 'python'\n",
    "\n",
    "'pt' in 'python'\n",
    "\n",
    "'py' in 'python'\n",
    "\n",
    "'z' not in 'python'\n",
    "\n",
    "'z'  in 'python'\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# iterating through string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n",
      "hello\n",
      "hello\n",
      "hello\n",
      "hello\n"
     ]
    }
   ],
   "source": [
    "s = 'hello'\n",
    "for i in s :\n",
    "    print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "h🐍e🐍l🐍l🐍o🐍"
     ]
    }
   ],
   "source": [
    "s = 'hello'\n",
    "for i in s :\n",
    "    print(i,end=\"🐍\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Enumerate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 -- h\n",
      "1 -- e\n",
      "2 -- l\n",
      "3 -- l\n",
      "4 -- o\n"
     ]
    }
   ],
   "source": [
    "s = 'hello'\n",
    "for index,value in enumerate(s):\n",
    "    print(index,\"--\",value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 p\n",
      "1 y\n",
      "2 t\n",
      "3 h\n",
      "4 o\n",
      "5 n\n"
     ]
    }
   ],
   "source": [
    "s = 'python'\n",
    "for i,j in enumerate(s):\n",
    "    print(i,j)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [],
   "source": [
    "enumerate??"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "50 p\n",
      "51 y\n",
      "52 t\n",
      "53 h\n",
      "54 o\n",
      "55 n\n"
     ]
    }
   ],
   "source": [
    "s = 'python'\n",
    "for i,j in enumerate(s,start=50):\n",
    "    print(i,j)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# string method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['__add__',\n",
       " '__class__',\n",
       " '__contains__',\n",
       " '__delattr__',\n",
       " '__dir__',\n",
       " '__doc__',\n",
       " '__eq__',\n",
       " '__format__',\n",
       " '__ge__',\n",
       " '__getattribute__',\n",
       " '__getitem__',\n",
       " '__getnewargs__',\n",
       " '__gt__',\n",
       " '__hash__',\n",
       " '__init__',\n",
       " '__init_subclass__',\n",
       " '__iter__',\n",
       " '__le__',\n",
       " '__len__',\n",
       " '__lt__',\n",
       " '__mod__',\n",
       " '__mul__',\n",
       " '__ne__',\n",
       " '__new__',\n",
       " '__reduce__',\n",
       " '__reduce_ex__',\n",
       " '__repr__',\n",
       " '__rmod__',\n",
       " '__rmul__',\n",
       " '__setattr__',\n",
       " '__sizeof__',\n",
       " '__str__',\n",
       " '__subclasshook__',\n",
       " 'capitalize',\n",
       " 'casefold',\n",
       " 'center',\n",
       " 'count',\n",
       " 'encode',\n",
       " 'endswith',\n",
       " 'expandtabs',\n",
       " 'find',\n",
       " 'format',\n",
       " 'format_map',\n",
       " 'index',\n",
       " 'isalnum',\n",
       " 'isalpha',\n",
       " 'isascii',\n",
       " 'isdecimal',\n",
       " 'isdigit',\n",
       " 'isidentifier',\n",
       " 'islower',\n",
       " 'isnumeric',\n",
       " 'isprintable',\n",
       " 'isspace',\n",
       " 'istitle',\n",
       " 'isupper',\n",
       " 'join',\n",
       " 'ljust',\n",
       " 'lower',\n",
       " 'lstrip',\n",
       " 'maketrans',\n",
       " 'partition',\n",
       " 'replace',\n",
       " 'rfind',\n",
       " 'rindex',\n",
       " 'rjust',\n",
       " 'rpartition',\n",
       " 'rsplit',\n",
       " 'rstrip',\n",
       " 'split',\n",
       " 'splitlines',\n",
       " 'startswith',\n",
       " 'strip',\n",
       " 'swapcase',\n",
       " 'title',\n",
       " 'translate',\n",
       " 'upper',\n",
       " 'zfill']"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#in exam if you forget string methods then use this .................\n",
    "s = \"THis is a python 101 tutorial\"\n",
    "dir(s)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# capitalize()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'This  is a python 101 tutorial'"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.capitalize()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# upper(),lower(),& swapcase()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'THIS  IS A PYTHON 101 TUTORIAL'"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.upper()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'this  is a python 101 tutorial'"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.lower()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'thIS  IS A PYTHON 101 TUTORIAL'"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.swapcase()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# title"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'This  Is A Python 101 Tutorial'"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.title()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "count() takes at most 3 arguments (4 given)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-80-f68bd47d8a17>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0ms\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcount\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'i'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m \u001b[0ms\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcount\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'i'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m6\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: count() takes at most 3 arguments (4 given)"
     ]
    }
   ],
   "source": [
    "s.count('i')\n",
    "\n",
    "s.count('i',3)\n",
    "\n",
    "s.count('i',3,5)\n",
    "\n",
    "s.count('i',3,6,1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# find"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# s.find(\"is\",3)\n",
    "s.find(\"is\",3,100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.find(\"z\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "THis  is a python 101 tutorial\n"
     ]
    }
   ],
   "source": [
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.index(\"is\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.index(\"is\",3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "substring not found",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-92-5dade37699b5>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0ms\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"z\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: substring not found"
     ]
    }
   ],
   "source": [
    "s.index(\"z\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# isalpha(),isalnum(),isdigit(),isnumeric(),islower(),isupper(),isspace()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 96,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "True\n",
      "True\n",
      "this\n",
      "THIS\n",
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "print (\"abc\".isalpha())\n",
    "print (\"123abc\".isalnum())\n",
    "print (\"123\".isdigit())\n",
    "print (\"456\".isnumeric())\n",
    "print (\"this\".lower())\n",
    "print (\"THIS\".upper())\n",
    "print (\"This Is\".istitle())\n",
    "print(\"\".isspace())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['this', 'is', 'a', 'python', 'class']"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = \"this is a python class\"\n",
    "# s.split()\n",
    "\n",
    "s.split(maxsplit=6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['python']"
      ]
     },
     "execution_count": 98,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = 'python'\n",
    "s.split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['this', 'isa', 'python']"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'this.isa.python'.split(\".\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['this', 'isa', 'python']"
      ]
     },
     "execution_count": 103,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'this#isa#python'.split(\"#\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['this', 'python#class']"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'this#python#class'.split(\"#\",1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['this', 'python', 'class']"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'this#python#class'.split(\"#\",-1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# join"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'this.is.a.python.class'"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\".\".join(['this', 'is', 'a', 'python', 'class'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'thisisapythonclass'"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"\".join(['this', 'is', 'a', 'python', 'class'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'this is a python class'"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\" \".join(['this', 'is', 'a', 'python', 'class'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# replace"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'thiz iz a python class'"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.replace(\"is\",\"iz\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'th🍕 is a python class'"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.replace(\"is\",\"🍕\",1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Strip method"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is a python class\n"
     ]
    }
   ],
   "source": [
    "\"  hello  \".strip()\n",
    "\n",
    "\"hello  \".strip()\n",
    "\n",
    "\"  hello\".strip()\n",
    "print(s)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'is is a python cla'"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.strip(\"ths\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'hello'"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"  hello  \".strip()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ello  '"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"hello  \".strip(\"oph\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# wap to count number of spaces , uppercase , lower case & digits in a given string\n",
    "## -input:\n",
    "    - This is a Python 101 course\n",
    "## -output :\n",
    "    -lowercase : 17\n",
    "    -uppercase : 2\n",
    "    -digits:-3\n",
    "    -spaces -5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a string: This is a Python 101 course\n",
      "Spaces: 5\n",
      "Uppercase letters: 2\n",
      "Lowercase letters: 17\n",
      "Digits: 3\n"
     ]
    }
   ],
   "source": [
    "# Input from user\n",
    "text = input(\"Enter a string: \")\n",
    "\n",
    "# Initialize counters\n",
    "spaces = 0\n",
    "uppercase = 0\n",
    "lowercase = 0\n",
    "digits = 0\n",
    "\n",
    "# Loop through each character in the string\n",
    "for char in text:\n",
    "    if char == ' ':\n",
    "        spaces += 1\n",
    "    elif char.isupper():\n",
    "        uppercase += 1\n",
    "    elif char.islower():\n",
    "        lowercase += 1\n",
    "    elif char.isdigit():\n",
    "        digits += 1\n",
    "\n",
    "# Display the results\n",
    "print(\"Spaces:\", spaces)\n",
    "print(\"Uppercase letters:\", uppercase)\n",
    "print(\"Lowercase letters:\", lowercase)\n",
    "print(\"Digits:\", digits)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
