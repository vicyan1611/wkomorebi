global komorebic := "C:\Users\vinhp\scoop\apps\komorebi\0.1.25\komorebic-no-console.exe "
~LWin::Send "{Blind}{vkE8}" ;disable normal windows key but keep windows key combinnations work
; #q::
; {
;     Run komorebic . "start"
; }

#q::Run "C:\Users\vinhp\AppData\Local\Microsoft\WindowsApps\wt.exe" ;run terminal


; manipulate windows
#t::Run komorebic . "toggle-float"

; create workspaces
#!+n::Run komorebic . "new-workspace"

; workspaces
#1::Run komorebic . "focus-workspace 0"
#2::Run komorebic . "focus-workspace 1"
#3::Run komorebic . "focus-workspace 2"
#4::Run komorebic . "focus-workspace 3"
#5::Run komorebic . "focus-workspace 4"
#6::Run komorebic . "focus-workspace 5"
#7::Run komorebic . "focus-workspace 6"
#8::Run komorebic . "focus-workspace 7"

; move windows across workspaces
#+1::Run komorebic . "move-to-workspace 0"
#+2::Run komorebic . "move-to-workspace 1"
#+3::Run komorebic . "move-to-workspace 2"
#+4::Run komorebic . "move-to-workspace 3"
#+5::Run komorebic . "move-to-workspace 4"
#+6::Run komorebic . "move-to-workspace 5"
#+7::Run komorebic . "move-to-workspace 6"
#+8::Run komorebic . "move-to-workspace 7"

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

; flip layouts
#x::Run komorebic . "flip-layout horizontal"
#y::Run komorebic . "flip-layout vertical"

; TODO: handle mouse scrolling