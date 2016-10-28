import importlib
import os

__modules = {}
module_list = sorted([
    item[:-3] for item in os.listdir('modules')
    if item[-3:] == ".py" and item[:2] != "__"
])
# use .py.disabled to disable a module

for module in module_list:
    if module[0] != "." and module[0] != "_":
        __modules[module] = importlib.import_module('modules.' + module)

enabled_modules = [
    __modules[module] for module in module_list
    if hasattr(__modules[module], "render")
]
