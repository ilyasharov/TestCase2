def is_even_bitwise(value):
  """
  Определяет четность целого числа с помощью операции поразрядного И.

  Args:
    value: Целое число

  Returns:
    True, если число четное, False - если нечетное
  """

  return (value & 1) == 0


def is_even_shift(value):
  """
  Определяет четность целого числа с помощью сдвига битов.

  Args:
    value: Целое число

  Returns:
    True, если число четное, False - если нечетное
  """

  return (value >> 1) << 1 == value
