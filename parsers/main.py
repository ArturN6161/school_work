import textwrap
import requests
from bs4 import BeautifulSoup


def draw_box(title, messages, width=100):
    """Вспомогательный метод для отрисовки рамок (DRY)."""
    if isinstance(messages, str):
        messages = textwrap.wrap(messages, width - 4)

    inner_width = width - 4

    print('\n' + '*' * width)
    print(f'*{title.upper():^{inner_width}}  *')
    print('*' * width)

    for msg in messages:
        # Если строка слишком длинная, она не сломает рамку
        print(f"* {msg:<{inner_width}} *")

    print("*" * width)


def find_cards():
    data = requests.get('https://pnevmat24.ru/pnevmaticheskie-vintovki/').text
    soup = BeautifulSoup(data, 'lxml')

    items = soup.find_all('div', class_='product-card')

    for i in items:
        name_container = i.find('div', class_="product-card__name")

        t = "Нет названия"
        f = "Нет ссылки"

        if name_container:
            link_tag = name_container.find('a', itemprop="url")
            if link_tag:
                # Название лежит в span внутри ссылки
                title_span = link_tag.find('span', class_="has-tooltip")
                t = title_span.get_text(strip=True) if title_span else "Нет названия"
                # Достаем саму ссылку
                f = f"https://pnevmat24.ru{link_tag['href']}"
        price = i.find('div', class_="product-card__price")
        sku = i.find('div', class_="product-card__sku")

        p = price.get_text(strip=True) if price else "Нет ценника"
        s = sku.get_text(strip=True) if sku else "Нет артикула"


        draw_box(title=t, messages=[f'Цена: {p}', f'Артикул: {s}', f'Url: {f}'])
        #print(f"Товар: {t} | Цена: {p} | Артикул: {s}")


if __name__ == '__main__':
    find_cards()

