import pymem
import pymem.process
import json
import re
import requests
from datetime import date

# Deadlock-Nightmare-Dumper - Offset Dumper (Source 2)
# =================================================================
# Pro Version: C++, C# SDKs & Discord Integration
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
        self.config = self.load_config()
        
        self.patterns = {
            "dwEntityList": "48 8B 0D ?? ?? ?? ?? 48 8D 05",
            "dwLocalPlayerController": "48 8B 05 ?? ?? ?? ?? 48 85 C0 74 4F",
            "dwViewMatrix": "48 8D 0D ?? ?? ?? ?? 48 C1 E0 06",
            "dwGlobalVars": "48 8B 05 ?? ?? ?? ?? 48 8B D8 48 85 C0"
        }

    def load_config(self):
        try:
            with open("config.json", "r") as f:
                return json.load(f)
        except:
            return {"discord_webhook": "", "generate_csharp": True, "generate_cpp": True}

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

    def generate_cs_sdk(self, data):
        """Gera um arquivo de cabealho C# (.cs) para uso em loaders .NET."""
        print(f"[*] Gerando C# SDK: {self.cs_file}")
        with open(self.cs_file, "w") as f:
            f.write(f"namespace NightmareOffsets {{\n")
            f.write(f"    public static class Globals {{\n")
            for name, val in data["globals"].items():
                f.write(f"        public const nint {name} = {hex(val)};\n")
            f.write(f"    }}\n\n")
            f.write(f"    public static class Offsets {{\n")
            for class_name, fields in data["classes"].items():
                f.write(f"        public static class {class_name} {{\n")
                for field_name, offset in fields.items():
                    f.write(f"            public const nint {field_name} = {hex(offset)};\n")
                f.write(f"        }}\n")
            f.write(f"    }}\n")
            f.write(f"}}\n")

    def generate_cpp_header(self, data):
        print(f"[*] Gerando C++ SDK: {self.header_file}")
        with open(self.header_file, "w") as f:
            f.write(f"#pragma once\n#include <cstddef>\n\nnamespace Nightmare {{\n")
            f.write(f"    namespace Globals {{\n")
            for name, val in data["globals"].items():
                f.write(f"        constexpr std::ptrdiff_t {name} = {hex(val)};\n")
            f.write(f"    }}\n\n")
            f.write(f"    namespace Offsets {{\n")
            for class_name, fields in data["classes"].items():
                f.write(f"        namespace {class_name} {{\n")
                for field_name, offset in fields.items():
                    f.write(f"            constexpr std::ptrdiff_t {field_name} = {hex(offset)};\n")
                f.write(f"        }}\n")
            f.write(f"    }}\n}}\n")

    def send_discord_notification(self, data):
        webhook_url = self.config.get("discord_webhook")
        if not webhook_url: return
        
        embed = {
            "title": "🌑 Nightmare Dumper - Offsets Atualizados",
            "color": 0x9400d3,
            "fields": [
                {"name": "dwEntityList", "value": hex(data["globals"]["dwEntityList"]), "inline": True},
                {"name": "dwLocalPlayer", "value": hex(data["globals"]["dwLocalPlayerController"]), "inline": True},
                {"name": "Version", "value": self.version, "inline": False}
            ],
            "footer": {"text": "Deadlock Nightmare Dumper | By 0xThiagoAmaral"}
        }
        try:
            requests.post(webhook_url, json={"embeds": [embed]})
            print("[+] Notificao enviada ao Discord!")
        except:
            print("[!] Falha ao enviar Webhook.")

    def run(self):
        if not self.attach(): return
        
        print(f"[*] Iniciando Nightmare Dumper v3 (Pro Edition)...")
        
        globals_found = {}
        for name, pattern in self.patterns.items():
            off = self.get_offset_from_pattern(pattern, "engine2.dll" if name == "dwGlobalVars" else "client.dll")
            globals_found[name] = off

        output = {
            "version": self.version, "generator": self.generator, "globals": globals_found,
            "classes": {
                "C_BaseEntity": {"m_iHealth": 0x334, "m_iMaxHealth": 0x330, "m_lifeState": 0x33C, "m_iTeamNum": 0x3E3, "m_pGameSceneNode": 0x310, "m_bSpotted": 0x2218, "m_vecAbsVelocity": 0x404},
                "CGameSceneNode": {"m_vecAbsOrigin": 0xC8, "m_vecAbsVelocity": 0x38, "m_modelState": 0x170},
                "CCitadelPlayerController": {"m_hHeroPawn": 0x8AC, "m_iszPlayerName": 0x6F0, "m_angEyeAngles": 0x6C4, "m_iPlayerState": 0x8B4, "m_vecInventory": 0x1110},
                "C_BasePlayerPawn": {"m_hActiveWeapon": 0x1030, "m_iClip1": 0x10A0, "m_hAbilities": 0x1B10},
                "C_BaseAbility": {"m_flNextReadyTime": 0x5D8, "m_nCharges": 0x5EC, "m_unLevel": 0x5F8}
            }
        }

        with open(self.output_file, "w") as f: json.dump(output, f, indent=2)
        if self.config.get("generate_cpp"): self.generate_cpp_header(output)
        if self.config.get("generate_csharp"): self.generate_cs_sdk(output)
        self.send_discord_notification(output)
        
        print(f"\n[v] TUDO PRONTO! SDKs e Notificaes processadas.")

if __name__ == "__main__":
    NightmareDumper().run()
