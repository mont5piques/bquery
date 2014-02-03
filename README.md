bquery
======

bQuery is a simple tool to quickly parse html streams with a jQuery-like expression.

Examples:
wget -qO- http://en.wikipedia.org/wiki/Secure_Shell |./bquery.py h1
> get h1 element text content

wget -qO- http://en.wikipedia.org/wiki/Secure_Shell |./bquery.py h2
> multiple results => multiple lines

wget -qO- http://en.wikipedia.org/wiki/Secure_Shell |./bquery.py h2:first
> get the first result

=============================================================================

By default, the inner plain text is output. If the found element is an input, the value is output.
To get the html content instead of plain text, just pass --html swith.

We can extract a specific attribute instead of text:

wget -qO- http://en.wikipedia.org/wiki/Secure_Shell |./bquery.py a -a href
> This example extracts all page links.

wget -qO- http://audacity.sourceforge.net/download/windows |./bquery a -a href|grep 'zip\|exe'|xargs -n1 wget
> Download all zip or exe files from audacity download page


=============================================================================
Installation:
=============================================================================
bquery requires python, python-pyquery (pyquery with pyquery module)
run "make install" to install it
