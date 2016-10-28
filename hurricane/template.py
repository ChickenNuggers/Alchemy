import jinja2

env = jinja2.Environment(autoescape=False)


def template(*args, **kwargs):
    return env.get_template(*args, **kwargs)
