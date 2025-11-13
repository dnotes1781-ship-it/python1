{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1) wap to find the maximum even number from given tuple ---\n",
    "- i/p : (6,7,8,4,2,5,9,1)\n",
    "- o/p :(6,8,4,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(6, 8, 4, 2)\n"
     ]
    }
   ],
   "source": [
    "x = tuple(i for i in (6,7,8,4,2,5,9,1) if i%2==0)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# generator \n",
    "- it store the values & lazily executes the line of code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8\n"
     ]
    }
   ],
   "source": [
    "x =max (tuple(i for i in (6,7,8,4,2,5,9,1) if i%2==0))\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "x =min (tuple(i for i in (6,7,8,4,2,5,9,1) if i%2==0))\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6]\n"
     ]
    }
   ],
   "source": [
    "x =sorted (tuple(i for i in (6,4,3,2,1) if i%2==0))\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 4, 6)\n"
     ]
    }
   ],
   "source": [
    "x =tuple(sorted (tuple(i for i in (6,4,3,2,1) if i%2==0)))\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{16, 1, 4, 9}\n"
     ]
    }
   ],
   "source": [
    "x = {i**2 for i in(1,2,1,3,4,2)}\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2 )wap \n",
    "- i/p : \"2+2+3+2+1+1+1+3+3+2+2+5+5+4+4+5+4+1+2\"\n",
    "- o/p : \"1+1+1+1+2+2+2+2+2+2+3+3+3+4+4+4+5+5+5\"\n",
    "- string i/p "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1+1+1+1+2+2+2+2+2+2+3+3+3+4+4+4+5+5+5'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = \"2+2+3+2+1+1+1+3+3+2+2+5+5+4+4+5+4+1+2\"\n",
    "\"+\".join(sorted(s.split(\"+\")))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 3)wap to shift a number -\n",
    "-i/p: 123456"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "54321\n"
     ]
    }
   ],
   "source": [
    "shift=6\n",
    "n =12345\n",
    "s=str(n)\n",
    "length = len(s)\n",
    "if shift > length:\n",
    "    x = s[::-1]\n",
    "else :\n",
    "    x=s[shift:]+s[:shift]\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# wap pb:312\n"
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
      "valid password\n"
     ]
    }
   ],
   "source": [
    "def passwordcheck(password):\n",
    "    l,u,p,d = 0,0,0,0\n",
    "    \n",
    "    if len(password) >= 8:\n",
    "        for i in password:\n",
    "            if i.isupper():\n",
    "                u+=1\n",
    "            if i.islower():\n",
    "                l+=1\n",
    "            if i.isdigit():\n",
    "                d+=1\n",
    "            if i in \"@_$\":\n",
    "                p+=1\n",
    "        if l>=1 and u>=1 and d>=1 and p>=1 and l+p+u+d == len(password):\n",
    "            print(\"valid password\")\n",
    "        else :\n",
    "            print(\"invalid password\")\n",
    "    else :\n",
    "        print(\"less than 8 elements - invalid password\")\n",
    "passwordcheck(\"Ram@_f1234\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# wap (pb.314)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'OMLHW HQJ'"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def encrypt(message,key):\n",
    "    message = message.upper()\n",
    "    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\n",
    "    result = \"\"\n",
    "    for letter in message:\n",
    "        if letter in alpha:\n",
    "            letterindex = (alpha.find(letter) +key) % len(alpha) \n",
    "            result += alpha[letterindex]\n",
    "        else:\n",
    "            result += letter\n",
    "    return result\n",
    "encrypt(\"LJIET ENG\",3)                                 "
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
       "'IGFBQ BKD'"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def encrypt(message,key):\n",
    "    message = message.upper()\n",
    "    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\n",
    "    result = \"\"\n",
    "    for letter in message:\n",
    "        if letter in alpha:\n",
    "            letterindex = (alpha.find(letter) +key) % len(alpha) \n",
    "            result += alpha[letterindex]\n",
    "        else:\n",
    "            result += letter\n",
    "    return result\n",
    "encrypt(\"LJIET ENG\",-3)                                 "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# WAP (PB:315) - sorted , find , membership"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a stringhello world\n",
      "enter a stringdlorw olleh\n",
      "balanced\n"
     ]
    }
   ],
   "source": [
    "s1 = input(\"enter a string: \")\n",
    "s2 = input(\"enter a string: \")\n",
    "if sorted(s1) == sorted(s2):\n",
    "    print(\"balanced\")\n",
    "else:\n",
    "    print(\"unbalanced\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a stringhello world\n",
      "enter a stringdlorw olleh\n",
      "balanced\n"
     ]
    }
   ],
   "source": [
    "s1 = input(\"enter a string: \")\n",
    "s2 = input(\"enter a string: \")\n",
    "flag = 0\n",
    "for i in s1:\n",
    "    if i in s2:\n",
    "        continue\n",
    "    else:\n",
    "        flag = 1\n",
    "        break \n",
    "if flag == 1:\n",
    "    print(\"not balanced \")\n",
    "else:\n",
    "    print(\"balanced\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# WAP (pb: 303)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a string: this is python\n",
      "ThiS IS PythoN \n"
     ]
    }
   ],
   "source": [
    "s = input(\"enter a string: \")\n",
    "s = s.title()\n",
    "s.split()\n",
    "m = s.split()\n",
    "result=\"\"\n",
    "for i in m:\n",
    "    result += i[:-1] + i[-1].upper() + \" \"\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\".join[i[:-1] + i[-1] .upper() +\" \" for i in ]"
   ]
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
