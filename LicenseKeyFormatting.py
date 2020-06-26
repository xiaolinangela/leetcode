def licenseKeyFormatting(S, K):
    new_s = S.replace("-", "").upper()
    if not new_s:
        return ""
    remain = len(new_s) % K
    result = ""
    result += new_s[:remain]
    i = remain
    if i != 0:
        result += "-"
    while i < len(new_s):
        result += new_s[i:i+K]
        result += "-"
        i += K
    if result[-1] == "-":
        result = result[:len(result)-1]
    return result


if __name__ == "__main__":
    S = "5F3Z-2e-9-w"
    print(licenseKeyFormatting(S, 4))
