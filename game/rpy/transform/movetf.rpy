
transform nod:
    ease 0.1 yoffset 20
    ease 0.1 yoffset 0
    repeat

transform nod_once:
    ease 0.1 yoffset 20
    ease 0.1 yoffset 0

transform nod_once_slow:
    ease 0.2 yoffset 20
    ease 0.2 yoffset 0

transform shake:
    ease 0.1 xoffset -10
    ease 0.2 xoffset 0
    ease 0.1 xoffset 10
    ease 0.2 xoffset 0
    repeat

transform shake_once:
    ease 0.2 xoffset -10
    ease 0.3 xoffset 0
    ease 0.2 xoffset 10
    ease 0.3 xoffset 0

transform jump_once:
    ease 0.1 yoffset -100
    pause 0.02
    ease 0.1 yoffset 0
    ease 0.1 yoffset -50
    pause 0.02
    ease 0.1 yoffset 0