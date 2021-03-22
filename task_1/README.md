## #1 Leetcode Questions

I ❤️ using Python. 🐍 

All Programs are made in Python only.

1. **XOR Operation in an Array**

First I made a list of numbers using list comprehension. I used reduce function to apply XOR operation to every element, and returned the result.

2. **Lucky Numbers in a Matrix**

It was easy to find minimum or maximum number in a row, but tricky to find in column. So I used zip function to make transpose of the given matrix. Then I simply found minimum number in each row from normal matrix and maximum number in each row from transposed matrix. Ultimately, returned the intersection of both to get the Lucky number.

3. **Minimum Time Visiting All Points**

I could not understand how to approach this problem. So I had to look up in the discussions for the hint. Sorry 🥺 (Please gimme points for being honest atleast)

4. **Merge Strings Alternately**

The code is pretty much self explanatory. I don't know how to write description for this. 😂

5. **Unique Morse Code Words**

I made a list of morse codes sorted alphabetically. Then for a given word, I ran a loop on its characters. Then looked up for the respected morse code in that list. I used ord function to find the unicode of the character and subtracted the unicode of first alphabet from it. So that I can get index of morse code from the list.