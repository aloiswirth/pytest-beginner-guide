def test_ehlo(smtp_connection) -> None:  
    """  
    Test the SMTP EHLO command  
      
    Args:  
        smtp_connection: A fixture to create an SMTP connection  
          
    Returns:  
        None  
    """  
    response, msg = smtp_connection.ehlo()  
    print("Test EHLO 2 ")  
    assert response == 250  
    assert b"smtp.gmail.com" in msg  
  
def test_noop(smtp_connection) -> None:  
    """  
    Test the SMTP NOOP command  
      
    Args:  
        smtp_connection: A fixture to create an SMTP connection  
          
    Returns:  
        None  
    """  
    response, msg = smtp_connection.noop()  
    print("Test NOOP 2 ")  
    assert response == 250  
    assert b"OK" in msg
