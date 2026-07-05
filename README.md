# Wwise Unreal AkEvent Differ
A simple tool for comparing what's in the Events folder in Unreal and highlighting redundancies for deletion in Wwise.

# The previous workflow
As a game project evolves over time, audio assets will be added to fit the new game features. 
But they don't always get removed when they're no longer used. 

Over time, this can add project bloat and create confusion if new audio assets have similar names to old ones, making it hard to tell what's actually in use.
Removing unused audio assets can be a bit of a pain when they exist simultaneously in the engine and in the middleware.

Deleting in the engine is pretty easy. A script can review a selected set of assets, identify those not referenced by anything, and mark them for deletion in the version control software.

But what about in Wwise? The middleware has the old audio events. Now the audio section of the editor has been cleaned up, and the audio middleware is still a mess.

At this point, a user would have to manually look at the version control changelist, find the asset in the middleware and delete it.
A tedious, time-consuming task, depending on how many files are removed.

