import pprintpp



def update(o: object, **attrs):
    for name, value in attrs.items():
        assert hasattr(o, name), "attribute %r does not exist on %r" % (name, o)
        setattr(o, name, value)


def updated(o: object, **attrs):
    update(o, **attrs)
    return o


def repr(o: object) -> str:
    return '%s.%s %s' % (
        type(o).__module__, type(o).__qualname__, pprintpp.pformat(o.__dict__))
