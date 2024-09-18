def alpha_complement(value):
    """Calculate the alpha complement of a value."""
    return 1 - value
def beta_complement(value):
    """Calculate the beta complement of a value."""
    return 1 - (value ** 2)
def main():
    alpha_value = 0.7
    beta_value = 0.6
    alpha_comp = alpha_complement(alpha_value)
    beta_comp = beta_complement(beta_value)
    print(f"Alpha complement of {alpha_value} is: {alpha_comp}")
    print(f"Beta complement of {beta_value} is: {beta_comp}")
if __name__ == "__main__":
    main()
