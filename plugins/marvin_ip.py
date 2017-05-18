import subprocess

def ip():
    proc = subprocess.Popen(['dig +short myip.opendns.com @resolver1.opendns.com'], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()

    print('    Your public IP address is ' + str(out.decode("utf-8")))


commands = [('ip', ip)]
help_options = [('ip', 'Gives you your current ip')]
