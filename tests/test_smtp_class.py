class TestSMTP1:
    def test_ehlo(self, smtp_connection) -> None:  
        """  
        Test the SMTP EHLO command  
        
        Args:  
            smtp_connection: A fixture to create an SMTP connection  
            
        Returns:  
            None  
        """  
        response, msg = smtp_connection.ehlo()  
        print("Test EHLO in Class ")  
        assert response == 250  
        assert b"smtp.gmail.com" in msg  
    
    def test_noop(self, smtp_connection) -> None:  
        """  
        Test the SMTP NOOP command  
        
        Args:  
            smtp_connection: A fixture to create an SMTP connection  
            
        Returns:  
            None  
        """  
        response, msg = smtp_connection.noop()  
        print("Test NOOP in Class ")  
        assert response == 250  
        assert b"OK" in msg
