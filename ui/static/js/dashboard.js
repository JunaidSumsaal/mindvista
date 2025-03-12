document.addEventListener('DOMContentLoaded', function () {
  const tabs = document.querySelectorAll('.tab-link');
  const contents = document.querySelectorAll('.tab-content');

  tabs.forEach((tab) => {
    tab.addEventListener('click', function () {
      tabs.forEach((t) =>
        t.classList.remove(
          'text-primary-600',
          'border-primary-600',
          'dark:text-primary-500',
          'dark:border-primary-500'
        )
      );
      this.classList.add(
        'text-primary-600',
        'border-primary-600',
        'dark:text-primary-500',
        'dark:border-primary-500'
      );

      contents.forEach((content) => content.classList.add('hidden'));

      const targetTab = document.getElementById(this.dataset.tab);
      if (targetTab) {
        targetTab.classList.remove('hidden');
      }
    });
  });
});

document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.start-focus').forEach((button) => {
    button.addEventListener('click', function () {
      const taskId = this.dataset.task;
      if (!taskId) {
        return;
      }

      fetch(`/focus/start/${taskId}/`)
        .then((response) => response.json())
        .then((data) => {
          if (data.session_id) {
            alert('Focus session started!');
            window.location.reload();
          } else {
            alert(data.error);
          }
        });
    });
  });

  document.querySelectorAll('.end-focus').forEach((button) => {
    button.addEventListener('click', function () {
      const sessionId = this.dataset.session;
      if (!sessionId) {
        return;
      }

      fetch(`/focus/end/${sessionId}/`)
        .then((response) => response.json())
        .then((data) => {
          alert(`Focus session ended! Duration: ${data.duration} mins`);
          window.location.reload();
        });
    });
  });
});

document.addEventListener('DOMContentLoaded', function () {
  const buttons = document.querySelectorAll('.dropdown-button');
  const dropdownMenu = document.getElementById('dropdown-menu');

  if (!dropdownMenu) {
    return;
  }

  buttons.forEach((button) => {
    button.addEventListener('click', function (event) {
      event.stopPropagation();

      const rect = button.getBoundingClientRect();
      dropdownMenu.style.top = `${rect.bottom + window.scrollY}px`;
      dropdownMenu.style.left = `${rect.left + window.scrollX}px`;

      // Get different dataset values
      const noteId = button.getAttribute('data-note-id');
      const taskId = button.getAttribute('data-task-id');
      const goalId = button.getAttribute('data-goal-id');

      // Ensure elements exist before modifying them
      const editGoal = document.getElementById('edit-goal');
      const deleteGoal = document.getElementById('delete-goal');
      const addMilestone = document.getElementById('add-milestone');

      if (noteId && editGoal && deleteGoal) {
        editGoal.href = `/notes/edit/${noteId}/`;
        deleteGoal.href = `/notes/delete/${noteId}/`;
      }

      if (taskId && editGoal && deleteGoal) {
        editGoal.href = `/tasks/${taskId}/update/`;
        deleteGoal.href = `/tasks/${taskId}/delete/`;
      }

      if (goalId && editGoal && deleteGoal) {
        editGoal.href = `/goals/${goalId}/update/`;
        deleteGoal.href = `/goals/${goalId}/delete/`;
      }

      if (goalId && addMilestone) {
        addMilestone.href = `/goals/${goalId}/milestone/create/`;
      }

      dropdownMenu.classList.toggle('hidden');
    });
  });

  document.addEventListener('click', function (event) {
    if (dropdownMenu && !dropdownMenu.contains(event.target)) {
      dropdownMenu.classList.add('hidden');
    }
  });
});
