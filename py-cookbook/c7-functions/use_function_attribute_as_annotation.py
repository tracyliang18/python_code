class Foo(WebService):
    @webmethod
    def bar(self, arg1, arg2):
        pass
#then I can define

def webmethod(func):
    func.is_webmethod = True
    return func
#Then, when a webservice call arrives, I look up the method, check whether the underlying function has the is_webmethod attribute (the actual value is irrelevant), and refuse the service if the method is absent or not meant to be called over the web.

