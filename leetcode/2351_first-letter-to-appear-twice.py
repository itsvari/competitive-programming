class Solution:
    def repeatedCharacter(self, s: str) -> str | None:
        seen = set()
        for character in s:
            if character in seen:
                return character
            seen.add(character)

        return None
