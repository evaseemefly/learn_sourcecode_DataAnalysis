
class outerclass:
    def __init__(self,carname):
        self.carname=carname

    def doinner(self,code):
        pass
        # self.inner=self.innerclass(self,code)
    class innerclass:
        def __init__(self,code,carname):
            super(outerclass.innerclass, self).__init__(carname)
            
            self.code=code
            # self.outer=outer
        def carname(self):
            super(outerclass.innerclass, self).carname

def main():
    # outer=outerclass("我的小汽车")
    # outer.doinner("123123")
    inner= outerclass.innerclass("123","dazhong")

if __name__ == '__main__':
    main()
    
    
    