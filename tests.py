from unittest import TestCase, mock
from scraper import Scraper


class ScraperFactory:
    @staticmethod
    def create(url=None, text=''):
        return Scraper(url, text)


class TestScraper(TestCase):

    def test_a_word_in_processed_words(self) -> None:
        scraper = ScraperFactory.create(None, "hello, how are you?")
        scraper.clean_up_n_words()
        self.assertIn(f"HELLO", scraper.words)

    def test_a_two_gram_is_present(self) -> None:
        scraper = ScraperFactory.create(None, "hello, how are you?")
        scraper.clean_up_n_words()
        scraper.prepare_n_grams()
        self.assertIn(f"HELLO-HOW", scraper.two_grams)

    def test_a_stop_word_removed(self) -> None:
        scraper = ScraperFactory.create(None, "hello, how are you?")
        scraper.clean_up_n_words()
        scraper.remove_stop_words()
        self.assertNotIn(f"HOW", scraper.words)

    def test_a_one_gram_count(self) -> None:
        test_str = """ Write an app/program to scan through a given webpage, and display the top 10 frequent words and 
        the top 10 frequent word pairs (two words in the same order) along with their frequency """
        scraper = ScraperFactory.create(None, test_str)
        scraper.clean_up_n_words()
        scraper.remove_stop_words()
        scraper.prepare_n_grams()
        self.assertEqual(2, scraper.one_grams["FREQUENT"])

    def test_a_two_gram_count(self) -> None:
        test_str = """ Write an app/program to scan through a given webpage, and display the top 10 frequent words and 
                the top 10 frequent word pairs (two words in the same order) along with their frequency """
        scraper = ScraperFactory.create(None, test_str)
        scraper.clean_up_n_words()
        scraper.remove_stop_words()
        scraper.prepare_n_grams()
        self.assertEqual(2, scraper.two_grams["TOP-FREQUENT"])