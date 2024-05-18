<h1 align="center" > Komorebi using Windows key</h1>

<p align="center">
  <img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/palette/macchiato.png" width="400" />
</p>

>This project is inspired by [Yasb](https://github.com/da-rth/yasb) and [komoTray](https://github.com/urob/komotray) and uses [komorebi](https://github.com/LGUG2Z/komorebi). I want to implement the code again so that I can improve my skills. Thanks a lot and keep up the good work!

![image](https://github.com/vicyan1611/wkomorebi/assets/56020046/742e0fb9-2d77-4ff3-a229-32dee8bcb1c4)


Wkomorebi is a tray status indicator for the [komorebi](https://github.com/LGUG2Z/komorebi) windows tiling manager, and it also contains my AutoHotkey script that disables the Windows (SUPER) button but keeps combinations of Windows button working. Wkomorebi shows the focused workspace and monitor and can be use to interact with komorebi.

 I highly recommend using the [wkomorebi.ahk](https://github.com/vicyan1611/wkomorebi/blob/main/wkomorebi.ahk) config with the flow launcher, if you don't, you can edit the file so that the Windows button still works.



https://github.com/vicyan1611/wkomorebi/assets/56020046/53cf1283-1826-42e0-9178-a0cbf140ea74

## How to install

1. Clone this repository.
2. Install all packages in the requirements file using ` pip install -r requirements.txt`
3. Run [`wkomorebi_tray.py`](https://github.com/vicyan1611/wkomorebi/blob/main/sources/wkomorebi_tray.py), note that it also starts the `komorebi` process. 
4. Run `wkomorebi.ahk`

**Change hotkey config in [`wkomorebi.ahk`](https://github.com/vicyan1611/wkomorebi/blob/main/wkomorebi.ahk)**

## Contribution
Feel free to contribute to this project and make it better.