from bs4 import BeautifulSoup as bs
import requests


class GbBlogParse:
    __domain = 'https://geekbrains.ru'
    __url = 'https://geekbrains.ru/posts'
    __done_urls = set()

    def __init__(self):
        self.posts_urls = set()
        self.pagination_urls = set()

    def get_page_soap(self, url):
        # todo метод запроса страницы и создания супа
        response = requests.get(url)
        soup = bs(response.text, 'lxml')
        return soup

    def run(self, url=None):
        # todo метод запуска парсинга
        url = url or self.__url
        soup = self.get_page_soap(url)
        self.pagination_urls.update(self.get_pagination(soup))
        self.posts_urls.update(self.get_posts_urls(soup))

        for url in tuple(self.pagination_urls):
            if url not in self.__done_urls:
                self.__done_urls.add(url)
                self.run(url)

    # todo Проход пагинации ленты
    def get_pagination(self, soup):
        ul = soup.find('ul', attrs={'class': 'gb__pagination'})
        a_list = [f'{self.__domain}{a.get("href")}' for a in ul.find_all('a') if a.get("href")]
        return a_list

    # todo Поиск ссылок на статьи на странице ленты
    def get_posts_urls(self, soup):
        posts_wrap = soup.find('div', attrs={'class': 'post-items-wrapper'})
        a_list = [f'{self.__domain}{a.get("href")}' for a in
                  posts_wrap.find_all('a', attrs={'class': 'post-item__title'})]
        return a_list


if __name__ == '__main__':
    parser = GbBlogParse()
    parser.run()
    print(1)
