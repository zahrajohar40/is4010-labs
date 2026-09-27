def calculate_average_age(users):
    """
    Return the average numeric age across a list of user dictionaries.

    Ages that are missing (no "age" key) or non-numeric (not int/float,
    or a bool) are ignored. Returns 0.0 when there are no valid ages.
    """
    valid_ages = []
    for user in users:
        age = user.get("age")
        if isinstance(age, (int, float)) and not isinstance(age, bool):
            valid_ages.append(age)

    if not valid_ages:
        return 0.0

    return sum(valid_ages) / len(valid_ages)


def get_active_user_emails(users):
    """
    Return a list of email addresses for active users.

    A user's email is included only when "is_active" is truthy AND
    the "email" key exists on that user's dictionary. Returns an
    empty list when no such users exist.
    """
    emails = []
    for user in users:
        if user.get("is_active") and "email" in user:
            emails.append(user["email"])
    return emails