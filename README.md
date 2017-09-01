# Bulk delete slack files

This Python script will bulk delete all Slack files older than 10 days (configurable) . Just add your API token into the token field and configure No of days to skip files in the file.

Rewrite of https://gist.github.com/jamescmartinez/909401b19c0f779fc9c1 written in Ruby

Slack has storage limit for files.

Problem you need to delete old files to free space to still able to upload and share files. To do this, you need to open Slack, find files and delete each one, there’s no way to bulk delete.

## Requirements

To run this you should have python installed. you can install it according to your environment. You can take help from http://docs.python-guide.org/en/latest/starting/installation/

### Using

You will need to clone this repo and just execute in your terminal like this:

````bash
python bulkdeleteslackfiles.py
````
