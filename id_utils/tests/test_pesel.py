import unittest
from id_utils import Pesel
import datetime

class TestPesel(unittest.TestCase):
    def test_validation(self):
        with self.assertRaises(ValueError):
            wrong_pesels = ["22222222223", "68122211263", "75080389486", "84090247841", "84092373763", "54081546124", "73120412962", "55041825320", "88010265844", "05311187841"]
            for pesel in wrong_pesels:
                Pesel(pesel)
    def test_sex(self):
        females = ["22222222222", "68122211261", "75080389482", "84090247842", "84092373767", "54081546126", "73120412965", "55041825321", "88010265846", "05311187842"]
        males = ["89092262617", "84010398618", "91042076571", "50110255492", "49120262152", "88101035233", "77110474573", "88010358751", "60010242539", "63122119632"]
        for pesel in females:
            self.assertEqual(Pesel(pesel).get_sex(), 'F')
        for pesel in males:
            self.assertEqual(Pesel(pesel).get_sex(), 'M')
    def test_date_of_birth(self):
        # 19th century
        self.assertEqual(Pesel("99872102446").get_date_of_birth(), datetime.date(1899, 7, 21))
        self.assertEqual(Pesel("30921302596").get_date_of_birth(), datetime.date(1830, 12, 13))
        # 20th century
        self.assertEqual(Pesel("61063022552").get_date_of_birth(), datetime.date(1961, 6, 30))
        self.assertEqual(Pesel("45120334819").get_date_of_birth(), datetime.date(1945, 12, 3))
        # 21st century
        self.assertEqual(Pesel("78211918139").get_date_of_birth(), datetime.date(2078, 1, 19))
        self.assertEqual(Pesel("52272783839").get_date_of_birth(), datetime.date(2052, 7, 27))
        # 22nd century
        self.assertEqual(Pesel("37440266017").get_date_of_birth(), datetime.date(2137, 4, 2))
        self.assertEqual(Pesel("00721869333").get_date_of_birth(), datetime.date(2200, 12, 18))

if __name__ == "__main__":
    unittest.main()
