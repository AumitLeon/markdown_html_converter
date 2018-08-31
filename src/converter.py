md_html_mapping = {}
md_html_mapping["##"] = "<h2>"
html_closing_tags = {}
html_closing_tags["<h2>"] = "</h2>"

html_doc = open("converted.html", "a")
filename = "test.md"
with open(filename) as f:
    content = f.readlines()
    #print content
    for sentence in content:
        words = sentence.split()
        print words
        print sentence
        if words[0] in md_html_mapping:
            #print md_html_mapping[words[0]] + sentence + html_closing_tags[md_html_mapping[words[0]]]
            html_doc.write(md_html_mapping[words[0]] + ''.join(words[1:]) + html_closing_tags[md_html_mapping[words[0]]] + "\n")
