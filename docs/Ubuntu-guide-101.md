## Ubuntu default settings 
https://askubuntu.com/questions/114429/default-save-directory-for-gnome-screenshot
**Cursor settings**

# Via GUI

Install dconf-editor
http://apt.ubuntu.com/p/dconf-tools

From the command line, run the command sudo apt-get install dconf-editor
Or click here to install from the Ubuntu Software Center:

Install via the software centerfile:///home/user/Desktop/
https://apps.ubuntu.com/cat/applications/dconf-editor

Press Alt + F2 and type dconf-editor

Go to org -> gnome -> gnome-screenshot

At "auto-save-directory" type the desired directory in the following format: file:///home/user/Desktop/

name: auto-save-directory, value: file:///full/path/

A tip for anyone who is using the configuration editor in unity: click on the arrow to the left the org text to expand it.

## System and Hardware Information in Linux

```bash
sudo lshw
```


You can print a summary of your hardware information by using the -short option.

```bash
sudo lshw -short
```


```bash
sudo lshw -html > lshw.html
```


## How to View Linux CPU Information

```bash
lscpu
```


for more click [here](https://www.tecmint.com/commands-to-collect-system-and-hardware-information-in-linux/)



