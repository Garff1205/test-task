**Task**: Using any programming language, you need to write the following automated tests for the website:
https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all

1. Select all rows from the Customers table and verify that the record with ContactName = 'Giovanni Rovelli' has Address = 'Via Ludovico il Moro 22'.
2. Select only the rows from the Customers table where City = 'London'. Verify that there are exactly 6 such records.
3. Add a new row to the Customers table and check that the row has been successfully inserted.
4. Update all fields (except CustomerID) in any row of the Customers table and verify that the changes have been saved to the database.
5. Create your own custom test case and implement it — your imagination is the only limit here.

You can fill the SQL input field using JavaScript code with the window.editor object.

Requirements:
- You must use Selenium WebDriver for test automation
- The test code should be uploaded to any Git repository
- Tests must be runnable inside a Docker container

**Execution**:
Run tests in Docker:
Run `web_driver` service from `docker_compose.yml` first, and then `tests` service.

Run tests in IDE:
Run only  `web_driver` service from `docker_compose.yml`

**Troubleshooting**:
- `All tests fail on the first run`:
Conditions: First start with docker-compose.
Solution: Restart only test container. Or start browser container first, then run the tests container.
Reason: `depends_on` in docker-compose waits only container start. Tests container and tests inside it could together start faster than browser after it's container ready. As a result the tests may go to the browser that has not yet started.
Note: Such a problem does not reprodice in CI, as in CI, the browser instances are correctly started in a separate job preceding the tests.
