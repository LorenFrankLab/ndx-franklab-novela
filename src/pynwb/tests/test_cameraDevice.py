from unittest import TestCase

from src.pynwb.ndx_franklab_novela import CameraDevice


class TestCameraDevice(TestCase):

    def test_cameraDevice_created_successfully(self):

        cam_1 = CameraDevice(
            name='1',
            description="Camera used for tracking running",
            meters_per_pixel=0.20,
            camera_name='test name',
            model='ndx2000',
            lens='500dpt',
            manufacturer='sony',
            serial_number='12345',
            frame_rate=30.0,
            resolution_in_pixels=(1292, 964),
        )

        self.assertEqual(cam_1.name, '1')
        self.assertEqual(cam_1.description, 'Camera used for tracking running')
        self.assertEqual(cam_1.meters_per_pixel, 0.20)
        self.assertEqual(cam_1.camera_name, 'test name')
        self.assertEqual(cam_1.model, 'ndx2000')
        self.assertEqual(cam_1.lens, '500dpt')
        self.assertEqual(cam_1.manufacturer, 'sony')
        self.assertEqual(cam_1.serial_number, '12345')
        self.assertEqual(cam_1.frame_rate, 30.0)
        self.assertEqual(cam_1.resolution_in_pixels, (1292, 964))
