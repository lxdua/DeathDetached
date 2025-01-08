
init python:

    renpy.image("u219", "images/other/219u.png")
    renpy.image("d219", "images/other/219d.png")

    def turn_219():
        _window_hide()
        #renpy.hide_screen("say")
        renpy.show("u219")
        renpy.show("d219")
        renpy.with_statement(dissolve)
    
    def turn_169():
        hide_narration219()
        renpy.hide("u219")
        renpy.hide("d219")
        renpy.with_statement(dissolve)

    def show_narration219(new_text):
        renpy.show_screen("narration219", text=new_text)
        renpy.pause()
    
    def hide_narration219():
        renpy.hide_screen("narration219")

screen narration219(text):
    text text:
        font "SourceHanSansLite.ttf"
        size 30
        color "#FFFFFF"
        xalign 0.5
        yalign 0.9