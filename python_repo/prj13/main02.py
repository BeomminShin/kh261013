zoe_hp = 100
zoe_atk = 10

syndra_hp = 80
syndra_atk = 15


def zoe_attack():
    pass

def zoe_q():
    pass

def zoe_w():
    pass

def zoe_e():
    pass

def zoe_r():
    pass

def syndra_attack():
    pass

def syndra_q():
    pass

def syndra_w():
    pass

def syndra_e():
    pass

def syndra_r():
    pass

# zoe(atk) -> syndra
zoe_attack()
syndra_hp = syndra_hp - zoe_atk

# syndra(atk) -> zoe
syndra_attack()
syndra_atk = zoe_hp - syndra_atk


