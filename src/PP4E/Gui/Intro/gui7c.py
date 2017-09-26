"""
Standalone container subclass example
"""
import gui7  # @UnresolvedImport


class HelloPackage(gui7.HelloPackage):
    '''
    Subclass example
    '''
    def __getattr__(self, name):
        return getattr(self.top, name)  # pass off to a real widget


if __name__ == '__main__':
    HelloPackage().mainloop()  # invokes __getattr__
