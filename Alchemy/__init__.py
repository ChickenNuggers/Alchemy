class Tag(object):
    def __init__(self):
        self._classes = []
        self._tagelements = []
        return self
    def __str__(self):
        """Generate string representation of Button
        """
        if len(self._classes) != 0:
            self._tagelements.append('class="' + " ".join(self._classes) + '"')

        if len(self._tagelements) != 0:
            elements = " " + " ".join(self._tagelements)
        else:
            elements = ""

        return Button.template.format(tagelements=elements, text=self._text)

class Button(Tag):

    """Creates HTML for an Angular Material button"""

    def __init__(self, text, type=0, action=None):
        """Initialize with type of button and JS action

        :type: Type of button (primary/simple/warning & raised & no-ink)
        :action: JavaScript scope action called when the button is clicked

        """
        self._text = text
        self._type = type
        self._action = action
        super(Button, self).__init__()

        # Initialize classes
        if self._type & Button.primary:
            self._classes.append('md-primary')
        elif self._type & Button.simple:
            pass # No class to add
        elif self._type & Button.warn:
            self._classes.append('md-warn')
        else:
            pass # No class to add

        if self._type & Button.raised:
            self._classes.append('md-raised')

        # Start adding in attributes
        if self._type & Button.no_ink:
            self._tagelements.append('md-no-ink')
        
        if self._action:
            self._tagelements.append('ng-click="' + self._action + '"')

    primary  = 2**0 # :: Types ::
    simple   = 2**1
    warn     = 2**2
    raised   = 2**3
    no_ink   = 2**4

    template = '<md-button{tagelements}>{text}</md-button>'
