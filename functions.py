import subprocess

"""
def ssh_command(server, username, command):
    #Execute a command on a remote server via SSH.
    try:
        # Build the SSH command
        ssh = ["ssh", f"{username}@{server}", command]

        # Execute the command using subprocess
        result = subprocess.run(ssh, capture_output=True, text=True, check=True)

        # Print the output of the command
        print("Output:")
        print(result.stdout)

        # Print any error message
        if result.stderr:
            print("Error:")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace these values with your server's details
    remote_server = "your_remote_server_ip_or_hostname"
    remote_username = "your_username"
    command_to_run = "ls -l"  # Example command

    ssh_command(remote_server, remote_username, command_to_run)
"""
# there will be 2d array for 
#dates is an array (dates)
def downloadLog(log,dates_status,dates,node):
    print(type(dates))
    valid_dates=ret_valid_date(dates_status,dates)
    #print(valid_dates)
    if log[0] == True: # Application Logs
        #Application log install subroess
        print(f"Application Logs {node}")
        #install_file_via_scp(node,"/home/ofsert/Desktop/PySub/logsTest/{node}/current_session*")
        #install_file_via_scp(node,"/mnt/c/Users/omer/Desktop/Havelsan/Qt/pythongui/logstest/{node}/current_session*")
        #for i in range(len(valid_dates)):
        #    download_directory_via_scp(node,f"/mnt/c/Users/omer/Desktop/Havelsan/Qt/pythongui/logstest/{node}/")
        for i in range(len(valid_dates)):
            download_directory_via_scp(node,f"/home/ofsert/Desktop/git/pythongui/PySub/logsTest/{node}/application_logs",valid_dates[i])
    if log[1] == True: #Core Dumps
        print(f"CoreDumps {node}")
        for i in range(len(valid_dates)):
            download_directory_via_scp(node,f"/home/ofsert/Desktop/git/pythongui/PySub/logsTest/{node}/",valid_dates[i])
        #Core dumps install subprocess
    if log[2] == True: #Genieware Logs
        print(f"Genieware Logs {node}")
        # Genieware log install subprocess
    if log[3] == True: #OS Logs
        print(f"OS Logs {node}")
        #OS Logs install subprocess
    if log[4] == True: #System Logs
        print(f"System Logs {node}")
        #System Logs install subprocess
    #else:
    #    print(f"Nothing chosen {node}")

def ListNodes():
    #Creting list for returning the nodes
    nodes = []
    returnlist = []
    #Creating Node Listing process
    #NodeList = ["cat $ANSIBLE_INVENTORY | grep -v '#' | grep -v '\[' | grep -v '^$' | cut '-' -f1,2"] # Target
    NodeList = ["cat", "/home/ofsert/Desktop/git/pythongui/PySub/test.txt"] #Internet
    #NodeList = ["cat", "/mnt/c/Users/omer/Desktop/Havelsan/Qt/pythongui/test.txt"] #Home
    nodes=subprocess.run(NodeList, capture_output=True, text=True, check=True)
    #print (nodes.stdout.splitlines()[0])
    return nodes.stdout.splitlines()

def ListDates(node):
    #Creating Dates list
    dates = []
    datesraw = []
    datesfinal = []
    #Creating Date Listing Process
    DateList = ["ls",f"/home/ofsert/Desktop/git/pythongui/PySub/logsTest/{node}/."] # Internet
    #DateList = ["ls",f"/mnt/c/Users/omer/Desktop/Havelsan/Qt/pythongui/logstest/{node}/."] #Home
    dates = subprocess.run(DateList, capture_output=True, text=True, check=True)
    #print(len(dates.stdout.splitlines()))
    datesraw = dates.stdout.splitlines()
    for i in range(len(datesraw)):
        if datesraw[i][0] == 'c':
            datesfinal.append(datesraw[i])
        else:
            datesfinal.append(datesraw[i][0:8])
    #print(datesfinal)
    return datesfinal

# Function to copy a file or directory using scp
def install_file_via_scp(target_node, target_path):
    # Define the source file and the scp command
    source_file = "~/."  # Update this if you want to copy a directory
    scp_command = ["scp", "-r", source_file, f"{target_node}:{target_path}"]  # Added -r for recursive

    try:
        # Execute the scp command using subprocess
        result = subprocess.run(scp_command, shell=True, capture_output=True, text=True, check=True)

        # Print the output of the command
        print("Output:")
        print(result.stdout)

        # Print any error message
        if result.stderr:
            print("Error:")
            print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Function to download a directory using scp
def download_directory_via_scp(target_node, source_path,date):
    #local_destination = "/home/aa/."
    local_destination="/home/ofsert/."
    # Define the scp command for downloading
    #scp_command = [f"scp -r 127.0.0.1:{source_path} {local_destination}"]  # Added -r for recursive #127.0.0.1 is the local machine it wll change to target_node
    ls_command = [f"ls /home/ofsert/Desktop/git/pythongui/PySub/logsTest/{target_node}/. | grep {date}"]
    filen = subprocess.run(ls_command, capture_output = True, text=True, check=True, shell=True)
    print(filen.stdout)
    download_file_name=filen.stdout.splitlines()[0]
    #tar_command = [f"ssh 127.0.0.1 'tar -C {source_path} -cvzf /var/tmp/{date}.tar {date}*'"]
    scp_command = [f"scp -r 127.0.0.1:/home/ofsert/Desktop/git/pythongui/PySub/logsTest/{target_node}/{download_file_name} {local_destination}"]
    try:
        # Execute the scp command using subprocess
        
        result = subprocess.run(scp_command, capture_output=True ,shell=True,text=True, check=True)

        # Print the output of the command
        #print("Output:")
        #print(result.stdout)

        # Print any error message
        #if result.stderr:
        #    print("Error:")
        #    print(result.stderr)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example usage
# install_file_via_scp("127.0.0.1", "/desired/target/path/")
# download_directory_via_scp("127.0.0.1", "/path/to/remote/directory", "/local/destination/path/")

def ret_valid_date(datesStatus,dates):
    valid_dates=[]
    for i in range(len(dates)):
        if datesStatus[i] == True:
            valid_dates.append(dates[i])
    return valid_dates 