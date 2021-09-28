import os
import yaml

# DEPENDENCIES
# pip install -U PyYAML


myDir = os.path.dirname(os.path.abspath(__file__))
tmpDir = '/../../tmp/'

def cycle():
    print("cycling")
    parsed = openConfig()
    cbl = parsed['current_keyboard_layout']    
    #os.system('echo "printing command test"')
    
def setLayout(inLayout):
    os.system('setxkbmap ' + inLayout)
    

def openConfig():
    tmpConfig_dir = myDir + tmpDir 

    config_file_name = 'keyboard_config.yaml'

    config_file = myDir + '/' + config_file_name 
    config_file_tmp = tmpConfig_dir + config_file_name
  
    print("Checking if tmp folder exists at: " + tmpConfig_dir)
    tmpDir_exists = os.path.exists(tmpConfig_dir)
    if tmpDir_exists:
        print("Directory exists")
    else:
        print("Directory does not exists, creating...")
        createDir_cmd = "mkdir " + tmpConfig_dir
        print(createDir_cmd)
        os.system(createDir_cmd) 

    print("Checking if config file and temp exists at: " + config_file)
    if os.path.exists(config_file):
        print("Config file exists, checking tmp")
        print("Checking if config tmp file and temp exists at: " + config_file_tmp)
        if os.path.exists(config_file_tmp):
            print("Temporary file also exists, getting values now")
        else:
            print("Temporary file does not exists, copying now from original")
            copyConfig_cmd = "cp " + config_file + " " + config_file_tmp
            print(copyConfig_cmd)
            os.system(copyConfig_cmd)
    else:
        print("ERROR: Config file does not exist, quitting now...")
        exit()


    print("Parsing YAML now")
    yaml_file = open(config_file_tmp)
    parsed = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print(parsed['layouts'])
    
    return parsed
    

if __name__ == "__main__":
    print("main function")
    openConfig()


