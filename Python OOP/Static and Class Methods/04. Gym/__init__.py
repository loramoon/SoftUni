from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.gym import Gym
from project.subscription import Subscription
from project.trainer import Trainer

import unittest


class TestGym(unittest.TestCase):
    def test_gym_subscription_info(self):
        Gym.id = 1
        Subscription.id = 1
        ExercisePlan.id = 1
        Equipment.id = 1
        Trainer.id = 1
        Customer.id = 1
        g = Gym()
        s = Subscription("10.02.2020", 1, 1, 1)
        p = ExercisePlan(1, 1, 10)
        e = Equipment("Pesho")
        t = Trainer("Pesho")
        c = Customer("Pesho", "addr.", "pesho@gmail.com")
        g.add_subscription(s)
        g.add_customer(c)
        g.add_equipment(e)
        g.add_plan(p)
        g.add_trainer(t)
        self.assertEqual(g.subscription_info(1).strip(),
                         "Subscription <1> on 10.02.2020\nCustomer <1> Pesho; Address: addr.; Email: pesho@gmail.com\nTrainer <1> Pesho\nEquipment <1> Pesho\nPlan <1> with duration 10 minutes")


if __name__ == "__main__":
    unittest.main()
