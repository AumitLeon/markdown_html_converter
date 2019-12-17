# Exit with non-zero status if any intermediate step fails
set -e

echo "Conducting tests..."

echo "Check that md-to-html is installed"
md-to-html -h 

echo "Convert test markdown file to html"
md-to-html --input test.md

echo "Make sure that a converted.html was created"
test -e converted.html

test -e sdfsd

echo "Make sure files are the same"
diff baseline.html converted.html

