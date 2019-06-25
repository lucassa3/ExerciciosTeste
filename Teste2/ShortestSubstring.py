{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf500
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red255\green255\blue254;\red0\green0\blue0;
\red19\green120\blue72;\red144\green1\blue18;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c100000\c100000\c99608;\cssrgb\c0\c0\c0;
\cssrgb\c3529\c53333\c35294;\cssrgb\c63922\c8235\c8235;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl420\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 def\cf4 \strokec4  findShortestSubstringLen(string, target):\cb1 \
\pard\pardeftab720\sl420\partightenfactor0
\cf4 \cb3   min_window_len = \cf5 \strokec5 0\cf4 \cb1 \strokec4 \
\cb3   char_dict = \{\}\cb1 \
\
\cb3   \cf2 \strokec2 for\cf4 \strokec4  i \cf2 \strokec2 in\cf4 \strokec4  \cf2 \strokec2 range\cf4 \strokec4 (\cf2 \strokec2 len\cf4 \strokec4 (target)):\cb1 \
\cb3     \cf2 \strokec2 if\cf4 \strokec4  target[i] \cf2 \strokec2 not\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  char_dict:\cb1 \
\cb3       char_dict[target[i]] = \cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 else\cf4 \strokec4 :\cb1 \
\cb3       char_dict[target[i]] += \cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\cb3   \cb1 \
\cb3   counter = \cf5 \strokec5 0\cf4 \cb1 \strokec4 \
\cb3   ptr = \cf5 \strokec5 0\cf4 \cb1 \strokec4 \
\
\cb3   \cf2 \strokec2 print\cf4 \strokec4 (char_dict)\cb1 \
\
\cb3   \cf2 \strokec2 for\cf4 \strokec4  i \cf2 \strokec2 in\cf4 \strokec4  \cf2 \strokec2 range\cf4 \strokec4 (\cf2 \strokec2 len\cf4 \strokec4 (string)):\cb1 \
\cb3     \cf2 \strokec2 if\cf4 \strokec4  string[i] \cf2 \strokec2 in\cf4 \strokec4  char_dict:\cb1 \
\cb3       char_dict[string[i]] -= \cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\
\cb3       \cf2 \strokec2 if\cf4 \strokec4  char_dict[string[i]] >= \cf5 \strokec5 0\cf4 \strokec4 :\cb1 \
\cb3         counter += \cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\cb3     \cb1 \
\cb3     \cf2 \strokec2 while\cf4 \strokec4  counter == \cf2 \strokec2 len\cf4 \strokec4 (target):\cb1 \
\cb3       \cf2 \strokec2 if\cf4 \strokec4  (i + \cf5 \strokec5 1\cf4 \strokec4  - ptr < min_window_len) \cf2 \strokec2 or\cf4 \strokec4  (min_window_len == \cf5 \strokec5 0\cf4 \strokec4 ):\cb1 \
\cb3         min_window_len = i + \cf5 \strokec5 1\cf4 \strokec4  - ptr\cb1 \
\cb3         \cf2 \strokec2 print\cf4 \strokec4 (string[ptr:i+\cf5 \strokec5 1\cf4 \strokec4 ])\cb1 \
\
\cb3       \cf2 \strokec2 if\cf4 \strokec4  string[ptr] \cf2 \strokec2 in\cf4 \strokec4  char_dict:\cb1 \
\cb3         char_dict[string[ptr]] += \cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\cb3       \cb1 \
\cb3         \cf2 \strokec2 if\cf4 \strokec4  char_dict[string[ptr]] > \cf5 \strokec5 0\cf4 \strokec4 :\cb1 \
\cb3           counter -= \cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\cb3           \cb1 \
\cb3       ptr += \cf5 \strokec5 1\cf4 \cb1 \strokec4 \
\cb3   \cb1 \
\cb3   \cf2 \strokec2 return\cf4 \strokec4  min_window_len\cb1 \
\
\
\pard\pardeftab720\sl420\partightenfactor0
\cf2 \cb3 \strokec2 print\cf4 \strokec4 (findShortestSubstringLen(\cf6 \strokec6 "dabbcabcd"\cf4 \strokec4 , \cf6 \strokec6 "abcd"\cf4 \strokec4 ))\cb1 \
}