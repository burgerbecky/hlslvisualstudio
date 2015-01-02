HLSL Visual Studio 2010+ Integration
====================================

**Or, how do I include DirectX shader code in my project?**

Copyright 2015 by Rebecca Ann Heineman becky@burgerbecky.com

It is released under an MIT Open Source license. Please see LICENSE
for license details. Yes, you can use it in a
commercial title without paying anything, just give me a credit.
Please? It's not like I'm asking you for money!

What is HLSL Visual Studio 2010+ Integration?
---------------------------------------------

This is a plug in for Visual Studio 2010 or higher that will
allow files with the HLSL extension to automatically be compiled
with the fxc tool found in the DirectX SDK. 

The tool will be listed as "Effect-Compiler Tool"

What does it require?
--------------------

Visual Studio 2010, 2012, 2013 or any other MSBuild compatible
IDE and the June 2010 or later Direct X SDK

How do I use it?
----------------

Copy the contents of the "plugin" folder to the folder 
<em>C:\Program Files (x86)\MSBuild\Microsoft.Cpp\v4.0\BuildCustomizations</em>

Find this line in your .vcxproj file
<em>&lt;Import Project="$(VCTargetsPath)\Microsoft.Cpp.props"/&gt;</em>

Insert this after it
<pre>&lt;ImportGroup Label="ExtensionSettings"/&gt;
	&lt;Import Project="$(VCTargetsPath)\BuildCustomizations\hlsl.props" /&gt;
&lt;/ImportGroup/&gt;
</pre>

Find this line near the end of your .vcxproj file
<em>&lt;Import Project="$(VCTargetsPath)\Microsoft.Cpp.targets" /&gt;</em>

Insert this after it.
<pre>&lt;ImportGroup Label="ExtensionTargets"&gt;
	&lt;Import Project="$(VCTargetsPath)\BuildCustomizations\hlsl.targets" /&gt;
&lt;/ImportGroup&gt;
</pre>

This is great/sucks! But, how can I change/rewrite/steal the tool?
----------------------------------------------------

The source code to the tool is in the folder "source". It will require Burgerlib for some
subroutines. https://github.com/Olde-Skuul/KitchenSink has the binaries of the library
and https://github.com/Olde-Skuul/burgerlib has the source to the library.
