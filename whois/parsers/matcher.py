import re


class Regex:
    def __init__(
        self,
        pattern,
        group,
        flags,
    ):
        self.pattern = pattern
        self.group = group
        self.flags = flags

    def match(
        self,
        subject,
    ):
        match = re.search(
            pattern=self.pattern,
            string=subject,
            flags=self.flags,
        )

        if not match or not match.groups():
            return None

        if self.group not in match.groupdict():
            return None

        return match.group(self.group)
