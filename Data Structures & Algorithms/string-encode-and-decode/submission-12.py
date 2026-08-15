class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "".join(f"Ω{s}" for s in strs)
        return encoded

    def decode(self, s: str) -> List[str]:
        return s.split("Ω")