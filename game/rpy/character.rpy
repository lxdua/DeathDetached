
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

define aki = Character("Aki", callback=active, cb_name="Aki", color="#cecde5")
image aki1 = get_role_img("Aki", "images/role/Aki(instead).png")

define mir = Character("Mir", callback=active, cb_name="Mir", color="#ffe76f")
image mir1 = get_role_img("Mir", "images/role/Mir(instead).png")

define angel = Character("Angel", callback=active, cb_name="Angel", color="#ffffff")
image angel1 = "9004"

define angel = Character("Trigger", callback=active, cb_name="Trigger", color="#ee819e")
image angel1 = "9005"

define fringilla = Character("Fringilla", callback=active, cb_name="Fringilla", color="#a81e32")
image fringilla1 = "9006"

define luo = Character("Luo", callback=active, cb_name="Luo", color="#003153")
image luo1 = "9007"

