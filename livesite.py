import argparse
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys

# Argument parser to get input file externally
parser = argparse.ArgumentParser(description="Check live status of websites from a TXT file.")
parser.add_argument('-f', '--file', required=True, help='Path to TXT file containing one URL per line (e.g., urls.txt)')
parser.add_argument('-t', '--threads', type=int, default=50, help='Number of concurrent threads (default: 50)')
parser.add_argument('-o', '--output', help='Optional output file to save results')
args = parser.parse_args()

TIMEOUT = 10  # seconds

def check_url(url):
    url = url.strip()
    if not url:
        return None
    # Add scheme if missing
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    try:
        response = requests.head(url, allow_redirects=True, timeout=TIMEOUT)
        status = response.status_code
        if 200 <= status < 400:
            return f"{url} - live"
        else:
            return f"{url} - Not-{status}"
    except requests.exceptions.RequestException as e:
        # Common error handling
        error_msg = str(e)
        if 'Name or service not known' in error_msg or 'Temporary failure in name resolution' in error_msg:
            code = "DNS"
        elif 'timed out' in error_msg:
            code = "Timeout"
        elif 'Connection refused' in error_msg:
            code = "Refused"
        else:
            code = "Error"
        return f"{url} - Not-{code}"

def main():
    try:
        with open(args.file, 'r') as f:
            urls = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found!")
        sys.exit(1)

    print(f"Checking {len(urls)} websites from '{args.file}' using {args.threads} threads...\n")

    results = []
    output_handle = open(args.output, 'w') if args.output else None

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        future_to_url = {executor.submit(check_url, url): url for url in urls}
        for future in as_completed(future_to_url):
            result = future.result()
            if result:
                print(result)
                results.append(result)
                if output_handle:
                    output_handle.write(result + '\n')

    if output_handle:
        output_handle.close()
        print(f"\nResults saved to: {args.output}")

    live = sum(1 for r in results if '- live' in r)
    print(f"\nSummary: {live}/{len(urls)} websites are live.")

if __name__ == "__main__":
    main()
