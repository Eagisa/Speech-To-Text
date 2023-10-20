#================================#
# Speech To Text setup installer
#================================#


#Speech To Text - ClientBootstrapper API-LINK
#=============================================================================================================================#
ClientBootstrapper = ("https://raw.githubusercontent.com/Eagisa/Speech-To-Text/main/ClientBootStrapper.json")
#=============================================================================================================================#

def FileChecker():
    # Creates SpeechToText, LocalStorage, Logs, automatically if not exists or created
    # ============================================================================= #
    def CreateFolders():
        # Get the path to the LocalAppData directory
        local_appdata = os.environ['LOCALAPPDATA']

        # Define the main folder name
        main_folder_name = 'SpeechToText'

        # Define subfolder names you want to create within the main folder
        subfolder_names = []  # Remove 'LocalStorage' from the list

        # Check if the main folder exists
        main_folder_path = os.path.join(local_appdata, main_folder_name)
        if not os.path.exists(main_folder_path):
            os.makedirs(main_folder_path)

        file_path = os.path.expanduser('~\\AppData\\Local\\SpeechToText\\speech.txt')

        if os.path.exists(file_path):
            pass
        else:
            with open(file_path, "w") as file:
                text = f'''Welcome To SpeechToText v{SpeechToText_Version}\n\nClick "Start" to record your voice into transcript.\n\n\nThank you for using the program!'''
                file.write(text)

    # Call the function to create the folders
    CreateFolders()
    # ============================================================================= #
    
    # Icon Installer
    # =============================================================================================== #
    def icon():
        try:
            # Extract the "class" value from the "SpeechIco" key
            SpeechToText_ico_file = ClientBootstrapper

            # Fetch the JSON data
            response = requests.get(SpeechToText_ico_file)
                
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON data
                data = json.loads(response.text)
                    
                # Extract the "class" value from the "SpeechEngine" key
                SpeechToText_ico_file = data.get("SpeechIco", {}).get("value", "")

            if SpeechToText_ico_file:
                # Define the URL of the icon to download
                icon_url = SpeechToText_ico_file

                # Define the destination directory in AppData\Local
                destination_directory = os.path.join(os.environ['LOCALAPPDATA'], 'SpeechToText')

                # Check if the destination directory exists, and create it if it doesn't
                if not os.path.exists(destination_directory):
                    os.makedirs(destination_directory)

                # Construct the full destination path by joining the directory and the file name
                destination_path = os.path.join(destination_directory, 'Speech.ico')

                # Check if the icon file already exists in the destination directory
                if not os.path.exists(destination_path):
                    # Download the icon from the URL
                    response = requests.get(icon_url, stream=True)
                    if response.status_code == 200:
                        with open(destination_path, 'wb') as file:
                            shutil.copyfileobj(response.raw, file)
        except Exception as e:
            messagebox.showerror("SpeechToText Error","Check your internet connection and try again.")
            sys.exit()

    # Call the icon() function to check and download the icon if necessary
    icon()
    # =============================================================================================== #

    #This will check if the Settingsicon exists or not if not then it will installs it
    #=================================================================================================#
    def Settings_icon():
        try:
            # Extract the "class" value from the "SpeechIco" key
            SpeechToText_settings_icon = ClientBootstrapper

            # Fetch the JSON data
            response = requests.get(SpeechToText_settings_icon)
                
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON data
                data = json.loads(response.text)
                    
                # Extract the "class" value from the "SpeechEngine" key
                SpeechToText_settings_icon = data.get("SpeechSettingsIco", {}).get("value", "")

            if SpeechToText_settings_icon:
                # Define the URL of the icon to download
                icon_url = SpeechToText_settings_icon

                # Define the destination directory in AppData\Local
                destination_directory = os.path.join(os.environ['LOCALAPPDATA'], 'SpeechToText')

                # Check if the destination directory exists, and create it if it doesn't
                if not os.path.exists(destination_directory):
                    os.makedirs(destination_directory)

                # Construct the full destination path by joining the directory and the file name
                destination_path = os.path.join(destination_directory, 'Settings.png')

                # Check if the icon file already exists in the destination directory
                if not os.path.exists(destination_path):
                    # Download the icon from the URL
                    response = requests.get(icon_url, stream=True)
                    if response.status_code == 200:
                        with open(destination_path, 'wb') as file:
                            shutil.copyfileobj(response.raw, file)
        except Exception as e:
            messagebox.showerror("SpeechToText Error","Check your internet connection and try again.")
            sys.exit()
    
    Settings_icon()
    #=================================================================================================#

    #This will check if MicSettingsjson file exists or not
    #=================================================================================================================================#
    def Mic_Settings_Json():
        # Initialize PyAudio
        audio = pyaudio.PyAudio()

        # Get the number of available devices
        num_devices = audio.get_device_count()

        # Create a list to store device information
        devices_info = []

        # Identify the default recording device index
        default_device_index = None

        # Iterate through all devices and filter recording devices
        for device_index in range(num_devices):
            device_info = audio.get_device_info_by_index(device_index)

            if device_info['maxInputChannels'] > 0 and device_info['hostApi'] == audio.get_host_api_info_by_index(0)['index']:
                device = {
                    'recording_device_name': device_info['name'],
                    'recording_device_channel': device_index
                }
                devices_info.append(device)

                if default_device_index is None:
                    default_device_index = device_index

        # Save the first default recording device information to a JSON file
        if default_device_index is not None:
            with open(os.path.expanduser('~\\AppData\\Local\\SpeechToText\\micsettings.json'), 'w') as json_file:
                json.dump(devices_info[0], json_file, indent=4)

        # Terminate PyAudio
        audio.terminate()
    
    if os.path.exists(os.path.expanduser('~\\AppData\\Local\\SpeechToText\\micsettings.json')):
        pass
    else:
        Mic_Settings_Json()
    #=================================================================================================================================#

    #Update Notifider
    #====================#
    UpdateNotifier()
    #====================#