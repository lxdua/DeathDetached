image demo_bg_1 = "images/bg/bghoba2.png"
image demo_bg_2 = "images/bg/bghobacorridor2.png"
image demo_bg_3 = "images/bg/bgxialu12.png"

label Chapter3:

    # 游乐园背景，Aki和Mir两人对话，白日伴奏
    scene demo_bg_1 with dissolve:
        fit "contain"

    play music"bgm/Old_city.mp3"

    show mir1 at right, jump_once
    mir "你好。"
    with dissolve

    show aki1 at left, nod_once_slow
    with dissolve
    aki "你好。"
    
    return