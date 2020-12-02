from migen.build.generic_platform import *
from migen.build.xilinx import XilinxPlatform


_io = [
    ("user_led", 0, Pins("AF19"), IOStandard("LVCMOS25")),
    ("user_led", 1, Pins("AF23"), IOStandard("LVCMOS25")),

    ("serial", 0,
        Subsignal("tx", Pins("Y18")),
        Subsignal("rx", Pins("AA18")),
        IOStandard("LVCMOS25"),
    ),

    ("sma_clkin", 0,
        Subsignal("p", Pins("AD20")),
        Subsignal("n", Pins("AD21")),
        IOStandard("LVCMOS25"), Misc("DIFF_TERM=TRUE")
    ),

    ("clk_gtp", 0,
        Subsignal("p", Pins("R6")),
        Subsignal("n", Pins("R5")),
    ),

    ("clk125_gtp", 0,
        Subsignal("p", Pins("U6")),
        Subsignal("n", Pins("U5")),
    ),

    ("sfp", 0,
        Subsignal("txp", Pins("AA2")),
        Subsignal("txn", Pins("AA1")),
        Subsignal("rxp", Pins("AB4")),
        Subsignal("rxn", Pins("AB3")),
    ),

    ("sfp", 1,
        Subsignal("txp", Pins("W2")),
        Subsignal("txn", Pins("W1")),
        Subsignal("rxp", Pins("Y4")),
        Subsignal("rxn", Pins("Y3")),
    ),

    ("sfp", 2,
        Subsignal("txp", Pins("U2")),
        Subsignal("txn", Pins("U1")),
        Subsignal("rxp", Pins("V4")),
        Subsignal("rxn", Pins("V3")),
    ),

    ("sfp", 3,
        Subsignal("txp", Pins("R2")),
        Subsignal("txn", Pins("R1")),
        Subsignal("rxp", Pins("T4")),
        Subsignal("rxn", Pins("T3")),
    ),

    ("cdr_clk", 0,
        Subsignal("p", Pins("G7")),
        Subsignal("n", Pins("F7")),
        IOStandard("LVDS_18"),
    ),
    ("cdr_clk_clean_fabric", 0,
        Subsignal("p", Pins("AD23")),
        Subsignal("n", Pins("AD24")),
        IOStandard("LVDS_25"),
    ),
    ("ddmtd_main_dcxo_i2c", 0,
        Subsignal("scl", Pins("AE22")),
        Subsignal("sda", Pins("AF22")),
        IOStandard("LVCMOS25")
    ),
    ("ddmtd_helper_dcxo_i2c", 0,
        Subsignal("scl", Pins("AC26")),
        Subsignal("sda", Pins("AB26")),
        IOStandard("LVCMOS25")
    ),
    ("ddmtd_helper_clk", 0,
        Subsignal("p", Pins("AC23")),
        Subsignal("n", Pins("AC24")),
        IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
    ),
]

_connectors_eem = [
    ("eem0", {
        "d0_n": "AD14",
        "d0_p": "AC14",
        "d1_n": "AF17",
        "d1_p": "AE17",
        "d2_n": "AA17",
        "d2_p": "Y17",
        "d3_n": "AB16",
        "d3_p": "AB17",
        "d4_n": "AC16",
        "d4_p": "AC17",
        "d5_n": "AD15",
        "d5_p": "AD16",
        "d6_n": "Y15",
        "d6_p": "Y16",
        "d7_n": "W15",
        "d7_p": "W16",
    }),
    ("eem1", {
        "d0_n": "AC22",
        "d0_p": "AC21",
        "d1_n": "AD26",
        "d1_p": "AD25",
        "d2_n": "AF25",
        "d2_p": "AF24",
        "d3_n": "AB22",
        "d3_p": "AB21",
        "d4_n": "AB25",
        "d4_p": "AA25",
        "d5_n": "AC19",
        "d5_p": "AC18",
        "d6_n": "AB19",
        "d6_p": "AA19",
        "d7_n": "W19",
        "d7_p": "W18",
    }),
    ("eem2", {
        "d0_n": "H14",
        "d0_p": "J14",
        "d1_n": "D16",
        "d1_p": "E16",
        "d2_n": "A17",
        "d2_p": "B17",
        "d3_n": "C16",
        "d3_p": "C17",
        "d4_n": "B15",
        "d4_p": "B16",
        "d5_n": "G15",
        "d5_p": "G16",
        "d6_n": "B14",
        "d6_p": "C14",
        "d7_n": "A14",
        "d7_p": "A15",
    }),
    ("eem3", {
        "d0_n": "E15",
        "d0_p": "F15",
        "d1_n": "J15",
        "d1_p": "K15",
        "d2_n": "C13",
        "d2_p": "D13",
        "d2_p": "G14",
        "d3_n": "A12",
        "d3_p": "A13",
        "d4_n": "B12",
        "d4_p": "C12",
        "d5_n": "E12",
        "d5_p": "F12",
        "d6_n": "D11",
        "d6_p": "E11",
        "d7_n": "D10",
        "d7_p": "E10",
    }),
    ("eem4", {
        "d0_n": "D14",
        "d0_p": "D15",
        "d1_n": "F14",
        "d2_n": "E13",
        "d2_p": "F13",
        "d3_n": "G11",
        "d3_p": "G12",
        "d4_n": "H12",
        "d4_p": "H13",
        "d5_n": "J13",
        "d5_p": "K13",
        "d6_n": "B11",
        "d6_p": "C11",
        "d7_n": "F10",
        "d7_p": "G10",
    }),
    ("eem5", {
        "d0_n": "E7",
        "d0_p": "F8",
        "d1_n": "A10",
        "d1_p": "B10",
        "d2_n": "H8",
        "d2_p": "J8",
        "d3_n": "A8",
        "d3_p": "A9",
        "d4_n": "D5",
        "d4_p": "E6",
        "d5_n": "E5",
        "d5_p": "F5",
        "d6_n": "G5",
        "d6_p": "G6",
        "d7_n": "H6",
        "d7_p": "H7",
    }),
    ("eem6", {
        "d0_n": "C6",
        "d0_p": "D6",
        "d1_n": "A7",
        "d1_p": "B7",
        "d2_n": "B4",
        "d2_p": "B5",
        "d3_n": "C3",
        "d3_p": "C4",
        "d4_n": "A5",
        "d4_p": "B6",
        "d5_n": "A3",
        "d5_p": "A4",
        "d6_n": "B1",
        "d6_p": "C2",
        "d7_n": "A2",
        "d7_p": "B2",
    }),
    ("eem7", {
        "d0_n": "K3",
        "d0_p": "L3",
        "d1_n": "D3",
        "d1_p": "D4",
        "d2_n": "F2",
        "d2_p": "G2",
        "d3_n": "C1",
        "d3_p": "D1",
        "d4_n": "E1",
        "d4_p": "E2",
        "d5_n": "E3",
        "d5_p": "F3",
        "d6_n": "H1",
        "d6_p": "J1",
        "d7_n": "H3",
        "d7_p": "H4",
    }),
    ("eem8", {
        "d0_n": "AD11",
        "d0_p": "AC12",
        "d1_n": "AC11",
        "d1_p": "AB12",
        "d2_n": "AA10",
        "d2_p": "Y10",
        "d3_n": "AB10",
        "d3_p": "AB11",
        "d4_n": "Y13",
        "d4_p": "W13",
        "d5_n": "AA12",
        "d5_p": "AA13",
        "d6_n": "Y11",
        "d6_p": "Y12",
        "d7_n": "AE15",
        "d7_p": "AE16",
    }),
    ("eem9", {
        "d0_n": "AD13",
        "d0_p": "AC13",
        "d1_n": "AF13",
        "d1_p": "AE13",
        "d2_n": "AD10",
        "d2_p": "AE10",
        "d3_n": "AF12",
        "d3_p": "AE12",
        "d4_n": "AF10",
        "d4_p": "AE11",
        "d5_n": "AB14",
        "d5_p": "AB15",
        "d6_n": "AA14",
        "d6_p": "AA15",
        "d7_n": "AF14",
        "d7_p": "AF15",
    }),
    ("eem10", {
        "d0_n": "J3",
        "d0_p": "J4",
        "d1_n": "G1",
        "d1_p": "H2",
        "d2_n": "K1",
        "d2_p": "K2",
        "d3_n": "F4",
        "d3_p": "G4",
        "d4_n": "M4",
        "d4_p": "N4",
        "d5_n": "L4",
        "d5_p": "L5",
        "d6_n": "N2",
        "d6_p": "N3",
        "d7_n": "L2",
        "d7_p": "M2",
    }),
    ("eem11", {
        "d0_n": "M5",
        "d0_p": "M6",
        "d1_n": "M1",
        "d1_p": "N1",
        "d2_n": "L7",
        "d2_p": "M7",
        "d3_n": "J5",
        "d3_p": "K5",
        "d4_n": "L8",
        "d4_p": "M8",
        "d5_n": "J6",
        "d5_p": "K6",
        "d6_n": "N6",
        "d6_p": "N7",
        "d7_n": "K7",
        "d7_p": "K8",
    }),
]

class Platform(XilinxPlatform):
    def __init__(self):
        XilinxPlatform.__init__(self, "xc7z030-ffg676-2", _io, _connectors_eem,
            toolchain="vivado")
