class BlockManLevels():

    def __init__(self):
        self.current_level = 0
        self.gravity = 0.3
        self.gravityDirection = 'down'

    levels = [[
        "PPPPPPPPPPPPPPPPPPPP",
        "P P                P",
        "P PC               P",
        "P PPPPPPPP  PPP  P P",
        "P   PP             P",
        "P   P              P",
        "P   P           PPPP",
        "P            PPPPPPP",
        "P         PPPPPPPPPP",
        "P      PPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPP"],

        [
        "PPPPPPPPPPPPPPPPPPPP",
        "P  C   PPPPPPPPPPPPP",
        "P PP   PPPPPPPPPPPPP",
        "P                  P",
        "P   P              P",
        "P            PP    P",
        "P      PPPP        P",
        "P      PPPP        P",
        "P      PPPP     P  P",
        "P                  P",
        "PPPPPPPPPPPPPPPPPPPP"],

        [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                            P",
        "P             PPPPPPP        PHHHHHHHHHHHHHHHHHHHHHHHHPPPPPP",
        "P          P                 F                             P",
        "P                        HHHHPHHHHHHHHHHHHHHHHHHHHHHHHP    P",
        "P           D                P                        P   CP",
        "PPPPP   PPPPPPPPPPPPP        P                        PPPPPP",
        "P                            P",
        "P                          C P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"],

        [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                            P",
        "P             PPPPPPP        P",
        "P          P                 p",
        "P                            P",
        "P           D                P",
        "PPPPP   PPPPPPPPPPPPP        P",
        "P                            P",
        "P                          C P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"],

        [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P P                          P",
        "P P    PPP          P      P P",
        "P P P       P    P     P   P P",
        "P P              P     P   P P",
        "P PP     D                 P P",
        "P P    PPPPPP             PP P",
        "P P   PPPPPPP  PPP    DP   P P",
        "P P   PPPPPPP  PPP PPPPPPPPP P",
        "P P PPPPPPPPP  PPP P         P",
        "P P      PPPP  PPP P         P",
        "P PP     PPPP  PPP P         P",
        "P  P        P  PPP P         P",
        "P   P       P      PP    PPPDP",
        "P    PPP    P  PPPPPPP  PPPPPP",
        "P    PP    PP  PPP       P   P",
        "P           P  PPP    PPPP   P",
        "P       P   P  PPP  D        P",
        "P     PPPD     PPP         C P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"],

    ]

    def levelTwo(self):
        self.gravity = 0.2
        self.gravityDirection = 'left'

    def level50(self):
        self.gravityDirection = 'right'


if __name__ == "__main__":
    print BlockManLevels.level_list