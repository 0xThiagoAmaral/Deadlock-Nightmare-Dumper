import pymem
import pymem.process
import json
import re
from datetime import date

# Deadlock-Nightmare-Dumper - Offset Dumper (Source 2)
# =================================================================
# Elite Edition: Backtrack & Anti-Spectator Support
# =================================================================

class NightmareDumper:
    def __init__(self):
        self.pm = None
        self.client_base = 0
        self.schema_base = 0
        self.version = str(date.today())
        self.output_file = "nightmare_offsets.json"
        self.header_file = "nightmare_offsets.hpp"
        self.cs_file = "nightmare_offsets.cs"
        self.generator = "Deadlock-Nightmare-Dumper"
        
        self.patterns = {
            "dwEntityList": "48 8B 0D ?? ?? ?? ?? 48 8D 05",
            "dwLocalPlayerController": "48 8B 05 ?? ?? ?? ?? 48 85 C0 74 4F",
            "dwViewMatrix": "48 8D 0D ?? ?? ?? ?? 48 C1 E0 06",
            "dwGlobalVars": "48 89 05 ?? ?? ?? ?? 48 8B D8"
        }

    def attach(self):
        try:
            self.pm = pymem.Pymem("deadlock.exe")
            self.client_base = pymem.process.module_from_name(self.pm.process_handle, "client.dll").lpBaseOfDll
            self.schema_base = pymem.process.module_from_name(self.pm.process_handle, "schemasystem.dll").lpBaseOfDll
            return True
        except: return False

    def get_offset_from_pattern(self, pattern, module_name="client.dll"):
        try:
            module = pymem.process.module_from_name(self.pm.process_handle, module_name)
            data = self.pm.read_bytes(module.lpBaseOfDll, module.SizeOfImage)
            re_pattern = b""
            for part in pattern.split():
                if part == "??": re_pattern += b"."
                else: re_pattern += re.escape(bytes([int(part, 16)]))
            match = re.search(re_pattern, data, re.DOTALL)
            if not match: return 0
            addr = module.lpBaseOfDll + match.start()
            return (addr + 7 + self.pm.read_int(addr + 3)) - module.lpBaseOfDll
        except: return 0

    def run(self):
        if not self.attach(): return
        print(f"[*] Iniciando Nightmare Dumper (ELITE EDITION)...")
        
        globals_found = {}
        for name, pattern in self.patterns.items():
            off = self.get_offset_from_pattern(pattern, "engine2.dll" if name == "dwGlobalVars" else "client.dll")
            globals_found[name] = off

        bone_indices = {
            "Head": 6, "Neck": 5, "Chest": 4, "Pelvis": 0,
            "L_Shoulder": 8, "R_Shoulder": 13, "L_Hand": 11, "R_Hand": 16,
            "L_Knee": 23, "R_Knee": 28, "L_Foot": 24, "R_Foot": 29
        }

        output = {
            "version": self.version, "generator": self.generator, "globals": globals_found,
            "bone_indices": bone_indices,
            "classes": {
                "C_BaseEntity": {
                    "m_iHealth": 0x334, "m_iMaxHealth": 0x330, "m_lifeState": 0x33C, "m_iTeamNum": 0x3E3, 
                    "m_pGameSceneNode": 0x310, "m_bSpotted": 0x2218, "m_vecAbsVelocity": 0x404, "m_fFlags": 0x3C8,
                    "m_hOwnerEntity": 0x41C, "m_flSimulationTime": 0x318 # ELITE: Backtrack/Interp
                },
                "CCitadelPlayerController": {
                    "m_hHeroPawn": 0x8AC, "m_iszPlayerName": 0x6F0, "m_angEyeAngles": 0x6C4, 
                    "m_nPlayerLevel": 0x7A0, "m_iKillStreak": 0x7B0, "m_vecInventory": 0x1110, 
                    "m_iNetWorth": 0x618, "m_iObserverMode": 0x21C # ELITE: Anti-Spectator
                },
                "C_BasePlayerPawn": {
                    "m_hActiveWeapon": 0x1030, "m_iClip1": 0x10A0, "m_hAbilities": 0x1B10, 
                    "m_vecViewOffset": 0x418, "m_nTickBase": 0x1120, "m_nCondition": 0x1F18,
                    "m_flFlashDuration": 0x1470 # ELITE: No-Flash/Anti-Blind
                },
                "C_BaseAbility": {
                    "m_flNextReadyTime": 0x5D8, "m_flNextPrimaryAttack": 0x168, 
                    "m_flCastTime": 0x5E0, "m_nCharges": 0x5EC, "m_unLevel": 0x5F8
                }
            }
        }

        with open(self.output_file, "w") as f: json.dump(output, f, indent=2)
        print(f"\n[v] DUMP ELITE CONCLUDO! SimulationTime, ObserverMode e FlashDuration mapeados.")

if __name__ == "__main__":
    NightmareDumper().run()
