from pybgpasn.bgp_asn_db import asn_data

class ASNCatalog:
    def __init__(self):
        self.asn_dict = asn_data

    def get_provider_name(self, asn):
        if asn < 0 or asn > 65536:  # Check for invalid ASN values
            raise ValueError("Invalid ASN number")

        if asn >= 64512 and asn <= 65535:  # Check for private AS numbers
            return "PRIVATE AS"

        asn_str = str(asn)
        return self.asn_dict.get(asn_str, "Unknown provider")
    