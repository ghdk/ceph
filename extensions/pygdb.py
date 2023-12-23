import gdb

class BP(gdb.Breakpoint):
    
    def __init__(self, loc):
        super().__init__(loc)
    
    def stop(self):
        f = gdb.newest_frame()
        while f:
            print(f.name())
            f = f.older()
        return True  # True == stop at bp
    
class BP_crush_do_rule(gdb.Breakpoint):
    
    def __init__(self):
        super().__init__("crush_do_rule")
    
    def stop(self):
        f = gdb.newest_frame()
        while f:
            print(f.name(), [f"{s}={s.value(f)}" for s in f.block() if s.is_argument or s.is_variable])
            f = f.older()
        return False  # True == stop at bp

BP_crush_do_rule()

# bps = gdb.rbreak("crush.cc:.*")
# for bp in bps:
#     bp.commands = """bt"""
