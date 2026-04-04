import requests
import csv
from bs4 import BeautifulSoup
from parser_site.dataclass import Product


def parser(url:str, max_items: int):
    create_csv()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    page = 1
    count_items = 0

    while count_items < max_items:
        current_url = f"{url}&page={page}"
        print(f"Парсим страницу {page}...")

        res = requests.get(url=current_url, headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')

        products = soup.find_all('div', class_='product-layout')

        # Если товаров на странице нет — выходим из цикла
        if not products:
            print("Товары на странице закончились. Завершаем.")
            break

        breadcrumb_ul = soup.find('ul', class_='breadcrumb')
        list_product = []

        for product in products:
            try:
                if count_items >= max_items:
                    break
                price_elem = product.find('div', class_='category_price')
                price_text = price_elem.find('p').text.strip()
                price = price_text.replace(' р.', '')
                title_box = product.find('h4')
                if title_box:
                    link_tag = title_box.find('a')
                    if link_tag:
                        name = link_tag.get_text(strip=True)
                        link = link_tag.get('href')

                sku_box = product.find('div', class_='image')
                if sku_box:
                    sku = sku_box.get_text(strip=True)

                if breadcrumb_ul:
                    categories = [item.get_text(strip=True) for item in breadcrumb_ul.find_all('li')]
                    path = ' / '.join(categories)
                    full_path = categories[-1]

                list_product.append(Product(name=name,
                                            price=price,
                                            link=link,
                                            sku=sku,
                                            path=path,
                                            full_path=full_path))
                count_items += 1  # Считаем каждый товар
            except Exception as e:
                print(f"Ошибка при разборе товара: {e}")
                continue

        write_csv(list_product)
        page += 1


def create_csv():
    with open(f'taggasm.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'name',
            'price',
            'full path',
            'path',
            'full path'
            'link',
            'sku'
        ])


def write_csv(products: list[Product]):
    with open(f'taggasm.csv', mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for product in products:
            writer.writerow([
                product.name,
                product.price,
                product.path,
                product.full_path,
                product.link,
                product.sku
            ])


if __name__ == '__main__':
    url = 'https://taggsm.ru/index.php?route=product/category&path=900000_900017&limit=100'
    parser(url=url, max_items=5252)