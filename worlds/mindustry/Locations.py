from BaseClasses import Location
from worlds.mindustry.Shared import MINDUSTRY_BASE_ID

class MindustryLocation(Location):
    """
    Class for a Mindustry Location
    """
    name: str = "Mindustry"

    def __init__(self, player: int, name="", code=None, parent=None) -> None:
        """
        Initialisation of the object
        :param player: the ID of the player
        :param name: the name of the location
        :param code: the ID (or address) of the location (Event if None)
        :param parent: the Region that this location belongs to
        """
        super(MindustryLocation, self).__init__(player, name, code, parent)
        self.event = code is None

class MindustryLocations:

    #serpulo_conveyor = {
    #    "Node Conveyor": MINDUSTRY_BASE_ID + 0,
    #}
    serpulo_junction = {
        "AP-S-01-02": MINDUSTRY_BASE_ID + 1,
    }
    serpulo_router = {
        "AP-S-01-03": MINDUSTRY_BASE_ID + 2,
    }
    serpulo_launch_pad = {
        "AP-S-01-04": MINDUSTRY_BASE_ID + 3,
    }
    serpulo_distributor = {
        "AP-S-01-05": MINDUSTRY_BASE_ID + 4,
    }
    serpulo_sorter = {
        "AP-S-01-06": MINDUSTRY_BASE_ID + 5,
    }
    serpulo_inverted_sorter = {
        "AP-S-01-07": MINDUSTRY_BASE_ID + 6,
    }
    serpulo_overflow_gate = {
        "AP-S-01-08": MINDUSTRY_BASE_ID + 7,
    }
    serpulo_underflow_gate = {
        "AP-S-01-09": MINDUSTRY_BASE_ID + 8,
    }
    serpulo_container = {
        "AP-S-01-10": MINDUSTRY_BASE_ID + 9,
    }
    serpulo_unloader = {
        "AP-S-01-11": MINDUSTRY_BASE_ID + 10,
    }
    serpulo_vault = {
        "AP-S-01-12": MINDUSTRY_BASE_ID + 11,
    }
    serpulo_bridge_conveyor = {
        "AP-S-01-13": MINDUSTRY_BASE_ID + 12,
    }
    serpulo_titanium_conveyor = {
        "AP-S-01-14": MINDUSTRY_BASE_ID + 13,
    }
    serpulo_phase_conveyor = {
        "AP-S-01-15": MINDUSTRY_BASE_ID + 14,
    }
    serpulo_mass_driver = {
        "AP-S-01-16": MINDUSTRY_BASE_ID + 15,
    }
    serpulo_payload_conveyor = {
        "AP-S-01-17": MINDUSTRY_BASE_ID + 16,
    }
    serpulo_payload_router = {
        "AP-S-01-18": MINDUSTRY_BASE_ID + 17,
    }
    serpulo_armored_conveyor = {
        "AP-S-01-19": MINDUSTRY_BASE_ID + 18,
    }
    serpulo_plastanium_conveyor = {
        "AP-S-01-20": MINDUSTRY_BASE_ID + 19,
    }
    serpulo_core_foundation = {
        "AP-S-02-01": MINDUSTRY_BASE_ID + 20,
    }
    serpulo_core_nucleus = {
        "AP-S-02-02": MINDUSTRY_BASE_ID + 21,
    }
    #serpulo_mechanical_drill = {
    #    "Node Mechanical Drill": MINDUSTRY_BASE_ID + 22,
    #}
    serpulo_mechanical_pump = {
        "AP-S-03-02": MINDUSTRY_BASE_ID + 23,
    }
    serpulo_conduit = {
        "AP-S-03-03": MINDUSTRY_BASE_ID + 24,
    }
    serpulo_liquid_junction = {
        "AP-S-03-04": MINDUSTRY_BASE_ID + 25,
    }
    serpulo_liquid_router = {
        "AP-S-03-05": MINDUSTRY_BASE_ID + 26,
    }
    serpulo_liquid_container = {
        "AP-S-03-06": MINDUSTRY_BASE_ID + 27,
    }
    serpulo_liquid_tank = {
        "AP-S-03-07": MINDUSTRY_BASE_ID + 28,
    }
    serpulo_bridge_conduit = {
        "AP-S-03-08": MINDUSTRY_BASE_ID + 29,
        }
    serpulo_pulse_conduit = {
        "AP-S-03-09": MINDUSTRY_BASE_ID + 30,
        }
    serpulo_phase_conduit = {
        "AP-S-03-10": MINDUSTRY_BASE_ID + 31,
    }
    serpulo_plated_conduit = {
        "AP-S-03-11": MINDUSTRY_BASE_ID + 32,
    }
    serpulo_rotary_pump = {
        "AP-S-03-12": MINDUSTRY_BASE_ID + 33,
    }
    serpulo_impulse_pump = {
        "AP-S-03-13": MINDUSTRY_BASE_ID + 34,
    }
    serpulo_graphite_press = {
        "AP-S-03-14": MINDUSTRY_BASE_ID + 35,
    }
    serpulo_pneumatic_drill = {
        "AP-S-03-15": MINDUSTRY_BASE_ID + 36,
    }
    serpulo_cultivator = {
        "AP-S-03-16": MINDUSTRY_BASE_ID + 37,
    }
    serpulo_laser_drill = {
        "AP-S-03-17": MINDUSTRY_BASE_ID + 38,
    }
    serpulo_airblast_drill = {
        "AP-S-03-18": MINDUSTRY_BASE_ID + 39,
    }
    serpulo_water_extractor = {
        "AP-S-03-19": MINDUSTRY_BASE_ID + 40,
    }
    serpulo_oil_extractor = {
        "AP-S-03-20": MINDUSTRY_BASE_ID + 41,
    }
    serpulo_pyratite_mixer = {
        "AP-S-03-21": MINDUSTRY_BASE_ID + 42,
    }
    serpulo_blast_mixer = {
        "AP-S-03-22": MINDUSTRY_BASE_ID + 43,
    }
    serpulo_silicon_smelter = {
        "AP-S-03-23": MINDUSTRY_BASE_ID + 44,
    }
    serpulo_spore_press = {
        "AP-S-03-24": MINDUSTRY_BASE_ID + 45,
    }
    serpulo_coal_centrifuge = {
        "AP-S-03-25": MINDUSTRY_BASE_ID + 46,
    }
    serpulo_multi_press = {
        "AP-S-03-26": MINDUSTRY_BASE_ID + 47,
    }
    serpulo_silicon_crucible = {
        "AP-S-03-27": MINDUSTRY_BASE_ID + 48,
    }
    serpulo_plastanium_compressor = {
        "AP-S-03-28": MINDUSTRY_BASE_ID + 49,
    }
    serpulo_phase_weaver = {
        "AP-S-03-29": MINDUSTRY_BASE_ID + 50,
    }
    serpulo_kiln = {
        "AP-S-03-30": MINDUSTRY_BASE_ID + 51,
    }
    serpulo_pulveriser = {
        "AP-S-03-31": MINDUSTRY_BASE_ID + 52,
    }
    serpulo_incinerator = {
        "AP-S-03-32": MINDUSTRY_BASE_ID + 53,
    }
    serpulo_melter = {
        "AP-S-03-33": MINDUSTRY_BASE_ID + 54,
    }
    serpulo_surge_smelter = {
        "AP-S-03-34": MINDUSTRY_BASE_ID + 55,
    }
    serpulo_separator = {
        "AP-S-03-35": MINDUSTRY_BASE_ID + 56,
    }
    serpulo_disassembler = {
        "AP-S-03-36": MINDUSTRY_BASE_ID + 57,
    }
    serpulo_cryofluid_mixer = {
        "AP-S-03-37": MINDUSTRY_BASE_ID + 58,
    }
    serpulo_micro_processor = {
        "AP-S-03-38": MINDUSTRY_BASE_ID + 59,
    }
    serpulo_switch = {
        "AP-S-03-39": MINDUSTRY_BASE_ID + 60,
    }
    serpulo_message = {
        "AP-S-03-40": MINDUSTRY_BASE_ID + 61,
    }
    serpulo_logic_display = {
        "AP-S-03-41": MINDUSTRY_BASE_ID + 62,
    }
    serpulo_large_logic_display = {
        "AP-S-03-42": MINDUSTRY_BASE_ID + 63,
    }
    serpulo_memory_cell = {
        "AP-S-03-43": MINDUSTRY_BASE_ID + 64,
    }
    serpulo_memory_bank = {
        "AP-S-03-44": MINDUSTRY_BASE_ID + 65,
    }
    serpulo_logic_processor = {
        "AP-S-03-45": MINDUSTRY_BASE_ID + 66,
    }
    serpulo_hyper_processor = {
        "AP-S-03-46": MINDUSTRY_BASE_ID + 67,
    }
    serpulo_illuminator = {
        "AP-S-03-47": MINDUSTRY_BASE_ID + 68,
    }
    serpulo_combustion_generator = {
        "AP-S-03-48": MINDUSTRY_BASE_ID + 69,
    }
    serpulo_power_node = {
        "AP-S-03-49": MINDUSTRY_BASE_ID + 70,
    }
    serpulo_large_power_node = {
        "AP-S-03-50": MINDUSTRY_BASE_ID + 71,
    }
    serpulo_battery_diode = {
        "AP-S-03-51": MINDUSTRY_BASE_ID + 72,
    }
    serpulo_surge_tower = {
        "AP-S-03-52": MINDUSTRY_BASE_ID + 73,
    }
    serpulo_battery = {
        "AP-S-03-53": MINDUSTRY_BASE_ID + 74,
    }
    serpulo_large_battery = {
        "AP-S-03-54": MINDUSTRY_BASE_ID + 75,
    }
    serpulo_mender = {
        "AP-S-03-55": MINDUSTRY_BASE_ID + 76,
    }
    serpulo_mend_projector = {
        "AP-S-03-56": MINDUSTRY_BASE_ID + 77,
    }
    serpulo_force_projector = {
        "AP-S-03-57": MINDUSTRY_BASE_ID + 78,
    }
    serpulo_overdrive_projector = {
        "AP-S-03-58": MINDUSTRY_BASE_ID + 79,
    }
    serpulo_overdrive_dome = {
        "AP-S-03-59": MINDUSTRY_BASE_ID + 80,
    }
    serpulo_repair_point = {
        "AP-S-03-60": MINDUSTRY_BASE_ID + 81,
    }
    serpulo_repair_turret = {
        "AP-S-03-61": MINDUSTRY_BASE_ID + 82,
    }
    serpulo_steam_generator = {
        "AP-S-03-62": MINDUSTRY_BASE_ID + 83,
    }
    serpulo_thermal_generator = {
        "AP-S-03-63": MINDUSTRY_BASE_ID + 84,
    }
    serpulo_differential_generator = {
        "AP-S-03-64": MINDUSTRY_BASE_ID + 85,
    }
    serpulo_thorium_reactor = {
        "AP-S-03-65": MINDUSTRY_BASE_ID + 86,
    }
    serpulo_impact_reactor = {
        "AP-S-03-66": MINDUSTRY_BASE_ID + 87,
    }
    serpulo_rtg_generator = {
        "AP-S-03-67": MINDUSTRY_BASE_ID + 88,
    }
    serpulo_solar_panel = {
        "AP-S-03-68": MINDUSTRY_BASE_ID + 89,
    }
    serpulo_large_solar_panel = {
        "AP-S-03-69": MINDUSTRY_BASE_ID + 90,
    }
    #serpulo_duo = {
    #    "Node Duo": MINDUSTRY_BASE_ID + 91,
    #}
    #serpulo_copper_wall = {
    #    "Node Copper Wall": MINDUSTRY_BASE_ID + 92,
    #}
    serpulo_large_copper_wall = {
        "AP-S-04-03": MINDUSTRY_BASE_ID + 93,
    }
    serpulo_titanium_wall = {
        "AP-S-04-04": MINDUSTRY_BASE_ID + 94,
    }
    serpulo_large_titanium_wall = {
        "AP-S-04-05": MINDUSTRY_BASE_ID + 95,
    }
    serpulo_door = {
        "AP-S-04-06": MINDUSTRY_BASE_ID + 96,
    }
    serpulo_large_door = {
        "AP-S-04-07": MINDUSTRY_BASE_ID + 97,
    }
    serpulo_plastanium_wall = {
        "AP-S-04-08": MINDUSTRY_BASE_ID + 98,
    }
    serpulo_large_plastanium_wall = {
        "AP-S-04-09": MINDUSTRY_BASE_ID + 99,
    }
    serpulo_thorium_wall = {
        "AP-S-04-10": MINDUSTRY_BASE_ID + 100,
    }
    serpulo_large_thorium_wall = {
        "AP-S-04-11": MINDUSTRY_BASE_ID + 101,
    }
    serpulo_surge_wall = {
        "AP-S-04-12": MINDUSTRY_BASE_ID + 102,
    }
    serpulo_large_surge_wall = {
        "AP-S-04-13": MINDUSTRY_BASE_ID + 103,
    }
    serpulo_phase_wall = {
        "AP-S-04-14": MINDUSTRY_BASE_ID + 104,
    }
    serpulo_large_phase_wall = {
        "AP-S-04-15": MINDUSTRY_BASE_ID + 105,
    }
    #serpulo_scatter = {
    #    "Node Scatter": MINDUSTRY_BASE_ID + 106,
    #}
    serpulo_hail = {
        "AP-S-04-17": MINDUSTRY_BASE_ID + 107,
    }
    serpulo_salvo = {
        "AP-S-04-18": MINDUSTRY_BASE_ID + 108,
    }
    serpulo_swarmer = {
        "AP-S-04-19": MINDUSTRY_BASE_ID + 109,
    }
    serpulo_cyclone = {
        "AP-S-04-20": MINDUSTRY_BASE_ID + 110,
    }
    serpulo_spectre = {
        "AP-S-04-21": MINDUSTRY_BASE_ID + 111,
    }
    serpulo_ripple = {
        "AP-S-04-22": MINDUSTRY_BASE_ID + 112,
    }
    serpulo_fuse = {
        "AP-S-04-23": MINDUSTRY_BASE_ID + 113,
    }
    serpulo_scorch = {
        "AP-S-04-24": MINDUSTRY_BASE_ID + 114,
    }
    serpulo_arc = {
        "AP-S-04-25": MINDUSTRY_BASE_ID + 115,
    }
    serpulo_wave = {
        "AP-S-04-26": MINDUSTRY_BASE_ID + 116,
    }
    serpulo_parallax = {
        "AP-S-04-27": MINDUSTRY_BASE_ID + 117,
    }
    serpulo_segment = {
        "AP-S-04-28": MINDUSTRY_BASE_ID + 118,
    }
    serpulo_tsunami = {
        "AP-S-04-29": MINDUSTRY_BASE_ID + 119,
    }
    serpulo_lancer = {
        "AP-S-04-30": MINDUSTRY_BASE_ID + 120,
    }
    serpulo_meltdown = {
        "AP-S-04-31": MINDUSTRY_BASE_ID + 121,
    }
    serpulo_foreshadow = {
        "AP-S-04-32": MINDUSTRY_BASE_ID + 122,
    }
    serpulo_shock_mine = {
        "AP-S-04-33": MINDUSTRY_BASE_ID + 123,
    }
    serpulo_ground_factory = {
        "AP-S-05-01": MINDUSTRY_BASE_ID + 124,
    }
    serpulo_dagger = {
        "AP-S-05-02": MINDUSTRY_BASE_ID + 125,
    }
    serpulo_mace = {
        "AP-S-05-03": MINDUSTRY_BASE_ID + 126,
    }
    serpulo_fortress = {
        "AP-S-05-04": MINDUSTRY_BASE_ID + 127,
    }
    serpulo_scepter = {
        "AP-S-05-05": MINDUSTRY_BASE_ID + 128,
    }
    serpulo_reign = {
        "AP-S-05-06": MINDUSTRY_BASE_ID + 129,
    }
    serpulo_nova = {
        "AP-S-05-07": MINDUSTRY_BASE_ID + 130,
    }
    serpulo_pulsar = {
        "AP-S-05-08": MINDUSTRY_BASE_ID + 131,
    }
    serpulo_quasar = {
        "AP-S-05-09": MINDUSTRY_BASE_ID + 132,
    }
    serpulo_vela = {
        "AP-S-05-10": MINDUSTRY_BASE_ID + 133,
    }
    serpulo_corvus = {
        "AP-S-05-11": MINDUSTRY_BASE_ID + 134,
    }
    serpulo_crawler = {
        "AP-S-05-12": MINDUSTRY_BASE_ID + 135,
    }
    serpulo_atrax = {
        "AP-S-05-13": MINDUSTRY_BASE_ID + 136,
    }
    serpulo_spiroct = {
        "AP-S-05-14": MINDUSTRY_BASE_ID + 137,
    }
    serpulo_arkyid = {
        "AP-S-05-15": MINDUSTRY_BASE_ID + 138,
    }
    serpulo_toxopid = {
        "AP-S-05-16": MINDUSTRY_BASE_ID + 139,
    }
    serpulo_air_factory = {
        "AP-S-05-17": MINDUSTRY_BASE_ID + 140,
    }
    serpulo_flare = {
        "AP-S-05-18": MINDUSTRY_BASE_ID + 141,
    }
    serpulo_horizon = {
        "AP-S-05-19": MINDUSTRY_BASE_ID + 142,
    }
    serpulo_zenith = {
        "AP-S-05-20": MINDUSTRY_BASE_ID + 143,
    }
    serpulo_antumbra = {
        "AP-S-05-21": MINDUSTRY_BASE_ID + 144,
    }
    serpulo_eclipse = {
        "AP-S-05-22": MINDUSTRY_BASE_ID + 145,
    }
    serpulo_mono = {
        "AP-S-05-23": MINDUSTRY_BASE_ID + 146,
    }
    serpulo_poly = {
        "AP-S-05-24": MINDUSTRY_BASE_ID + 147,
    }
    serpulo_mega = {
        "AP-S-05-25": MINDUSTRY_BASE_ID + 148,
    }
    serpulo_quad = {
        "AP-S-05-26": MINDUSTRY_BASE_ID + 149,
    }
    serpulo_oct = {
        "AP-S-05-27": MINDUSTRY_BASE_ID + 150,
    }
    serpulo_naval_factory = {
        "AP-S-05-28": MINDUSTRY_BASE_ID + 151,
    }
    serpulo_risso = {
        "AP-S-05-29": MINDUSTRY_BASE_ID + 152,
    }
    serpulo_minke = {
        "AP-S-05-30": MINDUSTRY_BASE_ID + 153,
    }
    serpulo_bryde = {
        "AP-S-05-31": MINDUSTRY_BASE_ID + 154,
    }
    serpulo_sei = {
        "AP-S-05-32": MINDUSTRY_BASE_ID + 155,
    }
    serpulo_omura = {
        "AP-S-05-33": MINDUSTRY_BASE_ID + 156,
    }
    serpulo_retusa = {
        "AP-S-05-34": MINDUSTRY_BASE_ID + 157,
    }
    serpulo_oxynoe = {
        "AP-S-05-35": MINDUSTRY_BASE_ID + 158,
    }
    serpulo_cyerce = {
        "AP-S-05-36": MINDUSTRY_BASE_ID + 159,
    }
    serpulo_aegires = {
        "AP-S-05-37": MINDUSTRY_BASE_ID + 160,
    }
    serpulo_navanax = {
        "AP-S-05-38": MINDUSTRY_BASE_ID + 161,
    }
    serpulo_additive_reconstructor = {
        "AP-S-05-39": MINDUSTRY_BASE_ID + 162,
    }
    serpulo_multiplicative_reconstructor = {
        "AP-S-05-40": MINDUSTRY_BASE_ID + 163,
    }
    serpulo_exponential_reconstructor = {
        "AP-S-06-41": MINDUSTRY_BASE_ID + 164,
    }
    serpulo_tetrative_reconstructor = {
        "AP-S-05-42": MINDUSTRY_BASE_ID + 165,
    }
    #serpulo_frozen_forest = {
    #    "Node Frozen Forest": MINDUSTRY_BASE_ID + 166,
    #}
    #serpulo_the_craters = {
    #    "Node The Craters": MINDUSTRY_BASE_ID + 167,
    #}
    #serpulo_ruinous_shores = {
    #    "Node Ruinous Shores": MINDUSTRY_BASE_ID + 168,
    #}
    #serpulo_windswept_islands = {
    #    "Node Windswept Islands": MINDUSTRY_BASE_ID + 169,
    #}
    #serpulo_tar_fields = {
    #    "Node Tar Fields": MINDUSTRY_BASE_ID + 170,
    #}
    #serpulo_impact_0078 = {
    #    "Node Impact 0078": MINDUSTRY_BASE_ID + 171,
    #}
    #serpulo_desolate_rift = {
    #    "Node Desolate Rift": MINDUSTRY_BASE_ID + 172,
    #}
    #serpulo_planetary_launch_terminal = {
    #    "Node Planetary Launch Terminal": MINDUSTRY_BASE_ID + 173,
    #}
    #serpulo_extraction_outpost = {
    #    "Node Extraction Outpost": MINDUSTRY_BASE_ID + 174,
    #}
    #serpulo_salt_flats = {
    #    "Node Slat Flats": MINDUSTRY_BASE_ID + 175,
    #}
    #serpulo_coastline = {
    #    "Node Coastline": MINDUSTRY_BASE_ID + 176,
    #}
    #serpulo_naval_fortress = {
    #    "Node Naval Fortress": MINDUSTRY_BASE_ID + 177,
    #}
    #serpulo_overgrowth = {
    #    "Node Overgrowth": MINDUSTRY_BASE_ID + 178,
    #}
    #serpulo_biomass_synthesis_facility = {
    #    "Node Biomass Synthesis Facility": MINDUSTRY_BASE_ID + 179,
    #}
    #serpulo_stained_mountains = {
    #    "Node Stained Mountains": MINDUSTRY_BASE_ID + 180,
    #}
    #serpulo_fungal_pass = {
    #    "Node Fungal Pass": MINDUSTRY_BASE_ID + 181,
    #}
    #serpulo_nuclear_production_complex = {
    #    "Node Nuclear Production Complex": MINDUSTRY_BASE_ID + 182,
    #}
    #serpulo_lead = {
    #    "Node Lead": MINDUSTRY_BASE_ID + 183,
    #}
    #serpulo_titanium = {
    #    "Node Titanium": MINDUSTRY_BASE_ID + 184,
    #}
    #serpulo_cryofluid = {
    #    "Node Cryofluid": MINDUSTRY_BASE_ID + 185,
    #}
    #all_thorium = {
    #    "Node Thorium": MINDUSTRY_BASE_ID + 186,
    #}
    #all_surge_alloy = {
    #    "Node Surge Alloy": MINDUSTRY_BASE_ID + 187,
    #}
    #all_phase_fabric = {
    #    "Node Phase Fabric": MINDUSTRY_BASE_ID + 188,
    #}
    #serpulo_metaglass = {
    #    "Node Metaglass": MINDUSTRY_BASE_ID + 189,
    #}
    #serpulo_scrap = {
    #    "Node Scrap": MINDUSTRY_BASE_ID + 190,
    #}
    #serpulo_slag = {
    #    "Node Slag": MINDUSTRY_BASE_ID + 191,
    #}
    #serpulo_coal = {
    #    "Node Coal": MINDUSTRY_BASE_ID + 192,
    #}
    #serpulo_graphite = {
    #    "Node Graphite": MINDUSTRY_BASE_ID + 193,
    #}
    #serpulo_silicon = {
    #    "Node Silicon": MINDUSTRY_BASE_ID + 194,
    #}
    #serpulo_pyratite = {
    #    "Node Pyratite": MINDUSTRY_BASE_ID + 195,
    #}
    #serpulo_blast_compound = {
    #    "Node Blast Compound": MINDUSTRY_BASE_ID + 196,
    #}
    #serpulo_spore_pod = {
    #    "Node Spore Pod": MINDUSTRY_BASE_ID + 197,
    #}
    #serpulo_oil = {
    #    "Node Oil": MINDUSTRY_BASE_ID + 198,
    #}
    #serpulo_plastanium = {
    #    "Node Plastanium": MINDUSTRY_BASE_ID + 199,
    #}


    erekir_duct = {
        "Node Duct": MINDUSTRY_BASE_ID + 200,
    }
    erekir_duct_router = {
        "Node Duct Router": MINDUSTRY_BASE_ID + 201,
    }
    erekir_duct_bridge = {
        "Node Duct Bridge": MINDUSTRY_BASE_ID + 202,
    }
    erekir_armored_duct = {
        "Node Armored Duct": MINDUSTRY_BASE_ID + 203,
    }
    erekir_surge_conveyor = {
        "Node Surge Conveyor": MINDUSTRY_BASE_ID + 204,
    }
    erekir_surge_router = {
        "Node Surge Router": MINDUSTRY_BASE_ID + 205,
    }
    erekir_unit_cargo_loader = {
        "Node Unit Cargo Loader": MINDUSTRY_BASE_ID + 206,
    }
    erekir_unit_cargo_unload_point = {
        "Node Unit Cargo Unload Point": MINDUSTRY_BASE_ID + 207,
    }
    erekir_overflow_duct = {
        "Node Overflow Duct": MINDUSTRY_BASE_ID + 208,
    }
    erekir_underflow_duct = {
        "Node Underflow Duct": MINDUSTRY_BASE_ID + 209,
    }
    erekir_reinforced_container = {
        "Node Reinforced Container": MINDUSTRY_BASE_ID + 210,
    }
    erekir_reinforced_vault = {
        "Node Reinforced Vault": MINDUSTRY_BASE_ID + 211,
    }
    erekir_reinforced_message = {
        "Node Reinforced Message": MINDUSTRY_BASE_ID + 212,
    }
    erekir_canvas = {
        "Node Canvas": MINDUSTRY_BASE_ID + 213,
    }
    erekir_reinforced_payload_conveyor = {
        "Node Reinforced Payload Conveyor": MINDUSTRY_BASE_ID + 214,
    }
    erekir_payload_mass_driver = {
        "Node Payload Mass Driver": MINDUSTRY_BASE_ID + 215,
    }
    erekir_payload_loader = {
        "Node Payload Loader": MINDUSTRY_BASE_ID + 216,
    }
    erekir_payload_unloader = {
        "Node Payload Unloader": MINDUSTRY_BASE_ID + 217,
    }
    erekir_large_payload_mass_driver = {
        "Node Large Payload Mass Driver": MINDUSTRY_BASE_ID + 218,
    }
    erekir_constructor = {
        "Node Constructor": MINDUSTRY_BASE_ID + 219,
    }
    erekir_deconstructor = {
        "Node Deconstructor": MINDUSTRY_BASE_ID + 220,
    }
    erekir_large_constructor = {
        "Node Large Constructor": MINDUSTRY_BASE_ID + 221,
    }
    erekir_large_deconstructor = {
        "Node Large Deconstructor": MINDUSTRY_BASE_ID + 222,
    }
    erekir_reinforced_payload_router = {
        "Node Reinforced Payload Router": MINDUSTRY_BASE_ID + 223,
    }
    erekir_plasma_bore = {
        "Node Plasma Bore": MINDUSTRY_BASE_ID + 224,
    }
    erekir_impact_drill = {
        "Node Impact Drill": MINDUSTRY_BASE_ID + 225,
    }
    erekir_large_plasma_bore = {
        "Node Large Plasma Bore": MINDUSTRY_BASE_ID + 226,
    }
    erekir_eruption_drill = {
        "Node Eruption Drill": MINDUSTRY_BASE_ID + 227,
    }
    erekir_turbine_condenser = {
        "Node Turbine Condenser": MINDUSTRY_BASE_ID + 228,
    }
    erekir_beam_node = {
        "Node Beam Node": MINDUSTRY_BASE_ID + 229,
    }
    erekir_vent_condenser = {
        "Node Vent Condenser": MINDUSTRY_BASE_ID + 230,
    }
    erekir_chemical_combustion_chamber = {
        "Node Chemical Combustion Chamber": MINDUSTRY_BASE_ID + 231,
    }
    erekir_pyrolysis_generator = {
        "Node Pyrolysis Generator": MINDUSTRY_BASE_ID + 232,
    }
    erekir_flux_reactor = {
        "Node Flux Reactor": MINDUSTRY_BASE_ID + 233,
    }
    erekir_neoplasia_reactor = {
        "Node Neoplasia Reactor": MINDUSTRY_BASE_ID + 234,
    }
    erekir_beam_tower = {
        "Node Beam Tower": MINDUSTRY_BASE_ID + 235,
    }
    erekir_regen_projector = {
        "Node Regen Projector": MINDUSTRY_BASE_ID + 236,
    }
    erekir_build_tower = {
        "Node Build Tower": MINDUSTRY_BASE_ID + 237,
    }
    erekir_shockwave_tower = {
        "Node Shockwave Tower": MINDUSTRY_BASE_ID + 238,
    }
    erekir_reinforced_conduit = {
        "Node Reinforced Conduit": MINDUSTRY_BASE_ID + 239,
    }
    erekir_reinforced_pump = {
        "Node Reinforced Pump": MINDUSTRY_BASE_ID + 240,
    }
    erekir_reinforced_liquid_junction = {
        "Node Reinforced Liquid Junction": MINDUSTRY_BASE_ID + 241,
    }
    erekir_reinforced_bridge_conduit = {
        "Node Reinforced Bridge Conduit": MINDUSTRY_BASE_ID + 242,
    }
    erekir_reinforced_liquid_router = {
        "Node Reinforced Liquid Router": MINDUSTRY_BASE_ID + 243,
    }
    erekir_reinforced_liquid_container = {
        "Node Reinforced Liquid Container": MINDUSTRY_BASE_ID + 244,
    }
    erekir_reinforced_liquid_tank = {
        "Node Reinforced Liquid Tank": MINDUSTRY_BASE_ID + 245,
    }
    erekir_cliff_crusher = {
        "Node Cliff Crusher": MINDUSTRY_BASE_ID + 246,
    }
    erekir_silicon_arc_furnace = {
        "Node Silicon Arc Furnace": MINDUSTRY_BASE_ID + 247,
    }
    erekir_electrolyzer = {
        "Node Electrolyzer": MINDUSTRY_BASE_ID + 248,
    }
    erekir_oxidation_chamber = {
        "Node Oxidation Chamber": MINDUSTRY_BASE_ID + 249,
    }
    erekir_surge_crucible = {
        "Node Surge Crucible": MINDUSTRY_BASE_ID + 250,
    }
    erekir_heat_redirector = {
        "Node Heat Redirector": MINDUSTRY_BASE_ID + 251,
    }
    erekir_electric_heater = {
        "Node Electric Heater": MINDUSTRY_BASE_ID + 252,
    }
    erekir_slag_heater = {
        "Node Slag Heater": MINDUSTRY_BASE_ID + 253,
    }
    erekir_atmospheric_concentrator = {
        "Node Atmospheric Concentrator": MINDUSTRY_BASE_ID + 254,
    }
    erekir_cyanogen_synthesizer = {
        "Node Cyanogen Synthesizer": MINDUSTRY_BASE_ID + 255,
    }
    erekir_carbide_crucible = {
        "Node Carbide Crucible": MINDUSTRY_BASE_ID + 256,
    }
    erekir_phase_synthesizer = {
        "Node Phase Synthesizer": MINDUSTRY_BASE_ID + 257,
    }
    erekir_phase_heater = {
        "Node Phase Heater": MINDUSTRY_BASE_ID + 258,
    }
    erekir_heat_router = {
        "Node Heat Router": MINDUSTRY_BASE_ID + 259,
    }
    erekir_slag_incinerator = {
        "Node Slag Incinerator": MINDUSTRY_BASE_ID + 260,
    }
    erekir_breach = {
        "Node Breach": MINDUSTRY_BASE_ID + 261,
    }
    erekir_beryllium_wall = {
        "Node Beryllium Wall": MINDUSTRY_BASE_ID + 262,
    }
    erekir_large_beryllium_wall = {
        "Node Large Beryllium Wall": MINDUSTRY_BASE_ID + 263,
    }
    erekir_tungsten_wall = {
        "Node Tungsten Wall": MINDUSTRY_BASE_ID + 264,
    }
    erekir_large_tungsten_wall = {
        "Node Large Tungsten Wall": MINDUSTRY_BASE_ID + 265,
    }
    erekir_blast_door = {
        "Node Blast Door": MINDUSTRY_BASE_ID + 266,
    }
    erekir_reinforced_surge_wall = {
        "Node Reinforced Surge Wall": MINDUSTRY_BASE_ID + 267,
    }
    erekir_large_reinforced_surge_wall = {
        "Node Large Reinforced Surge Wall": MINDUSTRY_BASE_ID + 268,
    }
    erekir_shielded_wall = {
        "Node Shielded Wall": MINDUSTRY_BASE_ID + 269,
    }
    erekir_carbide_wall = {
        "Node Carbide Wall": MINDUSTRY_BASE_ID + 270,
    }
    erekir_large_carbide_wall = {
        "Node Large Carbide Wall": MINDUSTRY_BASE_ID + 271,
    }
    erekir_diffuse = {
        "Node Diffuse": MINDUSTRY_BASE_ID + 272,
    }
    erekir_sublimate = {
        "Node Sublimate": MINDUSTRY_BASE_ID + 273,
    }
    erekir_afflict = {
        "Node Afflict": MINDUSTRY_BASE_ID + 274,
    }
    erekir_titan = {
        "Node Titan": MINDUSTRY_BASE_ID + 275,
    }
    erekir_lustre = {
        "Node Lustre": MINDUSTRY_BASE_ID + 276,
    }
    erekir_smite = {
        "Node Smite": MINDUSTRY_BASE_ID + 277,
    }
    erekir_disperse = {
        "Node Disperse": MINDUSTRY_BASE_ID + 278,
    }
    erekir_scathe = {
        "Node Scathe": MINDUSTRY_BASE_ID + 279,
    }
    erekir_malign = {
        "Node Malign": MINDUSTRY_BASE_ID + 280,
    }
    erekir_radar = {
        "Node Radar": MINDUSTRY_BASE_ID + 281,
    }
    erekir_core_citadel = {
        "Node Core Citadel": MINDUSTRY_BASE_ID + 282,
    }
    erekir_core_acropolis = {
        "Node Core Acropolis": MINDUSTRY_BASE_ID + 283,
    }
    erekir_tank_fabricator = {
        "Node Tank Fabricator": MINDUSTRY_BASE_ID + 284,
    }
    erekir_stell = {
        "Node Stell": MINDUSTRY_BASE_ID + 285,
    }
    erekir_unit_repair_tower = {
        "Node Unit Repair Tower": MINDUSTRY_BASE_ID + 286,
    }
    erekir_ship_fabricator = {
        "Node Ship Fabricator": MINDUSTRY_BASE_ID + 287,
    }
    erekir_elude = {
        "Node Elude": MINDUSTRY_BASE_ID + 288,
    }
    erekir_mech_fabricator = {
        "Node Mech Fabricator": MINDUSTRY_BASE_ID + 289,
    }
    erekir_merui = {
        "Node Merui": MINDUSTRY_BASE_ID + 290,
    }
    erekir_tank_refabricator = {
        "Node Tank Refabricator": MINDUSTRY_BASE_ID + 291,
    }
    erekir_locus = {
        "Node Locus": MINDUSTRY_BASE_ID + 292,
    }
    erekir_mech_refrabricator = {
        "Node Mech Refrabricator": MINDUSTRY_BASE_ID + 293,
    }
    erekir_cleroi = {
        "Node Cleroi": MINDUSTRY_BASE_ID + 294,
    }
    erekir_ship_refabricator = {
        "Node Ship Refabricator": MINDUSTRY_BASE_ID + 295,
    }
    erekir_avert = {
        "Node Avert": MINDUSTRY_BASE_ID + 296,
    }
    erekir_prime_refabricator = {
        "Node Prime Refabricator": MINDUSTRY_BASE_ID + 297,
    }
    erekir_precept = {
        "Node Precept": MINDUSTRY_BASE_ID + 298,
    }
    erekir_anthicus = {
        "Node Anthicus": MINDUSTRY_BASE_ID + 299,
    }
    erekir_obviate = {
        "Node Obviate": MINDUSTRY_BASE_ID + 300,
    }
    erekir_tank_assembler = {
        "Node Tank Assembler": MINDUSTRY_BASE_ID + 301,
    }
    erekir_vanquish = {
        "Node Vanquish": MINDUSTRY_BASE_ID + 302,
    }
    erekir_conquer = {
        "Node Conquer": MINDUSTRY_BASE_ID + 303,
    }
    erekir_ship_assembler = {
        "Node Ship Assembler": MINDUSTRY_BASE_ID + 304,
    }
    erekir_quell = {
        "Node Quell": MINDUSTRY_BASE_ID + 305,
    }
    erekir_disrupt = {
        "Node Disrupt": MINDUSTRY_BASE_ID + 306,
    }
    erekir_mech_assembler = {
        "Node Mech Assembler": MINDUSTRY_BASE_ID + 307,
    }
    erekir_tecta = {
        "Node Tecta": MINDUSTRY_BASE_ID + 308,
    }
    erekir_collaris = {
        "Node Collaris": MINDUSTRY_BASE_ID + 309,
    }
    erekir_basic_assembler_module = {
        "Node Basic Assembler Module": MINDUSTRY_BASE_ID + 310,
    }
    erekir_aegis = {
        "Node Aegis": MINDUSTRY_BASE_ID + 311,
    }
    erekir_lake = {
        "Node Lake": MINDUSTRY_BASE_ID + 312,
    }
    erekir_intersect = {
        "Node Intersect": MINDUSTRY_BASE_ID + 313,
    }
    erekir_atlas = {
        "Node Atlas": MINDUSTRY_BASE_ID + 314,
    }
    erekir_split = {
        "Node Split": MINDUSTRY_BASE_ID + 315,
    }
    erekir_basin = {
        "Node Basin": MINDUSTRY_BASE_ID + 316,
    }
    erekir_marsh = {
        "Node Marsh": MINDUSTRY_BASE_ID + 317,
    }
    erekir_ravine = {
        "Node Ravine": MINDUSTRY_BASE_ID + 318,
    }
    erekir_caldera = {
        "Node Caldera": MINDUSTRY_BASE_ID + 319,
    }
    erekir_stronghold = {
        "Node Stronghold": MINDUSTRY_BASE_ID + 320,
    }
    erekir_crevice = {
        "Node Crevice": MINDUSTRY_BASE_ID + 321,
    }
    erekir_siege = {
        "Node Siege": MINDUSTRY_BASE_ID + 322,
    }
    erekir_crossroads = {
        "Node Crossroads": MINDUSTRY_BASE_ID + 323,
    }
    erekir_krast = {
        "Node Krast": MINDUSTRY_BASE_ID + 324,
    }
    erekir_origin = {
        "Node Origin": MINDUSTRY_BASE_ID + 325,
    }
    erekir_peaks = {
        "Node Peaks": MINDUSTRY_BASE_ID + 326,
    }
    erekir_oxide = {
        "Node Oxide": MINDUSTRY_BASE_ID + 327,
    }
    erekir_ozone = {
        "Node Ozone": MINDUSTRY_BASE_ID + 328,
    }
    erekir_hydrogen = {
        "Node Hydrogen": MINDUSTRY_BASE_ID + 329,
    }
    erekir_nitrogen = {
        "Node Nitrogen": MINDUSTRY_BASE_ID + 330,
    }
    erekir_cyanogen = {
        "Node Cyanogen": MINDUSTRY_BASE_ID + 331,
    }
    erekir_neoplasm = {
        "Node Neoplasm": MINDUSTRY_BASE_ID + 332,
    }
    erekir_tungsten = {
        "Node Tungsten": MINDUSTRY_BASE_ID + 333,
    }
    erekir_slag = {
        "Node Slag": MINDUSTRY_BASE_ID + 334,
    }
    erekir_arkycite = {
        "Node Arkycite": MINDUSTRY_BASE_ID + 335,
    }
    erekir_carbide = {
        "Node Carbide": MINDUSTRY_BASE_ID + 336,
    }




location_table = {
    #**MindustryLocations.serpulo_conveyor,
    **MindustryLocations.serpulo_junction,
    **MindustryLocations.serpulo_router,
    **MindustryLocations.serpulo_launch_pad,
    **MindustryLocations.serpulo_distributor,
    **MindustryLocations.serpulo_sorter,
    **MindustryLocations.serpulo_inverted_sorter,
    **MindustryLocations.serpulo_overflow_gate,
    **MindustryLocations.serpulo_underflow_gate,
    **MindustryLocations.serpulo_container,
    **MindustryLocations.serpulo_unloader,
    **MindustryLocations.serpulo_vault,
    **MindustryLocations.serpulo_bridge_conveyor,
    **MindustryLocations.serpulo_titanium_conveyor,
    **MindustryLocations.serpulo_phase_conveyor,
    **MindustryLocations.serpulo_mass_driver,
    **MindustryLocations.serpulo_payload_conveyor,
    **MindustryLocations.serpulo_payload_router,
    **MindustryLocations.serpulo_armored_conveyor,
    **MindustryLocations.serpulo_plastanium_conveyor,
    **MindustryLocations.serpulo_core_foundation,
    **MindustryLocations.serpulo_core_nucleus,
    #**MindustryLocations.serpulo_mechanical_drill,
    **MindustryLocations.serpulo_mechanical_pump,
    **MindustryLocations.serpulo_conduit,
    **MindustryLocations.serpulo_liquid_junction,
    **MindustryLocations.serpulo_liquid_router,
    **MindustryLocations.serpulo_liquid_container,
    **MindustryLocations.serpulo_liquid_tank,
    **MindustryLocations.serpulo_bridge_conduit,
    **MindustryLocations.serpulo_pulse_conduit,
    **MindustryLocations.serpulo_phase_conduit,
    **MindustryLocations.serpulo_plated_conduit,
    **MindustryLocations.serpulo_rotary_pump,
    **MindustryLocations.serpulo_impulse_pump,
    **MindustryLocations.serpulo_graphite_press,
    **MindustryLocations.serpulo_pneumatic_drill,
    **MindustryLocations.serpulo_cultivator,
    **MindustryLocations.serpulo_laser_drill,
    **MindustryLocations.serpulo_airblast_drill,
    **MindustryLocations.serpulo_water_extractor,
    **MindustryLocations.serpulo_oil_extractor,
    **MindustryLocations.serpulo_pyratite_mixer,
    **MindustryLocations.serpulo_blast_mixer,
    **MindustryLocations.serpulo_silicon_smelter,
    **MindustryLocations.serpulo_spore_press,
    **MindustryLocations.serpulo_coal_centrifuge,
    **MindustryLocations.serpulo_multi_press,
    **MindustryLocations.serpulo_silicon_crucible,
    **MindustryLocations.serpulo_plastanium_compressor,
    **MindustryLocations.serpulo_phase_weaver,
    **MindustryLocations.serpulo_kiln,
    **MindustryLocations.serpulo_pulveriser,
    **MindustryLocations.serpulo_incinerator,
    **MindustryLocations.serpulo_melter,
    **MindustryLocations.serpulo_surge_smelter,
    **MindustryLocations.serpulo_separator,
    **MindustryLocations.serpulo_disassembler,
    **MindustryLocations.serpulo_cryofluid_mixer,
    **MindustryLocations.serpulo_micro_processor,
    **MindustryLocations.serpulo_switch,
    **MindustryLocations.serpulo_message,
    **MindustryLocations.serpulo_logic_display,
    **MindustryLocations.serpulo_large_logic_display,
    **MindustryLocations.serpulo_memory_cell,
    **MindustryLocations.serpulo_memory_bank,
    **MindustryLocations.serpulo_logic_processor,
    **MindustryLocations.serpulo_hyper_processor,
    **MindustryLocations.serpulo_illuminator,
    **MindustryLocations.serpulo_combustion_generator,
    **MindustryLocations.serpulo_power_node,
    **MindustryLocations.serpulo_large_power_node,
    **MindustryLocations.serpulo_battery_diode,
    **MindustryLocations.serpulo_surge_tower,
    **MindustryLocations.serpulo_battery,
    **MindustryLocations.serpulo_large_battery,
    **MindustryLocations.serpulo_mender,
    **MindustryLocations.serpulo_mend_projector,
    **MindustryLocations.serpulo_force_projector,
    **MindustryLocations.serpulo_overdrive_projector,
    **MindustryLocations.serpulo_overdrive_dome,
    **MindustryLocations.serpulo_repair_point,
    **MindustryLocations.serpulo_repair_turret,
    **MindustryLocations.serpulo_steam_generator,
    **MindustryLocations.serpulo_thermal_generator,
    **MindustryLocations.serpulo_differential_generator,
    **MindustryLocations.serpulo_thorium_reactor,
    **MindustryLocations.serpulo_impact_reactor,
    **MindustryLocations.serpulo_rtg_generator,
    **MindustryLocations.serpulo_solar_panel,
    **MindustryLocations.serpulo_large_solar_panel,
    #**MindustryLocations.serpulo_duo,
    #**MindustryLocations.serpulo_copper_wall,
    **MindustryLocations.serpulo_large_copper_wall,
    **MindustryLocations.serpulo_titanium_wall,
    **MindustryLocations.serpulo_large_titanium_wall,
    **MindustryLocations.serpulo_door,
    **MindustryLocations.serpulo_large_door,
    **MindustryLocations.serpulo_plastanium_wall,
    **MindustryLocations.serpulo_large_plastanium_wall,
    **MindustryLocations.serpulo_thorium_wall,
    **MindustryLocations.serpulo_large_thorium_wall,
    **MindustryLocations.serpulo_surge_wall,
    **MindustryLocations.serpulo_large_surge_wall,
    **MindustryLocations.serpulo_phase_wall,
    **MindustryLocations.serpulo_large_phase_wall,
    #**MindustryLocations.serpulo_scatter,
    **MindustryLocations.serpulo_hail,
    **MindustryLocations.serpulo_salvo,
    **MindustryLocations.serpulo_swarmer,
    **MindustryLocations.serpulo_cyclone,
    **MindustryLocations.serpulo_spectre,
    **MindustryLocations.serpulo_ripple,
    **MindustryLocations.serpulo_fuse,
    **MindustryLocations.serpulo_scorch,
    **MindustryLocations.serpulo_arc,
    **MindustryLocations.serpulo_wave,
    **MindustryLocations.serpulo_parallax,
    **MindustryLocations.serpulo_segment,
    **MindustryLocations.serpulo_tsunami,
    **MindustryLocations.serpulo_lancer,
    **MindustryLocations.serpulo_meltdown,
    **MindustryLocations.serpulo_foreshadow,
    **MindustryLocations.serpulo_shock_mine,
    **MindustryLocations.serpulo_ground_factory,
    **MindustryLocations.serpulo_dagger,
    **MindustryLocations.serpulo_mace,
    **MindustryLocations.serpulo_fortress,
    **MindustryLocations.serpulo_scepter,
    **MindustryLocations.serpulo_reign,
    **MindustryLocations.serpulo_nova,
    **MindustryLocations.serpulo_pulsar,
    **MindustryLocations.serpulo_quasar,
    **MindustryLocations.serpulo_vela,
    **MindustryLocations.serpulo_corvus,
    **MindustryLocations.serpulo_crawler,
    **MindustryLocations.serpulo_atrax,
    **MindustryLocations.serpulo_spiroct,
    **MindustryLocations.serpulo_arkyid,
    **MindustryLocations.serpulo_toxopid,
    **MindustryLocations.serpulo_air_factory,
    **MindustryLocations.serpulo_flare,
    **MindustryLocations.serpulo_horizon,
    **MindustryLocations.serpulo_zenith,
    **MindustryLocations.serpulo_antumbra,
    **MindustryLocations.serpulo_eclipse,
    **MindustryLocations.serpulo_mono,
    **MindustryLocations.serpulo_poly,
    **MindustryLocations.serpulo_mega,
    **MindustryLocations.serpulo_quad,
    **MindustryLocations.serpulo_oct,
    **MindustryLocations.serpulo_naval_factory,
    **MindustryLocations.serpulo_risso,
    **MindustryLocations.serpulo_minke,
    **MindustryLocations.serpulo_bryde,
    **MindustryLocations.serpulo_sei,
    **MindustryLocations.serpulo_omura,
    **MindustryLocations.serpulo_retusa,
    **MindustryLocations.serpulo_oxynoe,
    **MindustryLocations.serpulo_cyerce,
    **MindustryLocations.serpulo_aegires,
    **MindustryLocations.serpulo_navanax,
    **MindustryLocations.serpulo_additive_reconstructor,
    **MindustryLocations.serpulo_multiplicative_reconstructor,
    **MindustryLocations.serpulo_exponential_reconstructor,
    **MindustryLocations.serpulo_tetrative_reconstructor,
    #**MindustryLocations.serpulo_frozen_forest,
    #**MindustryLocations.serpulo_the_craters,
    #**MindustryLocations.serpulo_ruinous_shores,
    #**MindustryLocations.serpulo_windswept_islands,
    #**MindustryLocations.serpulo_tar_fields,
    #**MindustryLocations.serpulo_impact_0078,
    #**MindustryLocations.serpulo_desolate_rift,
    #**MindustryLocations.serpulo_planetary_launch_terminal,
    #**MindustryLocations.serpulo_extraction_outpost,
    #**MindustryLocations.serpulo_salt_flats,
    #**MindustryLocations.serpulo_coastline,
    #**MindustryLocations.serpulo_naval_fortress,
    #**MindustryLocations.serpulo_overgrowth,
    #**MindustryLocations.serpulo_biomass_synthesis_facility,
    #**MindustryLocations.serpulo_stained_mountains,
    #**MindustryLocations.serpulo_fungal_pass,
    #**MindustryLocations.serpulo_nuclear_production_complex,
    #**MindustryLocations.serpulo_lead,
    #**MindustryLocations.serpulo_titanium,
    #**MindustryLocations.serpulo_cryofluid,
    #**MindustryLocations.serpulo_thorium,
    #**MindustryLocations.serpulo_surge_alloy,
    #**MindustryLocations.serpulo_phase_fabric,
    #**MindustryLocations.serpulo_metaglass,
    #**MindustryLocations.serpulo_scrap,
    #**MindustryLocations.serpulo_slag,
    #**MindustryLocations.serpulo_coal,
    #**MindustryLocations.serpulo_graphite,
    #**MindustryLocations.serpulo_silicon,
    #**MindustryLocations.serpulo_pyratite,
    #**MindustryLocations.serpulo_blast_compound,
    #**MindustryLocations.serpulo_spore_pod,
    #**MindustryLocations.serpulo_oil,
    #**MindustryLocations.serpulo_plastanium,

    #**MindustryLocations.erekir_duct,
    **MindustryLocations.erekir_duct_router,
    **MindustryLocations.erekir_duct_bridge,
    **MindustryLocations.erekir_armored_duct,
    **MindustryLocations.erekir_surge_conveyor,
    **MindustryLocations.erekir_surge_router,
    **MindustryLocations.erekir_unit_cargo_loader,
    **MindustryLocations.erekir_unit_cargo_unload_point,
    **MindustryLocations.erekir_overflow_duct,
    **MindustryLocations.erekir_underflow_duct,
    **MindustryLocations.erekir_reinforced_container,
    **MindustryLocations.erekir_reinforced_vault,
    **MindustryLocations.erekir_reinforced_message,
    **MindustryLocations.erekir_canvas,
    **MindustryLocations.erekir_reinforced_payload_conveyor,
    **MindustryLocations.erekir_payload_mass_driver,
    **MindustryLocations.erekir_payload_loader,
    **MindustryLocations.erekir_payload_unloader,
    **MindustryLocations.erekir_large_payload_mass_driver,
    **MindustryLocations.erekir_constructor,
    **MindustryLocations.erekir_deconstructor,
    **MindustryLocations.erekir_large_constructor,
    **MindustryLocations.erekir_large_deconstructor,
    **MindustryLocations.erekir_reinforced_payload_router,
    #**MindustryLocations.erekir_plasma_bore,
    **MindustryLocations.erekir_impact_drill,
    **MindustryLocations.erekir_large_plasma_bore,
    **MindustryLocations.erekir_eruption_drill,
    #**MindustryLocations.erekir_turbine_condenser,
    #**MindustryLocations.erekir_beam_node,
    **MindustryLocations.erekir_vent_condenser,
    **MindustryLocations.erekir_chemical_combustion_chamber,
    **MindustryLocations.erekir_pyrolysis_generator,
    **MindustryLocations.erekir_flux_reactor,
    **MindustryLocations.erekir_neoplasia_reactor,
    **MindustryLocations.erekir_beam_tower,
    **MindustryLocations.erekir_regen_projector,
    **MindustryLocations.erekir_build_tower,
    **MindustryLocations.erekir_shockwave_tower,
    **MindustryLocations.erekir_reinforced_conduit,
    **MindustryLocations.erekir_reinforced_pump,
    **MindustryLocations.erekir_reinforced_liquid_junction,
    **MindustryLocations.erekir_reinforced_bridge_conduit,
    **MindustryLocations.erekir_reinforced_liquid_router,
    **MindustryLocations.erekir_reinforced_liquid_container,
    **MindustryLocations.erekir_reinforced_liquid_tank,
    #**MindustryLocations.erekir_cliff_crusher,
    **MindustryLocations.erekir_silicon_arc_furnace,
    **MindustryLocations.erekir_electrolyzer,
    **MindustryLocations.erekir_oxidation_chamber,
    **MindustryLocations.erekir_surge_crucible,
    **MindustryLocations.erekir_heat_redirector,
    **MindustryLocations.erekir_electric_heater,
    **MindustryLocations.erekir_slag_heater,
    **MindustryLocations.erekir_atmospheric_concentrator,
    **MindustryLocations.erekir_cyanogen_synthesizer,
    **MindustryLocations.erekir_carbide_crucible,
    **MindustryLocations.erekir_phase_synthesizer,
    **MindustryLocations.erekir_phase_heater,
    **MindustryLocations.erekir_heat_router,
    **MindustryLocations.erekir_slag_incinerator,
    #**MindustryLocations.erekir_breach,
    #**MindustryLocations.erekir_beryllium_wall,
    **MindustryLocations.erekir_large_beryllium_wall,
    **MindustryLocations.erekir_tungsten_wall,
    **MindustryLocations.erekir_large_tungsten_wall,
    **MindustryLocations.erekir_blast_door,
    **MindustryLocations.erekir_reinforced_surge_wall,
    **MindustryLocations.erekir_large_reinforced_surge_wall,
    **MindustryLocations.erekir_shielded_wall,
    **MindustryLocations.erekir_carbide_wall,
    **MindustryLocations.erekir_large_carbide_wall,
    **MindustryLocations.erekir_diffuse,
    **MindustryLocations.erekir_sublimate,
    **MindustryLocations.erekir_afflict,
    **MindustryLocations.erekir_titan,
    **MindustryLocations.erekir_lustre,
    **MindustryLocations.erekir_smite,
    **MindustryLocations.erekir_disperse,
    **MindustryLocations.erekir_scathe,
    **MindustryLocations.erekir_malign,
    **MindustryLocations.erekir_radar,
    **MindustryLocations.erekir_core_citadel,
    **MindustryLocations.erekir_core_acropolis,
    #**MindustryLocations.erekir_tank_fabricator,
    #**MindustryLocations.erekir_stell,
    **MindustryLocations.erekir_unit_repair_tower,
    **MindustryLocations.erekir_ship_fabricator,
    **MindustryLocations.erekir_elude,
    **MindustryLocations.erekir_mech_fabricator,
    **MindustryLocations.erekir_merui,
    **MindustryLocations.erekir_tank_refabricator,
    **MindustryLocations.erekir_locus,
    **MindustryLocations.erekir_mech_refrabricator,
    **MindustryLocations.erekir_cleroi,
    **MindustryLocations.erekir_ship_refabricator,
    **MindustryLocations.erekir_avert,
    **MindustryLocations.erekir_prime_refabricator,
    **MindustryLocations.erekir_precept,
    **MindustryLocations.erekir_anthicus,
    **MindustryLocations.erekir_obviate,
    **MindustryLocations.erekir_tank_assembler,
    **MindustryLocations.erekir_vanquish,
    **MindustryLocations.erekir_conquer,
    **MindustryLocations.erekir_ship_assembler,
    **MindustryLocations.erekir_quell,
    **MindustryLocations.erekir_disrupt,
    **MindustryLocations.erekir_mech_assembler,
    **MindustryLocations.erekir_tecta,
    **MindustryLocations.erekir_collaris,
    **MindustryLocations.erekir_basic_assembler_module,
    **MindustryLocations.erekir_aegis,
    **MindustryLocations.erekir_lake,
    **MindustryLocations.erekir_intersect,
    **MindustryLocations.erekir_atlas,
    **MindustryLocations.erekir_split,
    **MindustryLocations.erekir_basin,
    **MindustryLocations.erekir_marsh,
    **MindustryLocations.erekir_ravine,
    **MindustryLocations.erekir_caldera,
    **MindustryLocations.erekir_stronghold,
    **MindustryLocations.erekir_crevice,
    **MindustryLocations.erekir_siege,
    **MindustryLocations.erekir_crossroads,
    **MindustryLocations.erekir_krast,
    **MindustryLocations.erekir_origin,
    **MindustryLocations.erekir_peaks,
    **MindustryLocations.erekir_oxide,
    **MindustryLocations.erekir_ozone,
    **MindustryLocations.erekir_hydrogen,
    **MindustryLocations.erekir_nitrogen,
    **MindustryLocations.erekir_cyanogen,
    **MindustryLocations.erekir_neoplasm,
    **MindustryLocations.erekir_tungsten,
    **MindustryLocations.erekir_slag,
    **MindustryLocations.erekir_arkycite,
    **MindustryLocations.erekir_carbide,
}
