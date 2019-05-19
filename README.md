# Azure Blob Operations

This repository will assist you in interacting with the Azure blob. i.e. Uploading, Downloading and Deleting a file in Azure.
Before we start will those operations. A quick overview on how blob is created.
There are various methods to do that, but the one discussed here is through azure cli `az`

Note: Make sure you have Azure cli installed [https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest]

- Login to your Azure account via. command below
```bash
az login
```

- Select a subscription which will be used to create a resource group
```bash
az account set --subscription `subscription_name`
```
Variables to replace:
`subscription_name`

- Create a resource group 
```bash
az group create --name `resource_group` --location `location`
```
Variables to replace:
`resource_group`
`location`: e.g. northeurope

- Create the storage account 
```bash
az storage account create --name `storage_account` --resource-group `resource_group` \
--location `location` --sku Standard_RAGRS --kind StorageV2
```
Variables to replace:
`storage_account`
`resource_group`
`location`: e.g. northeurope

