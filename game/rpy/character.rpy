
init python:

    current_speaker = None

    def active(event, name, interact=True, **kwargs):
        global current_speaker
        if not interact:
            return
        if event == "begin":
            current_speaker = name

    def get_role_img(role_name, img_path):
        return ConditionSwitch(
            "current_speaker == " + "'"+role_name+"'", img_path,
            "current_speaker != " + "'"+role_name+"'", ConditionSwitch(
                "current_speaker is None", img_path,
                "current_speaker is not None", im.MatrixColor(img_path, im.matrix.saturation(0.4) * im.matrix.brightness(-0.2))
                )
            )

define sp = Character("sp", callback=active, cb_name="sp", color="#cecde5")
image sp = get_role_img("sp", "images/role/2104_8.png")
image sp sword = get_role_img("sp", "images/role/2104_9.png")


define aki = Character("Aki", callback=active, cb_name="Aki", color="#cecde5")
image aki = get_role_img("Aki", "images/role/Aki(instead).png")
image aki 9004 = get_role_img("Aki", "images/role/9004.png")
image aki 9005 = get_role_img("Aki", "images/role/9005.png")

define mir = Character("Mir", callback=active, cb_name="Mir", color="#ffe76f")
image mir = get_role_img("Mir", "images/role/Mir(instead).png")

define angel = Character("Angel", callback=active, cb_name="Angel", color="#ffffff")
image angel = "9004"

define trigger = Character("Trigger", callback=active, cb_name="Trigger", color="#ee819e")
image trigger = "9005"

define fringilla = Character("Fringilla", callback=active, cb_name="Fringilla", color="#a81e32")
image fringilla = "9006"

define luo = Character("Luo", callback=active, cb_name="Luo", color="#003153")
image luo = "9007"

define mir_child = Character("Mir_child", callback=active, cb_name="Mir", color="#ffe76f")
image mir_child = get_role_img("Mir_child", "images/role/Child.png")

define mir_mother = Character("Mir_mother", callback=active, cb_name="Mir", color="#ffe76f")
image mir_mother = get_role_img("Mir_mother", "images/role/9009.png")

define shadow = Character("??", callback=active, cb_name="??", color="#ffe76f")
image shadow = get_role_img("??", "images/role/Shadow.png")