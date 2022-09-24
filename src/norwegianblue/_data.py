from __future__ import annotations

import random

d = {}
for c in (32, 126):
    for i in range(94):
        d[chr(i + c)] = chr((i + 47) % 94 + c)


def text(s):
    return "".join([d.get(c, c) for c in s])


prefix = text(
    """
OOOOOOOOOOOOOOOOOOOOOOO]]OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO]ilZZl]
OOOOOOOOOOOOOOOOOOOOOOO\\lYZ\\OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO]\\lYRYli
OOOOOOOOOOOOOOOOOOOOOOOOO]\\ZZ\\OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOi\\ZRRYl\\]
OOOOOOOOOOOOOOOOOOOOO]]]]OO]lRYZ\\]OOOOOOOOOOOOOOOOOOOOOi\\lllYRRYli]
OOOOO]OOOO]\\lll\\lZRTTTTTTTTRYRRRliOOOOOOOOOOOOO]iiilZRTTTRRYZi
OO]lYY\\OiYRRRRRTTTTRRRRRRRRRRTRRRRRl]]O]]ii\\ZYYYYYYYRRYl\\i
O\\lYRYRYRRRRRRRRRRYYYYYYYYYRRRRRRRRTTTTTRYYYYYYYYYZli]
lRYlIllZYYYRRRRRRRYZZZZZZZZZYRRRRRRRRRRRRRRRZl\\i
OiZZZZZYYYYRRRRYRYYZZlZllZZZYRYYYYYYRRRRRYRRYli
OOO]\\ZZYYYYYYRRRYYYYZZlllZZllYYYYYYYYYYYYYRRRYi]
OOOOOO]i\\lll\\\\\\lZZZZZZYYZZl\\lllZZYYl\\llZZZZYYZl\\i

"""
)
latest = random.choice(
    (
        "5625",
        "C6DE:?8",
        "DE@?6O5625",
        "DEF??65",
        "A:?:?8O7@COE96O7;@C5D",
        "A2DD65O@?",
        "?@O>@C6",
        "462D65OE@O36",
        "6IA:C65O2?5O8@?6OE@O>66EO9:DO>2<6C",
        "2ODE:77",
        "36C67EO@7O=:76",
        "C6DEDO:?OA6246",
        "AFD9:?8OFAOE96O52:D:6D",
        ">6E23@=:4OAC@46DD6DO2C6O?@HO9:DE@CJ",
        "@77OE96OEH:8",
        "<:4<65OE96O3F4<6E",
        "D9F77=65O@77O9:DO>@CE2=O4@:=",
        "CF?O5@H?OE96O4FCE2:?O2?5O;@:?65OE96O3=665:?VO49@:CO:?G:D:3=6",
        r"6I\A2CC@E",
    )
)


res = [
    {
        "cycle": text("}@CH68:2?Oq=F6"),
        "release": text("`heh\\`a\\_f"),
        "eol": text("`heh\\`a\\_f"),
        "latest": text(latest),
    },
]
