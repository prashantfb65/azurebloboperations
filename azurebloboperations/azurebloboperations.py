import os
from azure.storage.blob import \
    BlockBlobService, PublicAccess


class AzureBlobOperations(object):
    """
    This class is for the Azure file related operations.
    One can upload, download and delete the file using this class
    To initialize the constructor you will need to supply three attributes
    to it

    account name (mandatory)
    account key (mandatory)
    container name (optional)
    """

    def __init__(self, account_name=None, account_key=None
                 , container_name=None):
        """
        Axure blob operation initialization
        :param account_name: account name azure
        :param account_key: key to the account name created
        :param container_name: container name in which file is to be
        downloaded, uploaded or deleted from
        """
        if not account_name:
            raise ValueError(f'Account Name can not be empty {account_name}')
        if not account_key:
            raise ValueError(f'Key to access the blob can not be empty {account_key}')
        self._blob_service = BlockBlobService(account_name=account_name, account_key=account_key)
        if not self._blob_service:
            raise Exception(f'The blob service could not be initialized for {account_name}!')
        if not container_name:
            self._container_name = 'default'
        else:
            self._container_name=container_name
        print(f'Blob service for {account_name} initialized!')

    def _create_container(self):
        """
        Method to create the container in the blob
        uploaded, deleted and downloaded from
        :return: true if the container is created successfully
        """
        return self._blob_service.create_container(self._container_name)

    def _set_container_acl(self):
        """
        Setting container ACL
        :return: None
        """
        try:
            self._blob_service.set_container_acl\
                (self._container_name, public_access=PublicAccess.Container)
        except Exception as error:
            raise Exception(f'Problem while setting the ACL for '
                            f'container {self._container_name}') from error

    def upload_file_to_blob(self, file_path=None):
        """
        Method is used to upload the file to the
        Azure blob
        :param file_path: path to the file on the local drive
        :return: true if upload successful
        """
        try:
            if not file_path:
                raise Exception('The file path for uploading the file missing')
            if not os.path.exists(file_path):
                raise Exception(f'The file path {file_path} does not exist !')
            if not os.path.isfile(file_path):
                raise Exception(f'{file_path}, is not a file !')
            local_file_name = os.path.splitext(file_path)[0]
            self._create_container()
            container_name = self._set_container_acl()
            self._blob_service.create_blob_from_path(container_name,
                                                     local_file_name,
                                                     file_path)
            return True
        except Exception as error:
            raise Exception(f'Problem while uploading the file '
                            f' {file_path} to Azure') from error

    def download_file_from_blob(self, file_name, download_path=None):
        """
        Method to download the file from Azure blob
        :param file_name: name of the file to be downloaded
        :param download_path: local folder path where this file is to be downloaded
        :return: true if file is downloaded successfully
        """
        try:
            if not download_path:
                download_path = os.path.curdir()
            if not os.path.isdir(download_path):
                raise Exception(f'The download path {download_path} is not a valid folder !')
            container_name = self._container_name
            self._blob_service.get_blob_to_path(container_name,
                                                file_name,
                                                download_path)
            return True
        except Exception as error:
            raise Exception(f'Problem while downloading the file '
                            f' {file_name} from Azure') from error

    def delete_file_from_blob(self, file_name, delete_container='N'):
        """
        Delete the file from Blob
        :param file_name: name of file in blob
        :param delete_container: by default 'N' meaning that it will not
        delete the container, 'Y' will delete the container along with the
        file
        :return: True if deletion successful
        """
        try:
            self._blob_service.delete_blob(container_name=self._container_name,
                                           blob_name=file_name)
            print(f'File: {file_name} deleted ..')
            if delete_container == 'Y':
                self._blob_service.delete_container(container_name=self._container_name)
        except Exception as error:
            raise Exception(f'Problem while deleting the file '
                            f' {file_name} from Azure, '
                            f'container {self._container_name}') from error


if __name__ == '__main__':
    account_name = os.environ['AZ_ACCOUNT_NAME']
    account_key = os.environ['AZ_ACCOUNT_KEY']
    container_name = os.environ['AZ_CONTAINER_NAME']
    azops = AzureBlobOperations(account_name=account_name,
                                account_key=account_key,
                                container_name=container_name)

    # upload a file to azure blob
    file_path = ''  # insert file path here
    file_name = ''  # insert file name here
    download_path = ''  # path where you want to download the file to

    # Uncomment the below for different operations:
    # azops.upload_file_to_blob(file_path=file_path)
    # azops.download_file_from_blob(file_name, download_path=download_path)
