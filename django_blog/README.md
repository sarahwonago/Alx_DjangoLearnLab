# Blog Post Management (CRUD) — Documentation

## Overview

This feature set adds Create, Read, Update, Delete operations for the `Post` model.

## URLs

- `/posts/` — list all posts (public)
- `/posts/new/` — create post (authenticated only)
- `/posts/<pk>/` — view single post (public)
- `/posts/<pk>/edit/` — edit post (author only)
- `/posts/<pk>/delete/` — delete post (author only)

## Permissions

- Creating posts: `LoginRequiredMixin` ensures only logged-in users can create.
- Editing/deleting posts: `UserPassesTestMixin` ensures only the post author can edit/delete.

## Forms

- `PostForm` uses `title` and `content`. Author is set automatically in the view's `form_valid`.

## Tests

Run `python manage.py test blog` to execute the included unit tests.

## Notes

- Templates are under `blog/templates/blog`.

## Comment Feature

- Authenticated users can add, edit, and delete their own comments.
- Comments are displayed under each post in reverse chronological order.
- Only the author of a comment can modify or delete it.
- Anonymous users can read comments but must log in to comment.
