from todos_testing.Module import todos


def test_clear():
        todos.open()
        todos.add('33','22','11')
        todos.should_be('33','22','11')
        todos.toggle('22')
        todos.clear_completed()
        todos.should_be_active('33','11')
