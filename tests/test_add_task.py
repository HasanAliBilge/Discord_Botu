import unittest
import asyncio
from database import Database
import aiosqlite

class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        asyncio.get_event_loop().run_until_complete(self.db.setup())
        self.clean_database()

    def clean_database(self):
        async def _clean():
            async with aiosqlite.connect(self.db.db_name) as db:
                await db.execute('DELETE FROM tasks')
                await db.commit()
        asyncio.get_event_loop().run_until_complete(_clean())

    def test_add_task(self):
        print("Testing add_task() function.")
        
        # Görev ekle
        task_id = asyncio.get_event_loop().run_until_complete(
            self.db.add_task("Test görevi")
        )
        self.assertIsNotNone(task_id)
        print(f"Test passed: Task added with ID: {task_id}")

        # Eklenen görevi kontrol et
        tasks = asyncio.get_event_loop().run_until_complete(self.db.get_tasks())
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0][1], "Test görevi")
        print("Test passed: Task description matches correctly.")

    def tearDown(self):
        self.clean_database() 