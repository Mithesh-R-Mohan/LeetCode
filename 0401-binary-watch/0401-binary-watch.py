class Solution:
    def readBinaryWatch(self, turnedOn):
        if turnedOn > 8:
            return []
        valid_times = []
        for h in range(12):
            for m in range(60):
                if h.bit_count() + m.bit_count() == turnedOn:
                    valid_times.append(f"{h}:{m:02d}")    
        return valid_times