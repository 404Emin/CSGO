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


def trigger():
    
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:

        if keyboard.is_pressed('H'):
            exit(0)

        while keyboard.is_pressed('V'):

            LocalPlayer = pm.read_int(client + x.dwLocalPlayer)
            crosshairID = pm.read_int(LocalPlayer + x.m_iCrosshairId)
            getTeam = pm.read_int(client + x.dwEntityList + (crosshairID - 1) * 0x10)
            localTeam = pm.read_int(LocalPlayer + x.m_iTeamNum)
            crosshairTeam = pm.read_int(getTeam + x.m_iTeamNum)

            if crosshairID > 0 and crosshairID < 32 and localTeam != crosshairTeam:
                pm.write_int(client + x.dwForceAttack, 6)

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

def map():
    
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:
         
         if keyboard.is_pressed('H'):
                exit(0)

         for i in range(32):
                
                entity = pm.read_int(client + x.dwEntityList + i * 0x10)

                if entity:
                    pm.write_uchar(entity + x.m_bSpotted, 1)



