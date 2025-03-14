import unittest
import asyncio

def run_tests():
    # Test klasöründeki tüm testleri bul ve çalıştır
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Test sonuçlarını göster
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    # Windows'ta asyncio hatasını önlemek için
    if asyncio.get_event_loop().is_closed():
        asyncio.set_event_loop(asyncio.new_event_loop())
    
    # Testleri çalıştır
    run_tests() 