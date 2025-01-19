def format_response(message: str, data: dict = None):
    """
    Formats a consistent API response.
    
    Args:
        message (str): A response message.
        data (dict): Optional additional data.
        
    Returns:
        dict: A formatted response dictionary.
    """
    return {
        "status": "success",
        "message": message,
        "data": data or {}
    }
