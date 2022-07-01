from datetime import datetime

def writeDebugLog(DebugText, filepath = ''):
    Timestamp = datetime.now()
    if filepath == '':
        filepath = Timestamp.strftime('%Y%m%d%H%M%S_Debug.txt')
    with open(filepath, 'w+', "utf-8") as debugfile:
        debugfile.write(f'{Timestamp.strftime("%Y.%m.%d")}\n{Timestamp.strftime("%H:%M:%S")}\n\n{DebugText}')
    return