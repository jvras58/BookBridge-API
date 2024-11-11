from factory import Factory, Sequence
from app.models.todo import TodoItem as TodoModel

class TodoFactory(Factory):
    class Meta:
        model = TodoModel

    id = Sequence(lambda n: n)
    task = "Tarefa de exemplo"
