image bg_11_1 = "images/bg/11/11_1.png"
image bg_11_2 = "images/bg/11/11_2.png"
image bg_11_3 = "images/bg/11/11_3.png"
image bg_11_4 = "images/bg/11/11_4.png"
image bg_11_5 = "images/bg/All_Black.png"
image bg_11_6 = "images/bg/Bg_Aquarium.png"
image bg_11_7 = "images/bg/BG_FerrisWheel.png"
image bg_11_8 = "images/bg/Bg_Movie_Theater.png"
image bg_11_9 = "images/bg/Bg_Watching_Death.png"
image bg_11_10 = "images/bg/Bg_WatchingDeath_2.png"
image bg_All_Black = "images/bg/All_Black.png"
image bg_All_White = "images/bg/All_White.png"
image Bg_Title = "images/bg/Bg_Title.png"

label Chapter11JP:

    # 游乐园背景，Aki和Mir两人对话，白日伴奏
    scene bg_11_1 with dissolve:
        fit "contain"

    play music"bgm/Old_City_Respite.mp3"


    voice"voice/Demo11/Mother1.wav"
    mir_mother "痛い...今度は赤い消毒薬を使おう、ちゃんと消毒できないけど、少なくとも痛くはないから..."

    show mir at right
    show mir child
    with dissolve
    
    voice"voice/Demo11/Child01.wav"
    mir  "母さん、大丈夫？ またお父さんが虐めたの？ 逃げよう？ もうあの人に虐められるの見たくない..."

    voice"voice/Demo11/Mother2.wav"
    mir_mother" 逃げたってどこへ行けるの...家のお金は全部あの人が稼いで握ってる。お金がなければ、どこへ逃げても同じ...生きていけないわ"

    voice"voice/Demo11/Child02.wav"
    mir "祖父母のところへ行こう、警察のおじさんに相談しよう、先生に...先生は「人を叩くのは間違ってる、虐められたら先生に相談すべき」って教えてくれた"

    voice"voice/Demo11/Mother3.wav"
    mir_mother "馬鹿な子、誰に相談しても噂が広がるだけ。覚えてる？ 前回祖父母の家に逃げた時、あの人が包丁を持って階下まで追いかけてきて、入口を塞いで動かなかった..."

    voice"voice/Demo11/Mother4.wav"
    mir_mother "あの人の商売が早く好転するよう祈るしかないわ...商売がうまくいけば、暴力もなくなるから。\nあの人も大変なの...毎日営業で飛び回り、接待。外でたくさん辛い目に遭って、家で八つ当たりするのも女の宿命よ..."

    voice"voice/Demo11/Child03.wav"
    mir  "でも先生は授業で「どんな理由があっても暴力は間違ってる！ 絶対に人を傷つけちゃダメ！」って言ってた!"

    show mir -child
    with dissolve

    voice"voice/Demo11/Mir1.wav"
    mir "可哀想な母子だ...こんなに長く暴力に耐えて、少しも抵抗する考えがなかったなんて"
    
    voice"voice/Demo11/Mir2.wav"
    mir "「どんな理由があっても人を傷つけない」？ この人食い世界じゃ真っ先に食い殺されるわ。糧食を貪る時が来た。"
    
    # 回到两人同框场景
    scene bg_11_2 with dissolve:
        fit "contain"
    show shadow at left
    with dissolve
    
    voice"voice/Demo11/801.wav"
    shadow "普段は威張ってたのに、どうして続けて高飛車な態度取らないの？"
    voice"voice/Demo11/802.wav"
    shadow "勉強ができるからって、いつも小人の得手勝手な様子、本当に腹立たしい"
    
    play sound "sound/DropWater.wav"
    #（播放泼水音）
    voice"voice/Demo11/803.wav"
    shadow "眠くなってきた...シャワー浴びてさっぱりしよう"
    voice"voice/Demo11/804.wav"
    shadow "はははははははははは!!!"
    voice"voice/Demo11/80_Mir1.wav"
    mir"（中学生） あなたたち...ひどすぎる"
    voice"voice/Demo11/805.wav"
    shadow "事実はさておき、虐められるのは普段の行いが悪いからじゃない？"
    
    play sound "sound/Boxing.wav"
    #（播放拳打音效）

    voice"voice/Demo11/806.wav"
    shadow "プッ...まだ反抗する気？ やれ！ 動けなくなるまで叩け"
    
    play sound "sound/80Fight.mp3"
    voice"voice/Demo11/80_Mir2.wav"
    mir"（中学生） できるものならやってみなさいよ！"
    #（播放拳打音效）
    hide shadow
    show mir at left
    show mir left
    with dissolve

    voice"voice/Demo11/Mir3.wav"
    mir"（叹气） まだ幼稚だな、この程度の反撃じゃ彼女らを威嚇できない。\n 恐怖の種を心に植え付けるべきだ、直接反撃するより効果的だ。"
    
    # 回到两人同框场景
    scene bg_11_3 with dissolve:
        fit "contain"
    with dissolve
    voice"voice/Demo11/Mir_JustWorked/Mir_JustWorked1.wav"
    mir "そう、今週の土曜も残業。今日も部長に怒鳴られた...夜勤終わりに「効率悪い、ここ数日の仕事が終わってない、自覚持って週末出勤しろ」って"
    
    voice"voice/Demo11/Mir_JustWorked/Mir_JustWorked2.wav"
    mir "明らかに他の人をクビにして、私一人で数人分の仕事をさせて、どんどんプレッシャーかけてくる。もっと働けって言わんばかりに。"

    voice"voice/Demo11/Mir_JustWorked/Mir_JustWorked3.wav"
    mir "直属上司が通した提案は社長が却下し、社長の提案は上司が却下する。彼らが求めてるものが違うのに、意見を統一せず、突然二人の好みを満たす作品を出せと。"

    voice"voice/Demo11/Mir_JustWorked/Mir_JustWorked4.wav"
    mir "でも彼らが何を望んでるのか全然分からない...."

    voice"voice/Demo11/Mir_JustWorked/Mother (1).wav"
    shadow"(電話の向こう) アルバイトは辛いものだよ。それに君も言った通り、社長が他の人を切って君だけ残したのは、君を重宝してる証拠だ。チャンスを逃すな"
    
    voice"voice/Demo11/Mir_JustWorked/Mir_JustWorked5.wav"
    mir "辞めたい...また勉強したい、留学したい。合格した留学枠があるのに、たとえ2年逃げるように過ごしても、海外に残るか、高い学歴で帰ってくるか、今よりましだ"
    
    voice"voice/Demo11/Mir_JustWorked/Mother (2).wav"
    shadow"(電話の向こう) うちの事情も分かってくれ...もう大人なんだから、家族を養うために働いて稼いでほしい。そんな大金出せるわけない。"
    
    voice"voice/Demo11/Mir_JustWorked/Mother (3).wav"
    shadow"(電話の向こう) 今は仕事探しも大変だ、失業者だらけだから、もう少し頑張れ。時が経てば良くなる"

    voice"voice/Demo11/Mir_JustWorked/Mir_JustWorked6.wav"
    mir "でも友達はみんな留学してる...私だって合格枠取れたのに.\n将来学歴で馬鹿にされたくない、彼らに劣ってないのに。"
    
    voice"voice/Demo11/Mir_JustWorked/Mother (4).wav"
    shadow "(電話の向こう) 海外が何だっていうんだ！ ニュースで海外の混乱ぶりを見てないのか？\n 留学したいなら自分で費用を工面しろ。"
    #（播放电话挂线音）
    play sound "sound/Tel_DuDu.mp3"

    hide shadow
    show mir left at left
    with dissolve
    voice"voice/Demo11/Mir4.wav"
    mir "哀れだね...生まれが全てを決めるって気付いてなかったんだ。まだ努力で未来を変えられると信じて、無駄な抵抗を続けてた。"

    # 回到两人同框场景
    scene bg_11_4 with dissolve:
        fit "contain"
    with dissolve
    
    show mir left at left
    with dissolve
    
    voice"voice/Demo11/Angel1.wav"
    angel "また悪いこと考えてる？ いつも暗い顔して、過去に囚われてたら、良い日々は来ないよ\n私と一緒にいる時は元気出して！ 一緒に過ごす時間を大切に！ 余計なこと考えるな！"
    
    voice"voice/Demo11/Angel2.wav"
    angel "次に会う時は冬だね！ ずいぶん先だけど、きっと会える\n絶対また会おうね！！"
    

    show mir amazing 
    stop music fadeout 4.0

    mir "...?"
    
    scene bg_11_5 with dissolve:
        fit "contain"
    with dissolve

    show mir amazing at left
    voice"voice/Demo11/Aki_Death/Aki_Death01.wav"
    aki_Death "最初から最後まで自分の過去を嘲笑ってる。今の君も哀れだね、続けて話して"
    
    voice"voice/Demo11/Mir5.wav"
    mir  "何の音？ ここはどこ？ 真っ暗で何も見えない"
    show mir left
    
    voice"voice/Demo11/Mir6.wav"
    mir  "待って...どうやってここに来たの？\n睡眠薬を飲みきって、無理してAkiに答えを求めに行き、Akiを見つめて倒れた。彼女が何を言ったか忘れたけど、嬉しそうに目を閉じた"
    voice"voice/Demo11/Mir7.wav"
    mir  "じゃあ目覚めたらAkiがいるはず？ なぜ全部思い出して、その後に暗闇が広がってるの？"
    voice"voice/Demo11/Mir8.wav"
    mir  "つまり...私死んだの？"
    voice"voice/Demo11/Mir9.wav"
    mir  "信じられない、溺死でも転落死でもなく、傷の感染でも首吊りでもなく、こんな荒唐な死に方をするなんて。現代医学の用量では28錠の睡眠薬じゃ死なないと思ってた"
    voice"voice/Demo11/Mir10.wav"
    mir  "でもいいわ...全て終わった"
    
    show mir smile

    voice"voice/Demo11/Mir11.wav"
    mir "ようやく終わった"

    show mir sad

    voice"voice/Demo11/Mir13.wav"
    mir "ただ少し残念だ、Akiを利用して逃げ出しちゃって、彼女がどう受け止めるか分からない。彼女と過ごした日々は楽しかった、このまま永遠に続けば良かったのに"
    voice"voice/Demo11/Mir14.wav"
    mir "自殺者は天国に行けず地獄へ堕ちる。次に待ってるのはどんな光景？ 判官？ 閻魔？ 黒白無常？ 死神？"

    hide mir

    show aki_Death Knife
    with dissolve

    voice"voice/Demo11/Aki_Death/Aki_Death02.wav"
    aki_Death "死神"

    voice"voice/Demo11/Mir15.wav"
    mir"（驚き）Aki？ どうしてここに！ ここはどこ？ 周りは見えず君だけが見える..."
    
    voice"voice/Demo11/Aki_Death/Aki_Death03.wav"
    aki_Death "死神に顔はない、君が会いたい人の姿を映し出すだけ。これは君に許された最後の人間性だが、本人と同一視しないで"

    voice"voice/Demo11/Mir16.wav"
    mir"（落胆）そう...死神さん、次は何が待ってるの？ 十八地獄？ それとも裁判？ 死後の世界はどうなってるの"
    
    voice"voice/Demo11/Aki_Death/Aki_Death04.wav"
    aki_Death  "何もない、死んだら終わり。ただ一人でここに永遠に閉じ込められる"

    voice"voice/Demo11/Mir17.wav"
    mir "この暗い牢獄のような場所に\nまだ状況が飲み込めてない...このままなの？"

    voice"voice/Demo11/Aki_Death/Aki_Death05.wav"
    aki_Death  "いや、この世界は元々虚無なんだ。別の場所に移動して話そう、終わりが来るまで、少し付き合ってあげる"

    scene bg_11_6 with dissolve:
        fit "contain"
    with dissolve

    play music"bgm/水族馆白噪音.mp3"
    show aki_Death at right
    with dissolve
    show mir left at left
    with dissolve

    voice"voice/Demo11/Aquarium/Aki_Death_Aquarium01.wav"
    aki_Death "ここはどう？ ずっと行きたかった水族館。行きたい人と一緒には行けなかったけど、半分は願いが叶ったね"
    
    voice"voice/Demo11/Aquarium/Mir_Aquarium01.wav"
    mir  "願いが半分って？ 言葉遊びしても、叶えられない願いは叶ったとは言えない。遅れて、形を変えて、同等のもので叶えても意味ない"
    
    voice"voice/Demo11/Aquarium/Aki_Death_Aquarium02.wav"
    aki_Death "まだ駆け引きする気？ 君に資格は全くない。生前叶わなかった願いが死後の世界で叶うわけない。生きてたって八九分うまくいかない、まして死後ならなおさら"
    
    voice"voice/Demo11/Aquarium/Mir_Aquarium02.wav"
    mir  "駆け引きしてない、ただ偽善で哀れむのはやめて。吐き気がする"
    show aki_Death Sign
    
    voice"voice/Demo11/Aquarium/Aki_Death_Aquarium03.wav"
    aki_Death"（溜息）相変わらずの悪い性格"
    
    voice"voice/Demo11/Aquarium/Aki_Death_Aquarium04.wav"
    extend "落ち着いて、本当にここが嫌なの？ この美しい場所は君だけのもの、誰にも邪魔されず、永遠に泳ぎ続ける\n魚たちと時々自ら飛び込んで、彼らと一緒に没入できる"
    
    voice"voice/Demo11/Aquarium/Aki_Death_Aquarium05.wav"
    aki_Death"（溜息）気に入るかと思ったのに残念だ"
    
    voice"voice/Demo11/Aquarium/Mir_Aquarium03.wav"
    mir "確かにこの情景は好きだけど、みんなで見るべきものだわ\n私だけがここで来る日も来る日もこの魚たちに直面していると、海底に沈むように無力になるだろう。"
    show aki_Death -Sign
    
    voice"voice/Demo11/Aquarium/Aki_Death_Aquarium06.wav"
    aki_Death "でもあなた、沈むのが一番好きじゃなかった？ 何度も海へ、川へ、バスタブへと沈んでた\nその感覚を拒絶してるように聞こえるわ。どうしてまともに生きられないの"
    menu:
        "二つの害の軽い方を選んだだけ":
            
            voice"voice/Demo11/Aquarium/Mir_Aquarium04.wav"
            mir "身体の苦痛は精神の苦痛を忘れさせてくれる、二つの害の軽い方を選んだだけ"

            voice"voice/Demo11/Aquarium/Aki_Death_Aquarium07.wav"
            aki_Death"でもそんな風にしていたら、ずっと苦しみの中にいることになる。あなたが選ぶ必要なんてないのに"


        "死地に置かれた後の興奮":
            
            voice"voice/Demo11/Aquarium/Mir_Aquarium05.wav"
            mir "沈むたびに誰かに救われるのを期待してた。死地に置かれた後の興奮、再生の喜び、救出者への感謝が苦痛を和らげ、傷跡を消してくれる"
            
            voice"voice/Demo11/Aquarium/Aki_Death_Aquarium08.wav"
            aki_Death "ストックホルム症候群みたい。"
            
    voice"voice/Demo11/Aquarium/Aki_Death_Aquarium09.wav"
    aki_Death "とにかく、君がここを気に入らない理由が分かった――私が君と一緒に没入したい相手じゃないから。次へ行こう"

    scene bg_11_7 with dissolve:
        fit "contain"
    with dissolve

    play music"bgm/Daylight.mp3"
    show aki_Death at right
    with dissolve
    show mir left at left
    with dissolve
    
    voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel01.wav"
    aki_Death "ここはどう？ 観覧車のロマンスは、永遠に君を中心に回ること。\nしかもここでは時間が止まってる、永遠にループする。愛しいAkiと一緒にいられるから、水族館ほど寂しくない。"
    
    voice"voice/Demo11/FerrisWheel/Mir_FerrisWheel01.wav"
    mir "愛しい...？ 寂しい...？"

    voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel02.wav"
    aki_Death "そう、幸せな記憶の中に留まり、脳内でループさせれば本当に幸せになれるんだよ？"
    
    voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel03.wav"
    aki_Death "多くの人はこれを逃避と呼び、臆病者のように、ダチョウのように頭を低くするだけで勇敢に前進しないと批判する。でも私は違うと思う！ 人生はずっと前進する必要ない、大多数は流れに押されて進むもの。自分で止まれる機会があれば、しっかり休んだり徹底的に堕落したり！ そんな時間を留めるのも悪くない"
    menu:
            "Akiはそんな存在じゃない":
                voice"voice/Demo11/FerrisWheel/Mir_FerrisWheel02.wav"
                mir "Akiはそんな存在じゃない。彼女はいつも私のそばに、そして前の方にいてくれた。突然いなくなったり消えたりするんじゃないかと恐れたことは一度もない。彼女は過去でもなければ、過去になることもない。過去に縛られる必要だってない。必要としてるのは私の方で..."
                
                voice"voice/Demo11/FerrisWheel/Mir_FerrisWheel03.wav"
                mir "でも過去に彼女と留まりたくはない、留まりたいのは別の人、でも今でも探し続け、次に会うのを期待してる、もう会えなくても..."
                
                voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel04.wav"
                aki_Death  "自分の状況を把握し、目標も明確...\n立派だね、ここまで自覚ある人が自殺するなんて、私の仕事が面白くなる."

            "こういうことは他人が決めるべきじゃない":
                
                voice"voice/Demo11/FerrisWheel/Mir_FerriSWheel04.wav"
                mir "こういうことは他人が決めるべきじゃない、どんな記憶に留まり、どんな人生を送り、どんな時に止まるか、全て他人が決めるべきじゃない"
                
                voice"voice/Demo11/FerrisWheel/Mir_FerriSWheel05.wav"
                mir "今日はここに留めてくれるけど、一瞬だけに留まらないでしょ？ 留まるにしても多くの瞬間の中を漂い、振り子のように一つのものを見続けない。"
                
                voice"voice/Demo11/FerrisWheel/Mir_FerriSWheel06.wav"
                mir "まして、ある日この瞬間を取り上げられたら、私はどうなる？\n再びバラバラになり、苦悶の表情で君の慰みものになる？"
                show aki_Death amazing
                
                voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel05.wav"
                aki_Death "（驚き）ここまで来ても反抗する、本当に他人からの施しが嫌いなんだね。"
                show aki_Death -amazing
                
                voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel06.wav"
                aki_Death "でも正しい、君も分かってる、もう他人に自分を委ねちゃいけない。ちなみに、雄々しい姿も可愛いよ、振り子じゃないんだから..."
                show mir amazing
                mir "（惊讶） ...？"

                 
    voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel07.wav"
    aki_Death "さあ！ 観覧車が頂上に着く、願い事をしなさい。「世界滅亡」でも「憂鬱協会の発展」でも"
    show mir left
    
    voice"voice/Demo11/FerrisWheel/Mir_FerrisWheel07.wav"
    mir  "つまらない台詞、私が昔言ってた言葉、憂鬱協会もとっくに解散した。今更願い事したって無意味、叶わない"
    
    voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel08.wav"
    aki_Death "许願い事の本質は、願う瞬間の祈りや怨みが本物であること。叶うかどうかは重要じゃない{nw=2}"
    show aki_Death Smile
    extend"適当に願えば"
    menu:
            "Life":
                
                voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel09.wav"
                aki_Death"（笑顔）何考えてるの？ ここでは私が支配者、君に選択権はない。（表情変えて）その不満そうな顔、安易に命を棄てたからだよ"
            "Hope":
                
                voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel09.wav"
                aki_Death"（笑顔）何考えてるの？ ここでは私が支配者、君に選択権はない。（表情変えて）その不満そうな顔、安易に命を棄てたからだよ"
            "Living under sunshine":
                
                voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel09.wav"
                aki_Death"（笑顔）何考えてるの？ ここでは私が支配者、君に選択権はない。（表情変えて）その不満そうな顔、安易に命を棄てたからだよ"
            "Death":
                
                voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel09.wav"
                aki_Death"（笑顔）何考えてるの？ ここでは私が支配者、君に選択権はない。（表情変えて）その不満そうな顔、安易に命を棄てたからだよ"
            " ":
                
                voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel09.wav"
                aki_Death"（笑顔）何考えてるの？ ここでは私が支配者、君に選択権はない。（表情変えて）その不満そうな顔、安易に命を棄てたからだよ"

    
    show mir fire at left
    #（出现Q版MIr生气的表情）
    
    voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel10.wav"
    aki_Death"（汗）ごめん！ 冗談だよ。早く次へ進んで業務終わらせよう？ 終わったら君の好きにしていい、私も今日の仕事終わらせて休める" 
    menu:
            "謝れ！":
                
                voice"voice/Demo11/FerrisWheel/Mir_FerriSWheel08.wav"
                mir"（険）謝れ！！"
                
                voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel11.wav"
                aki_Death"（泣き）許して！ 早く終わらせないと残業代も減らされ、パフォーマンス評価下がって退職年齢に響く！ お願いだから許して"
                
                voice"voice/Demo11/FerrisWheel/Mir_FerrisWheel09.wav"
                mir"（得意）あなたをだましたのは、私に影響を与えることはありません。生きている人だけがこのような繁雑な束縛を受けなければなりません"
                
                voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel12.wav"
                aki_Death "（笑顔）嘘だよ、影響なんてない。生きてる人間だけがそんな形式に縛られる"
                
                voice"voice/Demo11/FerrisWheel/Mir_FerrisWheel00.wav"
                mir "誰もが死んだ後、あなたはおもちゃとしてあなたのこの程度の辱めと拷問を受けなければなりませんか？"
            "死神にもKPIと休憩があるの？":
                
                voice"voice/Demo11/FerrisWheel/Mir_FerrisWheel10.wav"
                mir "死神にもKPIと休憩があるの？"
                voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel13.wav"
                aki_Death "（汗笑顔）いい姉さん、ここは死後の世界、世界の果て。社畜ビルでも黒人奴隷鉱山でもない。"
                
                voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel14.wav"
                aki_Death"（得意）死神は1日2人対応、4時間勤務でOK！ "

    
    voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel15.wav"
    aki_Death "遊び飽きた！ そろそろ本気出す"
    
    voice"voice/Demo11/FerrisWheel/Aki_Death_FerrisWheel16.wav"
    aki_Death "次の目的地は！{nw=4}"
    
    scene bg_11_8 with dissolve:
        fit "contain"
    with dissolve
    
    play music"bgm/电磁白噪音.mp3"
    show aki_Death LowLight at right
    with dissolve
    show mir left at left
    with dissolve
    extend  "（眼神消失）次の目的地は映画館"
    
    
    voice"voice/Demo11/Theater/Aki_Death_Theater01.wav"
    aki_Death"（眼神消失）ここが終点、最後の場所。全ての死者が最終的にたどり着く。やりたいこと、見たいもの、何でもある。自分の人生、他人の人生、全て見られる。人生の段落を編集して、理想の人生を構成することも"
    show mir amazing at left
    
    voice"voice/Demo11/Theater/Mir_Theater_a.wav"
    mir "（汗）（心の声） 雰囲気が一変した...怖い......"
    
    voice"voice/Demo11/Theater/Mir_Theater_b.wav"
    mir "理想の人生を作れる？ さっきの「編集」って？"
    
    voice"voice/Demo11/Theater/Aki_Death_Theater02.wav"
    aki_Death "（眼神消失）物を切り貼りするように、想像通りの世界を縫い合わせられる。素材さえ見つければ望む修正が可能"
    
    voice"voice/Demo11/Theater/Mir_Theater_c.wav"
    mir "つまり...ここで全てを変えられる？ 果たせなかった願い、後悔した決断、選ばなかった道、縁のなかった人生...？"
    
    voice"voice/Demo11/Theater/Aki_Death_Theater03.wav"
    aki_Death "（眼神消失） 後者は全て体験できるが、何も変えられない。変えられるのは記憶だけ\nさあ、修正を始めなさい。自分を騙すのもいい、人生に完璧な終止符を打って。"
    
    voice"voice/Demo11/Theater/Mir_Theater_d.wav"
    mir "待って...あなたここが大嫌いそうね、さっきまで笑ってたのに、ここへ来たら急に...苦しそう。急かすような態度、嫌だ。やめて"
    #（故障转场特效，转场到Aki（Death）特写，之后不出现Aki（Death）立绘）

    scene bg_11_9 with dissolve:
        fit "contain"
    with dissolve
    show mir left at left
    
    voice"voice/Demo11/Theater/Aki_Death_Theater04.wav"
    aki_Death "すまない、ここへ来ると自然とこうなる。この終点が大嫌いだ。多くの者がここへ来ると修正に狂い、何かを取り戻そうとする"
    
    voice"voice/Demo11/Theater/Aki_Death_Theater05.wav"
    aki_Death "さっきも言った通り、ここで変えられるのは自分の記憶だけ――死後に自分を騙し、終わった人生に幕を引く。そして繰り返し眺め、私が口を挟めなくなるまで。彼らも知ってる、これは偽物だと"
    show mir amazing at left
    voice"voice/Demo11/Theater/Mir_Theater01.wav"
    mir "（驚き）偽物...？"
    
    voice"voice/Demo11/Theater/Aki_Death_Theater06.wav"
    aki_Death "そう、皆自分を騙して生きることに熱中する。死後の世界でも同じ過ちを繰り返し、この世界でも死んでいく。\n本当に孤独だ、ここへ連れて来ると、どんな関係を築いても私を置いていく"
    
    voice"voice/Demo11/Theater/Aki_Death_Theater07.wav"
    aki_Death "死ぬのは怖くない、死にきれないのが怖い。私は死ねない上に、彼らの死を何度も見届ける。彼らを受け入れ、導き、再び死ぬまで。まるで私が最初から存在しなかったように、自分が死ぬより辛い"
    
    voice"voice/Demo11/Theater/Aki_Death_Theater08.wav"
    aki_Death "第一にこの仕事が終わりなく続くこと、第二に無駄な努力ほど絶望的なものはない。できれば死神もやりたくない。でも選択肢はない。\n君と話せて楽しかった、全てに終わりがあるから。もう感覚麻痺してる、これ以上は無理。ご自由に"
    show mir left
    
    voice"voice/Demo11/Theater/Mir_Theater01.wav"
    mir "後悔はしてるけど、修正する必要ない。過去の記憶を弄るより、君の相手をした方がいい。君もずっと辛かったでしょ"
    
    scene bg_11_10 with dissolve:
        fit "contain"
    with dissolve

    # (Aki（Death）转头看向Mir）
    
    voice"voice/Demo11/Theater/Aki_Death_Theater09.wav"
    aki_Death "死んでまで不安定なこと言う...代わりに死神やる？ そうすれば私は本当に死ねる"
    
    voice"voice/Demo11/Theater/Mir_Theater03.wav"
    mir "死神は一人だけ？"
    
    voice"voice/Demo11/Theater/Aki_Death_Theater10.wav"
    aki_Death "死神はただ一人のみ存在する。これが残酷な定めだ。その役を担う者は、死者であれ、必ず孤独を強いられる。"
    
    voice"voice/Demo11/Theater/Mir_Theater04.wav"
    mir "お断り、シーシュポスの神話みたい。永遠に一人で無駄なことを"
    
    voice"voice/Demo11/Theater/Aki_Death_Theater11.wav"
    aki_Death "シーシュポス？ 岩を転がす？\nかつて「シーシュポスは幸福だと想像すべきだ」と言われた。彼は岩を転がすだけでなく、頂上へ登り続けることで、その過程自体が心を満たすと"
    
    voice"voice/Demo11/Theater/Aki_Death_Theater12.wav"
    aki_Death "馬鹿げてる、虚無で満たされた心が虚無じゃないと？"
    
    voice"voice/Demo11/Theater/Mir_Theater05.wav"
    mir "Akiに似てる、声も似てる、ただ性格はAkiよりずっと悪い。"
    
    voice"voice/Demo11/Theater/Aki_Death_Theater13.wav"
    aki_Death "（憂い）顔も声も似てれば十分じゃない？ 性格まで似せたら、私はAkiになれる。自分を変えず、君が自己欺瞞すれば、私をAkiと思える"
    
    voice"voice/Demo11/Theater/Aki_Death_Theater14.wav"
    aki_Death "その時、Akiへの愛を少し分けて？ 私を愛するのはAkiを愛するのと同じ？"
    
    scene bg_All_Black with dissolve:
        fit "contain"
    with dissolve

    scene bg_All_White with dissolve:
        fit "contain"
    with dissolve

    scene bg_11_9 with dissolve:
        fit "contain"
    with dissolve

    voice"voice/Demo11/Theater/Aki_Death_Theater15.wav"
    aki_Death "そろそろ時間みたいねごめんね、徹底的に騙しちゃった"
    
    voice"voice/Demo11/Theater/Aki_Death_Theater16.wav"
    aki_Death "実はあなたまだ死んでないわ、ただ今の状態が死んだも同然だから、遊びに誘っただけ。これが死神の特権だから"
    
    voice"voice/Demo11/Theater/Aki_Death_Theater17.wav"
    aki_Death "ほら、戻れって呼んでる。さっさと行きなさい"


    voice"voice/Demo11/Theater/Aki_Death_Theater18.wav"
    aki_Death "人生はまったくの駄作だ。最低最悪の映画だ"
    
    stop music fadeout 4.0


    scene Bg_Title with dissolve:
        fit "contain"
    with dissolve
    
    $ show_narration219("Chapter11,over")
    





    return