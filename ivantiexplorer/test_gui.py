from nicegui import ui
from nicegui.events import ValueChangeEventArguments
import pandas as pd

def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')


with ui.row():
    ui.select(['servicereqs'], on_change=show)
    ui.switch('Switch', on_change=show)
ui.radio(['A', 'B', 'C'], value='A', on_change=show).props('inline')
with ui.row():
    ui.input('Text input', on_change=show)
    ui.select(['One', 'Two'], value='One', on_change=show)
ui.link('And many more...', '/documentation').classes('mt-8')


df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})

df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
ui.table(
    columns=[{'name': col, 'label': col, 'field': col} for col in df.columns],
    rows=df.to_dict('records'),
)
ui.run()

