import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5301   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, 'Elevator'),
    TXT(0x02, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5301.x'
    header.mapIndex       = 1
    header.bgm            = 64
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x86F
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0xC8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xC8
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 101980,
            y           = -2000,
            z           = 850,
            range       = 3000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0xE8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xE8
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_F9',
    )

    OP_A3(0x10F0)
    Event(0, 0x0002)

    Jump('loc_11C')

    def _loc_F9(): pass

    label('loc_F9')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10C',
    )

    Event(0, 0x0004)

    Jump('loc_11C')

    def _loc_10C(): pass

    label('loc_10C')

    If(
        (
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x73),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11C',
    )

    Event(0, 0x0006)

    def _loc_11C(): pass

    label('loc_11C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 3, 0x2233)),
            Expr.Return,
        ),
        'loc_163',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_163',
    )

    OP_A2(0x0000)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_163(): pass

    label('loc_163')

    Return()

# id: 0x0001 offset: 0x164
@scena.Code('Init')
def Init():
    OP_10(0x00, 0x00)
    OP_82(0x84, 0x00)
    OP_82(0x85, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 3, 0x2233)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18C',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 0)
    OP_10(0x0F, 0x00)

    Jump('loc_1DD')

    def _loc_18C(): pass

    label('loc_18C')

    OP_72(0x0000, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_6F(0x0000, 600)
    OP_10(0x0F, 0x01)
    OP_82(0x83, 0x00)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_1B(0x0F, 0x00, 0x0005)

    def _loc_1DD(): pass

    label('loc_1DD')

    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_6F(0x0001, 0)
    OP_22(0x0140, 0x00, 0x64)

    Return()

# id: 0x0002 offset: 0x1F4
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    OP_6D(-28890, 80, 108700, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(301000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x00000258)
    Sleep(1500)

    OP_22(0x00E1, 0x00, 0x64)
    Sleep(3000)

    OP_22(0x0070, 0x00, 0x64)
    OP_73(0x0000)

    @scena.Lambda('lambda_027C')
    def lambda_027C():
        OP_6D(-890, 1090, 98940, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_027C)

    @scena.Lambda('lambda_0294')
    def lambda_0294():
        OP_67(0, 9500, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0294)

    OP_6C(315000, 5000)
    OP_6B(3500, 0)
    OP_6E(262, 0)
    Fade(1000)
    OP_22(0x00D7, 0x00, 0x64)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(3000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5308._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x31D
@scena.Code('func_03_31D')
def func_03_31D():
    EventBegin(0x00)
    OP_A1(0x0008, 0x0001)
    SetChrPos(0x0008, 101980, -1750, 850, 0)
    Yield()
    Fade(1000)
    OP_6D(101980, 0, 850, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 102000, 0, 2000, 0)
    OP_89(0x0001, 103000, 0, 1000, 90)
    OP_89(0x0002, 101000, 0, 1000, 270)
    OP_89(0x0003, 102000, 0, 0, 180)
    OP_0D()
    Sleep(300)

    SetMapFlags(0x00100000)
    OP_22(0x00EB, 0x00, 0x64)

    @scena.Lambda('lambda_03D2')
    def lambda_03D2():
        OP_67(0, 6500, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03D2)

    @scena.Lambda('lambda_03EA')
    def lambda_03EA():
        OP_6B(3700, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_03EA)

    @scena.Lambda('lambda_03FA')
    def lambda_03FA():
        OP_91(0x00FE, 0, -10000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_03FA)

    Sleep(2000)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_A3(0x228C)
    OP_A2(0x228D)
    OP_A3(0x228E)
    OP_A3(0x228F)
    OP_A3(0x2290)
    OP_A3(0x2291)
    OP_A3(0x2292)
    OP_A3(0x2293)
    OP_A3(0x2294)
    OP_A3(0x2295)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C5316._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x44A
@scena.Code('func_04_44A')
def func_04_44A():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_A1(0x0008, 0x0001)
    SetChrPos(0x0008, 101980, -11750, 850, 0)
    Yield()
    OP_6D(101980, 0, 850, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x0000, 102000, 0, 2000, 0)
    OP_89(0x0001, 103000, 0, 1000, 90)
    OP_89(0x0002, 101000, 0, 1000, 270)
    OP_89(0x0003, 102000, 0, 0, 180)
    OP_22(0x00EB, 0x00, 0x64)

    @scena.Lambda('lambda_04F9')
    def lambda_04F9():
        OP_6B(3500, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_04F9)

    FadeIn(1000, 0)
    SetPlaceName(0x011D)

    @scena.Lambda('lambda_0515')
    def lambda_0515():
        OP_91(0x00FE, 0, 10000, 0, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0515)

    Sleep(2200)

    OP_24(0x00EB, 0x5A)
    Sleep(50)

    OP_24(0x00EB, 0x50)
    Sleep(50)

    OP_24(0x00EB, 0x46)
    Sleep(50)

    OP_24(0x00EB, 0x3C)
    Sleep(50)

    OP_24(0x00EB, 0x32)
    Sleep(50)

    OP_24(0x00EB, 0x28)
    Sleep(50)

    OP_24(0x00EB, 0x1E)
    Sleep(50)

    OP_24(0x00EB, 0x14)
    Sleep(50)

    OP_24(0x00EB, 0x0A)
    Sleep(50)

    OP_23(0x00EB)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)
    Sleep(500)

    Fade(1000)
    SetChrPos(0x0000, 102080, 0, 5330, 0)
    SetChrPos(0x0001, 102080, 0, 5330, 0)
    SetChrPos(0x0002, 102080, 0, 5330, 0)
    SetChrPos(0x0003, 102080, 0, 5330, 0)
    OP_69(0x0000, 0x00000000)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x5E6
@scena.Code('func_05_5E6')
def func_05_5E6():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    OP_6D(-1000, 1050, 99000, 0)
    SetChrPos(0x0101, -500, 1050, 98500, 180)
    SetChrPos(0x0102, -1500, 1050, 98500, 180)
    SetChrPos(0x00F8, -500, 1050, 99500, 180)
    SetChrPos(0x00F9, -1500, 1050, 99500, 180)
    OP_0D()
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    @scena.Lambda('lambda_0691')
    def lambda_0691():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0691)

    @scena.Lambda('lambda_06A3')
    def lambda_06A3():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_06A3)

    @scena.Lambda('lambda_06B5')
    def lambda_06B5():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_06B5)

    @scena.Lambda('lambda_06C7')
    def lambda_06C7():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_06C7)

    Sleep(2000)

    NewScene('ED6_DT21/C5300._SN', 122, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x6E2
@scena.Code('func_06_6E2')
def func_06_6E2():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_6D(-1000, 1050, 99000, 0)
    SetChrPos(0x0101, -1500, 1050, 99500, 0)
    SetChrPos(0x0102, -500, 1050, 99500, 0)
    SetChrPos(0x00F8, -1500, 1050, 98500, 0)
    SetChrPos(0x00F9, -500, 1050, 98500, 0)
    OP_9F(0x0000, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0001, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0002, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    OP_9F(0x0003, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    FadeIn(500, 0)
    OP_0D()
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_22(0x0099, 0x00, 0x64)
    OP_22(0x00B8, 0x00, 0x64)

    @scena.Lambda('lambda_07BD')
    def lambda_07BD():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_07BD)

    @scena.Lambda('lambda_07CF')
    def lambda_07CF():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_07CF)

    @scena.Lambda('lambda_07E1')
    def lambda_07E1():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_07E1)

    @scena.Lambda('lambda_07F3')
    def lambda_07F3():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_07F3)

    Sleep(2500)

    Fade(500)
    OP_6D(-1000, 0, 103000, 0)
    SetChrPos(0x0000, -1000, 0, 103000, 0)
    SetChrPos(0x0001, -1000, 0, 103000, 0)
    SetChrPos(0x0002, -1000, 0, 103000, 0)
    SetChrPos(0x0003, -1000, 0, 103000, 0)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
