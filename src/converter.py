"""
@author Aumit Leon
Convert Markdown documents to HTML

Supports Markdown Documents with bullet lists, links, and headers. 

@TODO: Add formatting support for bold, italics. Support regular paragraph formatting.
"""

import re

"""
Convert link from markdown format to HTML
@param (string) md_link: The markdown match for a link ex. [text](link)
@return (string) link_html: HTML rendition of the markdown text.
"""
def link_md_to_html(md_link):
    phrase_split = md_link.split("]")
    text_link = phrase_split[0][1:]
    url_link = phrase_split[1][1:-1]
    link_html = "<a href='" + url_link + "'>" + text_link + "</a>"
    return link_html

"""
Convert a list from markdown format to HTML
@param (list) matches: Every entry is a list of matches from a particular line
@param (list) text: Every entry is the text corresponding to a particular line
@return (string) bullet_html: HTML rendition of the markdown bullet list
"""
def list_md_to_html(matches, text):
    bullet_html = "\t\t<ul>\n"
    for match, phrase in zip(matches, text):
        if len(match) == 1: 
            bullet_html += "\t\t\t<li>" + phrase + "</li>\n"
        else:
            bullet_html += "\t\t\t<li>" + inner_tags(match) + "</li>\n"
    bullet_html += "\t\t</ul>\n"
    return bullet_html

"""
Convert inner Markdown tags to their HTML counterpart.
An inner tag is defined as a tag that doesn't need to start at the begninning of the line
@param (list) matches: Every entry is a markdown element to be converted
@return (string) inner_htmk: HTML rendition of the markdown tags provided
"""
def inner_tags(matches):
    for match in matches:
        # skip first pattern match
        if matches.index(match) == 0:
            continue 
        # could be pulled out to a different function
        if match[0] == "[":
            inner_html = link_md_to_html(match)
    return inner_html

def main(args):
    # matches headers, bullet lists, and links
    pattern = re.compile('([#*]+\s|\w*\[\w*\]\(\w*\))')
    text = re.compile('\w+\s*\w*\s*')
    html_doc = open(args.output, "a")
    html_doc.write("<!DOCTYPE html>\n")
    html_doc.write("<!--Converted via md-to-html-->\n")
    html_doc.write("<html>\n\t<head>\n\t</head>\n\t<body>\n")


    # place these vars somewhere better
    bullet_matches = []
    text_bullets = []

    with open(args.input) as f:
        content = f.readlines()
        for line in content:
            matches = pattern.findall(line)
            text_matches = text.findall(line)
            if matches:
                # link
                if matches[0][0] == "[":
                    html_doc.write("\t\t" + link_md_to_html(matches[0]) + "\n")
                # bullet list
                if matches[0][0] == "*":
                    cur_ind = content.index(line)
                    # Save the matches
                    bullet_matches.append(matches)
                    # Save the line if there is more than one match
                    if len(matches) > 1:
                        text_bullets.append(line)
                    # Not at the end of the list and next line is also a bullet
                    if len(content) != cur_ind+1 and content[cur_ind+1][0] == "*":
                        # save the matches  
                        if len(matches) == 1:
                            text_bullets.append(line[2:].strip())
                    else:
                        # End of list. Write to doc
                        html_doc.write(list_md_to_html(bullet_matches, text_bullets))
                if matches[0][0] == "#":
                    header_size = 0
                    for char in matches[0]:
                        if char == "#":
                            header_size += 1
                    if len(matches) > 1:
                        header_html = "\t\t<h" + str(header_size) + ">" + inner_tags(matches) + "</h" + str(header_size) + ">\n"
                    else:
                        header_html = "\t\t<h" + str(header_size) + ">" + line[header_size+1:].strip() + "</h" + str(header_size) + ">\n"
                    html_doc.write(header_html)
    html_doc.write("\t</body>\n</html>")

if __name__ == '__main__':
    main()
    
