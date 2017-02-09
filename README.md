# Tractor
Download files over different protocols with ease. Currently only supports SFTP, but soon to support HTTP and FTP.

**Credits**
- SFTP module built using [Paramiko](http://docs.paramiko.org/en/2.1/index.html).

## Example Usage:
```python
import os

import tractor

def main():
    """
    Example script main function
    """

    private_key_file = os.path.expanduser(os.path.join('~', '.ssh', 'id_rsa'))

    downloader = tractor.SFTPDownloader(
        'remoteuser',
        'sftp.server.com',
        private_key_file,
        callback=tractor.SFTPDownloader.display_percent_complete)
    downloader.get_file('file.txt', r'C:\Users\auserhasnoname\Desktop\file.txt')

if __name__ == '__main__':
    main()
```

## Output:
```
brian@LAPTOP-071C4V5H MINGW64 ~/Documents/Workspace/Projects/orion-network-solutions/tractor
$ python "c:/Users/brian/Documents/Workspace/Projects/orion-network-solutions/tractor/example.py"
Complete           100.0%
```
