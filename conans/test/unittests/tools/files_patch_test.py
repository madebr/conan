    test_processed_profile
        self.assertIn("patch: error: no patch data found!", client.out)
        self.assertIn("ERROR: conanfile.py (test/1.9.10@None/None): "
        ret = loader.load_consumer(file_path, test_processed_profile())
        self.assertEquals(content, msg)