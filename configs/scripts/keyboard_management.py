import os
import yaml

# DEPENDENCIES
# pip install -U PyYAML


myDir = os.path.dirname(os.path.abspath(__file__))
tmpDir = '/../../tmp/'
config_file_name = 'keyboard_config.yaml'

def cycle():
    print("cycling")
    parsed = openConfig()
    layouts = parsed['layouts']
    primary_layout = parsed['primary']
    parsed['primary'] = primary_layout
    for l in range(len(layouts)):
        #print (layouts[l])
        if layouts[l] == primary_layout:
            print('found match ' + layouts[l])
            if l == len(layouts) - 1:
                primary_layout = layouts[0]
            else:
                primary_layout = layouts[l+1]
            break

    parsed['primary'] = primary_layout

    saveConfig(parsed)

    cmd = 'setxkbmap -layout ' + primary_layout
   
    print(cmd)
    os.system(cmd)
    
def setLayout(inLayout):
    os.system('setxkbmap ' + inLayout)
    

def saveConfig(outParsed):
    tmpConfig_dir = myDir + tmpDir 
    config_file_tmp = tmpConfig_dir + config_file_name
    with open(config_file_tmp, 'w') as f:
        yaml.dump(outParsed, f)

def openConfig():
    tmpConfig_dir = myDir + tmpDir 

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


