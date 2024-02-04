# factor
- maximum factor on the left (<= sqrt(n), where n is the number ) 

# nCr
C(n,r)=n!(r!(n−r)!)

# Triangle number
![picture 1](images/b402f45c06008fe6798374e21c746fe6e7e6a73fbf8b7279151904e8acc879c6.png)  

# Closed-form formula
![picture 2](images/a4d3758192fd775c06a03ff3b300e43631d6e7c70e4de964df749f059cb2c6e6.png)  

# knowledge about // and % (mod)
assume there is N stones, each round can take 1 / 2 / 3 stone per round, how many rounds are needed

-1 0 1 2 3 4 5 6 7      N
-1 0 0 0 1 1 1 2 2      N//3
 2 0 1 2 0 1 2 0 1      N % 3
 - - 1 1 1 2 2 2 2      (N+2)//3   move 2 left  <---- this need practice

or
 - - 0 0 0 1 1 1 2      (N-1)//3
