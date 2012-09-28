This is a writeup of the information contained in [this user group discussion](https://groups.google.com/forum/?hl=no&fromgroups=#!topic/ontowiki-user/BCssISSQoNk). Please help extend it.

# Configure extension resourcecreationuri

The extension called resourcecreationuri is responsible for selecting the naming scheme of cloned resources. It uses the literal of one or more configured propertiers from the used class to create the name.

## Tweaking the default setup 

By default, prefLabel is the first choice in the ladder. For a list of possible choices, see the file ```extensions/resourcecreationuri/doap.n3``` in your OntoWiki installation directory.

To use your own naming scheme, you could create and use your own property in this file. It might be a property which is NOT used by the titleHelper and only used by the resourcecreationuri extension.
