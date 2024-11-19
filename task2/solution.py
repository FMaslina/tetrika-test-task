import requests
from bs4 import BeautifulSoup
import csv
from collections import defaultdict

BASE_URL = "https://ru.wikipedia.org"

START_URL = f"{BASE_URL}/wiki/Категория:Животные_по_алфавиту"


def fetch_animals_count(url):
    animal_counts = defaultdict(int)

    while url:
        print(f"Fetching: {url}")
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.select(".mw-category-group a"):
            try:
                first_letter = link.text.strip()[0].upper()
                animal_counts[first_letter] += 1
            except IndexError:
                continue

        next_page = soup.find("a", text="Следующая страница")
        url = f"{BASE_URL}{next_page['href']}" if next_page else None

    return animal_counts


def save_to_csv(data, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for letter, count in sorted(data.items()):
            writer.writerow([letter, count])


if __name__ == "__main__":
    animal_counts = fetch_animals_count(START_URL)
    save_to_csv(animal_counts, "beasts.csv")
    print("Data saved to beasts.csv")
