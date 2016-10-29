class BlockManLevels():

    def __init__(self):
        self.current_level = 8
        self.gravity = 0.15
        self.gravityDirection = 'down'

    levels = [[

        "HHHHH",
        "H   H",
        "H PFPPPPPPPPPPPPPP",
        "H P              P",
        "H PS             P",
        "H PPP          PCP",
        "H PPPPPPPPPPPPPPPP",
        "H H",
        "H H",
        "H H",
        "H H",
        "H HHHHHHHHHHHHHHHH",
        "H                H",
        "H                H",
        "H                H",
        "H       PWP      H",
        "HPPPPPPPPPPPPPPPP"],
        [
        "PPPPPPPPPPPPPPPPPPPP",
        "PSP                P",
        "P PCP              P",
        "P PPPPPPPP  PPP  P P",
        "P   P              P",
        "P   P              P",
        "P   P           PPPP",
        "P            PPPPPPP",
        "P         PPPPPPPPPP",
        "P      PPPPPPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPP"],

        [
        "PPPPPPPPPPPPPPPPPPPP",
        "PSPP               P",
        "P PP   PPPPPPPPPPPCP",
        "P                PPP",
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
        "PS          D                P                        PPPPWP",
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
        "P                                                        P",
        "P                                                        P",
        "P                                                        P",
        "P                                                 P      P",
        "P                                                 P      P",
        "P                                           P     P      P",
        "P   S                                P      P     P      P",
        "P   P                  P             P      P     P      P",
        "P   P     P      P     P        P    P      P     P    PCP",
        "PDDDPDDDDDPDDDDDDPDDDDDPDDDDDDDDPDDDDPDDDDDDPDDDDDPDDDDPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"],

        [
        "PPPPPPPPPPPPPPPPPPPPPHHHHHHH",
        "P        P         F       H",
        "P      P P         PHHHHHH H",
        "P     PP P         P     H H",
        "P    PPPCP        SP     H H",
        "PFPPPPPPPPPPPPPPPPPPHHHHHH H",
        "P                          H",
        "PPPPPPPPPPPPPPPPPPPPHHHHHHHH"],

        [

        "PPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "PPPPPPPPPCPPPPPPPPP        P",
        "PPPPPPPPP     PPPPP  PPP  PP",
        "PPPPPPP       PPP    PPP   P",
        "PPPPPP     PPPPD    PPPP   P",
        "PD         PW PD     PPD   P",
        "PD         P  PP     PPD   P",
        "PPPPP    H FFFPPP    PPP   P",
        "PD         FFFPPPP   PPP   P",
        "PD         PPPPPPPPP PPPP  P",
        "PPPPP     PP       P PP    P",
        "PPPP      PD   PPP P P     P",
        "PD        P    PPP P P   PPP",
        "PP             PPP   P    SP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPP"],

        [
        "      HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH",
        "     H                                                            H",
        "     H                                                            P",
        "     H                                                            P",
        "     H                                                            P",
        "     H                                                            P",
        "     H                                                            P",
        "     H                                                            P",
        "     H                                                            P",       
        "      PFPPPPPPPPPPPPPPPPPPPPP     PPP       PPP       PPP      PPPP",
        "      PFPPPPPDDDDDDDDDDDPPPPP                                     H",
        "      PFPPPP              PPP                                     H",
        "      PFP                   P                                     H",
        "      PFPC                  P                                     H",
        "      PFPPPPPPPPPPPPPPP     P                                     H",
        "      PFPPDDDDPPPPPPPPP     P                                     H",
        "      P      DPPPPPD  D    PPP                                    H",
        "      P      DPPD            P       HHHHHHHHHHHHHHHHHHHHHHHHHHHHH ",
        "      P      PD              P       H",
        "      DJDD   P               P       H",
        "PPPPPPDDDD   D             D P       H",
        "P            D        PPPPPPFFF      H",
        "P            D     PPPD P DPPPPPPPPPP",
        "P     DD   DDD    P DP      DDDDPPPPP",
        "P  DDDPPPPPPPPP  PP             DDPPP",
        "P                                 DPP",
        "P                                  DP",
        "P                S  PPPPP           P",
        "PPPPDDDDDDDDDDDDPPPP    H   P       P",
        "PPPPPPPPPPPPPPPP        H   P       P",
        "PPPPPPPPPPPPP           H   P       P",
        "PD  PPP   P             PPPPP      PP",
        "P                                   P",
        "P                                   P",
        "P             PPPPP                 P",
        "PP  PP   P                DD     PPPP",
        "P    P                   DPPDDDPP   P",
        "P    P               DPPPP  PPP     P",
        "P   PPF            DDP        P     P",
        "P    P           DDPP            PP P",
        "P    P          DPP             PPP P",
        "PPPFFP    F     P               PPP P",
        "PFFFPP          P               PPP P",
        "PFPPPP                          P   P",
        "PFPPPPPPPPPPPP  PPPPP          PPPPPP",
        "PFFFFFFFFFFFF  PPPPPPPDDDDDDDPPPPPPPP",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"],

        [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P   P                      P",
        "P   P                      P",
        "P   P                      P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPP"],

        [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "PPPPP                      P",
        "P   P                      P",
        "P   P                      P",
        "P                          P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPP"],

        [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPP"],

        [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPP"],

        [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "P                          P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPP"],

    ]

    def level_spex(self):
        if self.current_level == 0:
            self.spex_function(0.3, 'down')
        elif self.current_level == 1:
            self.spex_function(0.3, 'down')
        elif self.current_level == 2:
            self.spex_function(0.3, 'down')
        elif self.current_level == 3:
            self.spex_function(0.3, 'down')
        elif self.current_level == 4:
            self.spex_function(0.3, 'down')
        elif self.current_level == 5:
            self.spex_function(0.3, 'down')
        elif self.current_level == 6:
            self.spex_function(0.3, 'down')
        elif self.current_level == 7:
            self.spex_function(0.3, 'left')
        elif self.current_level == 8:
            self.spex_function(0.15, 'down')
        elif self.current_level == 9:
            self.spex_function(0.3, 'down')


    def spex_function(self, gravity, direction):
        self.gravity = gravity
        self.gravityDirection = direction

    def warp_instance(self):

        if self.current_level == 3:
            self.current_level = 5
        elif self.current_level == 0:
            self.current_level = 7
        elif self.current_level == 7:
            self.current_level = 20
        else:
            pass

    def little_warp(self):

        pass

        #block that warps you in the same level



if __name__ == "__main__":
    print BlockManLevels.level_list