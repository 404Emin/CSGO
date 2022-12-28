import pymem
import pymem.process
import keyboard
import offsets as x


def glow():
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    
    while True:
        if keyboard.is_pressed('H'):
            exit(0)

        glow_manager = pm.read_int(client + x.dwGlowObjectManager)

        for i in range(1,32):
            entity = pm.read_int(client + x.dwEntityList + i * 0x10)
            if entity:
                entity_team_id = pm.read_int(entity + x.m_iTeamNum)
                entity_glow = pm.read_int(entity + x.m_iGlowIndex)

                if entity_team_id == 2: #terrorist glow
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1)) #R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0)) #G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1)) #B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1)) #A
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)

                elif entity_team_id == 3: #counter terrorist glow
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0)) #R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1)) #G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1)) #B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1)) #A
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)


glow()
