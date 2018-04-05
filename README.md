## Installation


## Configuration

### Editing the Story


The json structure is structured like this:

    {
    	"RandomStories": {
    		"<RandomGroupID>": [{
    			"TEXT": "INSERT RANDOM STORY",
    			"ID": " < OPTION ID > ",
    			"OPTIONS": [{
    				"SUCCESS": "DoSomething",
    				"FAILED": "DoSomethingElse",
    				"PERCENT": 5
    			}]
    		}]
    	},
    	"Stories": {
    		"< StoryUID >": {
    			"DATA": "INSERT RANDOM STORY",
    			"ID": " < OPTION ID > ",
    			"OPTIONS": {
    				"SUCCESS": [{
    					"SHOW": "< Insert StoryUID >"
    				}],
    				"FAILED": [{
    					"DISPLAY": "< Insert TextUID >"
    				}],
    				"PERCENT": 5
    			}
    		}
    	},

    	"Options": {
    		"<OPTION ID>": ["Options", "To", "Choose", "From"]
    	},
    	"Text": {
    		"<TextUID>": "INSERT_TEXT_HERE"
    	}
    }
