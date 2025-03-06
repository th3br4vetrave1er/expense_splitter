def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    if number_of_people < 1:
        raise ValueError('Number of people must be greater than one')

    share_per_person: float = total_amount / number_of_people
    print(
        f'Total expense: {currency}{total_amount:,.2f}'
    )

    print(
        f'Number of people: {number_of_people}'
    )

    print(
        f'Each person should pay {currency}{share_per_person:,.2f}'
    )


def main() -> None:
    running: bool = True
    while running:
        try:
            total_amount: float = float(input('Enter the total amount of the expense: '))
            number_of_people: int = int(input('How many people sharing expense: '))

            calculate_split(
                total_amount=total_amount,
                number_of_people=number_of_people,
                currency='$'
                )
            running = False
        except ValueError as e:
            print(
                f'Error {e}'
            )
            print(
                'Oopsie! Please try again with a propper value!'
            )


if __name__ == '__main__':
    main()

# TODO add somehow not even splits! for example person1 had just a glass of water,
# and person2 had steak, the splitting should not be equal!