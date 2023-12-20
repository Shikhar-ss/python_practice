This module is a submodule in /Python git repo.
It has been added into it as submodule using:
    git submodule add /home/shikhar/Documents/Python/decorators_py

Now, a submodule repo is like any other file in a repo.
But, any change pushed inside this module should also be commited in the outter repo.

To do that;

    First clone the submodule repo using --recursive flag
        git clone --recursive <url>

        and push like normal

        Go to outside repo, add and push the decorators_py folder.