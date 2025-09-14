## paginator

Provides a pagination mechanism for displaying data across multiple pages on Discord, allowing users to navigate interactively using buttons or reactions.

### Parameters:
- `data`: Data to be paginated (list or iterable).
- `per_page`: Number of items per page.
- `embed_func`: Function to create embeds per page.
- Other parameters to control navigation and appearance.

### Return:
- Displays embeds in a paginated format and handles user interactions for page navigation.

### Actions:
- **prev**: Moves to the previous embed page.
- **next**: Moves to the next embed page.
- **cancel**: Deletes the embed message.
- **navigate**: Displays the current embed page number. When pressed, prompts the user to enter a page number and navigates to the specified page.