# BananaCreater

Banana Creator is part of Banana zero.

## Script Descritpion

It will install system and packages configuration, needed scripts, services, and will install all required packages for the Pi Zero W to work over a fresh Raspbian Lite.

Simply launch the folllowing command within Rapsbian Lite :

```
bash bashHelper.sh
```

## Features

- USB Gadget : Mass Storage and UAC2
- Samba share ( points to Mass storage USB gadget which is a partition on the SD Card)
- AccessPoint and Traffic routing
- [WAPPIC](https://github.com/Azkali/BananaPi/WAPPIC)
- Takes advantage of systemctl services

Ships with :
- Emulationstation
- Mopidy
