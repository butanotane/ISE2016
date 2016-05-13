import _winreg

LM_key_list = ['Software\\Microsoft\\Windows\\CurrentVersion\\Run', 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce']
KU_key_list = ['Software\\Microsoft\\Windows\\CurrentVersion\\Run', 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce']

def enum_values(key):
    try:
        i = 0
        while True:
            yield _winreg.EnumValue(key, i)
            i += 1
    except EnvironmentError:
        pass

for keys in LM_key_list:
    j=1
    reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, keys)
    print "\r\n[+] printing keys in HKEY_LOCAL_MACHINE\\" + keys 
    try:
        for name, value, type_ in enum_values(reg):
            print j, name, value
            j += 1
    finally:
        _winreg.CloseKey(reg)

for keys2 in LM_key_list:
    reg = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, keys2)
    print "\r\n[+] printing keys in HKEY_CURRENT_USER\\" + keys2 
    try:
        for name, value, type_ in enum_values(reg):
            print name, value
    finally:
        _winreg.CloseKey(reg)
