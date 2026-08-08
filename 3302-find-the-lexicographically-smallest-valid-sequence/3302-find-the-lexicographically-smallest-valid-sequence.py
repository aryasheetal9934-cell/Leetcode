class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:

        m = len(word2)

        # last[j] = last index in word1
        # where word2[j] can be matched
        last = [-1] * m

        i = len(word1) - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        mismatch_used = False

        for i in range(len(word1)):

            if j == m:
                break

            # Normal matching
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed mismatch
            elif not mismatch_used:

                # If this is the last character,
                # no more character is needed.
                #
                # Otherwise, word2[j+1] must be
                # matchable after index i.
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    j += 1
                    mismatch_used = True

        if j == m:
            return ans

        return []