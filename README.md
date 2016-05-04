# Tacool #
## Introduce ##
> Some tools of Python for self-use.

## Environment ##
> Python 3.5.0

## Document ##

### syscript.py ###
__This file includes some tools used as system scripts.__

___*Warning: In Windows, the script will stop if certain command crashes because of the Program Compatibility Assistant Service.___

    class multiCommand: run several commands with process pool.
        def __init__(self,cmds,maxpool):
            :param cmds: List of cmd. Every cmd is in form of subprocess.Popen()
            :param maxpool: the maximum amount of process running at the same time
            :return: None
        def run(self):
            run the commands.
            :return: List of command output in order of self.cmds

### toy.py ###
__This file includes some tools which looks useless :J__


    def pic2