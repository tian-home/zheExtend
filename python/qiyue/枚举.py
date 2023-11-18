from enum import Enum
from enum import IntEnum,unique

@unique
class VIP(IntEnum):
    YELLOW = 1
    # GREEN = 2
    # GREEN = 1
    GREEN = 1
    BLACK = 3
    RED = 4


# class Common():
#     YELLOW = 1
#
# print(VIP.BLACK.name)
# print(VIP.BLACK.value)
#
# a = 1
# print(VIP(a))

# for v in VIP:
# for v in VIP.__members__.items():
#     print(v)