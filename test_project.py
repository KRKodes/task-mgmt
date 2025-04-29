from project import add_task, update_task, view_tasks, search_tasks, main
from unittest.mock import patch
from io import StringIO

# Main Tests
@patch('builtins.input', side_effect=['1', 'New Task', 'Description', '2025-01-07', 'yes', 'work', '5'])
@patch('sys.stdout', new_callable=StringIO)
def test_main_add_task(mock_stdout, mock_input):
    main()
    output = mock_stdout.getvalue()
    expected_messages = [
        "Task added successfully!",
        "Title already exists.",
        "Invalid date format. Please use YYYY-MM-DD.",
        "Invalid input for completion status. Please enter 'yes' or 'no'.",
        "An error occurred: ..."
    ]
    assert any(msg in output for msg in expected_messages)

@patch('builtins.input', side_effect=['2', '3'])
@patch('sys.stdout', new_callable=StringIO)
def test_main_view_tasks(mock_stdout, mock_input):
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
    output = mock_stdout.getvalue()
    assert "Sort by:" in output

@patch('builtins.input', side_effect=['3', '1', '123', 'Updated Title', 'Updated Description', '2025-01-07', 'no', 'work', '5'])
@patch('sys.stdout', new_callable=StringIO)
def test_main_update_task(mock_stdout, mock_input):
    main()
    output = mock_stdout.getvalue()
    assert "Task updated successfully!" in output

@patch('builtins.input', side_effect=['4', '3', '2025-01-07', '5'])
@patch('sys.stdout', new_callable=StringIO)
def test_main_search_tasks(mock_stdout, mock_input):
    main()
    output = mock_stdout.getvalue()
    assert "Search Results" in output

# Add Test
@patch('builtins.input', side_effect=['New Task', 'Description', '2025-01-07', 'yes', 'work'])
@patch('sys.stdout', new_callable=StringIO)
def test_add_task(mock_stdout, mock_input):
    result = add_task()
    expected_messages = [
        "Task added successfully!",
        "Title already exists.",
        "Invalid date format. Please use YYYY-MM-DD.",
        "Invalid input for completion status. Please enter 'yes' or 'no'.",
        "An error occurred: ..."
    ]
    assert result in expected_messages

# Update Tests
@patch('builtins.input', side_effect=['1', '123', 'New Title', 'New Description', '2025-01-07', 'yes', 'work'])
@patch('sys.stdout', new_callable=StringIO)
def test_update_task_by_id(mock_stdout, mock_input):
    result = update_task()
    assert result == "Task updated successfully!"

@patch('builtins.input', side_effect=['2', 'Old Title', 'New Title', 'New Description', '2025-01-07', 'yes', 'work'])
@patch('sys.stdout', new_callable=StringIO)
def test_update_task_by_title(mock_stdout, mock_input):
    result = update_task()
    assert result == "Task updated successfully!"

# View Tests
@patch('builtins.input', side_effect=['1'])  # Sort by ID
@patch('sys.stdout', new_callable=StringIO)
def test_view_tasks_sort_by_id(mock_stdout, mock_input):
    result = view_tasks()
    assert isinstance(result, list)  # Ensure the result is a list
    assert all(isinstance(task, dict) for task in result)  # Ensure each task is a dictionary


@patch('builtins.input', side_effect=['2'])  # Sort by Title A-Z
@patch('sys.stdout', new_callable=StringIO)
def test_view_tasks_sort_by_title_az(mock_stdout, mock_input):
    result = view_tasks()
    assert isinstance(result, list)
    assert all(isinstance(task, dict) for task in result)

@patch('builtins.input', side_effect=['3'])  # Sort by Title Z-A
@patch('sys.stdout', new_callable=StringIO)
def test_view_tasks_sort_by_title_za(mock_stdout, mock_input):
    result = view_tasks()
    assert isinstance(result, list)
    assert all(isinstance(task, dict) for task in result)

@patch('builtins.input', side_effect=['4'])  # Sort by Date Newest to Oldest
@patch('sys.stdout', new_callable=StringIO)
def test_view_tasks_sort_by_date_newest(mock_stdout, mock_input):
    result = view_tasks()
    assert isinstance(result, list)
    assert all(isinstance(task, dict) for task in result)

@patch('builtins.input', side_effect=['5'])  # Sort by Date Oldest to Newest
@patch('sys.stdout', new_callable=StringIO)
def test_view_tasks_sort_by_date_oldest(mock_stdout, mock_input):
    result = view_tasks()
    assert isinstance(result, list)
    assert all(isinstance(task, dict) for task in result)

# Search Tests
@patch('builtins.input', side_effect=['3', '2025-01-07'])
@patch('sys.stdout', new_callable=StringIO)
def test_search_tasks_by_date(mock_stdout, mock_input):
    result = search_tasks()
    assert isinstance(result, list)  # Ensure the result is a list
    assert all(isinstance(task, dict) for task in result)  # Ensure each task is a dictionary

@patch('builtins.input', side_effect=['2', 'yes'])
@patch('sys.stdout', new_callable=StringIO)
def test_search_tasks_by_completion(mock_stdout, mock_input):
    result = search_tasks()
    assert isinstance(result, list)
    assert all(isinstance(task, dict) for task in result)

@patch('builtins.input', side_effect=['1', 'learning'])
@patch('sys.stdout', new_callable=StringIO)
def test_search_tasks_by_category(mock_stdout, mock_input):
    result = search_tasks()
    assert isinstance(result, list)
    assert all(isinstance(task, dict) for task in result)



if __name__ == "__main__":
    main_menu()
