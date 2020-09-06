import requests
import re
import openpyxl
from collections import defaultdict
from bs4 import BeautifulSoup
from config import Config


class Scraper(object):

    def __init__(self, url=None, text=''):
        self.url = url
        self.one_grams = defaultdict(int)
        self.two_grams = defaultdict(int)
        self.raw_text = text
        self.text = ''
        self.write_excel = True
        self.words = []

    def scrape(self):
        if self.url:
            res = requests.get(self.url)
            soup = BeautifulSoup(res.text)
            self.raw_text = soup.text

    def clean_up_n_words(self):

        if Config.replace_html_entities:
            self.replace_letters(Config.html_entities)

        if Config.replace_x_codes:
            self.replace_letters(Config.x_codes)

        if Config.replace_umlaut:
            self.replace_letters(Config.umlaut)

        self.text = self.raw_text.replace("\n", " ")
        self.text = re.sub('[^A-Za-z0-9]+', ' ', self.text)
        self.text = self.text.replace("  ", " ")
        self.text = self.text.upper()
        self.words = self.text.split()

    def run(self, remove_stop=True):
        self.scrape()
        self.clean_up_n_words()
        if remove_stop:
            self.remove_stop_words()
        self.prepare_n_grams()
        self.output()

    def replace_letters(self, letter_dict):
        for k, v in letter_dict.items():
            self.text = self.text.replace(k, v)

    def remove_stop_words(self):
        temp = []
        for w in self.words:
            if w in Config.stop_words:
                continue
            if w.isdigit():
                continue
            temp.append(w)
        self.words = temp

    def prepare_n_grams(self):
        for i in range(len(self.words)-1):
            self.one_grams[self.words[i]] += 1
            w = self.words[i] + "-" + self.words[i + 1]
            self.two_grams[w] += 1
        self.one_grams[self.words[-1]] += 1

    def output(self):

        top_one_grams = sorted(self.one_grams.items(), key=lambda x: x[1], reverse=True)[:10]
        top_two_grams = sorted(self.two_grams.items(), key=lambda x: x[1], reverse=True)[:10]

        for k, v in top_one_grams:
            print(v, k)
        for k, v in top_two_grams:
            print(v, k.split("-"))

        if self.write_excel:
            wb = openpyxl.Workbook()
            ws1 = wb.active
            ws1.title = "One grams"
            ws1.append(["Count", "Word"])
            for k, v in top_one_grams:
                ws1.append([k, v])

            ws2 = wb.create_sheet(title="Two grams")
            ws2.append(["Count", "Word1", "Word2"])
            for k, v in top_two_grams:
                ws2.append([v] + k.split("-"))

            wb.save("top_10_one_grams_and_two_grams.xlsx")


if __name__ == "__main__":
    test_str = """ Write an app/program to scan through a given webpage, and display the top 10 frequent words and 
            the top 10 frequent word pairs (two words in the same order) along with their frequency """

    url = "https://en.wikipedia.org/wiki/Main_Page"
    scraper = Scraper(url)
    # scraper = Scraper(None, test_str)
    scraper.run()




