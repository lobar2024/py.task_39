class PluginMeta(type):
    _registry = {}

    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        if bases:  # bazaviy klassni o'zi ro'yxatga olmasin
            PluginMeta._registry[name] = cls

class Plugin(metaclass=PluginMeta):
    @classmethod
    def all(cls):
        return PluginMeta._registry

    def run(self):
        raise NotImplementedError

class PDFPlugin(Plugin):
    def run(self):
        return "PDF qayta ishlandi"

class ImagePlugin(Plugin):
    def run(self):
        return "Rasm qayta ishlandi"

class VideoPlugin(Plugin):
    def run(self):
        return "Video qayta ishlandi"

print(Plugin.all())
# {'PDFPlugin': <class>, 'ImagePlugin': <class>, 'VideoPlugin': <class>}

for name, klass in Plugin.all().items():
    print(f"{name}: {klass().run()}")
