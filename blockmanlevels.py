class BlockManLevels():

    def __init__(self):
        self.current_level = 5
        self.gravity = 0.3
        self.gravityDirection = 'down'

    levels = [[
        "PPPPPPPPPPPPPPPPPPPP",
        "PSP                P",
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
        "PSPC   PPPPPPPPPPPPP",
        "P PP   PPPPPPPPPPPPP",
        "P                  P",
        "P   P              P",
        "P            PP    P",
        "P      PPPP        P",
        "P      PPPP        P",
        "P      PPPP     P  P",
        "P       M          P",
        "PPPPPPPPPPPPPPPPPPPP"],

        [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                            P",
        "P             PPPPPPP        PHHHHHHHHHHHHHHHHHHHHHHHHPPPPPP",
        "P          P                 F                             P",
        "P                        HHHHPHHHHHHHHHHHHHHHHHHHHHHHHP    P",
        "PS          D                P                        P   CP",
        "PPPPP   PPPPPPPPPPPPP        P                        PPPPPP",
        "P                            P",
        "P                         PCPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"],

        [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PSP                          P",
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
        "P           P  FFF    PPPP   P",
        "P       P   P  PPP  D        P",
        "P     PPPD     PPP        PCPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"],

        [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P   S                                                    P",
        "P                                                        P",
        "P                                                        P",
        "P                                                        P",
        "P                                                        P",
        "P                                                        P",
        "P                                                        P",
        "P                                                        P",
        "P                                                        P",
        "P                                                        P",
        "P                      C                                 P",
        "P   P                  P                                 P",
        "P   P     P      P     P                                 P",
        "PDDDPDDDDDPDDDDDDPDDDDDPDDDDDD                           P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"],

                [
        "PPPPPPPPPPPPPPPPPPPP",
        "PSPC   PPPPPPPPPPPPP",
        "P PP   PPPPPPPPPPPPP",
        "P                  P",
        "P   P              P",
        "P            PP    P",
        "P                  P",
        "P        P         P",
        "P    P          P  P",
        "P       M          P",
        "PPPPPPPPPPPPPPPPPPPP"],

                [
        "PPPPPPPPPPPPPPPPPPPP",
        "PS          P      P",
        "P  P               P",
        "P                  P",
        "P   P              P",
        "P            PP    P",
        "P      PPPP        P",
        "P      PC          P",
        "P      PPPP     P  P",
        "P       M          P",
        "PPPPPPPPPPPPPPPPPPPP"],

                [
        "PPPPPPPPPPPPPPPPPPPP",
        "PSPC   PPPPPPPPPPPPP",
        "P PP   PPPPPPPPPPPPP",
        "P                  P",
        "P   P              P",
        "P            PP    P",
        "P      PPPP        P",
        "P      PPPP        P",
        "P      PPPP     P  P",
        "P       M          P",
        "PPPPPPPPPPPPPPPPPPPP"],



    ]

    def levelTwo(self):
        self.gravity = 0.2
        self.gravityDirection = 'left'

    def level50(self):
        self.gravityDirection = 'right'


if __name__ == "__main__":
    print BlockManLevels.level_list