🔗 LiveLink-Extractor

LiveLink-Extractor is a simple tool created to check whether a link is active on the internet or not.
It is mainly built to save time during live site testing when you have a large number of URLs to verify.

Instead of opening each link manually in a browser, you can put all links into a text file and test them in one go.

**Why This Tool?**

When testing a domain or website, you may get hundreds of links.
Checking each link manually takes a lot of time and effort.

<--LiveLink-Extractor helps by-->

-> Taking all links from a .txt file

-> Testing them automatically

-> Showing which links are working (live) and which are not

*This makes link testing faster, easier, and more efficient*

<--What It Does-->

-> Reads multiple URLs from a text file

-> Checks if each link is reachable on the internet

-> Identifies live and inactive links

(--Example--)

1.Collect subdomains

subfinder -d example.com -o example.txt

This command collects all subdomains of the target domain and saves them to a file.


2.Clone the LiveLink-Extractor tool

git clone <repository-url>

Clone the LiveLink-Extractor repository to your Linux system.


3.Check live links

python3 <python_file_name>.py -f example.txt

This command tests all the collected subdomain links and shows which sites are live on the target domain.



