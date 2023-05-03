### PYBGPASN

pybgpasn is a Python package for looking up Autonomous System Number (ASN) information. The package includes a database of ASNs and their corresponding provider names.


## Installation

You can install pybgpasn using pip:

```sh 
pip install pybgpasn
```


## Usage

### Basic Usage

To use pybgpasn, first create an instance of the ASNCatalog class:

```sh 
from pybgpasn import ASNCatalog

catalog = ASNCatalog()

```

The ASNCatalog class loads the ASN data from the package database file during initialization.

To look up an ASN's provider name, call the get_provider_name method:
```sh 
asn = 15169  # Google LLC
provider_name = catalog.get_provider_name(asn)
print(provider_name)  # prints "Google LLC"

```

### Private ASNs

If the provided ASN falls within the range of 64512 to 65535 (inclusive), the get_provider_name method will return "PRIVATE AS":

```sh 
asn = 64512  # Start of private ASN range
provider_name = catalog.get_provider_name(asn)
print(provider_name)  # prints "PRIVATE AS"

asn = 65535  # End of private ASN range
provider_name = catalog.get_provider_name(asn)
print(provider_name)  # prints "PRIVATE AS"

```

### Errors
If an invalid ASN is provided to the get_provider_name method, an error will be raised.

- If the provided ASN is not an integer, a TypeError will be raised.
- If the provided ASN is outside the valid range of 0 to 4294967295, a ValueError will be raised.

Here's an example of handling errors when looking up an ASN:
```sh 
from pybgpasn import ASNCatalog

catalog = ASNCatalog()

try:
    asn = "invalid"  # Not an integer
    provider_name = catalog.get_provider_name(asn)
except TypeError as e:
    print(f"Error: {e}")
    # Output: Error: ASN must be an integer

try:
    asn = -1  # Negative ASN
    provider_name = catalog.get_provider_name(asn)
except ValueError as e:
    print(f"Error: {e}")
    # Output: Error: Invalid ASN number

```

## License

pybgpasn is licensed under the MIT License. See the LICENSE file for more information.

## Acknowledgments
pybgpasn includes data from the Border Gateway Protocol (BGP) Autonomous System (AS) Numbers registry maintained by the Internet Assigned Numbers Authority (IANA).

