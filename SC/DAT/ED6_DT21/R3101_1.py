import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R3101_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3101_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3101.x'
    header.mapIndex       = 1
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1260
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
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_BD',
    )

    OP_99(0x00FE, 0x00, 0x0C, 0x000007D0)

    Jump('PreInit')

    def _loc_BD(): pass

    label('loc_BD')

    Return()

# id: 0x0001 offset: 0xBE
@scena.Code('Init')
def Init():
    OP_B5(0x00)
    FadeOut(0, 0, -1)
    EventBegin(0x00)
    OP_6D(21160, 0, -32460, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(4250, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0009, 33300, 0, -32150, 270)
    SetChrPos(0x000A, 34470, 0, -30990, 270)
    SetChrPos(0x000B, 33870, 0, -34110, 270)
    SetChrPos(0x000C, 35470, 0, -33030, 270)
    SetChrPos(0x000D, 33840, 10, -30000, 270)
    SetChrPos(0x000E, 35840, 10, -32150, 270)
    SetChrFlags(0x0000, 0x0008)
    SetChrFlags(0x0001, 0x0008)
    SetChrFlags(0x0002, 0x0008)
    SetChrFlags(0x0003, 0x0008)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    SetChrChipByIndex(0x000D, 7)
    SetChrChipByIndex(0x000A, 25)
    SetChrChipByIndex(0x0009, 28)
    SetChrChipByIndex(0x000C, 25)
    SetChrChipByIndex(0x000B, 7)
    SetChrChipByIndex(0x000E, 7)
    SetChrFlags(0x00F7, 0x0040)
    SetChrFlags(0x00F8, 0x0040)
    SetChrFlags(0x00F9, 0x0040)
    SetChrPos(0x00F6, 35300, 0, -32150, 270)
    SetChrPos(0x00F7, 39860, 0, -30640, 270)
    SetChrPos(0x00F8, 42600, 0, -32910, 270)
    SetChrPos(0x00F9, 40460, 0, -33870, 270)
    LoadEffect(0x00, 'map\\\\snddst1.eff')
    SetChrChipByIndex(0x0101, 18)
    SetChrChipByIndex(0x0107, 21)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_257',
    )

    OP_D2(0x00070218, 0x00070224, 0x1E)
    OP_D2(0x00070219, 0x00070225, 0x1F)
    OP_D2(0x0007021A, 0x00070226, 0x20)

    Jump('loc_275')

    def _loc_257(): pass

    label('loc_257')

    OP_D2(0x000701D0, 0x000701DC, 0x1E)
    OP_D2(0x000701D1, 0x000701DD, 0x1F)
    OP_D2(0x000701D2, 0x000701DE, 0x20)

    def _loc_275(): pass

    label('loc_275')

    SetChrChipByIndex(0x00F7, 30)

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29F',
    )

    OP_D2(0x000701E8, 0x000701F4, 0x21)
    OP_D2(0x000701E9, 0x000701F5, 0x22)

    Jump('loc_2B3')

    def _loc_29F(): pass

    label('loc_29F')

    OP_D2(0x00070200, 0x0007020C, 0x21)
    OP_D2(0x00070201, 0x0007020D, 0x22)

    def _loc_2B3(): pass

    label('loc_2B3')

    SetChrChipByIndex(0x00F9, 33)
    FadeIn(1000, 0)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    CreateThread(0x000D, 0x00, 0x00, 0x0002)
    CreateThread(0x000E, 0x00, 0x00, 0x0002)

    @scena.Lambda('lambda_02F1')
    def lambda_02F1():
        OP_8E(0x000B, 3870, 0, -34110, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_02F1)

    @scena.Lambda('lambda_030C')
    def lambda_030C():
        OP_8E(0x000D, 3840, 10, -30000, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_030C)

    @scena.Lambda('lambda_0327')
    def lambda_0327():
        OP_8E(0x0009, 3300, 0, -32150, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0327)

    @scena.Lambda('lambda_0342')
    def lambda_0342():
        OP_8E(0x000C, 5470, 0, -33030, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0342)

    @scena.Lambda('lambda_035D')
    def lambda_035D():
        OP_8E(0x000A, 4470, 0, -30990, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_035D)

    @scena.Lambda('lambda_0378')
    def lambda_0378():
        OP_8E(0x000E, 5770, 0, -32150, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0378)

    @scena.Lambda('lambda_0393')
    def lambda_0393():
        OP_6B(3250, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0393)

    Sleep(2500)

    ClearChrFlags(0x0000, 0x0008)
    ClearChrFlags(0x0001, 0x0008)
    ClearChrFlags(0x0002, 0x0008)
    ClearChrFlags(0x0003, 0x0008)

    @scena.Lambda('lambda_03BC')
    def lambda_03BC():
        OP_8E(0x0101, 20300, 0, -32150, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F6, 0x0001, lambda_03BC)

    @scena.Lambda('lambda_03D7')
    def lambda_03D7():
        OP_8E(0x00F7, 16860, 0, -30990, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_03D7)

    @scena.Lambda('lambda_03F2')
    def lambda_03F2():
        OP_8E(0x00F8, 17600, 0, -32910, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_03F2)

    @scena.Lambda('lambda_040D')
    def lambda_040D():
        OP_8E(0x00F9, 16460, 0, -33870, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_040D)

    @scena.Lambda('lambda_0428')
    def lambda_0428():
        OP_6C(120000, 3000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0003, lambda_0428)

    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    ClearMapFlags(0x02000000)

    ChrTalk(
        0x0101,
        (
            '#0010451468V#1005F#2P#3S呀──！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    SetChrChipByIndex(0x0101, 20)
    OP_22(0x01F4, 0x00, 0x64)

    @scena.Lambda('lambda_0473')
    def lambda_0473():
        OP_96(0x0101, 0x00003FAC, 0x0000005A, 0xFFFF826A, 0x000007D0, 0x00001770)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0473)

    SetChrFlags(0x0101, 0x0800)

    @scena.Lambda('lambda_0496')
    def lambda_0496():
        OP_6D(15300, 0, -32460, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0496)

    CreateThread(0x00F7, 0x02, 0x01, 0x0003)
    OP_99(0x0101, 0x00, 0x0A, 0x000007D0)
    OP_4A(0x0009, 255)
    OP_4A(0x000A, 255)
    OP_4A(0x000B, 255)
    OP_4A(0x000C, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(30)

    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(80)

    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    SetChrChipByIndex(0x000D, 6)
    SetChrChipByIndex(0x000A, 24)
    SetChrChipByIndex(0x0009, 27)
    SetChrChipByIndex(0x000C, 24)
    SetChrChipByIndex(0x000B, 6)
    SetChrChipByIndex(0x000E, 6)

    @scena.Lambda('lambda_05A0')
    def lambda_05A0():
        OP_95(0x0009, 0x00000000, 0x00000000, 0x00000000, 0x000005DC, 0x00002710)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_05A0)

    @scena.Lambda('lambda_05BE')
    def lambda_05BE():
        OP_95(0x000A, 0x00000000, 0x00000000, 0x00000000, 0x000005DC, 0x00002710)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_05BE)

    @scena.Lambda('lambda_05DC')
    def lambda_05DC():
        OP_95(0x000B, 0x00000000, 0x00000000, 0x00000000, 0x000005DC, 0x00002710)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_05DC)

    @scena.Lambda('lambda_05FA')
    def lambda_05FA():
        OP_95(0x000C, 0x00000000, 0x00000000, 0x00000000, 0x000005DC, 0x00002710)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_05FA)

    @scena.Lambda('lambda_0618')
    def lambda_0618():
        OP_95(0x000E, 0x00000000, 0x00000000, 0x00000000, 0x000005DC, 0x00002710)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0618)

    OP_95(0x000D, 0x00000000, 0x00000000, 0x00000000, 0x000005DC, 0x00002710)
    OP_63(0x0009)
    OP_63(0x000A)
    OP_63(0x000B)
    OP_63(0x000C)
    OP_63(0x000D)
    OP_63(0x000E)

    @scena.Lambda('lambda_065F')
    def lambda_065F():
        ChrTurnDirection(0x0009, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_065F)

    @scena.Lambda('lambda_066D')
    def lambda_066D():
        ChrTurnDirection(0x000A, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_066D)

    @scena.Lambda('lambda_067B')
    def lambda_067B():
        ChrTurnDirection(0x000B, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_067B)

    @scena.Lambda('lambda_0689')
    def lambda_0689():
        ChrTurnDirection(0x000C, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0689)

    @scena.Lambda('lambda_0697')
    def lambda_0697():
        ChrTurnDirection(0x000E, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0697)

    ChrTurnDirection(0x000D, 0x0101, 400)
    Sleep(1000)

    @scena.Lambda('lambda_06B1')
    def lambda_06B1():
        OP_8F(0x0009, 11660, 0, -32150, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_06B1)

    @scena.Lambda('lambda_06CC')
    def lambda_06CC():
        OP_8F(0x000A, 12410, 0, -30000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_06CC)

    @scena.Lambda('lambda_06E7')
    def lambda_06E7():
        OP_8F(0x000B, 13160, 0, -36140, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_06E7)

    @scena.Lambda('lambda_0702')
    def lambda_0702():
        OP_8F(0x000C, 12100, 0, -34260, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0702)

    @scena.Lambda('lambda_071D')
    def lambda_071D():
        OP_8F(0x000E, 12900, 0, -32500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_071D)

    @scena.Lambda('lambda_0738')
    def lambda_0738():
        OP_67(0, 6000, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0738)

    OP_8F(0x000D, 13940, 10, -28430, 2000, 0x00)
    OP_99(0x0101, 0x0A, 0x0C, 0x000007D0)
    ClearChrFlags(0x0101, 0x0800)

    ChrTalk(
        0x0101,
        (
            '#0010451469V#1002F──看来终于觉悟了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x00F7, 0x0001)
    WaitForThreadExit(0x00F8, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    ClearChrFlags(0x00F7, 0x0040)
    ClearChrFlags(0x00F8, 0x0040)
    ClearChrFlags(0x00F9, 0x0040)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_7ED',
    )

    ChrTalk(
        0x0106,
        (
            '#0050451470V#057F稍微教训你们一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_818')

    def _loc_7ED(): pass

    label('loc_7ED')

    ChrTalk(
        0x0103,
        (
            '#0030451471V#525F稍微惩罚你们一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_818(): pass

    label('loc_818')

    @scena.Lambda('lambda_081E')
    def lambda_081E():
        OP_92(0x0009, 0x0101, 0x000003E8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_081E)

    @scena.Lambda('lambda_0833')
    def lambda_0833():
        OP_92(0x000A, 0x0101, 0x000003E8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0833)

    @scena.Lambda('lambda_0848')
    def lambda_0848():
        OP_92(0x000B, 0x0101, 0x000003E8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0848)

    @scena.Lambda('lambda_085D')
    def lambda_085D():
        OP_92(0x000C, 0x0101, 0x000003E8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_085D)

    @scena.Lambda('lambda_0872')
    def lambda_0872():
        OP_92(0x000D, 0x0101, 0x000003E8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_0872)

    @scena.Lambda('lambda_0887')
    def lambda_0887():
        OP_92(0x000E, 0x0101, 0x000003E8, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0887)

    Sleep(300)

    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x000E, 0xFF)
    Battle(0x000001EB, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_8CC'),
        (-1, 'loc_8CF'),
    )

    def _loc_8CC(): pass

    label('loc_8CC')

    OP_B4(0x00)

    Return()

    def _loc_8CF(): pass

    label('loc_8CF')

    Call(1, 0x0002)

    Return()

# id: 0x0002 offset: 0x8D4
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    LoadEffect(0x00, 'map\\\\snddst1.eff')
    OP_6D(15300, 0, -32460, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(120000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 16300, 0, -32150, 270)
    SetChrPos(0x00F7, 16860, 0, -30640, 270)
    SetChrPos(0x00F8, 17600, 0, -32910, 270)
    SetChrPos(0x00F9, 16460, 0, -33870, 270)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x0009, 11660, 0, -32150, 315)
    SetChrPos(0x000A, 12410, 0, -30000, 180)
    SetChrPos(0x000B, 13160, 0, -36140, 270)
    SetChrPos(0x000C, 12100, 0, -34260, 90)
    SetChrPos(0x000D, 13940, 10, -28430, 135)
    SetChrPos(0x000E, 13460, 0, -32350, 0)
    SetChrChipByIndex(0x000D, 23)
    SetChrChipByIndex(0x000A, 26)
    SetChrChipByIndex(0x0009, 29)
    SetChrChipByIndex(0x000C, 26)
    SetChrChipByIndex(0x000B, 23)
    SetChrChipByIndex(0x000E, 23)
    SetChrSubChip(0x0009, 0)
    SetChrSubChip(0x000A, 0)
    SetChrSubChip(0x000B, 0)
    SetChrSubChip(0x000C, 0)
    SetChrSubChip(0x000D, 0)
    SetChrSubChip(0x000E, 0)
    SetChrChipByIndex(0x0101, 18)
    SetChrChipByIndex(0x0107, 21)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_A5C',
    )

    OP_D2(0x00070218, 0x00070224, 0x1E)
    OP_D2(0x00070219, 0x00070225, 0x1F)
    OP_D2(0x0007021A, 0x00070226, 0x20)

    Jump('loc_A7A')

    def _loc_A5C(): pass

    label('loc_A5C')

    OP_D2(0x000701D0, 0x000701DC, 0x1E)
    OP_D2(0x000701D1, 0x000701DD, 0x1F)
    OP_D2(0x000701D2, 0x000701DE, 0x20)

    def _loc_A7A(): pass

    label('loc_A7A')

    SetChrChipByIndex(0x00F7, 30)

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_AA4',
    )

    OP_D2(0x000701E8, 0x000701F4, 0x21)
    OP_D2(0x000701E9, 0x000701F5, 0x22)

    Jump('loc_AB8')

    def _loc_AA4(): pass

    label('loc_AA4')

    OP_D2(0x00070200, 0x0007020C, 0x21)
    OP_D2(0x00070201, 0x0007020D, 0x22)

    def _loc_AB8(): pass

    label('loc_AB8')

    SetChrChipByIndex(0x00F9, 33)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010451472V#1002F这样一来总算……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B22',
    )

    ChrTalk(
        0x0105,
        (
            '#0060451473V#047F嗯，已经分出胜负了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B59')

    def _loc_B22(): pass

    label('loc_B22')

    If(
        (
            (Expr.Eval, "OP_42(0x03)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B59',
    )

    ChrTalk(
        0x0104,
        (
            '#0040451474V#030F嗯，已经收拾好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B59(): pass

    label('loc_B59')

    ChrTalk(
        0x0107,
        (
            '#0070451475V#065F想、想不到还会合体……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_BD4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050451476V#053F算了，有此教训以后\n',
            '应该不会再敢来村里了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C12')

    def _loc_BD4(): pass

    label('loc_BD4')

    ChrTalk(
        0x0103,
        (
            '#0030451479V#026F有此教训以后\n',
            '应该不会再敢来村里了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C12(): pass

    label('loc_C12')

    OP_96(0x00F7, 0x00003D04, 0x00000000, 0xFFFF8AD0, 0x000003E8, 0x00002710)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_C57',
    )

    SetChrChipByIndex(0x0106, 32)
    SetChrFlags(0x0106, 0x0800)
    CreateThread(0x00F7, 0x02, 0x01, 0x0004)
    OP_99(0x0106, 0x00, 0x07, 0x000007D0)
    WaitForThreadExit(0x0106, 0x0000)
    SetChrSubChip(0x0106, 0)

    Jump('loc_C7B')

    def _loc_C57(): pass

    label('loc_C57')

    SetChrChipByIndex(0x0103, 32)
    SetChrFlags(0x0103, 0x0800)
    CreateThread(0x00F7, 0x02, 0x01, 0x0005)
    OP_99(0x0103, 0x00, 0x09, 0x000007D0)
    WaitForThreadExit(0x0103, 0x0000)
    SetChrSubChip(0x0103, 9)

    def _loc_C7B(): pass

    label('loc_C7B')

    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(120)

    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000C, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(60)

    OP_62(0x000E, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    ChrTurnDirection(0x0009, 0x0101, 0)
    ChrTurnDirection(0x000A, 0x0101, 0)
    ChrTurnDirection(0x000B, 0x0101, 0)
    ChrTurnDirection(0x000C, 0x0101, 0)
    ChrTurnDirection(0x000D, 0x0101, 0)
    ChrTurnDirection(0x000E, 0x0101, 0)
    SetChrChipByIndex(0x000D, 6)
    SetChrChipByIndex(0x000A, 24)
    SetChrChipByIndex(0x0009, 27)
    SetChrChipByIndex(0x000C, 24)
    SetChrChipByIndex(0x000B, 6)
    SetChrChipByIndex(0x000E, 6)

    @scena.Lambda('lambda_0D5D')
    def lambda_0D5D():
        OP_95(0x0009, 0x00000000, 0x00000000, 0x00000000, 0x000003E8, 0x00002710)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0D5D)

    @scena.Lambda('lambda_0D7B')
    def lambda_0D7B():
        OP_95(0x000A, 0x00000000, 0x00000000, 0x00000000, 0x000003E8, 0x00002710)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0D7B)

    @scena.Lambda('lambda_0D99')
    def lambda_0D99():
        OP_95(0x000B, 0x00000000, 0x00000000, 0x00000000, 0x000003E8, 0x00002710)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0D99)

    @scena.Lambda('lambda_0DB7')
    def lambda_0DB7():
        OP_95(0x000C, 0x00000000, 0x00000000, 0x00000000, 0x000003E8, 0x00002710)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0DB7)

    @scena.Lambda('lambda_0DD5')
    def lambda_0DD5():
        OP_95(0x000E, 0x00000000, 0x00000000, 0x00000000, 0x000003E8, 0x00002710)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0DD5)

    OP_95(0x000D, 0x00000000, 0x00000000, 0x00000000, 0x000003E8, 0x00002710)
    OP_63(0x0009)
    OP_63(0x000A)
    OP_63(0x000B)
    OP_63(0x000C)
    OP_63(0x000D)
    OP_63(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_E7E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050451477V#057F#1P下次再来的话\n',
            '就要你们的小命。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050451478V#054F明白的话，就快滚吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EE2')

    def _loc_E7E(): pass

    label('loc_E7E')

    ChrTalk(
        0x0103,
        (
            '#0030451480V#027F#1P下次再来的话\n',
            '我会更加疼爱你们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030451481V#024F明白的话，就赶快走吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EE2(): pass

    label('loc_EE2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_F10',
    )

    SetChrChipByIndex(0x0106, 32)
    SetChrFlags(0x0106, 0x0800)
    CreateThread(0x00F7, 0x02, 0x01, 0x0004)
    OP_99(0x0106, 0x00, 0x07, 0x000007D0)
    WaitForThreadExit(0x0106, 0x0000)
    ClearChrFlags(0x0106, 0x0800)

    Jump('loc_F39')

    def _loc_F10(): pass

    label('loc_F10')

    SetChrChipByIndex(0x0103, 32)
    SetChrFlags(0x0103, 0x0800)
    CreateThread(0x00F7, 0x02, 0x01, 0x0005)
    OP_99(0x0103, 0x00, 0x09, 0x000007D0)
    WaitForThreadExit(0x0103, 0x0000)
    SetChrSubChip(0x0103, 9)
    ClearChrFlags(0x0103, 0x0800)

    def _loc_F39(): pass

    label('loc_F39')

    @scena.Lambda('lambda_0F3F')
    def lambda_0F3F():
        OP_95(0x0009, 0x00000000, 0x00000000, 0x00000000, 0x00000258, 0x00002710)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0F3F)

    @scena.Lambda('lambda_0F5D')
    def lambda_0F5D():
        OP_95(0x000A, 0x00000000, 0x00000000, 0x00000000, 0x00000258, 0x00002710)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0F5D)

    @scena.Lambda('lambda_0F7B')
    def lambda_0F7B():
        OP_95(0x000B, 0x00000000, 0x00000000, 0x00000000, 0x00000258, 0x00002710)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0F7B)

    @scena.Lambda('lambda_0F99')
    def lambda_0F99():
        OP_95(0x000C, 0x00000000, 0x00000000, 0x00000000, 0x00000258, 0x00002710)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0F99)

    @scena.Lambda('lambda_0FB7')
    def lambda_0FB7():
        OP_95(0x000E, 0x00000000, 0x00000000, 0x00000000, 0x00000258, 0x00002710)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_0FB7)

    OP_95(0x000D, 0x00000000, 0x00000000, 0x00000000, 0x000003E8, 0x00002710)
    OP_62(0x0009, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000A, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000B, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000C, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000D, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000E, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    CreateThread(0x000A, 0x00, 0x00, 0x0002)
    CreateThread(0x000B, 0x00, 0x00, 0x0002)
    CreateThread(0x000C, 0x00, 0x00, 0x0002)
    CreateThread(0x000D, 0x00, 0x00, 0x0002)
    CreateThread(0x000E, 0x00, 0x00, 0x0002)
    SetChrChipByIndex(0x000D, 7)
    SetChrChipByIndex(0x000A, 25)
    SetChrChipByIndex(0x0009, 28)
    SetChrChipByIndex(0x000C, 25)
    SetChrChipByIndex(0x000B, 7)
    SetChrChipByIndex(0x000E, 7)

    @scena.Lambda('lambda_10A0')
    def lambda_10A0():
        OP_8E(0x0009, 4320, 0, -29140, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_10A0)

    Sleep(100)

    @scena.Lambda('lambda_10C0')
    def lambda_10C0():
        OP_8E(0x000A, 5760, 0, -26330, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_10C0)

    @scena.Lambda('lambda_10DB')
    def lambda_10DB():
        OP_8E(0x000B, 6480, 0, -39970, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_10DB)

    Sleep(100)

    @scena.Lambda('lambda_10FB')
    def lambda_10FB():
        OP_8E(0x000C, 5220, 0, -36090, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_10FB)

    @scena.Lambda('lambda_1116')
    def lambda_1116():
        OP_8E(0x000D, 8380, 0, -22330, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_1116)

    @scena.Lambda('lambda_1131')
    def lambda_1131():
        OP_8E(0x000E, 5380, 0, -29330, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_1131)

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T3221._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x1168
@scena.Code('func_03_1168')
def func_03_1168():
    Sleep(700)

    OP_22(0x00A4, 0x00, 0x64)
    OP_22(0x0055, 0x00, 0x5A)
    PlayEffect(0x00, 0xFF, 0x00FF, 15300, 90, -32150, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x000001F4, 0x00000BB8, 0x00000064)

    Return()

# id: 0x0004 offset: 0x11BE
@scena.Code('func_04_11BE')
def func_04_11BE():
    Sleep(500)

    OP_22(0x00A4, 0x00, 0x64)
    OP_22(0x0055, 0x00, 0x5A)
    PlayEffect(0x00, 0xFF, 0x00FF, 14230, 30, -30150, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000000, 0x000001F4, 0x00000BB8, 0x00000064)

    Return()

# id: 0x0005 offset: 0x1214
@scena.Code('func_05_1214')
def func_05_1214():
    Sleep(200)

    OP_22(0x01F6, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, 13740, 20, -30120, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
