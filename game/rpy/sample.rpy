
image demo_bg_1 = "images/bg/bghoba2.png"
image demo_bg_2 = "images/bg/bghobacorridor2.png"
image demo_bg_3 = "images/bg/bgxialu12.png"

label Sample:

    # 背景，带拉伸
    scene demo_bg_1 with dissolve:
        fit "contain"

    show mir at right, jump_once
    mir "真是疲惫...但一口气玩了好多！把小时候没玩的内容全部补上了。"
    with dissolve
    hide mir

    # 表情
    show sp at left, nod_once_slow:
        zoom(0.5)#缩放
    with dissolve
    sp "表情的话看一下character文件的命名"
    show sp sword
    with dissolve
    sp "直接show就可以切了"
    show sp -sword
    with dissolve
    sp "还能直接减号移除"

    # 讲话讲一半夹东西
    show aki at default, nod_once_slow
    aki "这个可以讲话讲一半夹东西"
    show aki at right, nod_once_slow
    extend "但是要点一下" 

    show aki at default, nod_once_slow
    aki "如果在结尾这样写就不用点一下了\n{nw}"
    show aki at right, nod_once_slow
    extend "默认是立刻切\n{nw=2}"
    show aki at default, nod_once_slow
    extend "里面写个=2可以决定停2秒\n"

    show aki at default, nod_once_slow
    aki "进入21比9模式"
    
    $ turn_219()
    #window hide
    $ show_narration219("这是一个21:9画面的旁白示例")
    show aki at default, nod_once_slow
    $ show_narration219("你看看这个效果怎么样")
    show aki at default, nod_once_slow
    $ show_narration219("要打字机效果的话我后面补上")
    show aki at default, nod_once_slow
    #$ hide_narration219()
    $ turn_169()
    aki "退出21比9模式"


    aki "111111111111"
    aki "111111111111"
    aki "111111111111"
    aki "111111111111"


    return