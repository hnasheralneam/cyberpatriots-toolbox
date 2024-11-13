# Cyberpatriots Script Toolbox
**Because doing it by hand is like hard or something**

This repository contains a collection of scripts that address a specific part of the Cyberpatriots hardening requirements. The reason I've broken them up instead of putting them in a monolithic script is because this modularity allows us to use each script for one item on the checklist. The benefit of this is that we know exactly what's been done, what's left, and if something goes wrong it can be traced back to one script. Additionally, if the requirements vary from those of past competitions, we can drop scripts as needed.  
Python comes preinstalled on the Ubuntu image provideded by Cyberpatriots, so any script can be run like this: `python3 <script_name>`. Some scripts will need to be run as admin, so make sure to read the headers of the scripts with `cat <script_name>` before running.  
<br>
Recommended order of scripts:
1. `update.py`
2. `password-security.py`
3. `users.py`
4. `media-files.py`
