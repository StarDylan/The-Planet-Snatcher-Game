
## Configuration

Editing the Story
--------------


The json structure is structured like this:

{
"RandomStories": [{
  "TEXT": "INSERT RANDOM STORY",
  "ID": " < OPTION ID > ",
  "OPTIONS": [{
    "SUCCESS": "DoSomething",
    "FAILED": "DoSomethingElse",
    "PERCENT": 5
  }]
}],
"Stories": {
  "DoSomething": "This Happens when RANDOM Story has succeceded!"
},

"Options": {
  "<OPTION ID>": ["Options", "To", "Choose", "From"],


  "DisplayItem1": "This is printed when calling DisplayItem1"
}
}
