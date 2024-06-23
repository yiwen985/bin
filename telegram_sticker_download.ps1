$url = Read-Host "enter link"

c:/Users/aa/AppData/Local/sticker-convert/sticker-convert.exe --no-confirm --download-auto $url --telegram-token <token> --output-dir C:/Users/aa/Downloads/'Telegram Desktop'/stickers_output --preset custom --vid-format ".gif" --img-format ".png" 

explorer C:\Users\aa\Downloads\'Telegram Desktop'\stickers_output