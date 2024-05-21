#!/usr/bin/env python3
import datetime

class CreditCard:
    # TODO: Detect card type
    def _luhn_validate(self, cardNo: str):
        nSum = 0
        second_digit=False
        for d in list(cardNo)[::-1]:
            d = int(d)*(int(second_digit)+1)

            # double-digit handling.
            nSum += d // 10
            nSum += d % 10

            second_digit = not second_digit

        return (nSum % 10 == 0)

    def _validate(self, ccnumber: str):
        if (13 <= len(ccnumber) >= 19):
            return False
        return self._luhn_validate(ccnumber)

    def __init__(self, ccnumber: str):
        if self._validate(ccnumber) == False:
            raise ValueError("Provided Credit Card is Incorrect")
        self.ccnumber = ccnumber

class Pesel:
    def _validate(self, p: str) -> bool:
        weight = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        s = 0;
        pesel = list(p)

        for i in range(len(weight)):
            s+=(int(pesel[i])*weight[i])

        return (10-(s%10) == int(pesel[10]))

    def __init__(self, pesel: str):
        if (len(pesel)!=11 or not self._validate(pesel)):
            raise ValueError("Provided PESEL is Incorrect")
        self.pesel = pesel

    def get_sex(self) -> str:
        match(int(list(self.pesel)[9])%2):
            case 0:
                return 'F'
            case 1:
                return 'M'
            case _:
                raise ValueError('This error is unreachable.')

    def get_date_of_birth(self) -> datetime.date:
        year = int(self.pesel[0:2])
        month = int(self.pesel[2:4])
        day = int(self.pesel[4:6])
        if (month <= 12):
            year += 1900
        elif (month <= 32):
            year += 2000
            month -= 20
        elif (month <= 52):
            year += 2100
            month -= 40
        elif (month <= 72):
            year += 2200
            month -= 60
        elif (month <= 92):
            year += 1800
            month -= 80
        return datetime.date(year, month, day)
