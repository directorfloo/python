import unittest

from Bike import AutoBike

class TestAutoBike(unittest.TestCase):

    def test_initial_state(self):
        bike = AutoBike()
        self.assertFalse(bike.get_turn_on())   # bike should be off
        self.assertEqual(bike.get_gear(), 1)   # gear should start at 1
        self.assertEqual(bike.speed, 0)        # speed should start at 0
        self.assertEqual(bike.get_acceleration(), 0)
        self.assertEqual(bike.get_deceleration(), 0)

    def test_turn_on_bike(self):
        bike = AutoBike()
        bike.set_turn_on()
        self.assertTrue(bike.get_turn_on())

    def test_turn_off_bike_resets(self):
        bike = AutoBike()
        bike.set_turn_on()
        bike.set_acceleration()  # increase speed
        bike.set_turn_off()
        self.assertFalse(bike.get_turn_on())
        self.assertEqual(bike.speed, 0)   # reset speed
        self.assertEqual(bike.get_gear(), 1)  # reset gear

    def test_acceleration_increases_speed_and_counts(self):
        bike = AutoBike()
        bike.set_turn_on()
        bike.set_acceleration()
        self.assertEqual(bike.speed, 5)
        self.assertEqual(bike.get_acceleration(), 1)

    def test_multiple_accelerations_update_gear(self):
        bike = AutoBike()
        bike.set_turn_on()
        for _ in range(6):  # 6 * +5 = 30
            bike.set_acceleration()
        self.assertEqual(bike.speed, 30)
        self.assertEqual(bike.get_gear(), 2)  # should be gear 2

    def test_deceleration_reduces_speed_and_counts(self):
        bike = AutoBike()
        bike.set_turn_on()
        for _ in range(5):  # speed = 25
            bike.set_acceleration()
        bike.set_deceleration()
        self.assertEqual(bike.speed, 20)
        self.assertEqual(bike.get_deceleration(), 1)

    def test_cannot_decelerate_below_zero(self):
        bike = AutoBike()
        bike.set_turn_on()
        bike.set_deceleration()  # at 0 speed
        self.assertEqual(bike.speed, 0)  # no negative speed

    def test_gear_progression_up_to_max(self):
        bike = AutoBike()
        bike.set_turn_on()
        for _ in range(20):  # accelerate a lot
            bike.set_acceleration()
        self.assertGreaterEqual(bike.speed, 100)
        self.assertEqual(bike.get_gear(), 5)  # max gear is 5

if __name__ == "__main__":
    unittest.main()
