# Social Media API

## Description

This project is a RESTful API for a social media platform built using Django and Django REST Framework. The API allows users to create profiles, follow other users, create and retrieve posts, manage likes and comments, and perform basic social media actions.

## Features

### User Registration and Authentication
- Users can register with their email and password to create an account.
- Users can login with their credentials and receive a token for authentication.
- Users can logout and invalidate their token.

### User Profile
- Users can create and update their profile, including profile picture, bio, and other details.
- Users can retrieve their own profile and view profiles of other users.
- Users can search for users by username or other criteria.

### Follow/Unfollow
- Users can follow and unfollow other users.
- Users can view the list of users they are following and the list of users following them.

### Post Creation and Retrieval
- Users can create new posts with text content and optional media attachments (e.g., images).
- Users can retrieve their own posts and posts of users they are following.
- Users can retrieve posts by hashtags or other criteria.

### API Permissions
- Only authenticated users can perform actions such as creating posts, liking posts, and following/unfollowing users.
- Users can only update and delete their own posts and comments.
- Users can only update and delete their own profile.

## Setup and Installation

1. Clone the repository.

    $ git clone https://github.com/username/social-media-api.git

2. Change directory to the project folder.

    $ cd social-media-api

3. Create a virtual environment and activate it.

   $ python -m venv venv
   $ source venv/bin/activate

4. Install the required packages.

    $ pip install -r requirements.txt

5. Apply database migrations.

    $ python manage.py migrate

6. Run the development server.

    $   python manage.py runserver
