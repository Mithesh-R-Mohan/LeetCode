class Solution(object):
    def licenseKeyFormatting(self, s, k):
        cleaned_s = s.replace("-", ""). upper()
        if not cleaned_s:
            return ""
        first_group_len = len(cleaned_s) % k
        result = []
        if first_group_len > 0:
            result.append(cleaned_s[:first_group_len])
        for i in range(first_group_len, len(cleaned_s), k):
            result.append(cleaned_s[i:i+k])
        return "-".join(result)