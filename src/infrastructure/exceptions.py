class Exc(Exception):
    """
    Abstract exception class. Its instances are used on services'
    layer when something is wrong with user's request

    **Do not use it when there's an app problem, `Exc`
    subclasses' instances are used to show client-side errors
    and normally handled on CLI level**
    """
