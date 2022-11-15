# HLSL Visual Studio 2010+ Integration

**Or, how do I include DirectX HLSL shader code in my project?**

## What is HLSL Visual Studio 2010+ Integration

This is a plug in for Visual Studio 2010 or higher that will allow files with the HLSL extension to automatically be compiled with the fxc tool found in the DirectX SDK.

The tool will be listed as "Effect-Compiler Tool"

## What is required

Visual Studio 2010 or higher or any other MSBuild compatible
IDE and the [June 2010 or later Direct X SDK](https://www.microsoft.com/en-us/download/details.aspx?id=6812)

## How to install it

### For Visual Studio 2010 through 2015

[Head over to the releases page](https://github.com/burgerbecky/hlslvisualstudio/releases) and download the *.msi installer.

### For Visual Studio 2017

Download it directly from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=BurgerBecky.hlslvs2012)

### For Visual Studio 2019

Download it directly from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=BurgerBecky.hlslvs2019)

### For Visual Studio 2022

Download it directly from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=BurgerBecky.hlslvs2022)

## How to use it

After installation, open a project file and select BuildCustomizations as shown:

![Build customization menu][build]

When the dialog opens, check "hlsl" and you're done!

![Customization List][list]

All files that end with the suffix of *.hlsl will automatically map to this tool, however you can select the compiler by right clicking any source file in the project and select "Effect-Compiler Tool".

## This is great/sucks! But, how can I change/rewrite/steal the tool

The source code to the tool is in the folder "BuildCustomizations" on [Github](https://github.com/burgerbecky/hlslvisualstudio). Pull requests and bug reports are encouraged.

## Build prerequisite

In the extensions, install *Microsoft Visual Studio Installer Projects* so Visual Studio can load the \*.vdproj files

-------

## License

Copyright 2015-2022 by Rebecca Ann Heineman becky@burgerbecky.com

It is released under an MIT Open Source license. Please see LICENSE.txt for license details. Yes, you can use it in a commercial title without paying anything, just give me a credit.

Please? It's not like I'm asking you for money!

[build]: https://raw.githubusercontent.com/burgerbecky/hlslvisualstudio/master/Resources/buildcustomizations.png "BuildCustomizations menu item"

[list]: https://raw.githubusercontent.com/burgerbecky/hlslvisualstudio/master/Resources/customization_list.png "Customization list"
