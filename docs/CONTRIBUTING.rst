Contributing to django-threaded-multihost
-----------------------------------------

We are pleased to accept contributions and bugfixes for django-threaded-multihost.

To make a contribution:

1. First branch the project from launchpad.  See `django-threaded-multihost on Launchpad`_ for a list of the current branches.  If you simply want to branch the trunk, then all you need do is "bzr branch lp:banjo" to make your own local branch

2. Build and test your addon or update.  You **must** provide tests for us to accept your contribution, and these tests *should* be unit tests rather than doctests.  However, doctests in models are acceptible.  If you are fixing a bug, it is a good rule of thumb to provide a test which provides a regression-test against that bug.

3. If this is a simple patch, go to `django-threaded-multihost on Launchpad`_ and enter a bug with the "bundled" patch generated like this:

   - Go to the root of your working copy.
   - Issue the "bzr update" command. This updates your working copy with changes from the repository. Check for conflicts and resolve them.
   - Issue the "bzr status" command. This shows the status of files. Ensure that all conflicts are resolved.
   - Commit your changes locally with: bzr commit -m "your narrative here"
   - Create your bundle with: bzr bundle > diffname.txt

4. If this is a larger patch or a new feature, make a branch and propose its merger:

   - Make a branch on Launchpad for your addition:

     - Go to launchpad, login, go to your homepage, click on "code" and click on "register branch"
     - Enter "django-threaded-multihost" for the project, and "hosted" for the branch type.
     - When you submit the form, it will give you a command to update the branch, copy it.
     - Push your branch to launchpad using this command.  For example::

 	   "bzr push lp:~bkroeze/django-threaded-multihost/1.0-release"

     - Note: For some reason, you may need to force bzr to use the empty-and-waiting directory by adding the "use existing dir" switch, like so::

 	   "bzr push --use-existing-dir lp:~bkroeze/django-threaded-multihost/1.0-release"

   - Go to the page for your branch and click on "Propose for Merger."  See `Merge Proposals`_ documentation for more information about this.:

	  - Select the target branch: most likely the trunk.
	  - enter any notes in the whiteboard
	  - click "register"

.. _`django-threaded-multihost on Launchpad`: http://code.launchpad.net/django-threaded-multihost
.. _`Merge Proposals`: https://help.launchpad.net/BranchMergeProposals


