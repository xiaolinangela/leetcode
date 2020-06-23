def unique(emails):
    unique_list = set()
    for email in emails:
        local, domain = email.split("@")
        if "+" in local:
            local = local[:local.index("+")]
        local = local.replace(".", "")
        unique_list.add(local+"@"+domain)
    return len(unique_list)


if __name__ == "__main__":

    emails = ["test.email+alex@leetcode.com",
              "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    print(unique(emails))
