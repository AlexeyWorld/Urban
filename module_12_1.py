import time
import runner as rn
import unittest
from tqdm import tqdm








class RunnerTest(unittest.TestCase):

    def test_walk(self):
        run1 = rn.Runner('Пешеход')
        print('test_walk:', run1.name)
        for i in tqdm(range(10)):
            run1.walk()
            time.sleep(0.5)
        self.assertEqual(run1.distance, 50)

    def test_run(self):
        run2 = rn.Runner('Бегун')
        print('test_run:', run2.name)
        for i in tqdm(range(10)):
            run2.run()
            time.sleep(0.1)
        self.assertEqual(run2.distance, 100)

    def test_challenge(self):
        run1 = rn.Runner('Черепаха')
        run2 = rn.Runner('Заяц')
        print(f'test_challenge: {run2} (run) VS {run1} (walk)')
        for i in tqdm(range(10)):
            run1.walk()
            run2.run()
            time.sleep(0.25)
        self.assertNotEqual(run1.distance, run2.distance)


if __name__ == "__main__":
    unittest.main()