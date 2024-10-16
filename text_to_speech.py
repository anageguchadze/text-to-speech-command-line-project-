import os
import sys
from io import StringIO
from project import truncate_text, choose_language, read_pdf, text_to_speech

def test_choose_language():
    sys.stdin = StringIO('1\n')
    sys.stdout = StringIO()

    lang_code = choose_language()

    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__

    assert lang_code == 'en', f"Expected 'en', but got {lang_code}"
    print("test_choose_language passed")

def test_truncate_text():
    assert truncate_text("short text") == "short text", "Short text should not be truncated"

    long_text = "a" * 600
    expected_truncated_text = "a" * 500 + '...'
    assert truncate_text(long_text, 500) == expected_truncated_text, "Long text should be truncated correctly"

    print("test_truncate_text passed")

def test_read_pdf():
    pdf_content = read_pdf('lorem-ipsum.pdf')
    expected_phrases = ["Lorem Ipsum is simply dummy text"]
    for phrase in expected_phrases:
        assert phrase in pdf_content, f"The content should include the phrase: {phrase}"
    print("test_read_pdf passed")

def test_text_to_speech():
    test_text = "This is a test."
    lang_code = 'en'
    text_to_speech(test_text, lang_code)
    assert os.path.exists("speech.mp3"), "The speech file should be created"
    print("test_text_to_speech passed")

if __name__ == "__main__":
    test_choose_language()
    test_truncate_text()
    test_read_pdf()
    test_text_to_speech()