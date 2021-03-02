
def replace_domain(current_email, old_domain, new_domain):
    if "@" + old_domain in current_email:
        index = current_email.index("@")
        replaced_domain = current_email[:index] + "@" + new_domain
        print("domain changed to: " + replaced_domain)
        return replaced_domain
    return current_email
