# Deadlock-Nightmare-Dumper - Offset Dumper (Source 2)
# =================================================================
# Developed for Deadlock automation and industrialization.
# Focus: client.dll & schemasystem.dll
# =================================================================

import pymem
import pymem.process
import json
import re
from datetime import date

class NightmareDumper:
    def __init__(self):
        self.pm = None
        self.client_base = 0
        self.schema_base = 0
        self.version = str(date.today())
        self.output_file = "nightmare_offsets.json"
        self.generator = "Deadlock-Nightmare-Dumper"
        
        # Patterns de Elite (Deadlock / Source 2) - Versão Final
        self.patterns = {
            "dwEntityList": "48 8B 0D ?? ?? ?? ?? 48 8D 05",
            "dwLocalPlayerController": "48 8B 05 ?? ?? ?? ?? 48 85 C0 74 4F",
            "dwViewMatrix": "48 8D 0D ?? ?? ?? ?? 48 C1 E0 06",
            "dwGlobalVars": "48 8B 05 ?? ?? ?? ?? 48 8B D8 48 85 C0" 
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
        if not self.attach(): 
            print("[!] Jogo não detectado.")
            return
        
        print("[*] Iniciando Extração Final de Elite...")
        
        globals_found = {}
        for name, pattern in self.patterns.items():
            if name == "dwGlobalVars":
                off = self.get_offset_from_pattern(pattern, "engine2.dll")
            else:
                off = self.get_offset_from_pattern(pattern, "client.dll")
            
            globals_found[name] = off
            print(f"[>] {name}: {hex(off)}")

        output = {
            "version": self.version,
            "generator": "NightmareDumper",
            "client_dll_base": hex(self.client_base),
            "globals": globals_found,
            "classes": {
                "C_BaseEntity": {
                    "m_iHealth": 0x334,
                    "m_iMaxHealth": 0x330,
                    "m_lifeState": 0x33C,
                    "m_iTeamNum": 0x3E3,
                    "m_pGameSceneNode": 0x310,
                    "m_bSpotted": 0x2218,      # Visibilidade (Is Visible)
                    "m_vecAbsVelocity": 0x404
                },
                "CGameSceneNode": {
                    "m_vecAbsOrigin": 0xC8,
                    "m_vecAbsVelocity": 0x38,
                    "m_modelState": 0x170      # MATRIZ DE OSSOS (Para Headshots)
                },
                "CCitadelPlayerController": {
                    "m_hHeroPawn": 0x8AC,
                    "m_iszPlayerName": 0x6F0,
                    "m_angEyeAngles": 0x6C4,
                    "m_iPlayerState": 0x8B4,
                    "m_vecInventory": 0x1110
                },
                "C_BasePlayerPawn": {
                    "m_hActiveWeapon": 0x1030,
                    "m_iClip1": 0x10A0,
                    "m_hAbilities": 0x1B10
                },
                "C_BaseAbility": {
                    "m_flNextReadyTime": 0x5D8,
                    "m_nCharges": 0x5EC,
                    "m_unLevel": 0x5F8
                },
                "CEntityIdentity": {
                    "size": 112,
                    "m_pEntity": 0x00,
                    "m_designerName": 0x20,
                    "m_hHandle": 0x10,
                    "m_next": 0x58
                }
            }
        }

        with open(self.output_file, "w") as f:
            json.dump(output, f, indent=2)
        
        print(f"\n[v] DUMP DEFINITIVO CONCLUÍDO! O Loader mais forte do Deadlock está pronto.")

if __name__ == "__main__":
    NightmareDumper().run()
