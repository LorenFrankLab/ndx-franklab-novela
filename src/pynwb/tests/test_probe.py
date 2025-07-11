import unittest
from unittest.mock import Mock

from ndx_franklab_novela import Probe, ShanksElectrode, Shank


class TestShanksElectrode(unittest.TestCase):

    def test_shanks_electrode_successfully_created(self):
        shanks_electrode = ShanksElectrode(name="0", rel_x=1.0, rel_y=2.0, rel_z=3.0)

        self.assertIsInstance(shanks_electrode, ShanksElectrode)

        self.assertIsInstance(shanks_electrode.name, str)
        self.assertIsInstance(shanks_electrode.rel_x, float)
        self.assertIsInstance(shanks_electrode.rel_y, float)
        self.assertIsInstance(shanks_electrode.rel_z, float)

        self.assertEqual(shanks_electrode.name, "0")
        self.assertEqual(shanks_electrode.rel_x, 1.0)


class TestShank(unittest.TestCase):

    def test_shanks_electrode_successfully_created(self):

        mock_shanks_electrode_1 = Mock(spec=ShanksElectrode)
        mock_shanks_electrode_1.name = "1"
        mock_shanks_electrode_1.rel_x = 1.0
        mock_shanks_electrode_2 = Mock(spec=ShanksElectrode)
        mock_shanks_electrode_2.name = "2"
        mock_shanks_electrode_2.rel_x = 2.0

        shank = Shank(
            name="0",
        )

        shank.add_shanks_electrode(mock_shanks_electrode_1)
        shank.add_shanks_electrode(mock_shanks_electrode_2)

        self.assertIs(shank.get_shanks_electrode("1"), mock_shanks_electrode_1)
        self.assertIs(shank.get_shanks_electrode("2"), mock_shanks_electrode_2)

        self.assertIsInstance(shank, Shank)

        self.assertIsInstance(shank.name, str)
        self.assertIsInstance(shank.shanks_electrodes, dict)
        self.assertIsInstance(shank.shanks_electrodes["1"], ShanksElectrode)
        self.assertIsInstance(shank.shanks_electrodes["1"].rel_x, float)

        self.assertEqual(shank.name, "0")
        self.assertEqual(shank.shanks_electrodes, {"1": mock_shanks_electrode_1, "2": mock_shanks_electrode_2})
        self.assertEqual(shank.shanks_electrodes["1"].rel_x, 1.0)


class TestProbe(unittest.TestCase):

    def test_probe_successfully_created(self):
        mock_shank_1 = Mock(spec=Shank)
        mock_shank_1.name = "1"
        mock_shank_2 = Mock(spec=Shank)
        mock_shank_2.name = "2"

        probe = Probe(
            id=1,
            name="Probe1",
            probe_type="type_1",
            units="um",
            probe_description="sample description",
            contact_side_numbering=True,
            contact_size=1.0,
        )
        probe.add_shank(mock_shank_1)
        probe.add_shank(mock_shank_2)

        self.assertIs(probe.get_shank("1"), mock_shank_1)
        self.assertIs(probe.get_shank("2"), mock_shank_2)

        self.assertIsInstance(probe, Probe)

        self.assertIsInstance(probe.id, int)
        self.assertIsInstance(probe.name, str)
        self.assertIsInstance(probe.probe_type, str)
        self.assertIsInstance(probe.units, str)
        self.assertIsInstance(probe.probe_description, str)
        self.assertIsInstance(probe.contact_side_numbering, bool)
        self.assertIsInstance(probe.contact_size, float)
        self.assertIsInstance(probe.shanks, dict)

        self.assertEqual(probe.id, 1)
        self.assertEqual(probe.name, "Probe1")
        self.assertEqual(probe.probe_type, "type_1")
        self.assertEqual(probe.units, "um")
        self.assertEqual(probe.probe_description, "sample description")
        self.assertEqual(probe.contact_side_numbering, True)
        self.assertEqual(probe.contact_size, 1.0)
        self.assertEqual(probe.shanks, {"1": mock_shank_1, "2": mock_shank_2})
