# To-Do List Mobile App

## Features

### Task Management
- **Add Tasks**: Users can add a new task by typing its name.
- **Mark as Completed**: Users can mark tasks as completed by tapping a checkbox or the task name.  
  - Completed tasks will have a **strikethrough** or a different color.
- **Delete Tasks**: Users can delete tasks from the list.

---

### User Interface
- **Home Screen**: Displays all tasks in a scrollable list.
- **Add Task Screen**: Provides a simple form for adding new tasks.
- **Clear Layout**: Buttons and icons are easy to understand and use.

---

### Navigation
- **Smooth Navigation**: 
  - Switch between the **Home Screen** and **Add Task Screen**.
- **Easy to Use**: Navigation is simple and intuitive.

---

### Persistence
- **Save Tasks**: Tasks are saved, so they’re still there after the app is closed and reopened.
  - Use local storage (e.g., SQLite, Shared Preferences).

---

### Task Actions
- **Delete Tasks**: Users can remove tasks by swiping or tapping a delete button.
- **Mark as Completed**: Users can toggle tasks between **pending** and **completed**.

---

### User Interaction
- **Responsive App**: Works quickly and smoothly.
- **Confirmation Dialog**: Ask users for confirmation before deleting a task to prevent mistakes.

---

## Optional Features (Extra Credit)
- **Sort Tasks**: By completion status or other criteria.
- **Deadlines and Priorities**: Allow users to add due dates or priorities.
- **Categories/Tags**: Organize tasks into groups.
- **Reminders**: Notifications for pending tasks.
- **Edit Tasks**: Allow users to change task details.

---

## Non-Functional Requirements
- **Performance**: The app works well even with many tasks.
- **Usability**: Easy to understand and use, even for beginners.
- **Security**: Task data is stored securely.

---

## Acceptance Criteria
- Users can:
  - Add tasks.
  - Delete tasks.
  - Mark tasks as completed.
- **Tasks are saved** between app sessions.
- The app is:
  - **User-friendly**.
  - **Bug-free**.

---

## Tools and Technologies
- **Platform**: Android and iOS.
- **Programming Language**: Flutter/Dart (recommended for cross-platform apps).
- **Database**: SQLite or similar for task storage.

---

## Suggested Development Steps
1. **Set up the Project**:
   - Create a new Flutter project.
   - Set up the folder structure.

2. **Build the UI**:
   - Design the **Home Screen** (task list).
   - Design the **Add Task Screen** (input form).

3. **Implement Features**:
   - Add tasks.
   - Mark tasks as completed.
   - Delete tasks.
   - Save tasks locally.

4. **Test the App**:
   - Check for bugs.
   - Make sure tasks persist after closing the app.

5. **Polish the App**:
   - Improve the UI.
   - Add animations (optional).

---

Happy coding! 🎉
