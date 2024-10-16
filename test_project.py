import unittest
import os
from io import StringIO
from unittest.mock import patch
from gtts import gTTS
from project import truncate_text, choose_language, read_pdf, text_to_speech, download_pdf

class TestProjectFunctions(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_choose_language(self, mock_stdout, mock_input):
        lang_code = choose_language()
        self.assertEqual(lang_code, 'en', "Expected 'en' for English language choice")
        self.assertIn("You have selected: English (en)", mock_stdout.getvalue())
    
    def test_truncate_text_short(self):
        result = truncate_text("short text", max_length=500)
        self.assertEqual(result, "short text", "Expected short text to remain unchanged")

    def test_truncate_text_long(self):
        long_text = "a" * 600
        expected = "a" * 500 + '...'
        result = truncate_text(long_text, max_length=500)
        self.assertEqual(result, expected, "Expected the long text to be truncated at 500 characters with '...'")

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="Lorem Ipsum is simply dummy text")
    @patch('pypdf.PdfReader')
    def test_read_pdf(self, mock_pdf_reader, mock_file):
        mock_pdf_reader.return_value.pages = [unittest.mock.Mock(extract_text=lambda: "Lorem Ipsum is simply dummy text")]
        result = read_pdf("lorem-ipsum.pdf")
        self.assertIn("Lorem Ipsum is simply dummy text", result, "The content should include 'Lorem Ipsum is simply dummy text'")
    
    @patch('gtts.gTTS.save')
    def test_text_to_speech(self, mock_save):
        test_text = "This is a test."
        lang_code = 'en'
        text_to_speech(test_text, lang_code)
        mock_save.assert_called_once_with("speech.mp3")
        self.assertTrue(os.path.exists("speech.mp3"), "Expected the speech file 'speech.mp3' to be created")
    
    @patch('requests.get')
    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    def test_download_pdf(self, mock_open, mock_requests_get):
        mock_response = unittest.mock.Mock()
        mock_response.content = b'%PDF-1.4 Test PDF content'
        mock_requests_get.return_value = mock_response

        file_path = "downloaded_file.pdf"
        download_pdf("http://example.com/test.pdf", file_path)
        
        mock_requests_get.assert_called_once_with("http://example.com/test.pdf")
        mock_open.assert_called_once_with(file_path, 'wb')
        mock_open().write.assert_called_once_with(b'%PDF-1.4 Test PDF content')

if __name__ == '__main__':
    unittest.main()
