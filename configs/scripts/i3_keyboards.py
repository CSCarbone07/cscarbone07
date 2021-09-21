import os
import yaml

#layouts = ["us", "es", "it"]

def cycle():
    print("cycling")
    parsed = openConfig()
    cbl = parsed['current_keyboard_layout']    
    #os.system('echo "printing command test"')
    
def setLayout(inLayout)
    os.system('setxkbmap ' + inLayout)
    

def openConfig():
    myDir = os.path.dirname(os.path.abspath(__file__))

    if not(os.path.exists(myDir + '/../myConfigs_temp.yaml')):
        print("copying config file to temp file")
        copy_config_cmd = "cp " + myDir + "/../myConfigs.yaml " \
        + myDir + "/../myConfigs_temp.yaml"
        os.system(copy_config_cmd)
    yaml_file = open(myDir + '/../myConfigs_temp.yaml')
    parsed = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print(parsed['keyboard_layouts'])
    return parsed 

if __name__ == "__main__":
    print("main function")
    openConfig()


