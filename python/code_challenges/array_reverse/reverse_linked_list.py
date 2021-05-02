def reverse_list(ll):
    """Reverses a linked list
    Args:
        ll: linked list
    Returns:
        linked list in reversed form
    """
    # put your function implementation here
    ## FIRST WAY
    ll = ll[::-1]
    print(ll)

reverse_list([1,2,3,4,5,"ff", "yahya"])