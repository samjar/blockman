class BlockManLevels():
    current_level = 0
    levels = [
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
	"P   C PPPD     PPP         C P",
	"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP"],
    [
    "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
    "P                            P",
    "p             PPPPPPP        P",
    "p          P                 p",
    "p                            p",
    "p           D                p",
    "PPPPP   PPPPPPPPPPPPP        p",
    "p                            p",
    "p                          E p",
    "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
    ]

if __name__ == "__main__":
    print BlockManLevels.level_list
