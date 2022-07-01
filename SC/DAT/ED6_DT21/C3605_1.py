import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3605_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3605_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3605.x'
    header.mapIndex       = 1
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/C3605_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x441F
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
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('ReInit')
def ReInit():
    Call(1, 0x0003)
    Call(1, 0x0007)

    Return()

# id: 0x0003 offset: 0xB3
@scena.Code('func_03_B3')
def func_03_B3():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_CA',
    )

    Call(0, 0x0005)
    Call(0, 0x0006)

    def _loc_CA(): pass

    label('loc_CA')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_E7'),
        (0x00000005, 'loc_FE'),
        (0x00000004, 'loc_115'),
        (0x00000006, 'loc_12C'),
        (0x00000008, 'loc_143'),
        (-1, 'loc_15A'),
    )

    def _loc_E7(): pass

    label('loc_E7')

    OP_D2(0x000701D0, 0x000701DC, 0x12)
    OP_D2(0x000701D1, 0x000701DD, 0x13)

    Jump('loc_15A')

    def _loc_FE(): pass

    label('loc_FE')

    OP_D2(0x00070218, 0x00070224, 0x12)
    OP_D2(0x00070219, 0x00070225, 0x13)

    Jump('loc_15A')

    def _loc_115(): pass

    label('loc_115')

    OP_D2(0x00070200, 0x0007020C, 0x12)
    OP_D2(0x00070201, 0x0007020D, 0x13)

    Jump('loc_15A')

    def _loc_12C(): pass

    label('loc_12C')

    OP_D2(0x00070230, 0x0007023C, 0x12)
    OP_D2(0x00070231, 0x0007023D, 0x13)

    Jump('loc_15A')

    def _loc_143(): pass

    label('loc_143')

    OP_D2(0x00270176, 0x00270183, 0x12)
    OP_D2(0x00270177, 0x00270184, 0x13)

    Jump('loc_15A')

    def _loc_15A(): pass

    label('loc_15A')

    OP_D2(0x0026019C, 0x002601A1, 0x14)
    OP_D2(0x002600A0, 0x002600A5, 0x15)
    OP_D2(0x00260052, 0x00260057, 0x16)
    OP_D2(0x0029014C, 0x00290150, 0x17)
    OP_D2(0x0029014D, 0x00290151, 0x18)
    OP_6D(-3550, 13000, -1710, 0)
    OP_67(0, 5150, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(307000, 0)
    OP_6E(282, 0)
    SetChrPos(0x0008, -1150, 950, 12410, 180)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0002)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 20)
    OP_71(0x0005, 0x0004)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_70(0x0000, 0x00000008)
    OP_70(0x0001, 0x00000008)
    OP_70(0x0002, 0x00000008)
    OP_70(0x0003, 0x00000008)
    OP_70(0x0004, 0x00000008)
    LoadEffect(0x00, 'map\\\\mp061_00.eff')
    LoadEffect(0x01, 'Scraft\\\\sc005_03.eff')
    LoadEffect(0x02, 'scraft\\\\sc000_11.eff')
    LoadEffect(0x03, 'battle\\\\btbomb00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    SetChrPos(0x0101, 740, -1750, -7480, 0)
    SetChrPos(0x0102, -650, -1750, -7480, 0)
    SetChrPos(0x00F9, 820, -1750, -7480, 0)
    SetChrPos(0x0108, -750, -1750, -7480, 0)
    SetChrFlags(0x0101, 0x0080)
    SetChrFlags(0x0102, 0x0080)
    SetChrFlags(0x0108, 0x0080)
    SetChrFlags(0x00F9, 0x0080)
    OP_71(0x000C, 0x0004)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_0333')
    def lambda_0333():
        OP_6D(-550, 0, -1710, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0333)

    @scena.Lambda('lambda_034B')
    def lambda_034B():
        OP_67(0, 8480, -10000, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_034B)

    @scena.Lambda('lambda_0363')
    def lambda_0363():
        OP_6B(2900, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0363)

    @scena.Lambda('lambda_0373')
    def lambda_0373():
        OP_6C(320000, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0373)

    @scena.Lambda('lambda_0383')
    def lambda_0383():
        OP_6E(282, 6000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0383)

    Sleep(4000)

    ClearChrFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_039D')
    def lambda_039D():
        OP_8E(0x00FE, 740, 0, -2040, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_039D)

    Sleep(100)

    ClearChrFlags(0x0102, 0x0080)

    @scena.Lambda('lambda_03C2')
    def lambda_03C2():
        OP_8E(0x00FE, -650, 0, -2009, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_03C2)

    Sleep(800)

    ClearChrFlags(0x00F9, 0x0080)

    @scena.Lambda('lambda_03E7')
    def lambda_03E7():
        OP_8E(0x00FE, 820, 0, -3520, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_03E7)

    Sleep(100)

    ClearChrFlags(0x0108, 0x0080)

    @scena.Lambda('lambda_040C')
    def lambda_040C():
        OP_8E(0x00FE, -750, 0, -3590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_040C)

    WaitForThreadExit(0x0108, 0x0001)
    Sleep(500)

    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010341041V#1007F#6P终、终于到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341042V#1043F#6P比想象的\n',
            '还要花时间啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#0200341043V#3P呼呼……\n',
            '就知道你们差不多该来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_54B',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_589')

    def _loc_54B(): pass

    label('loc_54B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_572',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_589')

    def _loc_572(): pass

    label('loc_572')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_589(): pass

    label('loc_589')

    Sleep(1000)

    OP_1D(0x6F)
    Sleep(500)

    @scena.Lambda('lambda_059B')
    def lambda_059B():
        OP_6D(-1310, 950, 13270, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_059B)

    @scena.Lambda('lambda_05B3')
    def lambda_05B3():
        OP_67(0, 6500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_05B3)

    @scena.Lambda('lambda_05CB')
    def lambda_05CB():
        OP_6E(307, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_05CB)

    WaitForThreadExit(0x0101, 0x0003)
    SetChrPos(0x0108, 740, -1750, -7480, 0)
    SetChrPos(0x0102, -650, -1750, -7480, 0)
    SetChrPos(0x0101, 820, -1750, -7480, 0)
    SetChrPos(0x00F9, -750, -1750, -7480, 0)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 10)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0102, 12)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 14)
    SetChrSubChip(0x00F9, 0)
    SetChrChipByIndex(0x00F9, 18)

    @scena.Lambda('lambda_064C')
    def lambda_064C():
        OP_8F(0x00FE, -450, 0, 5000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_064C)

    Sleep(300)

    @scena.Lambda('lambda_066C')
    def lambda_066C():
        OP_8F(0x00FE, 670, 0, 3800, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_066C)

    Sleep(200)

    @scena.Lambda('lambda_068C')
    def lambda_068C():
        OP_8F(0x00FE, -1190, 0, 3900, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_068C)

    Sleep(300)

    @scena.Lambda('lambda_06AC')
    def lambda_06AC():
        OP_8F(0x00FE, 100, 0, 2100, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_06AC)

    Fade(500)
    OP_6D(-1490, 1000, 9000, 0)
    OP_67(0, 3640, -10000, 0)
    OP_6B(3640, 0)
    OP_6C(333000, 0)
    OP_6E(293, 0)
    OP_0D()
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0108,
        (
            '#0080341044V#072F#6P瓦鲁特……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341045V#250F#2P金……\n',
            '你果然来了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341046V还有『漆黑』小子。\n',
            '好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341047V#1035F#6P……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341048V#1042F不过，还真不知道\n',
            '你和金先生竟然是同门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341049V#252F#2P呼呼、俺除了『泰斗流』以外\n',
            '还吸收了各种各样的流派。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341050V一切都是为了要达到\n',
            '可以击败任何人的至高境地。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341051V你没注意到也不足为怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341052V#572F#6P瓦鲁特，你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341053V#250F#2P你又怎样……金？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341054V至今还死抱着『泰斗流』之类\n',
            '老掉牙的流派不放吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341055V#074F#6P……因为我就是这么笨。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080341056V#070F光是学习本门的武术就已经需要竭尽全力了，\n',
            '没有多余的时间去关注其他的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341057V#254F#2P啧……真没意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341058V#252F算了，我从刚才\n',
            '就一直很无聊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341059V干脆就在这里\n',
            '做个了结吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x00, 0x02, 0x000005DC)
    Sleep(1000)

    OP_99(0x0008, 0x03, 0x09, 0x000005DC)
    Sleep(200)

    ClearChrFlags(0x0008, 0x0002)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 2)
    Sleep(200)

    OP_99(0x0008, 0x01, 0x02, 0x000003E8)
    OP_22(0x00BC, 0x00, 0x64)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)

    @scena.Lambda('lambda_0A8A')
    def lambda_0A8A():
        OP_6D(-930, 1000, 5500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0A8A)

    @scena.Lambda('lambda_0AA2')
    def lambda_0AA2():
        OP_67(0, 4160, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0AA2)

    @scena.Lambda('lambda_0ABA')
    def lambda_0ABA():
        OP_6B(3690, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0ABA)

    @scena.Lambda('lambda_0ACA')
    def lambda_0ACA():
        OP_6E(293, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0ACA)

    SetChrPos(0x000A, 12740, 250, 9670, 270)
    SetChrPos(0x000B, -13570, 250, 6260, 90)
    SetChrPos(0x000C, 9220, 250, -3940, 270)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000A, 0x0800)
    CreateThread(0x000A, 0x03, 0x00, 0x0002)
    CreateThread(0x000B, 0x03, 0x00, 0x0002)
    CreateThread(0x000C, 0x03, 0x00, 0x0002)
    CreateThread(0x000A, 0x02, 0x01, 0x0004)
    Sleep(100)

    CreateThread(0x000B, 0x02, 0x01, 0x0005)
    Sleep(100)

    CreateThread(0x000C, 0x02, 0x01, 0x0006)
    Sleep(500)

    SetChrSubChip(0x0008, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BCA',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_C08')

    def _loc_BCA(): pass

    label('loc_BCA')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BF1',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_C08')

    def _loc_BF1(): pass

    label('loc_BF1')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_C08(): pass

    label('loc_C08')

    Sleep(1000)

    @scena.Lambda('lambda_0C13')
    def lambda_0C13():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0C13)

    Sleep(50)

    @scena.Lambda('lambda_0C26')
    def lambda_0C26():
        OP_8C(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0C26)

    Sleep(50)

    OP_8C(0x00F9, 180, 400)
    WaitForThreadExit(0x000A, 0x0002)
    WaitForThreadExit(0x000B, 0x0002)
    WaitForThreadExit(0x000C, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010341060V#1020F#5P哇哇……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341061V#1042F#6P『装甲猎豹』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CD4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050341062V#054F#2P结社的装甲兽啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DBE')

    def _loc_CD4(): pass

    label('loc_CD4')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D11',
    )

    ChrTalk(
        0x0103,
        (
            '#0030341063V#024F#2P结社的装甲兽……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DBE')

    def _loc_D11(): pass

    label('loc_D11')

    If(
        (
            (Expr.Eval, "OP_42(0x06)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D48',
    )

    ChrTalk(
        0x0107,
        (
            '#0070341064V#065F#2P啊哇哇……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DBE')

    def _loc_D48(): pass

    label('loc_D48')

    If(
        (
            (Expr.Eval, "OP_42(0x04)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D85',
    )

    ChrTalk(
        0x0105,
        (
            '#0060341065V#042F#2P结社的装甲兽……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DBE')

    def _loc_D85(): pass

    label('loc_D85')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DBE',
    )

    ChrTalk(
        0x0109,
        (
            '#0180341066V#1069F#5P结社的装甲兽吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DBE(): pass

    label('loc_DBE')

    ChrTalk(
        0x0008,
        (
            '#0200341067V#250F呼呼，小子们，\n',
            '就和这些家伙玩玩吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    Fade(500)
    OP_6D(-1040, 1200, 9600, 0)
    OP_67(0, 3100, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(356000, 0)
    OP_6E(240, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0200341068V#252F金……让我见识一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341069V这六年时间内\n',
            '你所练就的功夫！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341070V#072F#6P……如你所愿！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    Fade(250)
    SetChrChipByIndex(0x0008, 22)
    SetChrSubChip(0x0008, 1)
    OP_0D()
    Sleep(300)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_0EEE')
    def lambda_0EEE():
        OP_6D(-800, 950, 6000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0EEE)

    @scena.Lambda('lambda_0F06')
    def lambda_0F06():
        OP_67(0, 3960, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F06)

    @scena.Lambda('lambda_0F1E')
    def lambda_0F1E():
        OP_6B(3300, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0F1E)

    SetChrSubChip(0x0008, 2)
    OP_7D(0x00, 0x0008, 0x0032, 0x01F4)
    OP_22(0x023B, 0x00, 0x64)

    @scena.Lambda('lambda_0F40')
    def lambda_0F40():
        OP_96(0x00FE, 0xFFFFFE20, 0x00000000, 0x00001694, 0x000007D0, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_0F40)

    Sleep(100)

    SetChrChipByIndex(0x000A, 24)

    @scena.Lambda('lambda_0F68')
    def lambda_0F68():
        OP_8E(0x00FE, 760, 0, 3750, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_0F68)

    SetChrChipByIndex(0x000B, 24)

    @scena.Lambda('lambda_0F88')
    def lambda_0F88():
        OP_8E(0x00FE, -1340, 0, 4030, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_0F88)

    SetChrChipByIndex(0x000C, 24)

    @scena.Lambda('lambda_0FA8')
    def lambda_0FA8():
        OP_8E(0x00FE, -240, 0, 2470, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_0FA8)

    WaitForThreadExit(0x0101, 0x0000)
    OP_7D(0x01, 0x0008, 0x0000, 0x0000)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    Battle(0x00000455, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_FF3'),
        (-1, 'loc_FF8'),
    )

    def _loc_FF3(): pass

    label('loc_FF3')

    OP_B4(0x00)

    Jump('loc_FF8')

    def _loc_FF8(): pass

    label('loc_FF8')

    Return()

# id: 0x0004 offset: 0xFF9
@scena.Code('func_04_FF9')
def func_04_FF9():
    SetChrChipByIndex(0x00FE, 24)
    OP_8E(0x00FE, 10600, 250, 4960, 6000, 0x00)
    OP_8E(0x00FE, 6070, 250, 4430, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 23)
    OP_8C(0x00FE, 270, 400)

    Return()

# id: 0x0005 offset: 0x1033
@scena.Code('func_05_1033')
def func_05_1033():
    SetChrChipByIndex(0x00FE, 24)
    OP_8E(0x00FE, -9870, 250, 3200, 6000, 0x00)
    OP_8E(0x00FE, -6210, 250, 5070, 6000, 0x00)
    SetChrChipByIndex(0x00FE, 23)
    OP_8C(0x00FE, 90, 400)

    Return()

# id: 0x0006 offset: 0x106D
@scena.Code('func_06_106D')
def func_06_106D():
    SetChrChipByIndex(0x00FE, 24)
    SetChrFlags(0x00FE, 0x0004)
    OP_22(0x00A3, 0x00, 0x64)
    OP_96(0x00FE, 0x000013E2, 0x00001360, 0xFFFFE610, 0x00001388, 0x00001770)
    OP_22(0x00A4, 0x00, 0x64)
    OP_22(0x00A3, 0x00, 0x64)
    OP_96(0x00FE, 0xFFFFFF92, 0x00000000, 0xFFFFF330, 0x000007D0, 0x00001770)
    OP_22(0x00A4, 0x00, 0x64)
    SetChrChipByIndex(0x00FE, 23)
    ClearChrFlags(0x00FE, 0x0004)
    OP_8C(0x00FE, 0, 400)

    Return()

# id: 0x0007 offset: 0x10CB
@scena.Code('func_07_10CB')
def func_07_10CB():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x000B, 0x00)
    TerminateThread(0x000C, 0x00)
    TerminateThread(0x000C, 0x00)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    OP_7D(0x01, 0x0008, 0x0000, 0x0000)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_111B'),
        (0x00000005, 'loc_1132'),
        (0x00000004, 'loc_1149'),
        (0x00000006, 'loc_1160'),
        (0x00000008, 'loc_1177'),
        (-1, 'loc_118E'),
    )

    def _loc_111B(): pass

    label('loc_111B')

    OP_D2(0x000701D0, 0x000701DC, 0x12)
    OP_D2(0x000701D1, 0x000701DD, 0x13)

    Jump('loc_118E')

    def _loc_1132(): pass

    label('loc_1132')

    OP_D2(0x00070218, 0x00070224, 0x12)
    OP_D2(0x00070219, 0x00070225, 0x13)

    Jump('loc_118E')

    def _loc_1149(): pass

    label('loc_1149')

    OP_D2(0x00070200, 0x0007020C, 0x12)
    OP_D2(0x00070201, 0x0007020D, 0x13)

    Jump('loc_118E')

    def _loc_1160(): pass

    label('loc_1160')

    OP_D2(0x00070230, 0x0007023C, 0x12)
    OP_D2(0x00070231, 0x0007023D, 0x13)

    Jump('loc_118E')

    def _loc_1177(): pass

    label('loc_1177')

    OP_D2(0x00270176, 0x00270183, 0x12)
    OP_D2(0x00270177, 0x00270184, 0x13)

    Jump('loc_118E')

    def _loc_118E(): pass

    label('loc_118E')

    OP_D2(0x0026019C, 0x002601A1, 0x14)
    OP_D2(0x002600A0, 0x002600A5, 0x15)
    OP_D2(0x00260052, 0x00260057, 0x16)
    OP_D2(0x00070251, 0x0007025D, 0x17)
    OP_D2(0x0007024D, 0x00070259, 0x18)
    OP_D2(0x002601A7, 0x002601AC, 0x19)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 10)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0102, 12)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 65535)
    SetChrSubChip(0x00F9, 0)
    SetChrChipByIndex(0x00F9, 18)
    SetChrPos(0x0108, 40, 0, 5100, 0)
    SetChrPos(0x0101, 210, 0, 3200, 0)
    SetChrPos(0x0102, 1130, 0, 2410, 0)
    SetChrPos(0x00F9, -530, 0, 1460, 0)
    SetChrPos(0x0008, 50, 0, 10340, 180)
    ClearChrFlags(0x0008, 0x0080)
    SetChrChipByIndex(0x0008, 2)
    SetChrSubChip(0x0008, 0)
    OP_71(0x0005, 0x0004)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_70(0x0000, 0x00000008)
    OP_70(0x0001, 0x00000008)
    OP_70(0x0002, 0x00000008)
    OP_70(0x0003, 0x00000008)
    OP_70(0x0004, 0x00000008)
    LoadEffect(0x00, 'map\\\\mp061_00.eff')
    LoadEffect(0x01, 'scraft\\sc007_10.eff')
    LoadEffect(0x02, 'scraft\\\\sc000_11.eff')
    LoadEffect(0x03, 'battle\\\\btbomb00.eff')
    LoadEffect(0x04, 'scraft\\\\sc000_10.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    OP_6D(1110, 0, 8260, 0)
    OP_67(0, 6210, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(344, 0)
    OP_71(0x000C, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010310610V#1002F#6P呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341072V#1043F#4P果然棘手……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    OP_6D(0, 0, 8800, 0)
    OP_67(0, 4720, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(0, 0)
    OP_6E(287, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0200341073V#250F……看来功夫还是\n',
            '练得相当过硬啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341074V#252F只是，动作太过死板。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341075V这是你守着陈旧的\n',
            '『泰斗流』而固步自封的结果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341076V#070F#6P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341077V#254F……有什么好笑？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341078V#074F#6P你确实是个天才\n',
            '但却不明白最重要的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080341079V师父想必也相当遗憾吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341080V#254F嗬……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341081V你打算代替老头子\n',
            '向我说教吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341082V#070F#6P我才没\n',
            '那么狂妄呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080341083V#074F然而，拳脚相交之间\n',
            '我明白了一件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080341084V现在的我，可能\n',
            '难以胜过你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080341085V#072F但也不会输给你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080341086V你的拳头是打不倒我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341087V#254F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341088V#251F呼呼……有意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341089V没想到会从你的口中\n',
            '说出这种的话来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341090V原本只是想打发打发时间，\n',
            '不过我改变主意了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    Fade(500)
    SetChrSubChip(0x0008, 0)
    OP_0D()
    SetChrChipByIndex(0x0008, 25)
    OP_99(0x0008, 0x00, 0x02, 0x000003E8)
    Sleep(500)

    @scena.Lambda('lambda_177A')
    def lambda_177A():
        OP_6B(3400, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_177A)

    PlayEffect(0x01, 0x01, 0x0008, -100, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(
        0x0008,
        (
            '#0200341091V#254F来吧，金……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341092V我要让你体会到\n',
            '什么叫实力的差距……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341093V#072F#6P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 14)
    OP_0D()
    Sleep(500)

    PlayEffect(0x01, 0x02, 0x0108, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(
        0x0101,
        (
            '#0010341094V#1020F（怎、怎么办！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341095V#1042F#4P（这……\n',
            '看来插不进手啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    OP_1D(0x2C)
    Sleep(500)

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0x8, 0x1),
            (Expr.GetChrWork, 0x108, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.GetChrWork, 0x108, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0x8, 0x3),
            (Expr.GetChrWork, 0x108, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_1950')
    def lambda_1950():
        OP_6B(2500, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1950)

    @scena.Lambda('lambda_1960')
    def lambda_1960():
        OP_6C(12000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1960)

    @scena.Lambda('lambda_1970')
    def lambda_1970():
        OP_6D(0, 500, 9500, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1970)

    @scena.Lambda('lambda_1988')
    def lambda_1988():
        ChrTurnDirection(0x00FE, 0x0108, 400)
        Yield()

        Jump('lambda_1988')

    DispatchAsync2(0x0101, 0x0003, lambda_1988)

    @scena.Lambda('lambda_1999')
    def lambda_1999():
        ChrTurnDirection(0x00FE, 0x0108, 400)
        Yield()

        Jump('lambda_1999')

    DispatchAsync2(0x0102, 0x0003, lambda_1999)

    @scena.Lambda('lambda_19AA')
    def lambda_19AA():
        ChrTurnDirection(0x00FE, 0x0108, 400)
        Yield()

        Jump('lambda_19AA')

    DispatchAsync2(0x00F9, 0x0003, lambda_19AA)

    SetChrFlags(0x0008, 0x0040)
    SetChrFlags(0x0108, 0x0040)
    SetChrFlags(0x0008, 0x0020)
    SetChrFlags(0x0108, 0x1000)
    OP_82(0x01, 0x02)
    OP_82(0x02, 0x02)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearMapFlags(0x00000010)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_19ED')
    def lambda_19ED():
        OP_99(0x00FE, 0x00, 0x01, 0x00000640)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_19ED)

    @scena.Lambda('lambda_19FD')
    def lambda_19FD():
        OP_8F(0x00FE, 40, 0, 9990, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_19FD)

    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 16)

    @scena.Lambda('lambda_1A22')
    def lambda_1A22():
        OP_99(0x00FE, 0x00, 0x04, 0x000009C4)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_1A22)

    OP_8F(0x0108, 40, 0, 9150, 12000, 0x00)

    @scena.Lambda('lambda_1A46')
    def lambda_1A46():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x00001388, 0x000009C4)
        Yield()

        Jump('lambda_1A46')

    DispatchAsync2(0x0008, 0x0003, lambda_1A46)

    @scena.Lambda('lambda_1A63')
    def lambda_1A63():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x00001388, 0x000009C4)
        Yield()

        Jump('lambda_1A63')

    DispatchAsync2(0x0108, 0x0003, lambda_1A63)

    PlayEffect(0x04, 0xFF, 0x0008, 0, 700, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000064, 0x00000190, 0x00000BB8, 0x0000012C)
    Sleep(500)

    TerminateThread(0x0008, 0x03)
    TerminateThread(0x0108, 0x03)

    @scena.Lambda('lambda_1AD3')
    def lambda_1AD3():
        OP_6C(24000, 1200)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1AD3)

    @scena.Lambda('lambda_1AE3')
    def lambda_1AE3():
        OP_96(0x00FE, 0x00000910, 0x000000FA, 0x0000286E, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1AE3)

    @scena.Lambda('lambda_1B01')
    def lambda_1B01():
        OP_96(0x00FE, 0xFFFFF6F0, 0x000000FA, 0x0000286E, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1B01)

    WaitForThreadExit(0x0108, 0x0001)
    SetChrChipByIndex(0x0008, 5)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0108, 14)
    SetChrSubChip(0x0108, 0)
    OP_8C(0x0008, 270, 0)
    OP_8C(0x0108, 90, 0)

    @scena.Lambda('lambda_1B46')
    def lambda_1B46():
        OP_6D(-8380, 250, 9110, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1B46)

    @scena.Lambda('lambda_1B5E')
    def lambda_1B5E():
        OP_6B(2820, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1B5E)

    SetChrPos(0x0101, 300, 0, 2110, 0)
    SetChrPos(0x0102, 930, 0, 1470, 0)
    SetChrPos(0x00F9, -810, 0, 1110, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x00F9, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrSubChip(0x0102, 0)
    SetChrSubChip(0x00F9, 0)
    OP_96(0x0108, 0xFFFFDB02, 0x000000FA, 0x00002378, 0x000001F4, 0x00001F40)
    OP_96(0x0008, 0xFFFFDEEA, 0x000000FA, 0x00002364, 0x000001F4, 0x00001F40)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_1BF7')
    def lambda_1BF7():
        OP_99(0x00FE, 0x00, 0x0D, 0x00000640)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1BF7)

    SetChrChipByIndex(0x0108, 14)
    SetChrSubChip(0x0108, 0)
    Sleep(200)

    OP_22(0x01FB, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x0008, 0, 800, 700, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_1C50')
    def lambda_1C50():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x0000012C, 0x00000FA0)
        Yield()

        Jump('lambda_1C50')

    DispatchAsync2(0x0108, 0x0001, lambda_1C50)

    OP_7C(0x00000064, 0x000000C8, 0x00000BB8, 0x00000064)
    Sleep(300)

    OP_22(0x01FB, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x0008, 0, 800, 700, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000064, 0x000000C8, 0x00000BB8, 0x00000064)

    @scena.Lambda('lambda_1CCE')
    def lambda_1CCE():
        OP_96(0x00FE, 0xFFFFDDA0, 0x000000FA, 0x00002364, 0x0000012C, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1CCE)

    Sleep(400)

    OP_22(0x01FB, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x0008, 0, 1058642330, 1100, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000064, 0x000000C8, 0x00000BB8, 0x00000064)
    TerminateThread(0x0108, 0x01)
    SetChrChipByIndex(0x0108, 24)
    SetChrSubChip(0x0108, 1)
    Sleep(200)

    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 14)

    @scena.Lambda('lambda_1D59')
    def lambda_1D59():
        OP_91(0x00FE, -800, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_1D59)

    WaitForThreadExit(0x0008, 0x0001)
    OP_96(0x0108, 0xFFFFDEEA, 0x000000FA, 0x00001F90, 0x000001F4, 0x00001F40)
    ChrTurnDirection(0x0108, 0x0008, 0)
    ChrTurnDirection(0x0008, 0x0108, 0)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 5)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 16)

    @scena.Lambda('lambda_1DB2')
    def lambda_1DB2():
        OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1DB2)

    SetChrSubChip(0x0008, 2)
    SetChrChipByIndex(0x0008, 25)
    OP_22(0x01FB, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x0008, 0, 700, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000064, 0x000000C8, 0x00000BB8, 0x00000064)
    Sleep(100)

    OP_91(0x0008, 0, 0, 800, 10000, 0x00)
    WaitForThreadExit(0x0108, 0x0001)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 14)
    SetChrSubChip(0x0008, 3)
    Sleep(300)

    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 5)

    @scena.Lambda('lambda_1E53')
    def lambda_1E53():
        OP_96(0x00FE, 0xFFFFDB02, 0x000000FA, 0x0000209E, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1E53)

    Sleep(100)

    @scena.Lambda('lambda_1E76')
    def lambda_1E76():
        OP_96(0x00FE, 0xFFFFEAA2, 0x000000FA, 0x0000209E, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1E76)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_1E99')
    def lambda_1E99():
        OP_6D(-6390, 250, 2530, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1E99)

    @scena.Lambda('lambda_1EB1')
    def lambda_1EB1():
        OP_6C(48000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1EB1)

    ClearChrFlags(0x0008, 0x0020)
    ClearChrFlags(0x0108, 0x1000)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 6)

    @scena.Lambda('lambda_1ED5')
    def lambda_1ED5():
        OP_8E(0x00FE, -5470, 250, 4500, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1ED5)

    @scena.Lambda('lambda_1EF0')
    def lambda_1EF0():
        OP_8E(0x00FE, -9470, 250, 4520, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1EF0)

    WaitForThreadExit(0x0108, 0x0001)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 5)
    ChrTurnDirection(0x0108, 0x0008, 0)
    ChrTurnDirection(0x0008, 0x0108, 0)
    SetChrFlags(0x0008, 0x0020)
    SetChrFlags(0x0108, 0x1000)

    @scena.Lambda('lambda_1F32')
    def lambda_1F32():
        OP_96(0x00FE, 0xFFFFEAA2, 0x000000FA, 0x000011A8, 0x000001F4, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1F32)

    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 16)

    @scena.Lambda('lambda_1F5A')
    def lambda_1F5A():
        OP_99(0x00FE, 0x00, 0x04, 0x000009C4)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_1F5A)

    Sleep(100)

    OP_22(0x0208, 0x00, 0x64)

    @scena.Lambda('lambda_1F74')
    def lambda_1F74():
        OP_96(0x00FE, 0xFFFFEAA2, 0x000000FA, 0x00001784, 0x000001F4, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1F74)

    WaitForThreadExit(0x0108, 0x0001)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 14)
    WaitForThreadExit(0x0108, 0x0002)
    ChrTurnDirection(0x0108, 0x0008, 0)
    ChrTurnDirection(0x0008, 0x0108, 0)

    @scena.Lambda('lambda_1FB4')
    def lambda_1FB4():
        OP_6D(-2380, 250, -860, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1FB4)

    SetChrFlags(0x0108, 0x1000)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 9)

    @scena.Lambda('lambda_1FDB')
    def lambda_1FDB():
        OP_99(0x00FE, 0x00, 0x0D, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1FDB)

    Sleep(500)

    PlayEffect(0x04, 0xFF, 0x0108, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x3DCCCCCD, 0x00000FA0, 0x00000BB8, 0x00000064)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 17)

    @scena.Lambda('lambda_2040')
    def lambda_2040():
        OP_96(0x00FE, 0xFFFFEAA2, 0x000000FA, 0xFFFFF560, 0x00000064, 0x00003A98)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2040)

    WaitForThreadExit(0x0108, 0x0001)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 14)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 5)

    @scena.Lambda('lambda_2077')
    def lambda_2077():
        OP_6C(80000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2077)

    @scena.Lambda('lambda_2087')
    def lambda_2087():
        OP_96(0x0008, 0xFFFFEAA2, 0x000000FA, 0xFFFFF948, 0x000001F4, 0x00001B58)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2087)

    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_20AF')
    def lambda_20AF():
        OP_99(0x00FE, 0x00, 0x02, 0x000009C4)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_20AF)

    OP_22(0x0208, 0x00, 0x64)
    OP_96(0x0108, 0xFFFFF088, 0x000000FA, 0xFFFFF948, 0x000001F4, 0x00001F40)
    ChrTurnDirection(0x0108, 0x0008, 0)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 5)
    ChrTurnDirection(0x0008, 0x0108, 0)
    OP_8F(0x0008, -4960, 250, -1720, 10000, 0x00)
    OP_96(0x0108, 0xFFFFFC40, 0x000000FA, 0xFFFFFD30, 0x000001F4, 0x00001F40)
    OP_96(0x0108, 0x000007A8, 0x000000FA, 0xFFFFF560, 0x000001F4, 0x00001F40)
    OP_96(0x0108, 0x00000B90, 0x000000FA, 0xFFFFF948, 0x000001F4, 0x00001F40)

    @scena.Lambda('lambda_214C')
    def lambda_214C():
        OP_6D(10500, 250, -1530, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_214C)

    OP_96(0x0008, 0x000007A8, 0x000000FA, 0xFFFFF948, 0x000001F4, 0x00001B58)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 9)

    @scena.Lambda('lambda_2185')
    def lambda_2185():
        OP_99(0x00FE, 0x00, 0x0D, 0x00000DAC)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2185)

    OP_22(0x0208, 0x00, 0x64)
    OP_96(0x0108, 0xFFFFF088, 0x000000FA, 0xFFFFF948, 0x000007D0, 0x00001F40)
    ChrTurnDirection(0x0108, 0x0008, 0)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 16)

    @scena.Lambda('lambda_21C2')
    def lambda_21C2():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_21C2)

    @scena.Lambda('lambda_21D0')
    def lambda_21D0():
        OP_99(0x00FE, 0x00, 0x07, 0x000009C4)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_21D0)

    OP_8F(0x0108, 960, 250, -1720, 20000, 0x00)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 15)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 8)
    PlayEffect(0x04, 0xFF, 0x0008, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000064, 0x00000190, 0x00000BB8, 0x00000064)
    OP_8F(0x0008, 8960, 250, -1720, 22000, 0x00)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 5)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 16)

    @scena.Lambda('lambda_2276')
    def lambda_2276():
        OP_99(0x00FE, 0x00, 0x04, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_2276)

    @scena.Lambda('lambda_2286')
    def lambda_2286():
        OP_8F(0x00FE, 10960, 250, -1720, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2286)

    Sleep(200)

    OP_22(0x0208, 0x00, 0x64)

    @scena.Lambda('lambda_22AB')
    def lambda_22AB():
        OP_96(0x00FE, 0x00002300, 0x000000FA, 0xFFFFF178, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_22AB)

    @scena.Lambda('lambda_22C9')
    def lambda_22C9():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_22C9')

    DispatchAsync2(0x0008, 0x0002, lambda_22C9)

    WaitForThreadExit(0x0108, 0x0001)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 14)
    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_22EE')
    def lambda_22EE():
        OP_6C(128000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_22EE)

    @scena.Lambda('lambda_22FE')
    def lambda_22FE():
        OP_6D(10500, 250, -530, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_22FE)

    OP_96(0x0008, 0x00001F18, 0x000000FA, 0xFFFFF948, 0x000001F4, 0x00001F40)
    OP_96(0x0008, 0x0000267A, 0x000000FA, 0xFFFFF948, 0x000001F4, 0x00001F40)
    ChrTurnDirection(0x0108, 0x0008, 0)
    TerminateThread(0x0008, 0x02)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_2359')
    def lambda_2359():
        OP_99(0x00FE, 0x00, 0x0D, 0x00000640)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2359)

    OP_22(0x01FB, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x0108, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000064, 0x000000C8, 0x00000BB8, 0x00000064)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 16)

    @scena.Lambda('lambda_23BE')
    def lambda_23BE():
        OP_9E(0x00FE, 0x0000001E, 0x00000000, 0x0000012C, 0x00000FA0)
        Yield()

        Jump('lambda_23BE')

    DispatchAsync2(0x0108, 0x0001, lambda_23BE)

    Sleep(300)

    @scena.Lambda('lambda_23E0')
    def lambda_23E0():
        OP_99(0x00FE, 0x00, 0x02, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x0108, 0x0000, lambda_23E0)

    OP_22(0x01FB, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x0108, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000064, 0x000000C8, 0x00000BB8, 0x00000064)
    Sleep(500)

    SetChrChipByIndex(0x0108, 16)
    SetChrSubChip(0x0108, 0)
    OP_22(0x01FB, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x0108, 0, 700, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000064, 0x000000C8, 0x00000BB8, 0x00000064)
    TerminateThread(0x0108, 0x01)

    @scena.Lambda('lambda_2499')
    def lambda_2499():
        OP_91(0x00FE, 800, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2499)

    WaitForThreadExit(0x0008, 0x0001)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 5)
    WaitForThreadExit(0x0108, 0x0001)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 14)

    @scena.Lambda('lambda_24D2')
    def lambda_24D2():
        OP_91(0x00FE, -800, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_24D2)

    Sleep(100)

    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 16)

    @scena.Lambda('lambda_24FC')
    def lambda_24FC():
        OP_99(0x00FE, 0x00, 0x07, 0x000009C4)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_24FC)

    Sleep(100)

    OP_22(0x01FB, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x0008, 0, 700, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000064, 0x000000C8, 0x00000BB8, 0x00000064)
    Sleep(100)

    @scena.Lambda('lambda_2561')
    def lambda_2561():
        OP_91(0x00FE, -800, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2561)

    WaitForThreadExit(0x0108, 0x0002)

    @scena.Lambda('lambda_2581')
    def lambda_2581():
        OP_91(0x00FE, 800, 0, 0, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2581)

    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 9)

    @scena.Lambda('lambda_25A6')
    def lambda_25A6():
        OP_99(0x00FE, 0x00, 0x0D, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_25A6)

    Sleep(400)

    OP_22(0x0208, 0x00, 0x64)

    @scena.Lambda('lambda_25C0')
    def lambda_25C0():
        OP_96(0x00FE, 0x0000267A, 0x000000FA, 0xFFFFED90, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_25C0)

    WaitForThreadExit(0x0108, 0x0001)
    ChrTurnDirection(0x0108, 0x0008, 0)
    WaitForThreadExit(0x0008, 0x0002)
    ChrTurnDirection(0x0008, 0x0108, 0)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 5)

    @scena.Lambda('lambda_2600')
    def lambda_2600():
        OP_96(0x00FE, 0x0000267A, 0x000000FA, 0xFFFFF63C, 0x0000012C, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2600)

    Sleep(100)

    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 16)

    @scena.Lambda('lambda_262D')
    def lambda_262D():
        OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_262D)

    Sleep(50)

    OP_22(0x0208, 0x00, 0x64)
    Sleep(100)

    OP_96(0x0008, 0x0000267A, 0x000000FA, 0xFFFFFCC2, 0x000001F4, 0x00001F40)
    WaitForThreadExit(0x0108, 0x0002)

    @scena.Lambda('lambda_2668')
    def lambda_2668():
        OP_96(0x00FE, 0x0000267A, 0x000000FA, 0xFFFFFA06, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2668)

    Sleep(100)

    @scena.Lambda('lambda_268B')
    def lambda_268B():
        OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_268B)

    Sleep(50)

    OP_22(0x0208, 0x00, 0x64)
    Sleep(100)

    OP_96(0x0008, 0x0000290E, 0x000000FA, 0x00000384, 0x000001F4, 0x00001F40)

    @scena.Lambda('lambda_26C1')
    def lambda_26C1():
        OP_6D(8500, 250, 6500, 600)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_26C1)

    OP_96(0x0008, 0x00002832, 0x000000FA, 0x000012D4, 0x000001F4, 0x00001F40)
    OP_96(0x0008, 0x00001EDC, 0x000000FA, 0x000022B0, 0x000001F4, 0x00001F40)
    OP_96(0x0108, 0x00001E1E, 0x000000FA, 0x00001310, 0x000001F4, 0x00001F40)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 14)

    @scena.Lambda('lambda_2728')
    def lambda_2728():
        OP_96(0x00FE, 0x00001EDC, 0x000000FA, 0x00001CD4, 0x000001F4, 0x00002328)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2728)

    @scena.Lambda('lambda_2746')
    def lambda_2746():
        OP_96(0x00FE, 0x00001E1E, 0x000000FA, 0x000018EC, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2746)

    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 16)

    @scena.Lambda('lambda_276E')
    def lambda_276E():
        OP_99(0x00FE, 0x00, 0x07, 0x000007D0)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_276E)

    Sleep(100)

    WaitForThreadExit(0x0008, 0x0001)
    OP_22(0x01FB, 0x00, 0x64)
    SetChrChipByIndex(0x0008, 25)
    SetChrSubChip(0x0008, 2)
    PlayEffect(0x02, 0xFF, 0x0008, 0, 700, 500, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000064, 0x000000C8, 0x00000BB8, 0x00000064)

    @scena.Lambda('lambda_27DD')
    def lambda_27DD():
        OP_91(0x00FE, 0, 0, 800, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_27DD)

    SetChrSubChip(0x0008, 3)
    WaitForThreadExit(0x0108, 0x0002)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 14)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 5)

    @scena.Lambda('lambda_2816')
    def lambda_2816():
        OP_91(0x00FE, 0, 0, -800, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2816)

    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 9)

    @scena.Lambda('lambda_283B')
    def lambda_283B():
        OP_99(0x00FE, 0x00, 0x0D, 0x00000640)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_283B)

    Sleep(500)

    SetChrChipByIndex(0x0108, 24)
    SetChrSubChip(0x0108, 0)
    OP_22(0x01FB, 0x00, 0x64)
    PlayEffect(0x02, 0xFF, 0x0108, 0, 1300, 300, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000064, 0x000000C8, 0x00000BB8, 0x00000064)

    @scena.Lambda('lambda_28A5')
    def lambda_28A5():
        OP_9E(0x00FE, 0x00000014, 0x00000000, 0x00001388, 0x000009C4)
        Yield()

        Jump('lambda_28A5')

    DispatchAsync2(0x0108, 0x0003, lambda_28A5)

    @scena.Lambda('lambda_28C2')
    def lambda_28C2():
        OP_91(0x00FE, 0, 0, -800, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_28C2)

    WaitForThreadExit(0x0008, 0x0002)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 5)
    TerminateThread(0x0108, 0x03)
    WaitForThreadExit(0x0108, 0x0001)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 14)

    @scena.Lambda('lambda_28FF')
    def lambda_28FF():
        OP_96(0x00FE, 0x00001EDC, 0x000000FA, 0x000022B0, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_28FF)

    @scena.Lambda('lambda_291D')
    def lambda_291D():
        OP_96(0x00FE, 0x00001E1E, 0x000000FA, 0x00001310, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_291D)

    WaitForThreadExit(0x0108, 0x0001)

    @scena.Lambda('lambda_2940')
    def lambda_2940():
        OP_6D(630, 0, 6360, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2940)

    @scena.Lambda('lambda_2958')
    def lambda_2958():
        OP_6C(153000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2958)

    ClearChrFlags(0x0008, 0x0004)
    ClearChrFlags(0x0108, 0x0004)
    ClearChrFlags(0x0008, 0x0020)
    ClearChrFlags(0x0108, 0x1000)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 6)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 14)

    @scena.Lambda('lambda_2990')
    def lambda_2990():
        OP_8E(0x00FE, 0, 250, 8880, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2990)

    @scena.Lambda('lambda_29AB')
    def lambda_29AB():
        OP_8E(0x00FE, 0, 250, 4880, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_29AB)

    WaitForThreadExit(0x0108, 0x0001)
    ChrTurnDirection(0x0008, 0x0108, 0)
    ChrTurnDirection(0x0108, 0x0008, 0)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 5)
    SetChrFlags(0x0008, 0x0020)
    SetChrFlags(0x0108, 0x1000)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_29F7')
    def lambda_29F7():
        OP_96(0x00FE, 0x00000000, 0x000000FA, 0x00001504, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_29F7)

    @scena.Lambda('lambda_2A15')
    def lambda_2A15():
        OP_99(0x00FE, 0x00, 0x01, 0x00000640)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2A15)

    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 16)

    @scena.Lambda('lambda_2A2F')
    def lambda_2A2F():
        OP_96(0x00FE, 0x00000000, 0x000000FA, 0x000024A4, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2A2F)

    @scena.Lambda('lambda_2A4D')
    def lambda_2A4D():
        OP_99(0x00FE, 0x00, 0x04, 0x000009C4)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_2A4D)

    PlayEffect(0x04, 0xFF, 0x00FF, 0, 1200, 6880, 0, 0, 0, 1200, 1200, 1200, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000064, 0x00000190, 0x00000BB8, 0x00000096)
    WaitForThreadExit(0x0108, 0x0001)
    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 5)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 14)

    @scena.Lambda('lambda_2ABC')
    def lambda_2ABC():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2ABC)

    ChrTurnDirection(0x0108, 0x0008, 400)
    Sleep(700)

    @scena.Lambda('lambda_2AD6')
    def lambda_2AD6():
        OP_96(0x00FE, 0x00000B04, 0x000000FA, 0x00001AE0, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2AD6)

    @scena.Lambda('lambda_2AF4')
    def lambda_2AF4():
        OP_96(0x00FE, 0xFFFFF4CA, 0x000000FA, 0x00001AE0, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2AF4)

    WaitForThreadExit(0x0108, 0x0001)
    ChrTurnDirection(0x0008, 0x0108, 0)
    ChrTurnDirection(0x0108, 0x0008, 0)
    WaitForThreadExit(0x0108, 0x0001)
    Fade(500)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0102, 0x03)
    TerminateThread(0x00F9, 0x03)

    @scena.Lambda('lambda_2B3B')
    def lambda_2B3B():
        OP_8C(0x00FE, 0, 0)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2B3B)

    @scena.Lambda('lambda_2B49')
    def lambda_2B49():
        OP_8C(0x00FE, 0, 0)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_2B49)

    @scena.Lambda('lambda_2B57')
    def lambda_2B57():
        OP_8C(0x00FE, 0, 0)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_2B57)

    OP_6D(1220, 0, 8760, 0)
    OP_67(-500, 5590, -10000, 0)
    OP_6B(1900, 0)
    OP_6C(45000, 0)
    OP_6E(481, 0)
    OP_0D()
    Sleep(500)

    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 7)

    @scena.Lambda('lambda_2BB2')
    def lambda_2BB2():
        OP_96(0x00FE, 0xFFFFF4FC, 0x000000FA, 0x00001AE0, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2BB2)

    @scena.Lambda('lambda_2BD0')
    def lambda_2BD0():
        OP_99(0x00FE, 0x00, 0x01, 0x00000640)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2BD0)

    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 16)

    @scena.Lambda('lambda_2BEA')
    def lambda_2BEA():
        OP_96(0x00FE, 0x00000B36, 0x000000FA, 0x00001AE0, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2BEA)

    @scena.Lambda('lambda_2C08')
    def lambda_2C08():
        OP_99(0x00FE, 0x00, 0x04, 0x000009C4)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_2C08)

    PlayEffect(0x04, 0xFF, 0x00FF, 0, 1500, 6880, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x0108, 0x0001)
    PlayEffect(0x03, 0x03, 0x00FF, -4100, 1000, 7000, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x03, 0x04, 0x00FF, 4100, 1000, 7000, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    OP_7C(0x00000064, 0x000001F4, 0x00000BB8, 0x0000012C)
    OP_B0(0x0008, 0x0F)
    OP_6F(0x0008, 0)
    OP_70(0x0008, 0x0000001E)
    OP_B0(0x0009, 0x0F)
    OP_6F(0x0009, 0)
    OP_70(0x0009, 0x0000001E)
    OP_73(0x0008)
    OP_73(0x0009)
    OP_83(0x04, 0x02)
    Sleep(1000)

    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 5)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 14)

    @scena.Lambda('lambda_2D13')
    def lambda_2D13():
        OP_6D(1210, 0, 10570, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2D13)

    OP_22(0x023B, 0x00, 0x64)
    SetChrFlags(0x0008, 0x1000)

    @scena.Lambda('lambda_2D35')
    def lambda_2D35():
        OP_8C(0x00FE, 90, 600)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2D35)

    @scena.Lambda('lambda_2D43')
    def lambda_2D43():
        OP_96(0x00FE, 0xFFFFF182, 0x000000FA, 0x0000218E, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2D43)

    Sleep(100)

    OP_22(0x023B, 0x00, 0x64)
    SetChrFlags(0x0108, 0x1000)

    @scena.Lambda('lambda_2D70')
    def lambda_2D70():
        OP_8C(0x00FE, 270, 600)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_2D70)

    @scena.Lambda('lambda_2D7E')
    def lambda_2D7E():
        OP_96(0x00FE, 0x00000FDB, 0x000000FA, 0x00002378, 0x000001F4, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2D7E)

    WaitForThreadExit(0x0108, 0x0001)
    WaitForThreadExit(0x0008, 0x0001)
    ClearChrFlags(0x0108, 0x1000)
    ClearChrFlags(0x0008, 0x1000)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitForThreadExit(0x0108, 0x0001)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0200341096V#253F#6P呼呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341097V原来你并不是只会吹牛，\n',
            '还挺顽强的嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341098V#077F#2P你也一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080341099V#076F拥有那样的天赋\n',
            '怎么会堕入武术的黑暗中！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080341100V如果坚持在师傅的教导下苦练的话，\n',
            '一定可以到达正道的极致啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341101V#257F#6P哼，轮得到你说吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341102V#255F看来老头子的死因\n',
            '你还不清楚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0108, 0xFFFFFF38, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0108,
        (
            '#0080341103V#073F#2P……什…什么…！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341104V#253F#6P呼呼，脸色变了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341105V万一你要是赢了的话，\n',
            '我就说给你听吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341106V不过赌注就是你的命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x0008, 0)
    OP_0D()
    SetChrChipByIndex(0x0008, 25)
    OP_99(0x0008, 0x00, 0x02, 0x000005DC)
    Sleep(500)

    PlayEffect(0x01, 0x01, 0x0008, 100, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(
        0x0108,
        (
            '#0080341107V#074F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080341108V#072F……好吧。\n',
            '我就赌上这条命。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 23)
    OP_0D()
    OP_99(0x0108, 0x00, 0x0F, 0x000007D0)
    PlayEffect(0x01, 0x02, 0x0108, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    Fade(500)
    OP_6D(0, 0, 7000, 0)
    OP_67(0, 4580, -10000, 0)
    OP_6B(4080, 0)
    OP_6C(33000, 0)
    OP_6E(243, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010341109V#1020F#6P（金、金先生……！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341110V#1043F#4P（不行啊，艾丝蒂尔……\n',
            '  无法阻止了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    Fade(500)
    OP_6D(1000, 0, 10500, 0)
    OP_67(0, 6490, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(481, 0)
    ClearMapFlags(0x00000010)
    OP_0D()
    Sleep(300)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_320B')
    def lambda_320B():
        OP_6B(1650, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_320B)

    OP_7C(0x00000000, 0x00000064, 0x00000BB8, 0x00001388)

    ChrTalk(
        0x0008,
        (
            '#258F#30A呜喔喔喔喔喔喔……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0108,
        (
            '#0080341112V#077F#30A嗬啊啊啊啊啊啊……！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(5000)

    OP_56(0x00)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    SetChrPos(0x000E, 40, 2000, 2090, 270)
    ClearChrFlags(0x000E, 0x0080)
    SetChrChipByIndex(0x000E, 4)
    SetChrSubChip(0x000E, 16)
    SetChrFlags(0x000E, 0x0002)
    OP_22(0x038E, 0x00, 0x64)
    OP_7D(0x00, 0x000E, 0x0032, 0x01F4)

    @scena.Lambda('lambda_32C1')
    def lambda_32C1():
        OP_99(0x00FE, 0x10, 0x17, 0x00001F40)
        Yield()

        Jump('lambda_32C1')

    DispatchAsync2(0x000E, 0x0001, lambda_32C1)

    @scena.Lambda('lambda_32D4')
    def lambda_32D4():
        OP_8F(0x00FE, 0, 1200, 9600, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_32D4)

    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 5)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 14)

    @scena.Lambda('lambda_3303')
    def lambda_3303():
        OP_90(0x00FE, 2700, 0, 0, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3303)

    @scena.Lambda('lambda_331E')
    def lambda_331E():
        OP_90(0x00FE, -2700, 0, 0, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_331E)

    WaitForThreadExit(0x0008, 0x0001)
    OP_20(0x00000000)
    OP_22(0x023B, 0x00, 0x64)

    @scena.Lambda('lambda_3348')
    def lambda_3348():
        OP_96(0x00FE, 0xFFFFF614, 0x000000FA, 0x00002350, 0x000003E8, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3348)

    Sleep(100)

    OP_22(0x023B, 0x00, 0x64)

    @scena.Lambda('lambda_3370')
    def lambda_3370():
        OP_96(0x00FE, 0x00000AAA, 0x000000FA, 0x00002224, 0x000003E8, 0x00001F40)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_3370)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_82(0x01, 0x02)
    OP_82(0x02, 0x02)
    Sleep(1000)

    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0200341113V#259F#6P什么……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341114V#073F#2P偃月轮……怎么会！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrPos(0x0009, 40, 0, -3240, 0)
    ClearChrFlags(0x0009, 0x0080)
    SetChrFlags(0x0009, 0x0002)
    SetChrSubChip(0x0009, 2)
    SetChrChipByIndex(0x0009, 4)

    @scena.Lambda('lambda_344F')
    def lambda_344F():
        OP_8F(0x00FE, 500, 500, -3240, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_344F)

    @scena.Lambda('lambda_346A')
    def lambda_346A():
        OP_6D(310, 300, -800, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_346A)

    @scena.Lambda('lambda_3482')
    def lambda_3482():
        OP_67(0, 7680, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3482)

    @scena.Lambda('lambda_349A')
    def lambda_349A():
        OP_6B(1450, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_349A)

    @scena.Lambda('lambda_34AA')
    def lambda_34AA():
        OP_6E(533, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_34AA)

    SetChrSubChip(0x0008, 0)
    SetChrChipByIndex(0x0008, 2)
    SetChrSubChip(0x0108, 0)
    SetChrChipByIndex(0x0108, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0102, 0)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x00F9, 0)
    SetChrChipByIndex(0x00F9, 65535)

    @scena.Lambda('lambda_34EC')
    def lambda_34EC():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_34EC)

    Sleep(50)

    @scena.Lambda('lambda_34FF')
    def lambda_34FF():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_34FF)

    Sleep(50)

    @scena.Lambda('lambda_3512')
    def lambda_3512():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3512)

    Sleep(50)

    @scena.Lambda('lambda_3525')
    def lambda_3525():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3525)

    Sleep(50)

    @scena.Lambda('lambda_3538')
    def lambda_3538():
        OP_8C(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_3538)

    Sleep(600)

    OP_22(0x00D8, 0x00, 0x64)
    WaitForThreadExit(0x000E, 0x0002)
    SetChrFlags(0x000E, 0x0080)
    WaitForThreadExit(0x0101, 0x0002)
    OP_99(0x0009, 0x02, 0x08, 0x000005DC)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010341115V#1004F#5P雾、雾香小姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341116V#1044F#5P你怎么会在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0580341117V#792F#4P……蔡斯市的防卫战\n',
            '终于结束了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341118V#791F我把接待工作交给王，\n',
            '自己只是稍微来看看情况而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341119V#1016F#5P来、来看看情况……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x05)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36B7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050341120V#055F#5P那个『里塔』\n',
            '你一个人爬上来的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3792')

    def _loc_36B7(): pass

    label('loc_36B7')

    If(
        (
            (Expr.Eval, "OP_42(0x02)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3705',
    )

    ChrTalk(
        0x0103,
        (
            '#0030341121V#023F#5P那个『里塔』\n',
            '你一个人爬上来的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3792')

    def _loc_3705(): pass

    label('loc_3705')

    If(
        (
            (Expr.Eval, "OP_42(0x08)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3754',
    )

    ChrTalk(
        0x0109,
        (
            '#0180341122V#1064F#5P那个『里塔』\n',
            '你一个人爬上来的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3792')

    def _loc_3754(): pass

    label('loc_3754')

    ChrTalk(
        0x0102,
        (
            '#0020341123V#1044F#5P那个『里塔』\n',
            '你一个人爬上来的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3792(): pass

    label('loc_3792')

    Fade(250)
    SetMapFlags(0x00000010)
    OP_22(0x00D5, 0x00, 0x64)
    ClearChrFlags(0x0009, 0x0002)
    SetChrSubChip(0x0009, 0)
    SetChrChipByIndex(0x0009, 1)
    OP_0D()
    OP_1D(0x50)
    Sleep(1000)

    @scena.Lambda('lambda_37BE')
    def lambda_37BE():
        OP_6D(210, 0, 8800, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_37BE)

    @scena.Lambda('lambda_37D6')
    def lambda_37D6():
        OP_67(0, 4650, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_37D6)

    @scena.Lambda('lambda_37EE')
    def lambda_37EE():
        OP_6B(2880, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_37EE)

    @scena.Lambda('lambda_37FE')
    def lambda_37FE():
        OP_6C(0, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_37FE)

    @scena.Lambda('lambda_380E')
    def lambda_380E():
        OP_6E(315, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_380E)

    @scena.Lambda('lambda_381E')
    def lambda_381E():
        OP_8E(0x00FE, 0, 0, 6000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_381E)

    @scena.Lambda('lambda_3839')
    def lambda_3839():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_3839')

    DispatchAsync2(0x0108, 0x0003, lambda_3839)

    Sleep(500)

    @scena.Lambda('lambda_384F')
    def lambda_384F():
        OP_8E(0x00FE, 1500, 0, 1470, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_384F)

    Sleep(200)

    @scena.Lambda('lambda_386F')
    def lambda_386F():
        OP_8E(0x00FE, -1000, 0, 1110, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0003, lambda_386F)

    Sleep(300)

    @scena.Lambda('lambda_388F')
    def lambda_388F():
        OP_8E(0x00FE, 1000, 0, 2110, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_388F)

    WaitForThreadExit(0x0102, 0x0003)

    @scena.Lambda('lambda_38AF')
    def lambda_38AF():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_38AF')

    DispatchAsync2(0x0102, 0x0003, lambda_38AF)

    WaitForThreadExit(0x00F9, 0x0003)

    @scena.Lambda('lambda_38C5')
    def lambda_38C5():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_38C5')

    DispatchAsync2(0x00F9, 0x0003, lambda_38C5)

    WaitForThreadExit(0x0101, 0x0003)

    @scena.Lambda('lambda_38DB')
    def lambda_38DB():
        ChrTurnDirection(0x00FE, 0x0009, 400)
        Yield()

        Jump('lambda_38DB')

    DispatchAsync2(0x0101, 0x0003, lambda_38DB)

    WaitForThreadExit(0x0009, 0x0001)
    ChrTurnDirection(0x0009, 0x0008, 400)
    WaitForThreadExit(0x0102, 0x0000)
    TerminateThread(0x0108, 0x01)
    TerminateThread(0x0108, 0x03)
    TerminateThread(0x0008, 0x01)
    TerminateThread(0x0101, 0x03)
    TerminateThread(0x0102, 0x03)
    TerminateThread(0x00F9, 0x03)

    @scena.Lambda('lambda_3915')
    def lambda_3915():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_3915)

    WaitForThreadExit(0x0008, 0x0003)
    Sleep(500)

    ChrTalk(
        0x0108,
        (
            '#0080341124V#072F雾香，你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341125V#257F呼呼……还是老样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0200341126V#253F来看看情况，顺便\n',
            '再给老头子报仇吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0580341127V#791F怎么会呢……\n',
            '那只是公平决斗之后的结果吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341128V我没有理由去\n',
            '破坏父亲的决心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341129V#255F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341130V#572F雾香……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0580341131V#792F我来这里，\n',
            '只是为了向某个在六年前\n',
            '不辞而别的人说几句话，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341132V#790F只是如此而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341133V#251F说……几句话？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0580341134V#793F嗯嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341135V#792F……喂，瓦鲁特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341136V为什么要逃避\n',
            '对我的感觉……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341137V#255F#3S！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0580341138V#793F父亲对你说了些什么，\n',
            '详细内容我不清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341139V但是，那与我们的交往\n',
            '应该没有任何关系才对啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341140V#790F而金更是如此吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080341141V#073F！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341142V#254F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0580341143V#792F……果然是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341144V#794F瓦鲁特……你真傻。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341145V你以为父亲是\n',
            '会有那种想法的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341146V#254F这和老头子无关……\n',
            '是我自己的问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0008, 400)
    Sleep(500)

    ChrTalk(
        0x0108,
        (
            '#0080341147V#072F等，等一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080341148V#076F瓦鲁特！\n',
            '师父究竟和你说了些什么！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080341149V和我又有什么关系！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341150V#254F烦死了……\n',
            '我没有义务告诉你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0580341151V#792F嗯嗯，和金无关。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341152V#790F但是……\n',
            '你有义务告诉我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341153V如果一声不响地就消失掉\n',
            '那只不过是一种逃避而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#0200341142V#254F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0580341155V#792F我......对于漠视自己\n',
            '感情的人没有任何依恋。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341156V你愿意消失或离开都无所谓，\n',
            '喜欢堕落的话就继续堕落下去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0580341157V#790F而我只会以游击士协会负责人\n',
            '的身份来对你作出处理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0200341158V#250F……嘿嘿嘿……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0200341159V#252F#4S啊——哈哈哈！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0x00000000, 0x000000C8, 0x00000BB8, 0x00000064)
    CloseMessageWindow()
    Sleep(500)

    OP_22(0x0099, 0x00, 0x64)
    OP_23(0x00EB)
    OP_1F(0x5A, 0x000007D0)
    Fade(500)
    OP_6B(2700, 0)
    OP_82(0x00, 0x02)
    OP_82(0x81, 0x02)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_82(0x83, 0x02)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x04, 0x0002)
    OP_7B()
    Sleep(1000)

    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_412C',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_416A')

    def _loc_412C(): pass

    label('loc_412C')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4153',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    Jump('loc_416A')

    def _loc_4153(): pass

    label('loc_4153')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)

    def _loc_416A(): pass

    label('loc_416A')

    Sleep(1000)

    @scena.Lambda('lambda_4175')
    def lambda_4175():
        OP_6D(-250, 200, 17430, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_4175)

    @scena.Lambda('lambda_418D')
    def lambda_418D():
        OP_67(0, 3660, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_418D)

    @scena.Lambda('lambda_41A5')
    def lambda_41A5():
        OP_6B(3460, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_41A5)

    @scena.Lambda('lambda_41B5')
    def lambda_41B5():
        OP_8C(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_41B5)

    Sleep(50)

    @scena.Lambda('lambda_41C8')
    def lambda_41C8():
        OP_8C(0x00FE, 315, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_41C8)

    Sleep(50)

    OP_8C(0x0009, 0, 400)
    WaitForThreadExit(0x0101, 0x0000)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    OP_72(0x0001, 0x0020)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 0x0000003C)
    Sleep(100)

    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 0x0000003C)
    Sleep(100)

    OP_72(0x0003, 0x0020)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0x0000003C)
    Sleep(100)

    OP_72(0x0004, 0x0020)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 0x0000003C)

    ChrTalk(
        0x0101,
        (
            '#0010341160V#1004F#5P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341161V#1042F#5P回来了吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(300)

    OP_1F(0x64, 0x000007D0)
    Fade(1000)
    OP_6D(5030, 3860, 11650, 0)
    OP_67(0, 1590, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(45000, 0)
    OP_6E(363, 0)
    OP_0D()

    @scena.Lambda('lambda_42F4')
    def lambda_42F4():
        OP_6B(5500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_42F4)

    Sleep(500)

    OP_22(0x0139, 0x00, 0x64)
    LoadEffect(0x02, 'map\\mp049_02.eff')
    PlayEffect(0x02, 0x02, 0x00FF, 0, 0, 6720, 0, 0, 0, 550, 550, 550, 0x00FF, 0, 0, 0, 0)
    Sleep(800)

    OP_82(0x80, 0x00)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x02000000)
    OP_A2(0x10F0)
    NewScene('ED6_DT21/C3607._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x437A
@scena.Code('func_08_437A')
def func_08_437A():
    OP_6C(760000, 6000)

    Return()

# id: 0x0009 offset: 0x4384
@scena.Code('func_09_4384')
def func_09_4384():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_43D0',
    )

    ExecExpressionWithValue(
        0x000F,
        0x01,
        (
            (Expr.GetChrWork, 0x8, 0x1),
            (Expr.GetChrWork, 0x108, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x02,
        (
            (Expr.GetChrWork, 0x8, 0x2),
            (Expr.GetChrWork, 0x108, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x03,
        (
            (Expr.GetChrWork, 0x8, 0x3),
            (Expr.GetChrWork, 0x108, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_09_4384')

    def _loc_43D0(): pass

    label('loc_43D0')

    Return()

# id: 0x000A offset: 0x43D1
@scena.Code('func_0A_43D1')
def func_0A_43D1():
    OP_98(0x00, 0x000E)
    OP_98(0x01, 0x00000028, 0x000007D0, 0x0000334A)
    OP_98(0x01, 0x00000028, 0x00000BB8, 0x00003B1A)
    OP_98(0x01, 0x00000028, 0x00001770, 0x00004E20)
    OP_98(0x02, 0x00FE, 0x00004E20, 0x02)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
