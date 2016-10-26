import jinja2
import psutil
import collections

psutil.cpu_percent() # Initialize percent calculator

def _getnums():
    numbers = []
    numbers.append(('CPU Usage', psutil.cpu_percent(interval=1)))
    numbers.append(('Memory', psutil.virtual_memory().percent))

    return collections.OrderedDict(numbers)

def render():
    numbers = _getnums()
    with open('templates/example.html') as template:
        return jinja2.Template(template.read()).render(data=numbers)
