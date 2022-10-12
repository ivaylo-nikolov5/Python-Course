class Helper:
    @staticmethod
    def get_expenses(args):
        total_expenses = 0
        for arg in args:
            if arg.__class__.__name__ == "Child":
                total_expenses += arg.cost * 30
                continue
            total_expenses += arg.get_monthly_expense()

        return total_expenses