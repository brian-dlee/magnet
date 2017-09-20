
import os
import sys

import paramiko

class SFTPDownloader(object):
    """
    Implentation of a simple file downloader using SFTP
    Built on top of paramiko
    """

    @staticmethod
    def display_percent_complete(transferred, total):
        """
        Simple convenience method to display completion by percentage downloaded
        :param transferred int Number of bytes tranferred
        :param total int Total number of bytes to tranfer
        """
        if transferred != total:
            percent_completed = round(float(transferred) / total * 100, 1)
            sys.stdout.write('\rPercent Completed: ' + str(percent_completed) + '%')
        else:
            sys.stdout.write('\rComplete' + (' ' * 10))

        sys.stdout.flush()

    @staticmethod
    def get_host_key_matching_host(hostname, known_hosts_file=None):
        """
        Returns the first host key matched by the provided hostname.
        Reads from the system default known_hosts file or by param if supplied.
        :param hostname str Host name to find key for
        :param known_hosts_file str Optional path to a known_hosts file.
                                    System default is assumed if ommitted
        :return paramiko.PKey
        """
        used_known_hosts_file = known_hosts_file

        if not known_hosts_file:
            used_known_hosts_file = os.path.expanduser(os.path.join('~', '.ssh', 'known_hosts'))

        host_keys = paramiko.util.load_host_keys(used_known_hosts_file)
        return host_keys.lookup(hostname).items()[0][1]

    @staticmethod
    def load_private_key_from_file(private_key_file, password=None, type='RSA'):
        """
        Returns a paramiko.PKey object based on the file provided.
        :param private_key_file Path to private key
        :param password str Optional password if private key requires it
        :param type str Optional key type; RSA is assumed
        :return paramiko.Pkey
        """
        if type == 'RSA':
            return paramiko.RSAKey.from_private_key_file(private_key_file, password)
        else:
            return None

    def __init__(self, username, host, private_key_file, port=22, callback=None):
        self.username = username
        self.host = host
        self.port = port
        self.private_key_file = private_key_file
        self.callback = callback

        self.__host_key = SFTPDownloader.get_host_key_matching_host(self.host)
        self.__private_key = SFTPDownloader.load_private_key_from_file(private_key_file)
        self.__sftp_client = None
        self.__transport = None

        self.__establish_connection()

    def __establish_connection(self):
        self.__transport = paramiko.Transport((self.host, self.port))
        self.__transport.connect(self.__host_key, self.username, pkey=self.__private_key)

    def get_file(self, remote_file_path, local_file_path, callback=None):
        """
        Downloads a remote file and stores it at a local path
        :param remote_file_path str Remote path to file
        :param local_file_path str Local path to destination
        :param callback function Optional param to override callback
        """
        if self.__sftp_client is None:
            self.initialize_client()

        used_callback = callback if callback else self.callback
        return self.__sftp_client.get(remote_file_path, local_file_path, used_callback)

    def initialize_client(self):
        """
        Establishes the paramiko.SFTPClient so it's ready to download files
        """
        self.__sftp_client = paramiko.SFTPClient.from_transport(self.__transport)
