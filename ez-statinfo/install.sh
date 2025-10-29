#!/bin/bash

# Install ez-statinfo.py: Copies to $HOME and adds to menu
# Licensed under the MIT License

install_ez-statinfo() {
    local source_file="ez-statinfo.py"
    local target_file="$HOME/ez-statinfo.py"
    local desktop_file="$HOME/.local/share/applications/ez-statinfo.desktop"

    echo "Do you want to install ez-statinfo? (y/n)"
    read -r inst

# Copy ez-statinfo.py to $HOME

    if [[ "$inst" =~ ^[yY]$ ]]; then
        cp "$source_file" "$target_file"
        chmod +x "$target_file"
        echo "ez-statinfo.py has been copied to $HOME"

# Create .desktop file for menu 

        mkdir -p "$HOME/.local/share/applications"
        cat > "$desktop_file" << EOL
[Desktop Entry]
Name=Easy System Info
Comment=Display CPU, RAM, and Disk usage
Exec=python3 $target_file
Type=Application
Terminal=false
Categories=System;Utility;
EOL
        echo "Menu entry created at $desktop_file"
        echo
        echo "Done!"
        echo

        sleep 1
    elif [[ "$inst" =~ ^[nN]$ ]]; then
        echo "Operation cancelled"
        echo
    else
        echo "Invalid input. Please respond with 'y' or 'n'."
        echo
    fi
}

main() {
    install_ez-statinfo
}

main
