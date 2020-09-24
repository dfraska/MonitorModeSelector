#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

; To start with PC, press Win+R, then type "shell:startup" and press
; enter. Create a shortcut to this script.

#p::Run .\runnhide\RunNHide.exe .\MonitorModeSelector.bat