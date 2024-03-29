import os
import sys
import yaml

# DEPENDENCIES
# pip install -U PyYAML


myDir = os.path.dirname(os.path.abspath(__file__))
tmpDir = '/../../tmp/'
config_file_name = 'keyboard_config.yaml'

def cycle(inDirection):
    
    if inDirection:
        print("cycling forward")
    else:
        print("cycling backwards")

    parsed = openConfig()
    layouts = parsed['layouts']
    primary_layout = parsed['primary']
    secondary_layout = parsed['secondary']
    
    # Currently only cycling secondary keyboard since there is no clear way to have feedback
    # on which is the current layout (to go to the us or primary layout use
    # togglePrimarySecondary function)
    #current_layout = parsed['current']
    current_layout = "secondary"
    
    if(current_layout == "primary"):
        old_layout = primary_layout 
        new_layout = primary_layout 
    if(current_layout == "secondary"):
        old_layout = secondary_layout 
        new_layout = secondary_layout 

    for l in range(len(layouts)):
        #print (layouts[l])
        if layouts[l] == old_layout:
            print('found match ' + layouts[l] + ' at id ' + str(l))
            if inDirection:
                if l == len(layouts) - 1:
                    new_layout = layouts[0]
                else:
                    new_layout = layouts[l+1]
                break
            else:
                if l == 0:
                    new_layout = layouts[len(layouts)-1]
                else:
                    new_layout = layouts[l-1]
                break
                

    if(current_layout == "primary"):
        parsed['primary'] = new_layout
        parsed['current'] = "primary"
    if(current_layout == "secondary"):
        parsed['secondary'] = new_layout
        parsed['current'] = "secondary"
    
    cmd = 'setxkbmap -layout ' + new_layout 

    saveConfig(parsed)
    print(cmd)
    os.system(cmd)

def togglePrimarySecondary():
    
    parsed = openConfig()
    layouts = parsed['layouts']
    primary_layout = parsed['primary']
    secondary_layout = parsed['secondary']
    current_layout = parsed['current']
    
    if(current_layout == "primary"):
        cmd = 'setxkbmap -layout ' + secondary_layout
        parsed['current'] = "secondary"
    if(current_layout == "secondary"):
        cmd = 'setxkbmap -layout ' + primary_layout  
        parsed['current'] = "primary"
    
    saveConfig(parsed)
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
    try:
        function = sys.argv[1]
        print(len(sys.argv))
        #if len(sys.argv)>2:
            #globals()[function](sys.argv[2])
        if function == "cycle":
            if sys.argv[2] == "True":
                globals()[function](True)
            else:
                globals()[function](False)
        else:
            globals()[function]()

    except IndexError:
        raise Exception("Please provide function name")
    except KeyError:
        raise Exception("Function {} hasn't been found".format(function))


