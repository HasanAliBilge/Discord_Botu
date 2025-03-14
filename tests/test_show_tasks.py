import unittest
import asyncio
from database import Database
import aiosqlite

class TestShowTasks(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        asyncio.get_event_loop().run_until_complete(self.db.setup())
        # Test başlamadan önce veritabanını temizle
        self.clean_database()

    def clean_database(self):
        async def _clean():
            async with aiosqlite.connect(self.db.db_name) as db:
                await db.execute('DELETE FROM tasks')
                await db.commit()
        asyncio.get_event_loop().run_until_complete(_clean())

    def test_get_all_tasks(self):
        print("Testing get_all_tasks() function.")
        print("Database connection is initialized.")
        
        # Başlangıçta görev olmadığını kontrol et
        tasks = asyncio.get_event_loop().run_until_complete(self.db.get_tasks())
        print("Checking if there are any tasks in the database before the test starts.")
        self.assertEqual(len(tasks), 0)
        print("Test setup passed: No tasks found in the database before the test started.")

        # İki görev ekle
        print("Adding two tasks to the database.")
        asyncio.get_event_loop().run_until_complete(self.db.add_task("Test görevi 1"))
        asyncio.get_event_loop().run_until_complete(self.db.add_task("Test görevi 2"))

        # Görevleri kontrol et
        tasks = asyncio.get_event_loop().run_until_complete(self.db.get_tasks())
        self.assertEqual(len(tasks), 2)
        print("Test passed: Expected 2 tasks and correct number of tasks retrieved.")

        # Görev açıklamalarını kontrol et
        self.assertEqual(tasks[0][1], "Test görevi 1")
        self.assertEqual(tasks[1][1], "Test görevi 2")
        print("Test passed: Task descriptions match correctly.")

    def tearDown(self):
        # Test sonrası temizlik
        self.clean_database() 