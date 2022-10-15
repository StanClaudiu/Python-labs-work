def isPalindrom(number) :
    reversed = 0
    initial = number
    while(number != 0) :
        reversed = reversed * 10 + number % 10
        number = number // 10
    return reversed == initial

def findNumbPalAndBestPal(*numbers) :
    palindroms = list(filter(isPalindrom,numbers))
    return (len(palindroms),max(palindroms))

print(findNumbPalAndBestPal(11,12,15,21,121,919))        