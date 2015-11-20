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

        return self.template.format(attributes=elements, **dict((key[1:], value) for key, value in self.__dict__.items()))

class Types(object):
    def appendClass(obj):
        if obj._type & Button.primary:
            obj._classes.append('md-primary')
        elif obj._type & Button.accent:
            obj._classes.append('md-accent')
        elif obj._type & Button.warn:
            obj._classes.append('md-warn')
        
    primary  = 2**0 # :: Types ::
    accent   = 2**1
    warn     = 2**2

class Button(Tag):

    """Creates HTML for an Angular Material button"""

    def __init__(self, text, type=0, action=None):
        """Initialize with type of button and JS action

        :type: Type of button (primary/simple/warning & raised & no-ink)
        :action: JavaScript scope action called when the button is clicked

        """
        Tag.__init__(self)

        self._text = text
        self._type = type
        self._action = action

        # Initialize classes
        if self._type & Button.primary:
            self._classes.append('md-primary')
        elif self._type & Button.accent:
            self._classes.append('md-accent')
        elif self._type & Button.warn:
            self._classes.append('md-warn')

        if self._type & Button.raised:
            self._classes.append('md-raised')

        # Start adding in attributes
        if self._type & Button.no_ink:
            self._tagelements.append('md-no-ink')
        
        if self._action:
            self._tagelements.append('ng-click="' + self._action + '()"')

    primary  = 2**0 # :: Types ::
    accent   = 2**1
    warn     = 2**2
    raised   = 2**3
    no_ink   = 2**4

    template = '<md-button{attributes}>{text}</md-button>'

class Checkbox(Tag):

    """Angular Material - Checkbox"""
 
    def __init__(self, label, type=0, on=None, off=None):
        """

        :label: String
        :type: Integer
        :on: JavaScript method
        :off: JavaScript method

        """
        Tag.__init__(self)

        self._label = label
        self._type = type
        self._on = on
        self._off = off

        if self._type & Checkbox.primary:
            self._classes.append('md-primary')
        elif self._type & Checkbox.accent:
            self._classes.append('md-accent')
        elif self._type & Checkbox.warn:
            self._classes.append('md-warn')

        if self._type & Checkbox.no_ink:
            self._tagelements.append('md-no-ink')

        if self._on:
            self._tagelements.append('on="' + on.name + '()"')

        if self._off:
            self._tagelements.append('off="' + off.name + '()"')


    primary  = 2**0 # :: TYPES ::
    accent   = 2**1
    warn     = 2**2
    no_ink   = 2**3

    template = '<md-checkbox{attributes}>{label}</md-checkbox>'

class PercentageBar(Tag):

    """Angular Material - Progress // Linear"""

    def __init__(self, percentage, label, type=0):
        Tag.__init__(self)

        self._percentage = percentage
        self._label = label
        self._type = type

        if self._type & PercentageBar.primary:
            self._classes.append('md-primary')
        elif self._type & PercentageBar.accent:
            self._classes.append('md-accent')
        elif self._type & PercentageBar.warn:
            self._classes.append('md-warn')

        self._tagelements.append('value="' + str(self._percentage) + '"')
    
    primary  = 2**0 # :: TYPES ::
    accent   = 2**1
    warn     = 2**2

    template = '<h4>{label}</h4><md-progress-linear{attributes}></md-progress-linear>'
