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
#dates is an array (dates)
def downloadLog(log1,log2,log3,log4,log5):
    if log1 == True: # Application Logs
        #Application log install subroess
        print("Application Logs")
    if log2 == True: #Core Dumps
        print("CoreDumps")
        #Core dumps install subprocess
    if log3 == True: #Genieware Logs
        print("Genieware Logs")
        # Genieware log install subprocess
    if log4 == True: #OS Logs
        print("OS Logs")
        #OS Logs install subprocess
    if log5 == True: #System Logs
        print("System Logs")
        #System Logs install subprocess
    else:
        print("Nothing chosen")

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