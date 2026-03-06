def gradient_descent(learning_rate, num_iterations, initial_theta):
    theta = initial_theta
    for i in range(num_iterations):
        # Calculate the gradient
        gradient = compute_gradient(theta)
        # Update theta
        theta = theta - learning_rate * gradient
    return theta

# Example function for gradient calculation
# You need to implement this based on your specific problem

def compute_gradient(theta):
    # Placeholder for gradient of the loss function
    return theta * 0.1  # Example placeholder

# Example usage
if __name__ == '__main__':
    learning_rate = 0.01
    num_iterations = 1000
    initial_theta = 0.0
    optimal_theta = gradient_descent(learning_rate, num_iterations, initial_theta)
    print(f'Optimal theta: {optimal_theta}')