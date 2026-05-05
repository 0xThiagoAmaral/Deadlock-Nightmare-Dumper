import pymem
import pymem.process
import struct

class NightmareValidator:
    def __init__(self):
        try:
            self.pm = pymem.Pymem("deadlock.exe")
            self.client = pymem.process.module_from_name(self.pm.process_handle, "client.dll").lpBaseOfDll
            print("[+] Conectado para Validação.")
        except:
            print("[!] Jogo não encontrado.")
            return

    def validate(self):
        # Globais que JA VALIDAMOS (eles apontam para memorias validas)
        offsets = {
            "dwLocalPlayerController": 0x37665e0,
            "dwEntityList": 0x3761a58
        }

        print("\n--- INICIANDO BUSCA DE OFFSET REAL ---")

        try:
            lp_controller = self.pm.read_longlong(self.client + offsets["dwLocalPlayerController"])
            if lp_controller > 0x10000:
                print(f"[+] Controller Base: {hex(lp_controller)}")
                
                # Vamos ler 4KB da memória do controller e procurar seu nome
                mem_dump = self.pm.read_bytes(lp_controller, 0x1000)
                
                # Aqui você deve colocar seu nick da Steam (vou procurar por padrões comuns de string)
                # Como não sei seu nick, vou listar strings encontradas no range de offsets 0x500-0x900
                print("[*] Vasculhando offsets em busca de strings (Nomes)...")
                for i in range(0x500, 0x900, 4):
                    try:
                        potential_name = self.pm.read_string(lp_controller + i, 32)
                        if potential_name and len(potential_name) > 2 and potential_name.isprintable():
                            print(f"[!] ACHADO: Offset {hex(i)} -> '{potential_name}'")
                    except:
                        continue
            else:
                print("[FALHA] dwLocalPlayerController inválido.")
        except Exception as e:
            print(f"[ERRO] {e}")

if __name__ == "__main__":
    validator = NightmareValidator()
    validator.validate()
