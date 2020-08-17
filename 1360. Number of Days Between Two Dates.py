class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 平年的 12 个月的天数
        
        d1, d2 = min(date1, date2), max(date1, date2)  # d1 为较小的日期，d2 为较大的日期
        year1, month1, day1 = (int(i) for i in d1.split('-'))
        year2, month2, day2 = (int(i) for i in d2.split('-'))

        def is_leap(year):
            # 判断是否为闰年
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        
        def days_between_two_years(year1, year2):
            # 两个年份之间的间隔天数
            return sum(366 if is_leap(year) else 365 for year in range(year1, year2))
        
        def days_from_year_start(year, month, day):
            # 从当年的1月1号到当天的天数，对于闰年且过了2月的情况，要额外补偿1天
            return sum(month_days[:(month-1)]) + day + (1 if is_leap(year) and month > 2 else 0)
        
        # days(1999年1月15日, 2020年12月31日) = days(1999年1月1日, 2020年1月1日) + days(2020年1月1日, 2020年12月31日) - days(1999年1月1日, 1999年1月15日)
        num_days = days_between_two_years(year1, year2) + days_from_year_start(year2, month2, day2) - days_from_year_start(year1, month1, day1)
        return  num_days


if __name__ == '__main__':  
    func = Solution()
    date1 = "2019-06-29"
    date2 = "2019-08-30"
    print(func.daysBetweenDates(date1, date2))

