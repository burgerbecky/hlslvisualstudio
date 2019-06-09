#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copy up the HLSL visual studio plug in to sdks/visualstudio

Copyright 1995-2014 by Rebecca Ann Heineman becky@burgerbecky.com

It is released under an MIT Open Source license. Please see LICENSE
for license details. Yes, you can use it in a
commercial title without paying anything, just give me a credit.
Please? It's not like I'm asking you for money!
"""

from __future__ import absolute_import

import os
import sys
import burger

# List of files and folders to copy
PROPS_FILES = [
    'hlsl.props',
    'hlsl.targets',
    'hlsl.xml'
]

EXTRA_FILES = [
    'AUTHORS',
    'LICENSE',
    'README.md'
]


def main(working_dir):
    """
    Copy up the HLSL visual studio plug in to sdks/visualstudio
    """

    # Locate the SDKs folder so the files can be copied there
    sdks = burger.get_sdks_folder()

    rootpluginfolder = os.path.join(working_dir, 'plugin')

    #
    # Ensure the destination directory exists
    #

    visualstudiofolder = os.path.join(sdks, 'visualstudio')
    burger.create_folder_if_needed(visualstudiofolder)

    #
    # Create the github folder on PC hosts
    #

    githubfolder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.dirname(working_dir)))), 'github', 'hlslvisualstudio')
    githubpluginfolder = os.path.join(githubfolder, 'plugin')

    hostmachine = burger.host_machine()
    if hostmachine == 'windows':
        burger.create_folder_if_needed(githubfolder)
        burger.create_folder_if_needed(githubpluginfolder)

    #
    # Copy all the changed files for sdks\visualstudio
    #

    error = 0
    for item in PROPS_FILES:

        #
        # If the file had changed, update it in perforce
        #

        sourcefile = os.path.join(rootpluginfolder, item)
        destfile = os.path.join(visualstudiofolder, item)
        if os.path.isfile(destfile) is not True or \
                burger.compare_files(sourcefile, destfile) is not True:

            error = burger.copy_file_if_needed(
                sourcefile, destfile, perforce=True)
            if error:
                break

    #
    # Copy the files to the github folder
    # if the host is a PC
    #

    if error == 0 and hostmachine == 'windows':

        for item in PROPS_FILES:

            #
            # If the file had changed, update it
            #

            sourcefile = os.path.join(rootpluginfolder, item)
            destfile = os.path.join(githubpluginfolder, item)
            if os.path.isfile(destfile) is not True or \
                    burger.compare_files(sourcefile, destfile) is not True:
                error = burger.copy_file_if_needed(sourcefile, destfile)
                if error != 0:
                    break

        for item in EXTRA_FILES:

            #
            # If the file had changed, update it
            #

            sourcefile = os.path.join(working_dir, item)
            destfile = os.path.join(githubfolder, item)
            if os.path.isfile(destfile) is not True or \
                    burger.compare_files(sourcefile, destfile) is not True:
                error = burger.copy_file_if_needed(sourcefile, destfile)
                if error:
                    break
    return error

# Unused arguments
# pylint: disable=W0613

def rules(command, working_directory=None, root=True, **kargs):
    """
    Main entry point for build_rules.py.

    When ``makeprojects``, ``cleanme``, or ``buildme`` is executed, they will
    call this function to perform the actions required for build customization.

    The parameter ``working_directory`` is required, and if it has no default
    parameter, this function will only be called with the folder that this
    file resides in. If there is a default parameter of ``None``, it will be
    called with any folder that it is invoked on. If the default parameter is a
    directory, this function will only be called if that directory is desired.

    The optional parameter of ``root``` alerts the tool if subsequent processing
    of other ``build_rules.py`` files are needed or if set to have a default
    parameter of ``True``, processing will end once the calls to this
    ``rules()`` function are completed.

    Commands are 'build', 'clean', 'prebuild', 'postbuild', 'project',
    'configurations'

    Arg:
        command: Command to execute.
        working_directory: Directory for this function to operate on.
        root: If True, stop execution upon completion of this function
        kargs: Extra arguments specific to each command.
    Return:
        Zero on no error or no action.
    """

    if command == 'clean':
        burger.clean_directories(
            working_directory, ('bin', 'obj', 'Properties', '.vs'))
        burger.clean_files(working_directory, ('Key.snk', '*.user', '*.suo'))

    return 0


# If called as a command line and not a class, perform the build
if __name__ == "__main__":
    sys.exit(rules('build', os.path.dirname(os.path.abspath(__file__))))
