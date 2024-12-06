import pytest

@pytest.fixture
def sample_data():
    return {"a": 3, "b": 10}

import pytest  
import smtplib  
  
@pytest.fixture(scope='session', autouse=True)  
def smtp_connection() -> smtplib.SMTP:  
    """  
    A fixture to create an SMTP connection.  
      
    Returns:  
        An SMTP connection  
    """  
    print("SMTP Connection fixture start")  
    yield smtplib.SMTP("smtp.gmail.com", 587, timeout=60)  
    print("SMTP Connection Tear Down")