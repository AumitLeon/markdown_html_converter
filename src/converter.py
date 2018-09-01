import re

def link_md_to_html(md_link):
    phrase_split = md_link.split("]")
    text_link = phrase_split[0][1:]
    url_link = phrase_split[1][1:-1]
    link_html = "<a href=" + url_link + ">" + text_link + "</a>"
    return link_html

def list_md_to_html(matches, text):
    bullet_html = "\t\t<ul>\n"
    for match in matches:
        if match[0] == "*":
            if len(matches) > 1:
                bullet_html += "\t\t\t<li>" + inner_tags(matches) + "</li>\n"
            else: 
                bullet_html += "\t\t\t<li>" + text[0] + "</li>\n"
    bullet_html += "\t\t</ul>\n"
    return bullet_html

    
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
    text = re.compile('\w')
    html_doc = open(args.output, "a")
    html_doc.write("<!DOCTYPE html>\n")
    html_doc.write("<!--Converted via md-to-html-->\n")
    html_doc.write("<html>\n\t<head>\n\t</head>\n\t<body>\n")
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
                    html_doc.write(list_md_to_html(matches, text_matches))
                if matches[0][0] == "#":
                    header_size = 0
                    for char in matches[0]:
                        if char == "#":
                            header_size += 1
                    if len(matches) > 1:
                        header_html = "\t\t<h" + str(header_size) + ">" + inner_tags(matches) + "</h" + str(header_size) + ">\n"
                    else:
                        header_html = "\t\t<h" + str(header_size) + ">" + line.split()[1] + "</h" + str(header_size) + ">\n"
                    html_doc.write(header_html)
    html_doc.write("\t</body>\n</html>")

if __name__ == '__main__':
    main()
    