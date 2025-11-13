{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## t2 imp programs"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1) wap to convert int number to romam"
   ]
  },
  {
   "attachments": {
    "download.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![download.png](attachment:download.png)"
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
      "enter the number -2025\n",
      "the roman number for 2025 is MMXXV\n"
     ]
    }
   ],
   "source": [
    "def int_roman(num):\n",
    "    value_to_roman = [(1000,\"M\") , \n",
    "                      (900,\"CM\"),\n",
    "                      (500,\"D\"),\n",
    "                      (400,\"CD\"),\n",
    "                      (100,\"C\"),\n",
    "                      (90,\"XC\"),\n",
    "                      (50,\"L\"),\n",
    "                      (40,\"XL\"),\n",
    "                      (10,\"X\"),\n",
    "                      (9,\"IX\"),\n",
    "                      (5,\"V\"),\n",
    "                      (4,\"IV\"),\n",
    "                      (1,\"I\")\n",
    "                     ]\n",
    "    romannumber = \"\"\n",
    "    for value,roman in value_to_roman:\n",
    "        while num>=value:\n",
    "           romannumber += roman\n",
    "           num -= value\n",
    "    return romannumber \n",
    "number = int(input(\"enter the number -\"))\n",
    "if 1 <= number <=3999:\n",
    "    roman = int_roman(number)\n",
    "    print(f\"the roman number for {number} is {roman}\")\n",
    "else:\n",
    "    print(\"please enter the number from 1 to 3999\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2) WAP -> Roman to Int"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the roman numberMMXXV\n",
      "the integer value of MMXXV is 2025\n"
     ]
    }
   ],
   "source": [
    "def roman_to_int(roman):\n",
    "    romandict = {\n",
    "        'I':1,\n",
    "        \"V\":5,\n",
    "        \"X\":10,\n",
    "        \"L\":50,\n",
    "        \"C\":100,\n",
    "        \"D\":500,\n",
    "        \"M\":1000\n",
    "    }\n",
    "    total = 0\n",
    "    previous = 0\n",
    "    for char in reversed(roman):\n",
    "        current = romandict[char]\n",
    "        if current < previous:\n",
    "            total -= current\n",
    "        else:\n",
    "            total += current\n",
    "        previous = current\n",
    "    return total\n",
    "romannumber = input(\"enter the roman number\")\n",
    "integer = roman_to_int(romannumber)\n",
    "print(f\"the integer value of {romannumber} is {integer}\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3) From a given array of integers,find the length of longest consecutive elements sequence - \n",
    "    - i/p: [100,4,200,1,3,2]\n",
    "    - o/p : 4\n",
    "        \n",
    "    -i/p: [-3,-2,-1,0,6,7,9,8,4,5]\n",
    "    -o/p: 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "def longest(nums):\n",
    "    result = 0\n",
    "    nums = set(nums)\n",
    "    for num in nums:\n",
    "        if num-1 not in nums:\n",
    "            curr = num\n",
    "            length = 1\n",
    "            while curr+1 in nums:\n",
    "                curr +=1\n",
    "                length += 1\n",
    "            result = max(result,length)\n",
    "    return result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "longest([100,4,200,1,3,2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "longest([-3,-2,-1,0,6,7,9,8,4,5])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4) WAP to count number of zeros enclosed between 1 in given binary numbers\n",
    "\n",
    "```\n",
    "    i/p = 010010100\n",
    "    o/p = 3\n",
    "    \n",
    "    i/p =000100010000\n",
    "    o/p = 3\n",
    "    \n",
    "    i/p = 1000100010\n",
    "    o/p = 6\n",
    "\n",
    "```"
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
       "'100101'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s = '010010100'\n",
    "s = s.strip('0')\n",
    "s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.count('0')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5) WAP to perform following task\n",
    "```\n",
    "    i/p: 1+1+1+3+3+3+2+2+2+5+5+5+5+4+4+4+4\n",
    "    o/p: 1+1+1+2+2+2+3+3+3+4+4+4+4+5+5+5+5\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'1+1+1+2+2+2+3+3+3+4+4+4+4+5+5+5+5'"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\"+\".join(sorted('1+1+1+3+3+3+2+2+2+5+5+5+5+4+4+4+4'.split('+')))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6) WAP to convert number to English words"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "def convert_words(num):\n",
    "    units = [\"\", \"one\", \"two\", \"three\", \"four\", \"five\", \"six\", \"seven\", \"eight\", \"nine\"]\n",
    "    teens = [\"ten\", \"eleven\", \"twelve\", \"thirteen\", \"fourteen\", \"fifteen\", \n",
    "             \"sixteen\", \"seventeen\", \"eighteen\", \"nineteen\"]\n",
    "    tens = [\"\", \"\", \"twenty\", \"thirty\", \"forty\", \"fifty\", \n",
    "            \"sixty\", \"seventy\", \"eighty\", \"ninety\"]\n",
    "\n",
    "    def convertbelow100(n):\n",
    "        if n < 10:\n",
    "            return units[n]\n",
    "        elif 10 <= n < 20:\n",
    "            return teens[n - 10]\n",
    "        else:\n",
    "            return tens[n // 10] + (\" \" + units[n % 10] if n % 10 != 0 else \"\")\n",
    "\n",
    "    if num == 0:\n",
    "        return \"zero\"\n",
    "\n",
    "    result = \"\"\n",
    "    if num >= 100:\n",
    "        result += units[num // 100] + \" hundred\"\n",
    "        if num % 100 != 0:\n",
    "            result += \" \"\n",
    "\n",
    "    result += convertbelow100(num % 100)\n",
    "    return result.strip()\n"
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
       "'nine hundred eight'"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "convert_words(908)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 7) WAP to count number of substring that have equal number of 0 1 and 2 in a given string containing 0 1 and 2 only \n",
    "\n",
    "```\n",
    "    i/p : 102100211\n",
    "    o/p : 102\n",
    "        021\n",
    "        210\n",
    "        210021\n",
    "        021\n",
    "        total substring - 5\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "def getsubstring(s):\n",
    "    n = len(s)\n",
    "    count = 0\n",
    "    for i in range(n):\n",
    "        countzero = 0\n",
    "        countone = 0\n",
    "        counttwo = 0\n",
    "        \n",
    "        for j in range(i, n):\n",
    "            if s[j] == \"0\":\n",
    "                countzero += 1\n",
    "            elif s[j] == \"1\":\n",
    "                countone += 1\n",
    "            elif s[j] == \"2\":\n",
    "                counttwo += 1\n",
    "                \n",
    "            if countzero == countone and countone == counttwo:\n",
    "                count += 1\n",
    "                print(s[i:j+1])\n",
    "    \n",
    "    return count\n"
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
      "102\n",
      "021\n",
      "210\n",
      "210021\n",
      "021\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "getsubstring(\"102100211\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 8) pb-442"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter list :[1,2,3,4]\n",
      "('1', '2', '3', '4')\n"
     ]
    }
   ],
   "source": [
    "# part A\n",
    "l = eval(input(\"enter list :\"))\n",
    "t = tuple(map(lambda x:  str(x),l))\n",
    "print(t)"
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
      "enter list :[1,2,3,4]\n",
      "(10, 20, 30, 40)\n"
     ]
    }
   ],
   "source": [
    "# part B\n",
    "l = eval(input(\"enter list :\"))\n",
    "t = tuple(map(lambda x: x*10,l))\n",
    "print(t)"
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
      "enter list :[1,2,3,4]\n",
      "24\n"
     ]
    }
   ],
   "source": [
    "# part C\n",
    "from functools import reduce\n",
    "l = eval(input(\"enter list :\"))\n",
    "print((reduce(lambda x,y : x*y,l)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#part D\n",
    "def countchar(s,char):\n",
    "    count = 0\n",
    "    for c in s:\n",
    "        if c==char:\n",
    "            count+=1\n",
    "    return count\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "countchar('hello','l')"
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
      "1\n",
      "-1\n"
     ]
    }
   ],
   "source": [
    "#part E\n",
    "def findchar(s,char):\n",
    "    for i in range(len(s)):\n",
    "        if s[i] == char:\n",
    "            return i\n",
    "    return -1\n",
    "print(findchar('hello','e'))\n",
    "print(findchar('hello','z'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 9) pb-444"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'!\"#$%&\\'()*+,-./:;<=>?@[\\\\]^_`{|}~'"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import string\n",
    "string.punctuation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "def isvalid(password):\n",
    "    has_upper = False\n",
    "    has_lower = False\n",
    "    digitcount = 0\n",
    "    has_special = False\n",
    "    \n",
    "    for char in password:\n",
    "        \n",
    "        if char.isupper():\n",
    "            has_upper = True\n",
    "        \n",
    "        elif char.islower():\n",
    "            has_lower = True\n",
    "        \n",
    "        elif char.isdigit():\n",
    "            digitcount+=1\n",
    "        \n",
    "        elif char in \"!#$%&\\'()*+,-./:;<=>?@[\\\\]^_`{|}~\" :\n",
    "            has_special = True\n",
    "            \n",
    "#     if (has_upper and has_lower and 1<=digitcount <=3 and has_special and 8<= len(password) <=15):\n",
    "\n",
    "    if (has_upper and has_lower and 1<=digitcount and has_special and 8<= len(password)):\n",
    "       print(\"password is valid\")\n",
    "    else:\n",
    "       print(\"password is invalid\")\n",
    "                    \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "password is valid\n"
     ]
    }
   ],
   "source": [
    "isvalid(\"Ab1@defg\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 10)Given a list of scores of two students , return the avg of top 5 scores in following format\n",
    "```\n",
    "    i/p : [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]\n",
    "        \n",
    "    o/p: [[1,87] ,[2,88]]\n",
    "        \n",
    "    explanation - the student with id 1 has avg score 87\n",
    "    the student with id 2 has avg score of 88 (integer division of 88.6)\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "def highest(items):\n",
    "    if not items:\n",
    "        return[]\n",
    "    scoremap ={}\n",
    "    for item in items:\n",
    "        if item[0] in scoremap:\n",
    "            scoremap[item[0]].append(item[1])\n",
    "        else:\n",
    "            scoremap[item[0]] = [item[1]]\n",
    "    print(scoremap)\n",
    "    result =[]\n",
    "    for key,value in scoremap.items():\n",
    "        value.sort(reverse = True)\n",
    "        if len(value) >= 5:\n",
    "            average = value[:5]\n",
    "            print(scoremap)\n",
    "        else:\n",
    "            average = value\n",
    "        scoremap[key] = sum(average) // len(average)\n",
    "        result.append([key,scoremap[key]])\n",
    "    return result"
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
      "{1: [91, 92, 60, 65, 87, 100], 2: [93, 97, 77, 100, 76]}\n",
      "{1: [100, 92, 91, 87, 65, 60], 2: [93, 97, 77, 100, 76]}\n",
      "{1: 87, 2: [100, 97, 93, 77, 76]}\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[[1, 87], [2, 88]]"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "highest([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]])"
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
