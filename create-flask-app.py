#!/usr/bin/env python3
from scripts.workflow import get_app_name, isValid, get_args, create_dir, create_app, create_templates_folder, create_static_folder, create_dockerfile
from scripts.manual import print_manual
from scripts.Colors import bcolors
import sys

app_name = get_app_name()
args = get_args()
args.remove(app_name)
valid_args_list = ['-dB', '--debug', '-sS', '--css-js', '-dC', '--docker']

if (isValid(app_name)):

    # validate all arguments first!!
    valid_args =  all(arg in valid_args_list for arg in args)
    if valid_args is False:
        print('Unknown argument detected! Please check the help section\n')
        print_manual()
        print(f"{bcolors.FAIL}Creation of directory failed: %s" % app_name)
        sys.exit(1)
    else:
        # Create folder named app_name
        create_dir(app_name)

        # Arguments
        debugger_mode = False
        import_css_js = False
        use_docker = False

        if '-dB' in args or '--debug' in args:
            debugger_mode = True
            print("- Debugger mode on")
        if '-sS' in args or '--css-js' in args:
            import_css_js = True
            print("- Css and Js mode on")
        if '-dC' in args or '--docker' in args:
            use_docker = True
            print("- Docker mode on")
            print('  |__ cd %s' % app_name)
            print('  |__ \"docker-compose up -d\" to start app')

        
        if (debugger_mode is False and import_css_js is False and use_docker is False):
            print("- Debugger mode off")
            print("- Css and Js mode off")
            print("- Docker mode off")
    

    # if -sS enabled, creat static folder
    if(import_css_js):
        create_static_folder(app_name)

    # create templates folder to hold index.html
    create_templates_folder(app_name, import_css_js)

    # create app.py in root directory(app_name)
    create_app(app_name, debugger_mode)

    if (use_docker):
        create_dockerfile(app_name)

    print(f"{bcolors.OKGREEN}Creation of directory success: %s" % app_name)
else:
    if (app_name == '-h' or app_name == '--help'):
        print_manual()
    else:
        print(f'{bcolors.WARNING}Please choose another app name')
        print(f"{bcolors.FAIL}Creation of directory failed: %s" % app_name)