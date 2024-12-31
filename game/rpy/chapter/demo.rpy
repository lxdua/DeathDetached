
image demo_bg_1 = "images/bg/bghoba2.png"
image demo_bg_2 = "images/bg/bghobacorridor2.png"
image demo_bg_3 = "images/bg/bgxialu12.png"

label demo:

    # 游乐园背景，Aki和Mir两人对话，白日伴奏
    scene demo_bg_1 with dissolve:
        fit "contain"

    show mir1 at right, jump_once
    mir "真是疲惫...但一口气玩了好多！把小时候没玩的内容全部补上了。"
    with dissolve

    show mir1 at right, turn_dark
    show aki1 at left, nod_once_slow
    with dissolve
    aki "让你慢一点了....少玩几个项目下次来再玩也行的。呼....累死了。"
    
    show mir1 at right, shake_once, turn_norcol
    mir "下次再来就不知道是什么时候了，一次玩完才够尽兴嘛！快看看还有哪些剩下的内容可以玩。"
    
    show aki1 at left, nod_once, turn_norcol
    aki "还剩一个...那个大摩天轮。"
    
    show mir1 at right, nod_once
    mir "不是很想去又有点想去..."
    show mir1 at right, jump_once
    mir "好像只有它要额外收费诶？！"

    aki "这是什么说辞，不想去的话我们可以吃饭去了。下班，好耶！"

    show mir1 at right, jump_once
    mir "不行！你得陪我去，走吧走吧，钱我来出，算我请的了。"

    aki "能不能请晚饭而不是请摩天轮，算坐摩天轮的精神损失费。"
    mir "你坐摩天轮也会精神损失吗？可以请晚饭，但是那就得回家吃我做的了。"
    aki "(无语) 唉，生命体征维持餐。"
    mir "(生气)不想吃别吃！走了走了！去摩天轮。"
    aki "走慢一点..."

    # 切换到摩天轮内部场景
    scene demo_bg_2 with dissolve:
        fit "contain"
    pause 0.5
    show aki1 at left
    show mir1 at right
    with dissolve

    #$ renpy.music.play("bgm/where_are_you_going.mp3", loop=True)

    mir "(埋怨)明明游乐园门票已经花了600元，摩天轮还要额外收60元，坐地起价，能不能打电话举报。"
    aki "可以的，那你就得等到相关人员来到这里，调查取证等回馈...等忙完这些取回你的60元就一个多月过去了，说不定还取不回呢。\n既然坐上来了，抱怨的话之后再说吧，好好看风景啦。"
    mir "没有一点办法....当是做慈善了。\n话说回来，Aki上次坐摩天轮是什么时候呢？"
    aki "记不清了...还是小孩子的时候吧，被家里人拉着说“小孩子一定很喜欢这个”，就坐了上来，然后在空中摇摇晃晃地，不知不觉就落地了。"
    
    menu:
        "我猜是坠落的感觉":
            mir "虽然我也很喜欢坠落的感觉，但总不至于上摩天轮找吧？\n是那种，轻松暧昧的感觉。在摩天轮升起的时候，就只有我们两个人，然后四目相对，直至最高处。\n在那种瞬间，找到世界只属于我们两个人的感觉。"
            aki "那看来得和喜欢的人搭才能找到。这么说来，我倒是想自己搭一次摩天轮试试了。\n如果两个人来的感觉是世界只属于俩人，那么自己来的感觉，会不会是自己一个人逃离了这个世界呢？"

        "钱包破产的感觉":
            mir "还在提！刚刚变好的氛围一下被你破坏了！应该由你来出这个钱！等你的钱包也破产了就不会幸灾乐祸了！"
            aki "我的钱包早就到了打开见不到钱的地步了，没有破产的机会哦。"
            mir "移动支付先行者，小心哪天你卡里的钱取不出来了！钱还是握在自己手里有安全感..."
            aki "不否认如此，但是你刚才付钱的时候安全感就破裂了哦，还是用数字货币来掩埋一下花钱的心疼感吧"

    mir "在那之前，先抓住面前的景色吧，马上就到最高点了，有什么想说的吗？"

    aki "没有，我已经过了那种喊“哇哇哇，好厉害！”的年纪了。"

    mir "一点都不可爱（埋怨语气），或者是许个愿也好，这种环境多适合许愿，比如“世界统统毁灭！”"

    aki "那不是一样吗，不过真说许愿的话，想替你许个“忧郁协会顺利发展，能够帮助到更多人”的愿望吧。"

    mir "谢谢你，那样的话我就能许“能有一次机会和喜欢的人再来这里许愿”的愿望了。"

    aki "还真是不客气。套娃，这种愿望会不灵的，不过你竟然没有和哪个前男友来过这种地方吗？"

    mir "没有谈过前男友哦，有很喜欢的前女友，想和她一起来的，可惜想到的太晚，散的太早吧。\n也许带现在这个女友过来可以弥补一下之前的遗憾。"

    # 切换到摩天轮远景，考虑加拉伸视角特效
    scene demo_bg_1 with dissolve:
        fit "contain"

    aki "摩天轮的顶端不应该讲这么爆炸的内容吧？！"

    # 回到两人同框场景
    scene demo_bg_2 with dissolve:
        fit "contain"
    show aki1 at left
    show mir1 at right
    with dissolve

    mir "(流汗表情) 对不起，是应该早点告诉你的...不过摩天轮上说这些其实正合适，这样你就不会太怪我了。"


    aki "(黑脸)这和在哪告诉我没有关系，这和你女友会不会上门找我麻烦有关系，我已经想从摩天轮上逃掉了，打破窗户就是现在。"


    mir "(流汗表情)之后给你介绍一下吧...我和你说过“大多数人会让我感到痛苦不安”这件事，唯独她能一直让我感到心安，我总想和她多呆一会。"


    aki "(内心独白) 甜蜜的陷阱吗...."

    # 图片两人手机收到消息特写，消息内容是“请帮帮我...”，来源是“忧郁协会”
    scene demo_bg_3 with dissolve:
        fit "contain"

    aki "来单子了..."

    mir "不是单子，是“让世界变得更好”的方式。"

    # 切换至两人特写，状态由散漫变得严肃
    scene demo_bg_2 with dissolve:
        fit "contain"

    aki "今天晚饭是不是泡汤了，只能回家吃你做的糠咽菜了是吧。"

    mir "那下次我请你吃顿大餐，今天帮我把这个救下来吧。"

    aki "当然。"

    # 两人出摩天轮各自脚步特写
    scene demo_bg_1 with dissolve:
        fit "contain"

    "aki/mir" "(不出现立绘) 忧郁互助小队，出发！"

    aki "(无语表情，出现立绘) 太土了也...根本不适合我。"

    return