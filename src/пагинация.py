# ответ
class Pagination:
    def __init__(self, items=[], page_size=10):
        self.items = items
        self.page_size = page_size
        self.current_page = 1
        self.total_pages = 1 if not self.items else (len(self.items) // self.page_size) + 1 

    def get_current_page(self):
        return self.current_page

    def get_page_size(self):
        return self.page_size

    def get_items(self):
        return self.items

    def prev_page(self):
        if self.current_page == 1:
            return self
        self.current_page -= 1
        return self

    def next_page(self):
        if self.current_page == self.total_pages:
            return self
        self.current_page += 1
        return self

    def first_page(self):
        self.current_page = 1
        return self

    def last_page(self):
        self.current_page = self.total_pages
        return self

    def go_to_page(self, page):
        if page < 1:
            page = 1
        elif page > self.total_pages:
            page = self.total_pages
        self.current_page = page
        return self

    def get_visible_items(self):  # не должен принимать номер страницы
        start = (self.current_page - 1) * self.page_size
        end = start + self.page_size
        return self.items[start:end]

alphabetList = list('abcdefghijklmnopqrstuvwxyz')
p = Pagination(alphabetList, 10)

p.first_page()
p.get_visible_items()
p.next_page()
p.get_visible_items()
p.next_page()
p.get_visible_items()