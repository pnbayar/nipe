def number_to_words(n):
    to19 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six',
            'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen',
            'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty',
            'Sixty', 'Seventy', 'Eighty', 'Ninety']

    def words(num):
        if num < 20:
            return to19[num]
        elif num < 100:
            return tens[num // 10] + ('' if num % 10 == 0 else ' ' + to19[num % 10])
        elif num < 1000:
            return to19[num // 100] + ' Hundred' + ('' if num % 100 == 0 else ' and ' + words(num % 100))
        else:
            return words(num // 1000) + ' Thousand' + ('' if num % 1000 == 0 else ' and ' + words(num % 1000))

    return words(n)

# Example
print(number_to_words(112))  # Output: "One Hundred Twenty Three"
