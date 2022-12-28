import pymem
import pymem.process
import keyboard
import offsets as x


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

map()
