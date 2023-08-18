# Dependencies
Before setting up, you will need `GnuPG`, the `GPG PASS` script and `Poetry`  
- https://python-poetry.org/  
- https://wiki.archlinux.org/title/GnuPG  
- https://wiki.archlinux.org/title/Pass  

# Configuration
To start, you need to generate `GnuPG keys`, create a new encrypted password using `Pass`, and pass the path to the encrypted password to `start.sh`

## GnuPG
Generate GnuPG keys:  
    `gpg --full-key-gen`
    
Init PASS directory:  
    `pass init user@mail.com`
    
Create new encripder password:  
    `pass insert Category/Password`
    
## Configurate
Change in `start.sh` `GNUPG_PASS_DIR` the path to your encrypted password:
