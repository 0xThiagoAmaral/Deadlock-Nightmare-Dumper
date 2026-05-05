import pymem
import pymem.process
import re

def resolve_handle(pm, base, handle):
    try:
        entity_list = pm.read_longlong(base + 0x3761a58)
        entry = pm.read_longlong(entity_list + 0x8 * ((handle & 0x7FFF) >> 9) + 16)
        return pm.read_longlong(entry + 120 * (handle & 0x1FF))
    except: return 0

def validate():
    try:
        pm = pymem.Pymem("deadlock.exe")
        client = pymem.process.module_from_name(pm.process_handle, "client.dll")
        base = client.lpBaseOfDll
        print("--- Nightmare Final-Proof v3.9 ---")
        
        pattern = b"\x48\x8B\x05....\x48\x85\xC0\x74\x4F"
        data = pm.read_bytes(base, client.SizeOfImage)
        match = re.search(pattern, data, re.DOTALL)
        
        if match:
            addr = base + match.start()
            rel_offset = int.from_bytes(pm.read_bytes(addr + 3, 4), byteorder='little', signed=True)
            controller = pm.read_longlong(addr + 7 + rel_offset)
            
            if controller:
                h_pawn = pm.read_int(controller + 0x8AC)
                pawn = resolve_handle(pm, base, h_pawn)
                if pawn:
                    health = pm.read_int(pawn + 0x334)
                    print(f"[v] VIDA DETECTADA: {health} HP")
                    print(f"[v] ENDEREO DO PAWN: {hex(pawn)}")
                    if health == 790: print("[!!!] MATCH PERFEITO COM O PRINT!")
                else:
                    print("[!] Pawn no resolvido. Est vivo?")
        else:
            print("[!] Assinatura falhou.")

    except Exception as e:
        print(f"[!] Erro: {e}")

if __name__ == "__main__":
    validate()
