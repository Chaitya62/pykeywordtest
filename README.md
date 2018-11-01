# pykeywordtest

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)



## Introduction

A minimalist keyword-driven testing framework for websites. This tool helps you test certain features of any website without writing any code. All you have to do is fill an excel sheet and you are all set to test your website.


## Usage 

### Installation 


First you need to download the tool and install some dependencies.

```sh
git clone https://github.com/Chaitya62/pykeywordtest.git
cd pykeywordtest
pip install -r requirements.txt
```

Now you are all set to start using the tool.

### Writing Scripts using Excel

The Excel file should have two sheets in it.
- Test (Sheet)
- objects (Sheet)

*Note*: The name of the sheet should be `Test` and `objects`.

Let's look at each sheet in detail.

#### Test

This sheet has all the steps that are suppose to be executed.

There are 5 columns in this sheet:

- *Object*: Name of the object to work on
- *Keyword*: Keyword specifies the task to perform
- *Value*: This is an optional field which is required in certain tasks
- *Message*: This `Message` will show when that step is being executed
- *Screenshot*: Do you want to take a screenshot after performing the current task? (Y/N)


#### objects

This sheet has all the objects/elements that are mentioned in the script with the exception of the `Browser`. It is used to select all the elements on the webpage.

There are 6 columns in this sheet:

- *Name*: Unique name for the object, which is used to mention it in the *Test*
- *id*: `id` attribute value of the HTML element
- *class*: `class` attribute value of the HTML element
- *tag*: `tagname`  of the HTML element
- *css_selector*: `css_selector` of the HTML element
- *name*: `name` attribute value of the HTML element 

T

Now let's look at the different `keywords` that are currently supported.

#### Keywords

1. `open`: This keyword only works with the `Browser` object. It is used to open the browser.
2. `goto`: This keyword also works with the `Browser` object only, it is used to go to a particular url. The url should be mentioned in the `Value` column.
3. `type`: This keyword is used to send key strokes to the website. There should be some object to work with. `Value` column specifies the keystrokes to be sent.
4. `click`: This keyword clicks on the given `Object`.
5. `check`: This keyword works with `Browser` object only, it check whether a particular `Value` is present in the web page or not.
6. `close`: This keyword works with `Browser` only, it closes the web browser.


You can check the example script in the `scripts/` folder for more clarity.


## Contributing

Please reach out to me if you wish to contribute to this project


## Contributor
[@Chaitya62](https://github.com/Chaitya62)




