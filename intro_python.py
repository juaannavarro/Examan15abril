import numpy as np

def create_3d_domain(x, y, z):
    """
    Create and display a 3D array representing a simple structural domain.
    
    Parameters:
    - x (int): the size of the first dimension (depth)
    - y (int): the size of the second dimension (rows)
    - z (int): the size of the third dimension (columns)
    
    Returns:
    - np.ndarray: A 3D numpy array filled with zeros.
    """
    # Create a 3D domain using numpy zeros function
    domain = np.zeros((x, y, z))
    
    # Display the created domain
    print("3D Domain Array:")
    print(domain)
    
    return domain

# Example usage:
# create_3d_domain(10, 10, 10)  # Uncomment this line to test the function after reviewing the code
