class Solution:
    def intToRoman(self, num: int) -> str:

        roman = {
            1 : "I",
            5 : "V",
            10 : "X",
            50 : "L",
            100 : "C",
            500 : "D",
            1000 : "M"
        }

        op = ""

        if num > 999:
            temp = int(str(num)[0])
            op += "M" * temp
            num -= temp * 1000

        while num > 0:
            leng = len(str(num))
            temp = int(str(num)[0])
            mul = int("1" + "0" * (leng-1))
            num -= temp * mul
            l1 = roman[mul]
            l2 = roman[5 * mul]
            l3 = roman[mul * 10]
            if temp == 9:
                op += l1 + l3
            elif temp == 4:
                op += l1 + l2
            else:
                if temp > 5:
                    op += l2 + l1*(temp-5)
                elif temp < 5:
                    op += l1 * (temp)
                else:
                    op += l2


        '''if num > 999:
            temp = int(str(num)[0])
            op += "M" * temp
            num -= temp * 1000

        if num >= 100 and num < 1000:
            temp = int(str(num)[0])
            num -= temp * 100
            if temp == 9:
                op += "CM"
            elif temp == 4:
                op += "CD"
            else:
                if temp > 5:
                    op += "D" + "C"*(temp-5)
                elif temp < 5:
                    op += "C" * (temp)
                else:
                    op += "D"

        if num >= 10 and num < 100:
            temp = int(str(num)[0])
            num -= temp * 10
            if temp == 9:
                op += "XC"
            elif temp == 4:
                op += "XL"
            else:
                if temp > 5:
                    op += "L" + "X"*(temp-5)
                elif temp < 5:
                    op += "X" * (temp)
                else:
                    op += "L"

        if num < 10:
            if num == 9:
                op += "IX"
            elif num == 4:
                op += "IV"
            else:
                if num > 5:
                    op += "V" + "I"*(num-5)
                elif num < 5:
                    op += "I" * (num)
                else:
                    op += "V"

'''
        return op



        