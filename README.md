# SFTPDownloader
Simple module built using [Paramiko](http://docs.paramiko.org/en/2.1/index.html) for downloading files via SSH.

# Example Usage:
```python
import os

import sftpdownloader

def main():
    """
    Example script main function
    """

    private_key_file = os.path.expanduser(os.path.join('~', '.ssh', 'id_rsa'))

    downloader = sftpdownloader.SFTPDownloader(
        'remoteuser',
        'sftp.server.com',
        private_key_file,
        callback=sftpdownloader.SFTPDownloader.display_percent_complete)
    downloader.get_file('file.txt', r'C:\Users\auserhasnoname\Desktop\file.txt')

if __name__ == '__main__':
    main()
```

# Output:
```
brian@LAPTOP-071C4V5H MINGW64 ~/Documents/Workspace/Work Projects/orion-network-solutions/SFTPDownloader
$ python "c:/Users/brian/Documents/Workspace/Work Projects/orion-network-solutions/SFTPDownloader/example.py"
C:\Users\brian\.ssh\known_hosts
Complete           100.0%
```