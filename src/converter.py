import re

def link_md_to_html(md_link):
    phrase_split = md_link.split("]")
    text_link = phrase_split[0][1:]
    url_link = phrase_split[1][1:-1]
    link_html = "<a href=" + url_link + ">" + text_link + "</a>"
    return link_html
    
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
    html_doc = open(args.output, "a")

    with open(args.input) as f:
        content = f.readlines()
        for line in content:
            matches = pattern.findall(line)
            if matches:
                # link
                if matches[0][0] == "[":
                    html_doc.write(link_md_to_html(matches[0]) + "\n")
                # bullet list
                if matches[0][0] == "*":
                    bullet_html = "<ul>\n\t <li>" + inner_tags(matches) + "</li>\n</ul>\n"
                    html_doc.write(bullet_html)
                if matches[0][0] == "#":
                    header_html = "<h1>" + inner_tags(matches) + "</h1>\n"
                    html_doc.write(header_html)

if __name__ == '__main__':
    main()
    