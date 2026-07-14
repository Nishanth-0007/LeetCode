class Solution:
    def intToRoman(self, num: int) -> str:

        op = ""

        if num > 999:
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


        return op



        