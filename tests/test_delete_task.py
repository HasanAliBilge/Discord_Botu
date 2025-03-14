import unittest
import asyncio
from database import Database

class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        asyncio.get_event_loop().run_until_complete(self.db.setup())

    def test_delete_task(self):
        task_id = asyncio.get_event_loop().run_until_complete(
            self.db.add_task("Silinecek görev")
        )
        success = asyncio.get_event_loop().run_until_complete(
            self.db.delete_task(task_id)
        )
        self.assertTrue(success) 