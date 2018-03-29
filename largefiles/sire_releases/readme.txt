Place the URL of the file into "redirect_XXXXXX" where XXXXX is the name passed
to download.php. This will automatically redirect to the file in the URL.

For Azure uploads, I created a storage account called sire in westeurope using

```
$ az group create --name sire --location westeurope
```

(I used the Azure console to create a storage account in the 'sire' resource group
 that uses cold storage and is called 'sire')

I then got and set the login keys usin

```
$ az storage account keys list --account-name sire --resource-group sire --output table
KeyName    Permissions    Value
---------  -------------  ----------------------------------------------------------------------------------------
key1       Full           LOGIN_KEY

$ export AZURE_STORAGE_ACCOUNT="sire"
$ export AZURE_STORAGE_ACCESS_KEY="LOGIN_KEY"
```

Next I created a container called 'releases' for the group

```
az storage container create --name releases
```

Next, I uploaded the files using

```
az storage blob upload --container-name releases --name sire_2018_1_0_linux.run --file ./sire_2018_1_0_linux.run
az storage blob upload --container-name releases --name sire_2017_3_0_linux.run --file ./sire_2017_3_0_linux.run
az storage blob upload --container-name releases --name sire_2018_1_0_osx.run --file ./sire_2018_1_0_osx.run 
az storage blob upload --container-name releases --name sire_2017_3_0_osx.run --file ./sire_2017_3_0_osx.run
```

I could list these using

```
az storage blob list --container-name releases --output table 
Name                     Blob Type    Blob Tier        Length  Content Type              Last Modified              Snapshot
-----------------------  -----------  -----------  ----------  ------------------------  -------------------------  ----------
sire_2017_3_0_linux.run  BlockBlob    Cool          951373821  application/octet-stream  2018-03-29T11:26:29+01:00
sire_2017_3_0_osx.run    BlockBlob    Cool          770306858  application/octet-stream  2018-03-29T11:28:39+01:00
sire_2018_1_0_linux.run  BlockBlob    Cool         1027908067  application/octet-stream  2018-03-29T11:25:22+01:00
sire_2018_1_0_osx.run    BlockBlob    Cool          985339085  application/octet-stream  2018-03-29T11:27:47+01:00
```

From the Azure console I was then able to set the access policy of the "releases"
container to "public", and then get the public URL. These look like

```
https://sire.blob.core.windows.net/releases/sire_2018_1_0_osx.run
```

I've tested this and it downloads correctly :-)

