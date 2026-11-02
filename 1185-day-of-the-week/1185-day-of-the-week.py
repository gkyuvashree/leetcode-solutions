class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        import datetime

        days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday"]

        date = datetime.date(year, month, day)

        return days[date.weekday()]