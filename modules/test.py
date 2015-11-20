import jinja2
import psutil

psutil.cpu_percent() # Initialize percent calculator

def _getnums():
    numbers = []
    numbers.append(('CPU Usage', psutil.cpu_percent(interval=1)))
    numbers.append(('Memory', psutil.virtual_memory().percent))

    return dict(numbers)

def render():
    numbers = _getnums()
    with open('templates/test.html') as template:
        return jinja2.Template(template.read()).render(data=numbers)
