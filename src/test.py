class Methods:
    class Types:

        String = str()
        Integer = int()
        Float = float()
        Boolean = bool()
        List = list()
        Tuple = tuple()
        Set = set()

    class System:
        def out(self, out="\n"):
            """out(self, out="\n") prints the parameter out"""
            print(out)

        def inp(self, req=""):
            """inp(self, req="") prints the parameter req wich is the Input Request"""
            a = input(req)
            return a

        def binaer(self, num: int):
            """binaer(self, num) converts the given num to its binary representation"""
            return bin(num)

        def close(self):
            """close(self) exits the code"""
            exit()

        def istype(self, obj: object, tp) -> bool:
            """istype(self, obj, tp) returns if the obj is the type of tp"""
            return isinstance(obj, tp)

    class Func:
        def forif(self, bed: str, cd: str):
            """forif(self, bed, cd) checks if bed is True if so it executes the cd"""
            try:
                if bed:
                    cd
            except Exception as e:
                print(e)

        def loop(self, bed: str, cd: str):
            """loop(self, bed, cd) checks if bed is True if so it executes the cd
            Something is wrong IDK"""
            try:
                while bed:
                    exec(cd)
            except Exception as e:
                print(e)

        def run(self, code):
            """run(self, code) executes the code and returns the result of the code"""
            return exec(code)






py = Methods()
py.sys = Methods.System()
py.fc = Methods.Func()
t = Methods.Types()
