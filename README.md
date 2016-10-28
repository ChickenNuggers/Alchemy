# [Hurricane](https://chickennuggers.github.io/Hurricane)
Web application designed in Python using Flask and Python
modules and a set of functions for content generation.

## Usage
`./main.py`

Starting the program with systemd is possible as it doesn't
detach itself from the terminal. However, if you were to
run the program manually, you might experience inconsistencies
between root user running the program and regular user. To fix
this, start the program via `./main.py -escalate` or add in an
`"escalate"` field, set to `true`, in the `config.json`
configuration file.

Please make sure to at least check out `config.json` before
running the program. You can include a field `"escalate": true`
to automatically escalate the program to superuser when starting
or change options you don't think look up to par with what you
would rather use.

## Building modules

### ... with Python

Every Python module loaded from the `modules` directory
should have a .render() function to load modules in the
main page; however, modules also should have an interface
to the `app` Flask application and be able to hook their
own custom pages with the `app` class. This means that,
if users wanted, they could theoretically create their
own module extensions if they wanted, but this is not
entirely recommended. To avoid collisions, modules should
be named by their file and extensions named by the file,
a `/`, and the extension file name.

### ... with HTML

HTML templates can be created preferably using Jinja2
while iterating a repeatable format. This creates a
consistent format for the modules, and the modules
should be contained on a single piece of paper, inside
of the fieldset they are created on.

## Contributing

### ... via bug reports:

Bug reports are openly invited, so long as there isn't
already an issue. **If your issue is closed without
warning**, it is likely there is already an issue report
and I don't like cluttering up my mailbox with "Closed
due to duplicate report." If you have any questions
about submitting bugs, feel free to [drop me an E-Mail](
mailto:vandor2012@gmail.com).

### ... via feature requests:

Feature requests are welcome and can be made in an issue
starting with "[Feature]" - unlike bug reports which
should just openly state the problem. The feature should
be explained into detail. Below is a list of already
rejected feature requests:

 * Using something other than a Material Design framework
 * Using something other than Flask
 * Using an entirely different language
  * View my alternative development project [here](
  https://github.com/carbonsrv/diamond).

A list of features to be implemented:

 * [X] Modules
 * [ ] ~~Content generation class~~
 * [X] Monitoring of...
  * [X] Memory
  * [X] CPU Usage...
    - [X] currently
    - [ ] ~~over time~~
  * [X] Listening sockets

### ... via pull request:

Pull requests will be welcome to the project after
December 17th, as that is when the final project
is due for the reason behind this project.

I'm lazy and don't feel like making a lot of things
myself, or keeping everything all optimized, so if
anyone feels like implementing something... Feel
freer than an American with a bald eagle.
