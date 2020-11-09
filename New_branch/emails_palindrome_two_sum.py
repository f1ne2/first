class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result = set()
        emails_edit = []
        for item in emails:
            local, domain = item.split("@")
            if "+" in local:
                local = local[:local.index("+")]
            local = local.replace(".", "")
            emails_edit.append(local + "@" + domain)
        result = len(set(emails_edit))
        return result

class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_string = str(x)[::-1]
        return(str(x) == reverse_string)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            other = target - num
            if other in seen:
                return [seen[other], index]
            else:
                seen[num] = index 