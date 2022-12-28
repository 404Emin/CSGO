import pymem
import pymem.process
import keyboard
import offsets as x

def chams():
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll

    rgbT = [255, 51, 0]
    rgbCT =  [0, 51, 255]

    while True:

        if keyboard.is_pressed('H'):
            exit(0)

        try:
            for i in range(32):
                entity = pm.read_int(client + x.dwEntityList + i * 0x10)

                if entity:
                    entity_team_id = pm.read_int(entity + x.m_iTeamNum)

                    if entity_team_id == 2:
                        pm.write_int(entity + x.m_clrRender, (rgbT[0]))
                        pm.write_int(entity + x.m_clrRender + 0x1, (rgbT[1]))
                        pm.write_int(entity + x.m_clrRender + 0x2, (rgbT[2]))

                    elif entity_team_id == 3:
                        pm.write_int(entity + x.m_clrRender, (rgbCT[0]))
                        pm.write_int(entity + x.m_clrRender + 0x1, (rgbCT[1]))
                        pm.write_int(entity + x.m_clrRender + 0x2, (rgbCT[2]))

                else:
                    pass
        except Exception as e:
            print(e)

chams()