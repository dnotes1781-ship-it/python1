{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## unit-5 mutable data structure(15 marks)\n",
    "-list,dictionary,set,frozenset,lambda function"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## list\n",
    "- mutable,dynamicsequence\n",
    "- iterable,can be indexed,sliced and iterated through\n",
    "- duplicate elements are allowed\n",
    "- mixed datatypes are allowed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[] [] [1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "l = []\n",
    "m = list()\n",
    "n = [1,2,3,4]\n",
    "print(l,m,n)"
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
      "['p', 'y', 't', 'h', 'o', 'n']\n"
     ]
    }
   ],
   "source": [
    "l = 'python'\n",
    "m = list(l)\n",
    "print(m)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## list is slow"
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
      "1884366715968\n",
      "140721088702240\n",
      "140721088702336\n"
     ]
    }
   ],
   "source": [
    "l = [1,2,3,4]\n",
    "print(id(l))\n",
    "print(id(l[0]))\n",
    "print(id(l[-1]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## list is mutable"
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
      "[100, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "l = [1,2,3,4]\n",
    "l[0] = 100\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## indexing & slicing"
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
      "6\n",
      "9\n",
      "[10, 9, 8, 7, 6]\n",
      "[8, 9, 10]\n",
      "[6, 7, 8, 9, 10]\n",
      "[]\n",
      "[9, 8]\n"
     ]
    }
   ],
   "source": [
    "l = [6,7,8,9,10]\n",
    "print(l[0])\n",
    "print(l[-2])\n",
    "print(l[::-1])\n",
    "print(l[2::])\n",
    "print(l[:])\n",
    "print(l[-2:-4])\n",
    "print(l[-2:-4:-1])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1D,2D AND 3D List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 4, 5]\n",
      "[[1, 2, 3], [4, 5, 6]]\n",
      "[[[1, 2, 3], [4, 5, 6]]]\n"
     ]
    }
   ],
   "source": [
    "l = [3,4,5]\n",
    "m = [[1,2,3],[4,5,6]]\n",
    "n = [[[1,2,3],[4,5,6]]]\n",
    "print(l)\n",
    "print(m)\n",
    "print(n)\n"
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
      "3\n"
     ]
    }
   ],
   "source": [
    "print(l[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "m[0][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n[0][0][0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## '+ and *'"
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
      "[3, 4, 5, 8, 9, 7]\n",
      "[3, 4, 5, 3, 4, 5, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "l1 = [3,4,5]\n",
    "l2 = [8,9,7]\n",
    "print(l1+l2)\n",
    "print(l1*3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## iterating through list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "5\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "l = [4,5,6]\n",
    "for i in l:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0 4\n",
      "1 5\n",
      "2 6\n"
     ]
    }
   ],
   "source": [
    "for i,j in enumerate(l):\n",
    "    print(i,j)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 700, 800, 900, 6]\n"
     ]
    }
   ],
   "source": [
    "l = [3,4,5,6]\n",
    "l[1:3] = [700,800,900]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3, 700, 6]\n"
     ]
    }
   ],
   "source": [
    "l = [3,4,5,6]\n",
    "l[1:3] = [700]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## list method.........."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [1,2,3,4,5,6,7,8,9]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Append - add the elements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "l.append??"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "l.append(900)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 900]\n"
     ]
    }
   ],
   "source": [
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "print(l.append('python'))"
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
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 900, 'python']\n"
     ]
    }
   ],
   "source": [
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "append() takes exactly one argument (2 given)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-25-8a35ba4d631c>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0ml\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m80\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m90\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: append() takes exactly one argument (2 given)"
     ]
    }
   ],
   "source": [
    "l.append(80,90) #append() takes exactly one argument (2 given)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "# tuple\n",
    "l.append((80,90))"
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
       "[1, 2, 3, 4, 5, 6, 7, 8, 9, 900, 'python', (80, 90)]"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## extend "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [5,6,7,8]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "l.extend??"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'int' object is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-30-2fda3d9ef847>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0ml\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mextend\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m100\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'int' object is not iterable"
     ]
    }
   ],
   "source": [
    "l.extend(100) #'int' object is not iterable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "l.extend([100])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5, 6, 7, 8, 100]"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "l.extend('python')"
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
       "[5, 6, 7, 8, 100, 'p', 'y', 't', 'h', 'o', 'n']"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "l.extend([4,5,6])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5, 6, 7, 8, 100, 'p', 'y', 't', 'h', 'o', 'n', 4, 5, 6]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## delete & clear "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'l' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-37-5affab8eef36>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[0ml\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m[\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m6\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m7\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[1;32mdel\u001b[0m \u001b[0ml\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0ml\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'l' is not defined"
     ]
    }
   ],
   "source": [
    "l = [5,6,7]\n",
    "del l \n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[6, 7]\n"
     ]
    }
   ],
   "source": [
    "l = [5,6,7]\n",
    "del l[0]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "l = [5,6,7]\n",
    "l.clear()\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## copy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 6, 7]\n",
      "[5, 6, 7]\n",
      "[5, 6, 7] [900, 6, 7] [5, 6, 7]\n"
     ]
    }
   ],
   "source": [
    "l = [5,6,7]\n",
    "m = l.copy()\n",
    "n = l[:]\n",
    "print(m)\n",
    "print(n)\n",
    "m[0] = 100\n",
    "m[0] = 900\n",
    "print(l,m,n)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 6, 7]\n",
      "[100, 6, 7] [100, 6, 7]\n"
     ]
    }
   ],
   "source": [
    "l = [5,6,7]\n",
    "m=l\n",
    "print(m)\n",
    "m[0] = 100\n",
    "print(l,m)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [5,6,6,7,5,4,6,8]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.count(6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.count(100)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [3,4,5,6,3]"
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
       "0"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.index(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.index(3,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "100 is not in list",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-57-42afed85a69b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0ml\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m100\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: 100 is not in list"
     ]
    }
   ],
   "source": [
    "l.index(100)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## insert"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [3,4,5,6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "##l.insert?? #l.insert(index, object, /)\n",
    "#Docstring: Insert object before index."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "l.insert(100,0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4, 5, 6, 0]"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "l.insert(-1,90)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4, 5, 6, 90, 0]"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [],
   "source": [
    "l.insert(-100,700)"
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
       "[700, 3, 4, 5, 6, 90, 0]"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## POP"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [6,7,8,9]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [],
   "source": [
    "l.pop?? #Remove and return item at index (default last).\n",
    "#Raises IndexError if list is empty or index is out of range.\n",
    "#Type:      builtin_function_or_method"
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
       "9"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[6, 7, 8]"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.pop(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[6, 8]"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[6]"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "pop from empty list",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-80-33a5ac1f2384>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0ml\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpop\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m: pop from empty list"
     ]
    }
   ],
   "source": [
    "l.pop()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## remove"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [3,4,5,6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "list.remove(x): x not in list",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-82-3b4c153a6789>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0ml\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mremove\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m: list.remove(x): x not in list"
     ]
    }
   ],
   "source": [
    "l.remove(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "l.remove(6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4, 5]"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## reverse "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [4,5,6,7,8]"
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
       "[8, 7, 6, 5, 4]"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l[::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[8, 7, 6, 5, 4]\n"
     ]
    }
   ],
   "source": [
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[8, 7, 6, 5, 4]\n"
     ]
    }
   ],
   "source": [
    "l = [4,5,6,7,8]\n",
    "l.reverse()\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "print(l.reverse())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4, 5, 6, 7, 8]"
      ]
     },
     "execution_count": 94,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## sort"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 4, 5, 6, 8]\n"
     ]
    }
   ],
   "source": [
    "l = [5,4,2,6,8,1]\n",
    "l.sort()\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[8, 6, 5, 4, 2, 1]\n"
     ]
    }
   ],
   "source": [
    "l = [5,4,2,6,8,1]\n",
    "l.sort(reverse=True)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['python', 'this', 'java', 'a']\n"
     ]
    }
   ],
   "source": [
    "l = ['python','this','java','a']\n",
    "l.sort(key = len ,reverse=True )\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Universal methods................\n",
    "- len,min,max,sum,sorted"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "3\n",
      "7\n",
      "25\n",
      "[3, 4, 5, 6, 7]\n",
      "[7, 6, 5, 4, 3]\n"
     ]
    }
   ],
   "source": [
    "l = [3,4,5,6,7]\n",
    "print(len(l))\n",
    "print(min(l))\n",
    "print(max(l))\n",
    "print(sum(l))\n",
    "print(sorted(l))\n",
    "print(sorted(l,reverse=True))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### sorted Vs sort"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 5, 6, 6, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "l = [6,5,2,6,8,9]\n",
    "l.sort()\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[6, 5, 2, 6, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "l = [6,5,2,6,8,9]\n",
    "sorted(l)\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## wap to extract list of even positive numbers from a given list\n",
    "    -i/p: [-4,-3,0,1,2,3,4]\n",
    "    -o/p: [2,4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4]\n"
     ]
    }
   ],
   "source": [
    "l1 = [-4,-3,0,1,2,3,4]\n",
    "l2 = []\n",
    "for i in l1:\n",
    "    if i>0 and i%2==0:\n",
    "        l2.append(i)\n",
    "print(l2)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## list comprehension \n",
    "    *syntax:*\n",
    "        ''' python\n",
    "            [ expression for iterator in iterable if <condition> ]\n",
    "        '''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4]\n"
     ]
    }
   ],
   "source": [
    "l = [i for i in [-4,-3,0,1,2,3,4] if i%2==0 and i>0]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "l = sum([i for i in [-4,-3,0,1,2,3,4] if i%2==0 and i>0])\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "l = max([i for i in [-4,-3,0,1,2,3,4] if i%2==0 and i>0])\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## wap to find the sum of elements in a list without using sum method\n",
    "    - i/p : [-2,-4,2,4,10,20]\n",
    "    - o/p : 30"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "l1 = [-2,-4,2,4,10,20]\n",
    "sum=0\n",
    "for i in l1:\n",
    "    sum+=i\n",
    "print(sum)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## wap to find sum of elements in a list except 13 which is an unlucky number, also don't count the number immediately after 13\n",
    "    - i/p: [13,1,2,4,13]\n",
    "    - o/p: 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "l = [13,1,2,4,13]\n",
    "sum = 0\n",
    "for i in l:\n",
    "    if i==13:\n",
    "        continue\n",
    "        i+=1\n",
    "        sum+=i\n",
    "print(sum)\n",
    "        "
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
       "6"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def sumlist(l):\n",
    "    if len(l) == 0:\n",
    "        return 0\n",
    "    else:\n",
    "        sum1=0\n",
    "    for i in range(len(l)):\n",
    "        if l[i] == 13 or l[i-1] == 13 and i!=0:\n",
    "            continue\n",
    "        else :\n",
    "            sum1+=l[i]\n",
    "    return sum1\n",
    "sumlist([13,1,2,4,13])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## wap to swap 1st and last member of the list \n",
    "    - i/p : [4,5,6,7]\n",
    "    - o/p : [7,5,6,4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[7, 5, 6, 4]\n"
     ]
    }
   ],
   "source": [
    "l =  [4,5,6,7]\n",
    "l[0],l[-1] = l[-1],l[0]\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## WAP to extract the length of a longest consecutive members from a list \n",
    "    - i/p : [5,3,4,100,-1,-2,2]\n",
    "    - o/p : 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [5,3,4,100,-1,-2,2]\n",
    "l.sort()\n",
    "count = l[0]\n",
    "length = 0\n",
    "for i in range(len(l)):\n",
    "    if count == l[i]:\n",
    "        length+=1\n",
    "    count+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [],
   "source": [
    "def longest(nums):\n",
    "    result = 0\n",
    "    for num in nums:\n",
    "        if num-1 not in nums:\n",
    "            curr = num\n",
    "            length =1\n",
    "            while curr+1 in nums:\n",
    "                curr+=1\n",
    "                length+=1\n",
    "            result = max(result,length)\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 129,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "longest([5,3,4,100,-1,-2,2])"
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
