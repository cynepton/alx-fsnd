# ALX FSND

> Link to [Github Markdown Documentation](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

## A section

**This is bold**

__This is also bold__

*This is emphasized*

_This is also emphasized_

~~This was mistaken text~~

**This text is _extremely_ important**

***All this text is important***

Run: `flask run` to run the app

Sample endpoint:
```python
@app.route('/')
def root():
    # Do some stuff
    variable = "some stuff"

    return jsonify({
        "success": True,
        "list": ["1", "2"],
        "bool": False,
        "number": 245,
        "map": {
            "key": "value",
            "map": {
                "key": variable
            }
        }
    })
```

### Color! 🖌️

The background color should be `#ffffff` for light mode and `#0d1117` for dark mode.

Other colors: 	`rgb(9, 105, 218)`

### Links

[**Link to A section**](#a-section)

[Link to app.py](c2-api-dev/src/app.py)

[Link to a folder](c2-api-dev/src)


### Image

![This is an image](https://myoctocat.com/assets/images/base-octocat.svg)

![](img/red.jpg)

### List

- **Item 1**
- *Item 2*
- Item 3

* Item 1
* Item 2
* Item 3

1. Item 1
2. Item 2

Nested Lists

1. First list item
    - First nested list item
        - Second nested list item
    - FSecond nested list item
2. Second List item

- [x] Checked
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete 🎉 :8ball:

### A subsection

Some text
Still same paragraph

Another paragraph

<!-- This content will not appear in the rendered Markdown -->