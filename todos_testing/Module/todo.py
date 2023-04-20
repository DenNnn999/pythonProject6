from selene import have
from selene.support.shared import browser

completed = have.css_class('completed')

class TodoMVC:
    def __init__(self):
        self.todo_list = browser.all('#todo-list>li')

    def open(self):
        browser.open('http://todomvc.com/examples/emberjs/')
        # app_loaded = "return $._data($('#clear-completed')[0], 'events')" \
        #              ".hasOwnProperty('click')"
        # browser.should(have.js_returned(True, app_loaded))
        return self

    def add(self, *todos: str):
        for todo in todos:
            browser.element('#new-todo').type(todo).press_enter()
        return self

    def given_opened(self, *todos: str):
        self.open()
        self.add(*todos)

    def should_be(self, *todos: str):
        self.todo_list.should(have.exact_texts(*todos))
        return self

    def toggle(self, todo: str):
        self.todo_list.element_by(have.exact_text(todo)) .element('.toggle').click()
        return self

    def clear_completed(self):
        browser.element('#clear-completed').click()
        return self

    def should_be_active(self, *todos: str):
        self.todo_list.filtered_by(completed.not_).should(have.exact_texts(*todos))

