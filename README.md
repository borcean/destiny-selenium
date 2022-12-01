# Destiny Selenium Scripts

A script used to automate checking in a resource item to your site in Destiny.

## Set up - Packages

Using these scripts requires a working python install, and [ChromeDriver](https://chromedriver.chromium.org/). Install the python dependencies with pip.

```bash
pip install -r requirements.txt
```

## Set up - Configuration

The script expects a file `auth.txt` to be present with the username, password, and Destiny site ID. Create the file like so:

```txt
USERNAME
PASSWORD
SITE_ID
```

**_NOTE:_** SSO login is not supported, a local Destiny user is required. See the "Destiny Library Manager Manual" for a working login.

Find your site ID by opening [BSD Destiny page](https://library4.cascadetech.org/common/welcome.jsp?context=beaverton), expanding the relevant section, then hovering over your site. Look at the URL preview in the lower left of your browser. Site ID is the number at the end of the URL.

For example hovering over Central Collections shows: `https://library4.cascadetech.org/common/welcome.jsp?site=150`

| Site                | ID  |
|---------------------|-----|
| Central Collections | 150 |
| Tumwater Middle     | 403 |

## Usage

Scan, or paste serials/barcodes into the `serials.txt` file, one barcode per line.

From the directory your scripts, and .txt files are located run:

```bash
pytest check_in.py
```

## Gotchas

If the device being checked in has component items (charger, stylus, etc...) the script will accept whatever number of component items was previously recorded in Destiny. This may lead to inaccurate information if a component item was lost, or found since the device was last checked out.
