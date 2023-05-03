import unittest
from pybgpasn import ASNCatalog


class TestASNCatalog(unittest.TestCase):
    def setUp(self):
        self.asn_catalog = ASNCatalog()

    def test_get_provider_name(self):
        # Test a valid ASN number
        self.assertEqual(self.asn_catalog.get_provider_name(174), "COGENT Cogent/PSI")

        # Test a private ASN number
        self.assertEqual(self.asn_catalog.get_provider_name(64512), "PRIVATE AS")

        # Test an unknown ASN number
        self.assertEqual(self.asn_catalog.get_provider_name(35001), "Unknown provider")

    def test_get_provider_name_invalid_asn(self):
        # Test an invalid ASN number
        with self.assertRaises(ValueError):
            self.asn_catalog.get_provider_name(-1)

        with self.assertRaises(ValueError):
            self.asn_catalog.get_provider_name(70000)


if __name__ == '__main__':
    unittest.main()
