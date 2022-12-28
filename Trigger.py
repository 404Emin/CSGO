import pymem
import pymem.process
import keyboard
import offsets as x


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

trigger()