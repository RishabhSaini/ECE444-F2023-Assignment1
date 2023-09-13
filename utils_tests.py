import os
from utils import Utils

#Testing the reversed function
assert(Utils.reversed(5130798) == 8970315)
assert(Utils.reversed(-12) == -21)
assert(Utils.reversed(0) == 0)
try:
    Utils.reversed(434.0)
except Exception as inst:
    assert(type(inst) == TypeError)
    assert(inst.__str__() == "Inserted num can only be of type int" )
try:
    Utils.reversed("434")
except Exception as inst:
    assert(type(inst) == TypeError)
    assert(inst.__str__() == "Inserted num can only be of type int" )

#Testing the formatter function
assert(Utils.formatter(123) == ('0b1111011', '0o173'))
assert(Utils.formatter(-12) == ('-0b1100', '-0o14'))
assert(Utils.formatter(0) == ('0b0', '0o0'))
try:
    Utils.formatter(434.0)
except Exception as inst:
    assert(type(inst) == TypeError)
    assert(inst.__str__() == "Inserted num can only be of type int" )
try:
    Utils.formatter("434")
except Exception as inst:
    assert(type(inst) == TypeError)
    assert(inst.__str__() == "Inserted num can only be of type int" )
