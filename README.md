# Wwise Unreal Differ
A simple tool for comparing what's in the Events folder in Unreal and highlighting redundancies for deletion in Wwise.

<img width="615" height="561" alt="image" src="https://github.com/user-attachments/assets/171f42a0-aa5b-4bcb-ac43-82521ae7554c" />

# The previous workflow
As a game project evolves over time, audio assets will be added to fit the new game features. 
But they don't always get removed when they're no longer used. 

This can add project bloat and create confusion if new audio assets have similar names to old ones, making it hard to tell what's actually in use.
Removing unused audio assets can be a bit of a pain when they exist simultaneously in the engine and in the middleware.

Deleting in the engine is pretty easy. A script can review a selected set of assets, identify those not referenced by anything, and mark them for deletion in the version control software.

But what about in Wwise? The middleware has the old audio events. Now the audio section of the editor has been cleaned up, and the audio middleware is still a mess.

At this point, a user would have to manually review the version control changelist, locate the asset in the middleware, and delete it.
A tedious, time-consuming task, depending on how many files are removed.

# The solution
A simple tool to compare the audio events from the editor to the audio events in the Wwise middleware.
A user can get an overview of all the Wwise events that aren't in use by the editor, and with a single click remove them from Wwise.

<img src="https://github.com/user-attachments/assets/48cf63cf-3d9b-4b63-b70f-ca3367285073" />

# How to use 
1. Remove all audio assets from the editor.
2. Set the engine audio folder containing the engine audio assets.
3. Ensure you have your Wwise session open and the tool connects to the project
4. Click "Diff against Wwise project," and the list will populate with audio assets. The ones in red are not used by the engine.
5. Click "Delete Unused Ak Events from Wwise" to remove all unused events.





