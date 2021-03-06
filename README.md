# nextcloud-sync-fix
Replaces all files with their "(conflicted copy)" version. Useful after changing your local Nextcloud folder location and Nextcloud decides to rename all your work.

# Scenarios this might be useful

1. You've got all your files synced to your Nextcloud. You send your laptop off to get some work done and in the meantime you use a spare laptop with a copy of your work on it. When you get your laptop back, you copy the new files you made into the Nextcloud folder on your main laptop. Some time later, Nextcloud tells you that there are conflicting copies, and it's renamed and replaced all your files with the server versions. 

2. You've purchased a new computer, or upgraded your hard drive. You download the Nextcloud client and click yes to all the syncs, expecting it to redownload everything, but nothing happens. You then decide to copy all the files from your old hard drive to the new one, and you expect Nextcloud to verify your files are the same as the ones on the server without an issue. You then go about your work, saving changes to the Nextcloud folder, but some time later, you are informed that 971 files in 182 directories conflict with the server, so they've all been renamed and replaced with the server versions.

In both cases, your only choice now is to find and change every file to the version that you want. If you've only changed one or two, it's no problem, but if you've changed a lot, or you're part of a big team, this is a nightmare. 

# So what do?
This simple python script will walk through your entire file-system, starting from the directory it is placed in, and replace the server version with the (conflicted copy) version if it finds that one exists. It doesn't save the server version, nor check the file timestamps, because those could be messed up through syncing issues. It just flips the cards so Nextcloud takes your local version as the desired copy and not the one that's still on the server. 

### what?

Okay, so say your nextcloud folder was this on the server:
```
/stuff/
  file1.doc
  file2.xls
```

You then fell out of sync and did some work, moved folders, whatever, and the server is still as above but your local file system is now this:
```
/stuff/
  file1.doc (unchanged)
  file2.xls (changed)
  file3.ppt (new)
```
This is what Nextcloud will do to your local folder when it next syncs to the new folder:
```
/stuff/
  file1.doc
  file2.xls                                        <-------- SERVER VERSION
  file2 (conflicted copy YYYY-MM-DD HHMMSS).xls    <-------- YOUR NEW VERSION
  file3.ppt
```
It's no big deal if you have to change one or two files, but if you have many to change, then you'll find this script handy.
**IT WILL NOT SAVE YOUR SERVER VERSIONS FROM THEIR FATE**, so be sure to only run this if you want 100% of the conflicts to favor your local version instead of the server version. Once you run it from your base nextcloud folder, your folder in the above example will look like this:
```
/stuff/
  file1.doc
  file2.xls                                        <-------- YOUR NEW VERSION
  file3.ppt
```

# Ok how run?
First, make sure your client is synced and all damage it is going to do has been done. Then if you haven't got python installed [do that](https://python.org)
After that, open up powershell, go to your base Nextcloud folder and then:

### download script manually through...
#### powershell
```
wget https://raw.githubusercontent.com/zeroepix/nextcloud-sync-fix/main/nextcloud-make-conflicts-real.py -OutFile nextcloud-make-conflicts-real.py
```
#### or bash
```
wget https://raw.githubusercontent.com/zeroepix/nextcloud-sync-fix/main/nextcloud-make-conflicts-real.py
```
#### run it
```
python nextcloud-make-conflicts-real.py
```

It will run through and report what it's doing. After that, Nextcloud should sync your changes and you can carry on carrying on.