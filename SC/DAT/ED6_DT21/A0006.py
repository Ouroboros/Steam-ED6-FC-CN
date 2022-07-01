import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import A0006_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('A0006   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '12300待机'),
    TXT(0x02, '12301移动'),
    TXT(0x03, '12302攻击'),
    TXT(0x04, '12303伤害'),
    TXT(0x05, '12304倒下'),
    TXT(0x06, '12310待机'),
    TXT(0x07, '12311移动'),
    TXT(0x08, '12312攻击'),
    TXT(0x09, '12313伤害'),
    TXT(0x0A, '12314倒下'),
    TXT(0x0B, '12320待机'),
    TXT(0x0C, '12321移动'),
    TXT(0x0D, '12322攻击'),
    TXT(0x0E, '12323伤害'),
    TXT(0x0F, '12324倒下'),
    TXT(0x10, '12330待机'),
    TXT(0x11, '12331移动'),
    TXT(0x12, '12332攻击'),
    TXT(0x13, '12333伤害'),
    TXT(0x14, '12334倒下'),
    TXT(0x15, '12340待机'),
    TXT(0x16, '12341移动'),
    TXT(0x17, '12342攻击'),
    TXT(0x18, '12343伤害'),
    TXT(0x19, '12344倒下'),
    TXT(0x1A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'map1'
    header.mapModel       = 'T0030.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5EB
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
            dword_08        = 0x00000000,
            word_0C         = 0x0004,
            word_0E         = 0x0005,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
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
        ('ED6_DT29/CH12300._CH', 'ED6_DT29/CH12300P._CP'),
        ('ED6_DT29/CH12301._CH', 'ED6_DT29/CH12301P._CP'),
        ('ED6_DT29/CH12302._CH', 'ED6_DT29/CH12302P._CP'),
        ('ED6_DT29/CH12303._CH', 'ED6_DT29/CH12303P._CP'),
        ('ED6_DT29/CH12304._CH', 'ED6_DT29/CH12304P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12310._CH', 'ED6_DT29/CH12310P._CP'),
        ('ED6_DT29/CH12311._CH', 'ED6_DT29/CH12311P._CP'),
        ('ED6_DT29/CH12312._CH', 'ED6_DT29/CH12312P._CP'),
        ('ED6_DT29/CH12313._CH', 'ED6_DT29/CH12313P._CP'),
        ('ED6_DT29/CH12314._CH', 'ED6_DT29/CH12314P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12320._CH', 'ED6_DT29/CH12320P._CP'),
        ('ED6_DT29/CH12321._CH', 'ED6_DT29/CH12321P._CP'),
        ('ED6_DT29/CH12322._CH', 'ED6_DT29/CH12322P._CP'),
        ('ED6_DT29/CH12323._CH', 'ED6_DT29/CH12323P._CP'),
        ('ED6_DT29/CH12324._CH', 'ED6_DT29/CH12324P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12330._CH', 'ED6_DT29/CH12330P._CP'),
        ('ED6_DT29/CH12331._CH', 'ED6_DT29/CH12331P._CP'),
        ('ED6_DT29/CH12332._CH', 'ED6_DT29/CH12332P._CP'),
        ('ED6_DT29/CH12333._CH', 'ED6_DT29/CH12333P._CP'),
        ('ED6_DT29/CH12334._CH', 'ED6_DT29/CH12334P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12340._CH', 'ED6_DT29/CH12340P._CP'),
        ('ED6_DT29/CH12341._CH', 'ED6_DT29/CH12341P._CP'),
        ('ED6_DT29/CH12342._CH', 'ED6_DT29/CH12342P._CP'),
        ('ED6_DT29/CH12343._CH', 'ED6_DT29/CH12343P._CP'),
        ('ED6_DT29/CH12344._CH', 'ED6_DT29/CH12344P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
        ('ED6_DT29/CH12364._CH', 'ED6_DT29/CH12364P._CP'),
    ]

# id: 0x10002 offset: 0x23A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 4000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 13,
            chipIndex           = 13,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 8000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 20,
            chipIndex           = 20,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 21,
            chipIndex           = 21,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 12000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 30,
            chipIndex           = 30,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 31,
            chipIndex           = 31,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 32,
            chipIndex           = 32,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 33,
            chipIndex           = 33,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 16000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 34,
            chipIndex           = 34,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 4000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 40,
            chipIndex           = 40,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 8000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 41,
            chipIndex           = 41,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 12000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 42,
            chipIndex           = 42,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 16000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 43,
            chipIndex           = 43,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 20000,
            z                   = 0,
            y                   = 20000,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 44,
            chipIndex           = 44,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10003 offset: 0x55A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x55A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x55A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x55A
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x55B
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x55C
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x6),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_589'),
        (0x00000001, 'loc_591'),
        (0x00000002, 'loc_599'),
        (0x00000003, 'loc_5A1'),
        (0x00000004, 'loc_5A9'),
        (0x00000005, 'loc_5B1'),
        (-1, 'loc_5B9'),
    )

    def _loc_589(): pass

    label('loc_589')

    Sleep(100)

    Jump('loc_5B9')

    def _loc_591(): pass

    label('loc_591')

    Sleep(100)

    Jump('loc_5B9')

    def _loc_599(): pass

    label('loc_599')

    Sleep(200)

    Jump('loc_5B9')

    def _loc_5A1(): pass

    label('loc_5A1')

    Sleep(300)

    Jump('loc_5B9')

    def _loc_5A9(): pass

    label('loc_5A9')

    Sleep(400)

    Jump('loc_5B9')

    def _loc_5B1(): pass

    label('loc_5B1')

    Sleep(500)

    Jump('loc_5B9')

    def _loc_5B9(): pass

    label('loc_5B9')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5CE',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_5B9')

    def _loc_5CE(): pass

    label('loc_5CE')

    Return()

# id: 0x0003 offset: 0x5CF
@scena.Code('func_03_5CF')
def func_03_5CF():
    Return()

# id: 0x0004 offset: 0x5D0
@scena.Code('func_04_5D0')
def func_04_5D0():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '嗷—',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
