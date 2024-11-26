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
def downloadLog(log,dates,node):
    if log[0] == True: # Application Logs
        #Application log install subroess
        print(f"Application Logs {node}")
    if log[1] == True: #Core Dumps
        print(f"CoreDumps {node}")
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
    #NodeList = ["cat $ANSIBLE_INVENTORY | grep -v '#' | grep -v '\[' | grep -v '^$' | cut '-' -f1,2"]
    NodeList = ["cat", "/home/ofsert/Desktop/PySub/test.txt"]
    nodes=subprocess.run(NodeList, capture_output=True, text=True, check=True)
    #print (nodes.stdout.splitlines()[0])
    return nodes.stdout.splitlines()

def ListDates(node):
    #Creating Dates list
    dates = []
    datesraw = []
    datesfinal = []
    #Creating Date Listing Process
    DateList = ["ls",f"/home/ofsert/Desktop/PySub/logsTest/{node}/."]
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