import os
import json
import platform


# Function to execute commands from json file and create CSV to store system memory information
def execute_cmds(cmds_file_path):
    try:
        # Read json file to assess OS and Memory commands
        with open(cmds_file_path, 'r') as f:
            cmds_dict = json.load(f)

        # Check the operating system
        system = platform.system()
        if system == 'Linux':
            # Check Linux OS flavor
            os_name = os.popen(cmds_dict['os_flavor']).read().strip()
            if os_name == 'Ubuntu' or os_name == 'RedHat':
                # Execute the command to get system memory information
                output = os.popen(cmds_dict['mem_cmd']).read().strip()

                # Create the CSV file and write the output
                csvfile_path = 'mem_info.csv'
                with open(csvfile_path, 'w') as f:
                    f.write(output)
                    
                return True  # Return True if the CSV file was created
            else:
                print(f'Found different Linux flavor: {os_name}')
        else:
            print(f'Unsupported operating system: {system}')
    except Exception as e:
        print(f'This error occurred: {e}')


if __name__ == '__main__':
    # Call the function to create the CSV file
    execute_cmds(os.path.abspath('cmds_file.json'))
    print('Data stored successfully in CSV file!')
