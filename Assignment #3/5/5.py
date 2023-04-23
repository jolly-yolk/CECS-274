import DLLPalindrome

dll1 = DLLPalindrome.DLList()
dll2 = DLLPalindrome.DLList()

dll1.add(0, 'a')
dll1.add(1, 'b')
dll1.add(2, 'c')
dll1.add(3, 'b')
dll1.add(4, 'a')
print(f'DLL1: {dll1}')
print()

dll2.add(0, 'a')
dll2.add(1, 'b')
dll2.add(2, 'c')
dll2.add(3, 'd')
dll2.add(4, 'e')
print(f'DLL2: {dll2}')
print()


a = dll1.is_Palindrome()
b = dll2.is_Palindrome()

if a == True:
    print('DLL1: Is Palindrome')
    print()
else:
    print('DLL1: Is Not Palindrome')
    print()
if b == True:
    print('DLL2: Is Palindrome')
else:
    print('DLL2: Is Not Palindrome')

