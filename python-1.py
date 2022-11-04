# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 07:12:41 2019
@author: Faradars-pc2
"""
w = 'faradars'
v = ['a', 'e', 'i', 'o', 'u']
#bei jede durchlauf schreibt ein char von w ind letter
#dann prüft ob die geschpeicherte char im letter in v ist 
for letter in w:
   if letter in v:
       print(letter)
