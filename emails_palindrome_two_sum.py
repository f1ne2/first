def num_unique_emails(self,emails: List[str]) -> int:
    result = set()
    emails_edit = []
    for item in emails:
        local, domain = item.split("@")
        if "+" in local:
            local = local[:local.index("+")]
        local = local.replace(".","")
        emails_edit.append(local + "@" + domain)
    return len(set(emails_edit))


def is_palindrome(self, x: int) -> bool:
    reverse_string = str(x)[::-1]
    return str(x) == reverse_string


def two_sum(self, nums: List[int],target: int) -> List[int]:
    seen = {}
    for index, num in enumerate(nums):
        other = target - num
        if other in seen:
            return [seen[other],index]
        else:
            seen[num] = index