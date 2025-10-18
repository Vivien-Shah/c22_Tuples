'''Tuple Operations
Outline:
Write a program to perform the following
operations: 1. Create a tuple with different
datatypes 2. Create another tuple of integers 
3. Create a new tuple by adding 9 to the
previous tuple 4. Count the occurrences of an
element in the tuple 5. Perform slicing on 
the tuple

tuplex1 = ("tuple", False, 3.2,1)
print(tuplex1)

tuplex2 = ( 4,6,2,8,3,1)
print(tuplex2)

tuplex3= tuplex2 + (9,)
print(tuplex3)

tuplex4 = (27, 40, 44, 70, 40)
print(tuplex4.count(40))

tuplex5 = (2,4,3,5,4,6,7,8,6,1)
slice1 = tuplex5[3:5]


slice2 = tuplex5[:6]
print(slice2)'''



'''Flip Flop
Outline:
Write a program to check
 whether the given tuple
- (1,2,3,3,2,1) is a
palindrome or not. 
If it's a palindrome, then it
is the same after being
reversed.
def palind(r):
    e = len(r) - 1
    s=0
    while(s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True

r = (7,5,8,3,7,1)

if(palind(r)):
    print("The tuple is Flip-Flop")'''