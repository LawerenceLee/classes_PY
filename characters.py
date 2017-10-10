class Character:
    def __init__(self, name="", **kwargs):
        # The use of the empty sting gets rid of a
        # complication that arises due to loss of
        # the positional argument for name through
        # the use of inheritence (essentially using super)
        if not name:
            raise ValueError("'name' is required")
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)
            
            
    def __str__(self):
        return "{}: {}".format(self.__class__.__name__, self.name)
