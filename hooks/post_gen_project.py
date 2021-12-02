import subprocess

subprocess.call(['git', 'init', '--initial-branch=main'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

