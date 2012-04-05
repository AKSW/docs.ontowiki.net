# FAQ

## How can I change the start screen with the news feed?

OntoWiki is organized in terms of controllers which provide actions.
The news feed is provided by the action `news` from the controller `index`.
You can change the start screen by configuring a new action/controller in `config.ini` by add the following section:

    index.default.controller = "[controllername]"
    index.default.action = "[actionname]"

To create a simple custom start screen, you can use the [page
extension](https://github.com/AKSW/page.ontowiki).

