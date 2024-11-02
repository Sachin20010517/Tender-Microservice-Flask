def validate_tender_data(data):
    errors = []
    if not data.get("title"):
        errors.append("Title is required.")
    if not data.get("amount"):
        errors.append("Amount is required.")
    # Add other field validations as needed
    return errors if errors else None
