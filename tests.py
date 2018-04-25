import unittest
import habr_parser as hp
import date_processor as dp
import words_processor as wp


class TestWordProcessor(unittest.TestCase):

    def test_filter_words_in_title(self):
        filtered = wp.filter_words_in_title('Кто что vpn и как Роскомназор 12 котиков ограбил')
        self.assertEqual(type(filtered), list)
        self.assertEqual(filtered, ['vpn', 'роскомназор', 'котиков', 'ограбил'])

    def test_make_word_of_normal_form(self):
        normal = wp.make_word_of_normal_form('приплыли')
        self.assertEqual(normal, 'приплыть')


class TestDateProcessor(unittest.TestCase):

    def test_first_and_last_day_of_week(self):
        week_and_dates = dp.first_and_last_date_of_week((2018, 19, 1))
        self.assertEqual(type(week_and_dates), tuple)
        self.assertEqual(week_and_dates, ('2018-05-07', '2018-05-13'))

    def test_translate_month_name_to_number(self):
        month_number = dp.translate_month_name_to_number('мая')
        self.assertEqual(month_number, '5')
        month_number = dp.translate_month_name_to_number('котики')
        self.assertEqual(month_number, None)

if __name__ == '__main__':
    unittest.main()
