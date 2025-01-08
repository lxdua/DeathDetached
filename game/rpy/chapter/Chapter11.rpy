image bg_11_1 = "images/bg/11/11_1.png"
image bg_11_2 = "images/bg/11/11_2.png"
image bg_11_3 = "images/bg/11/11_3.png"
image bg_11_4 = "images/bg/11/11_4.png"
image bg_11_5 = "images/bg/All_Black.png"
image bg_11_6 = "images/bg/Bg_Aquarium.png"
image bg_11_7 = "images/bg/BG_Ferris_wheel.png"
image bg_11_8 = "images/bg/Bg_Movie_Theater.png"
image bg_11_9 = "images/bg/Bg_Watching_Death.png"
image bg_11_10 = "images/bg/Bg_WatchingDeath_2.png"
image bg_Final = "images/bg/All_Black.png"

label Chapter11:

    # 游乐园背景，Aki和Mir两人对话，白日伴奏
    scene bg_11_1 with dissolve:
        fit "contain"

    play music"bgm/Old_City_Respite.mp3"


    voice"voice/Demo11/Mother1.wav"
    mir_mother "真疼啊...下次还是用红药水吧，消毒不干净但好歹不那么疼..."

    show mir at right
    show mir child
    with dissolve
    
    voice"voice/Demo11/Child01.wav"
    mir  "妈妈你没事吧...是不是爸爸又欺负你了，我们逃吧？我不想再看到他欺负你了..."

    voice"voice/Demo11/Mother2.wav"
    mir_mother" 逃能逃到哪里去啊....家里的钱都是你爸爸挣来的，也都在他手里。没有钱的话，逃到哪都是一样的...都活不下去"

    voice"voice/Demo11/Child02.wav"
    mir "咱们去找外公外婆，去找警察叔叔，去找老师...老师说过打人是不对的，受欺负了要去找老师帮忙才对"

    voice"voice/Demo11/Mother3.wav"
    mir_mother "傻孩子，找谁这件事都会传开来。而且你记得吗？咱们上次逃回外公外婆家，他拿着刀追到楼下，堵在门口一动不动...."

    voice"voice/Demo11/Mother4.wav"
    mir_mother "咱们只能希望他那边生意尽快好起来吧...好起来后就不会打人了。\n他也辛苦.....每天都在跑业务，应酬。在外面受那么多委屈，回家难免有脾气，这就是女人的命啊..."

    voice"voice/Demo11/Child03.wav"
    mir  "可是老师上课说过，无论如何，打人都是不对的！不管怎么样都不应该去伤害别人！"

    show mir -child
    with dissolve

    voice"voice/Demo11/Mir1.wav"
    mir "真是可怜的母女，不知道是谁受了那么久的家暴，竟然一点反抗的想法都没有"
    
    voice"voice/Demo11/Mir2.wav"
    mir "无论如何都不去伤害他人吗。在这种人吃人的世界里只会第一个死掉吧，大啖食粮之刻已到。"
    
    # 回到两人同框场景
    scene bg_11_2 with dissolve:
        fit "contain"
    show shadow at left
    with dissolve
    
    voice"voice/Demo11/801.wav"
    shadow "平常都很嚣张嘛，怎么不继续趾高气扬，高高在上了。"
    voice"voice/Demo11/802.wav"
    shadow "学习好点怎么了，老是小人得志那样子，真是让人气愤。"
    #（播放泼水音）
    voice"voice/Demo11/803.wav"
    shadow "怎么要睡着了，冲个澡清凉一下吧"
    voice"voice/Demo11/804.wav"
    shadow "哈哈哈哈哈哈哈哈哈哈"
    mir"（中学生） 你们....太过分了"
    voice"voice/Demo11/805.wav"
    shadow "抛开事实不谈，你不觉得被人欺负是自己平时太过分了吗？"
    #（播放拳打音效）
    voice"voice/Demo11/806.wav"
    shadow "噗....还敢还手，给我上！打到她动不了为止"
    
    mir"（中学生） 做得到的话尽管试试啊！"
    #（播放拳打音效）
    hide shadow
    show mir at left
    show mir left
    with dissolve

    voice"voice/Demo11/Mir3.wav"
    mir"（叹气） 还是太幼稚了，这种程度的反击根本震慑不了她们。\n应该在她们心中种下恐惧的种子，比直接还击来得管用很多。"
    
    # 回到两人同框场景
    scene bg_11_3 with dissolve:
        fit "contain"
    with dissolve
    mir "是的，这周六也要加班。今天又被领导骂了.....晚上下班的时候把我留下来说“效率低，这几天的活都没完成，该自觉一点周末过来公司继续努力"
    mir "明明是把其他人裁掉了，让我一个人干几个人的活，然后不断给我加压，希望我能做的更多更多。"
    mir "直系上司通过的提案老板不通过，老板的提案通过的提案直系上司不通过，他们明明想要的东西都不一样，却不统一口径，只希望我能突然拿出一份满足他们俩口味的作品。"
    mir "可是我根本不知道他们想要什么..."
    shadow"电话那头 打工总是要吃苦的，而且你刚刚也说了，老板把那些人裁掉就剩你，这是器重你，要把握好机会。"
    mir "不想干了...想接着读书，去留学也好，明明申请到了留学名额，哪怕是去逃避两年也好，想办法留在外面，或者以更高的学历回来，都比现在窝在小公司腐烂来的好吧？"
    shadow"电话那头 孩子，你也要知道家里的情况...你已经长大了，我们还指望你工作赚大钱来回馈家庭呢，那么多钱拿不出来的。"
    shadow"电话那头 现在工作不好找，外面失业的人大把，还是努力撑一下吧，过去就好了。"
    mir "可是身边的好朋友都去留学了...我又不是没拿到学校的名额。\n不想以后在学历上被人看扁，明明我一点都不比他们差。"
    shadow "电话那头 国外有什么好的，天天想着往国外跑！没看到新闻里报道国外多乱吗？\n 想去留学可以，留学的钱你自己想办法吧。"
    #（播放电话挂线音）
    
    hide shadow
    show mir left at left
    with dissolve
    voice"voice/Demo11/Mir4.wav"
    mir "真是可怜，那个时候还没意识到出生就决定了一切吧。还在以为努力就能改变未来，还在做无畏的挣扎。"

    # 回到两人同框场景
    scene bg_11_4 with dissolve:
        fit "contain"
    with dissolve
    
    show mir left at left
    with dissolve
    
    voice"voice/Demo11/Angel1.wav"
    angel "又在想那些不好的事了吗？ 总是愁眉苦脸，总是活在过去，日子是不会好起来的\n和我待在一起的时候要打起精神来！珍惜每次相处的时间！不许乱想！"
    
    voice"voice/Demo11/Angel2.wav"
    angel "下次再见面的话就是冬天啦！虽然很久很久，但是一定会见面的。\n一定要再见面哦！"
    

    show mir amazing 
    stop music

    mir "...?"
    
    scene bg_11_5 with dissolve:
        fit "contain"
    with dissolve

    show mir amazing at left
    aki_Death "从头到尾都在嗤笑自己的过去。即使是现在的你，也很可怜呢，继续说下去吧。"
    
    voice"voice/Demo11/Mir5.wav"
    mir  "什么声音，这里是哪里？一片漆黑，什么也看不到"
    show mir left
    
    voice"voice/Demo11/Mir6.wav"
    mir  "等一下....我是怎么到这里的？\n吃完了安眠药，逞强着去找Aki要了答案，然后看着Aki然后倒了下去。忘了她说了什么，只是很开心地闭上了双眼"
    voice"voice/Demo11/Mir7.wav"
    mir  "那我再醒过来的时候应该看到的是Aki？为什么全是回忆，回忆完便是一片黑暗，漫无边际的黑暗。"
    voice"voice/Demo11/Mir8.wav"
    mir  "也就是说.... 我死掉了吗？"
    voice"voice/Demo11/Mir9.wav"
    mir  "真是想不到，不是淹死，不是坠落，不是伤口感染溃烂，不是上吊，竟然是以这么荒唐的死法死掉。还以为现代医学的剂量下，28颗安眠药是死不掉的。"
    voice"voice/Demo11/Mir10.wav"
    mir  "不过也好吧....一切都结束了"
    
    show mir smile

    voice"voice/Demo11/Mir11.wav"
    mir "终于结束了。"

    show mir sad

    voice"voice/Demo11/Mir13.wav"
    mir "只是觉得有些遗憾，把Aki用完就跑掉了，也不知道她会怎么接受这个结局。和她相处的日子很开心，真希望这样的日子没有尽头，永永远远，没有尽头。"
    voice"voice/Demo11/Mir14.wav"
    mir "自杀的人上不了天堂，只能下地狱。接下来我会面对什么样的画面呢？判官？阎罗？黑白无常？死神？"

    hide mir

    show aki_Death Knife
    with dissolve

    aki_Death "死神"
    voice"voice/Demo11/Mir15.wav"
    mir"（惊讶） Aki？你怎么在这里！我们这是在哪，为什么我只看得见你，看不见周围的一切..."
    aki_Death "死神是没有真实面貌的，我会以你想见到的样子出现。这是你能享受到的最后一点人性，但请不要把我代入对应的人。"
    voice"voice/Demo11/Mir16.wav"
    mir"（失落） 好吧...死神，接下来我会面对什么呢，十八层地狱还是审判庭？人死后是怎么样的。"
    aki_Death  "什么都没有，死了就是死了，你只能自己一个人呆在这里，永永远远地待在这个地方。"
    voice"voice/Demo11/Mir17.wav"
    mir "这个地方黑漆漆的，像是监牢一样。\n我还没有理解现在是什么状况....是只能这样了吗？"
    aki_Death  "不，只是这个世界，本就是一片虚无罢了。我们可以换个地方说话，在到达尽头之前，陪你多玩一会吧。"

    scene bg_11_6 with dissolve:
        fit "contain"
    with dissolve

    play music"bgm/水族馆白噪音.mp3"
    show aki_Death at right
    with dissolve
    show mir left at left
    with dissolve

    aki_Death "这里如何？你一直很想去水族馆，只是还没和想去的那个人一起去而已，算满足了你一半的心愿"
    mir  "心愿还有一半的嘛？不管怎么玩文字游戏，不能被如愿以偿完成的心愿，怎么都不算完成吧？ 迟来的，变相的，等价的，以这些方式完成的都不算完成。"
    aki_Death "竟然还和我讨价还价的吗，要知道你完全没有资格。也不是你有心愿就能在死掉的世界完成吧。人生在世本就十有八九不如意，更何况是死后呢？"
    mir  "我没有在和你讨价还价，只是让你不要用这种善意来可怜我，我只会觉得恶心。"
    show aki_Death Sign
    aki_Death"（叹气）还是熟悉的臭脾气。"
    extend "冷静下来，你真的不想呆在这里吗？这么美丽的地方只属于你，没有任何人打扰，有的只有眼前永不停歇的鱼。\n偶尔还能自己投入其中，与他们一起沉浸。"
    aki_Death"（叹气） 我还以为你会喜欢呢，真是可惜。"
    mir "我确实会喜欢这种场景，但这场景适合大家一起看吧。\n只有我在这里日复一日地面对这些鱼的话，会像沉入海底一样无助吧。"
    show aki_Death -Sign
    aki_Death "但你不是最喜欢沉没了吗？一次又一次地坠入海中，河中，甚至是浴缸中。\n听起来你很抵触这种感觉，为什么不好好地活着呢"
    menu:
        "两害相权取其轻":
            mir "身体上的不适可以帮助我忽略精神上的不适，两害相权取其轻罢了"
            aki_Death"但这样的话，总是会活在痛苦当中的，你不一定要是那个做出选择的人"


        "期待被救出的感觉":
            mir "每次沉没时都会期待有人把我救出，那种置之死地而后生的兴奋，重生的喜悦，以及对救援者的感激，能把痛苦冲淡，抹平回忆留下的疤"
            aki_Death "听起来更像斯德哥尔摩综合症。"
    aki_Death "总之，我明白你不喜欢待在这里的原因了——因为我不是那个你想要一起沉浸的人。让我们去下个地方吧"

    scene bg_11_7 with dissolve:
        fit "contain"
    with dissolve

    play music"bgm/Daylight.mp3"
    show aki_Death at right
    with dissolve
    show mir left at left
    with dissolve
    aki_Death "这里如何？摩天轮的浪漫是，永远以你为中心转动。\n而且这里的时间已经停止了，或者说是永远循环了，你可以看着心爱的Aki与自己待在一起，就不会再像水族馆那样孤独了。"
    mir "心爱...？孤独...？"
    aki_Death "是啊，只要待在回忆里幸福的场景，不断地在脑里将其循环，这样的话真的会变得幸福的哦？"
    aki_Death "很多人将其称之为逃避，说这种行为是像胆小鬼一样，像鸵鸟一样，只顾着把头埋低，而不勇敢前进。我倒觉得不是这样的！人生并不需要一直前进，大多数人都是被推着向前走的，真能有机会自己停下来的时候，好好休息一番，或者彻底摆烂！留住这样的时间，不好吗？"
    menu:
            "Aki不是那样的定位":
                mir "Aki不是那样的位置，她一直在我的身边，在我的前方。我从不害怕她会突然离开会消失，她并不是过去，并不会成为过去，她也不需要停留在过去。是我需要..."
                mir "但我并不希望就这么和她留在过去，我想停留下来的另有其人，但即使到今日，我仍在追寻，仍在期待下一次相见，即使没有再见的机会..."
                aki_Death  "对自己的情况很清晰，而且目标也很明确.....\n真是佩服你，活得这么清晰的人也会自杀吗，让我的工作有趣多了"

            "这样的事不该由其他人决定":
                mir "这样的事不应该由其他人决定，我想留在什么样的记忆片段，过什么样的生活，停在什么样的时间，全部都不该由其他人决定"
                mir "今天你会让我留在这里，但我并不会只停留在这一个瞬间吧，哪怕是停留，我也是停留在众多瞬间中，而不是只看着一个钟摆物一样转个不停。"
                mir "何况，万一有一天你把这一瞬间收回去了呢，我会变得怎么样？\n再次支离破碎，呈现出痛苦不堪的样子供你取乐吗？"
                show aki_Death amazing
                aki_Death "（惊讶） 到了这种时候，这种地方也在反抗，你还真是讨厌他人给予的一切啊。"
                show aki_Death -amazing
                aki_Death "但你说的对，你也很清楚，不能再把自己交给别人了，对吧？顺带一提，你超雄的样子也很可爱，那可不是钟摆物....."
                show mir amazing
                mir "（惊讶） ...？"

                
    aki_Death "好了！摩天轮马上就到最高点了，许个愿吧，不管是“世界毁灭”还是“忧郁协会顺利发展”都好哦"
    show mir left
    mir  "真是无聊的说辞，像我曾经说过的话，忧郁协会也早就解散了，事到如今，许下什么愿望也毫无意义了，根本不会实现。"
    aki_Death "许愿最重要的是，许下愿望的那一瞬间，那一瞬间的祈祷也好，哀怨也罢，是真实存在的，是真正抓住了那一瞬间的心里所想。实不实现也许，没那么重要。{nw=2}"
    show aki_Death Smile
    extend"随便许个愿吧"
    menu:
            "想要继续活着":
                aki_Death"（笑容）想什么呢，这里我说了算，你没有任何选择可以做。（切换表情）瞧你那副不满的样子，谁让你这么轻易就抛弃了生命，任人摆布呢？"
            "想要见期待的人":
                aki_Death"（笑容）想什么呢，这里我说了算，你没有任何选择可以做。（切换表情）瞧你那副不满的样子，谁让你这么轻易就抛弃了生命，任人摆布呢？"
            "想要换一个阳光明媚的地方待着":
                aki_Death"（笑容）想什么呢，这里我说了算，你没有任何选择可以做。（切换表情）瞧你那副不满的样子，谁让你这么轻易就抛弃了生命，任人摆布呢？"
            "想要永久地死过去":
                aki_Death"（笑容）想什么呢，这里我说了算，你没有任何选择可以做。（切换表情）瞧你那副不满的样子，谁让你这么轻易就抛弃了生命，任人摆布呢？"
            " ":
                aki_Death"（笑容）想什么呢，这里我说了算，你没有任何选择可以做。（切换表情）瞧你那副不满的样子，谁让你这么轻易就抛弃了生命，任人摆布呢？"

    
    show mir fire at left
    #（出现Q版MIr生气的表情）
    aki_Death"（流汗）对不起！我只是开个玩笑而已。让我们去下一站把流程走完好吗？走完你想怎么样怎么样，我也可以干完今天的活，下班休息去了。" 
    menu:
            "道歉":
                mir"（黑脸） 道歉！"
                aki_Death"（哭泣） 对不起！饶了我吧，早点完成早点下班，完不成的话额外加班还要扣薪水，绩效受影响的同时还要影响退休年龄！求求你饶了我吧"
                mir"（自豪） 那我从头到尾拖着你不让你走还给你打差评是不是会很大程度的妨碍你！我一定会这么做的"
                aki_Death "（笑容） 骗你的，才不会有影响，只有活人才需要受这种繁文缛节束缚。"
                aki_Death "每个人死后都要被你当成玩具受你这种程度的羞辱和折磨吗？"
            "死神也有kpi也能休息的吗？":
                mir "死神也有kpi也能休息的吗？"
                aki_Death "（流汗黄豆微笑） 好姐姐，这里是死后之地，是世界尽头。不是什么社畜大楼，也不是黑奴矿场。"
                aki_Death"（自豪） 身为死神，每天只要接待两个人，上班四小时就OK了！ "

    aki_Death "玩开心了！接下来就！不胡闹了，办正事吧。"
    aki_Death "我们的下一站是！{nw=4}"
    
    scene bg_11_8 with dissolve:
        fit "contain"
    with dissolve
    
    play music"bgm/电磁白噪音.mp3"
    show aki_Death LowLight at right
    with dissolve
    show mir left at left
    with dissolve
    extend  "（失去高光）我们的下一站是电影院"
    
    aki_Death"（失去高光） 这里就是尽头了，最后的场景，所有死后的人最后都会来到这里。你想要做什么，想要看什么，这里都会有，自己的人生，别人的人生，都能看得到。你甚至可以在这些人生的段落上做剪辑，去编纂你想要的人生。"
    show mir amazing at left
    mir "（流汗）（内心独白） 气氛完全不一样了，好吓人...."
    mir "我想要什么样的人生都可以吗？你刚刚说的“剪辑”，是什么意思"
    aki_Death "（失去高光）就好像把东西切开再缝合一样，你可以缝缝补补出一个完全由你想象的世界，只要你能找到对应的素材，就能做出想要的修改。"
    mir "也就是说...这里真的可以改变一切？未竟的愿望，后悔的决定，没有选择的另一条道路，与我无缘的某种人生...？"
    aki_Death "（失去高光） 后者你什么都能体验到，但你什么都改变不了，你能改变的，唯有你的记忆而已。\n好了，去动手吧，做什么样的修改都行，骗骗自己也好，给你的人生画下一个完美句号吧。"
    mir "等一下....你好像非常讨厌这里，为什么刚刚都有说有笑的，到这里就变得这么...痛苦了呢？像催促着我去完成任务似的...我讨厌这样，请不要这么对我。"
    #（故障转场特效，转场到Aki（Death）特写，之后不出现Aki（Death）立绘）

    scene bg_11_9 with dissolve:
        fit "contain"
    with dissolve
    show mir left at left
    aki_Death "不好意思，我一到这里就会这样。我很讨厌这里，讨厌这个终点。很多人到了这个地方之后就开始拼凑，疯了般地想要挽回什么。"
    aki_Death "但如我刚才所说，这里只能修改自己的记忆——也就是在死后，通过欺骗自己的方式，为自己刚刚逝去的生命，画上句号。然后反复观看，直至我再也插不上任何一句话。即使他们知道，这只是一个骗局"
    show mir amazing at left
    mir "（惊讶） 骗局...？"
    aki_Death "是的，大家都热衷于欺骗着自己活下去。大多数都这样做着，直至自己死去，在死后的世界里重蹈覆辙，在这个世界也一样死去。\n真的很孤独呢，只要陪着他们到了这个地方，不管之前相处成了怎么样的关系，他们都会把我抛下。"
    aki_Death "死亡并不可怕，可怕的是死不掉。而我不仅死不掉，还要一次又一次目睹这些人的死亡。接受他们的死亡，引领他们，直至他们再一次死亡，就好像我从未出现过一样，这比让我自己死去还痛苦。"
    aki_Death "一是这样的工作，漫长地毫无尽头，二是没有什么比无用的努力更让人绝望的了，可以的话，我也不想当这个死神。但我并没有任何选择。\b能与你聊天很开心，可惜万物终有尽头，我已经麻木了，不想再面对这些，请你自便吧。"
    show mir left
    mir "虽然我也很后悔，但其实没有什么好修改。与其花时间在排列组合过去的记忆上，不如多花点时间陪陪你吧，你也很辛苦了。"
    
    scene bg_11_10 with dissolve:
        fit "contain"
    with dissolve

    # (Aki（Death）转头看向Mir）
    aki_Death "死了还说这么不安分的话....不如你来替我当死神吧，这样我就可以真正的死去了。"
    mir "只能有一个死神吗？"
    aki_Death "有且只会有一个死神，这就是残酷的规则。扮演这个角色的人，或者是死人，一定会是孤独的。"
    mir "那我拒绝，简直就像人们口中的西西弗斯一样，永远地一个人做着徒劳无功的事。"
    aki_Death "西西弗斯？那个推石头的吗？\n有人曾和我说过，应当想象西西弗斯是幸福的，他不止是在推石头上山顶，而是在一次又一次地攀登顶峰，而攀登山顶的拼搏本身就足以充实一颗人心。"
    aki_Death "真是好笑，用虚无填满的人心，不仍然是虚无吗？"
    mir "你这家伙，长得像Aki，声音也像Aki，唯独性格，比Aki差多了。"
    aki_Death "（惆怅特写）脸长的一样，声音也像，这不就够了吗？性格再相似的话，我是不是就能成为Aki了，不去改变自己的性格，靠你欺骗自己，我也能成为Aki不是吗？"
    aki_Death "到那时，对AKi的爱是否能分我一些呢？爱我是不是就等同于爱AKi呢？"

    aki_Death "人生真是一部烂片，最烂最烂的片子"


    scene bg_Final with dissolve:
        fit "contain"
    with dissolve
    
    aki_Death "Chapter11,over"
    





    return