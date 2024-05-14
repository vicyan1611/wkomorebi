global komorebic := "C:\Users\vinhp\scoop\apps\komorebi\0.1.25\komorebic-no-console.exe "
~LWin::Send "{Blind}{vkE8}"
; #q::
; {
;     Run komorebic . "start"
; }

#q::Run "C:\Users\vinhp\AppData\Local\Microsoft\WindowsApps\wt.exe" ;run terminal


; manipulate windows
#t::Run komorebic . "toggle-float"

; workspaces
#1::Run komorebic . "focus-workspace 0"
#2::Run komorebic . "focus-workspace 1"
#3::Run komorebic . "focus-workspace 2"
#4::Run komorebic . "focus-workspace 3"

; move windows across workspaces
#+1::Run komorebic . "move-to-workspace 0"
#+2::Run komorebic . "move-to-workspace 1"
#+3::Run komorebic . "move-to-workspace 2"

; change focus windows
#Left::Run komorebic . "focus left"
#Down::Run komorebic . "focus down"
#Right::Run komorebic . "focus right"
#Up::Run komorebic . "focus up"

; move windows
#+Left::Run komorebic . "move left"
#+Down::Run komorebic . "move down"
#+Right::Run komorebic . "move right"
#+Up::Run komorebic . "move up"
