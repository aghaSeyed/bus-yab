
from AlibabaCrawler import AlibabaCrawler
from DataExtractor import DataExtractor
import json


def main():
    alibaba_crawler = AlibabaCrawler(
        "https://www.alibaba.ir/bus/AZD-IFN?departing=1402-06-27")
    page_source = alibaba_crawler.crawl()

    data_extractor = DataExtractor(page_source)
    data = data_extractor.extract()
    
    file_path = "data.json"

    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

    print(f"JSON data has been written to '{file_path}'")


if __name__ == "__main__":
    main()
