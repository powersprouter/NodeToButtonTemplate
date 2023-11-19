# NodeToButtonTemplate

This Blender add-on is a utility to make it easier to convert a geometry node into a really simple add-on with one big button in the N-Panel to APPLY and UNDO. (Note - the "apply" button only adds the geometry node to the modifier stack, it is intentionally non-destructive).


    Step 1: Create and name your geometry nodegroup in Blender.

    Step 2: Use NodeToPython add-on
    https://github.com/BrendanParmer/NodeToPython
    to generate a python script and copy to clipboard

    Step 3: Paste script into the nbt_geonodes.py file to replace where
    the sample voronoi creation script is currently parked. (I took my 
    voronoiThis addon script and generalized it for the purpose of creating
    this template. Just delete that script & plug in your own!)

    Step 4: The commented word Template is on every line that requires
    your attention. The most common need is to simply replace 'Node Name'
    and node_name with your geometry nodegroup name, but there are also 
    some spots in the panel that can benefit from better descriptions.
    There are four python files to modify: init, panel, ops, and geonodes.
    You can also modify this readme file to help your users. 
    
    Happy node buttoning! Please let me know if you find this helpful.

# Installation
To install the add-on, download the zip, go to user Preferences>Add-ons and install & activate the zip file without unzipping. This add-on requires Blender version 3.6 or more recent.