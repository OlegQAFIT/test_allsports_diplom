# Automation of quality control
## Final graduation project
### Testing UI automation for www.allsports.fit/by/ using Python and Selenium

This is the final project to automate TeachMeSkills quality control in Python courses to obtain
diploma. This project contains UI tests of the footer and header, main page, page for corporate clients and subscriptions, contacts, halls and maps.
elements. The project can be run in three browsers: Chrome and Edge and Opera. Design Pattern
this project is the page object model. Each page is presented separately
and contains the following:

*data for API testing
* elements (header and footer)
* helpers with basic methods for pages
* element locators for pages
* methods for pages
* tests of individual pages
* README file with information about the project
* folders for Allure report results
* Conftest - file with project settings

To start the project do the following
1. Clone the repository to your computer:
git clone https://github.com/OlegQAFIT/test_allsports_diplom
2. Install the dependencies specified in the require.txt file.
using the command pip install -r require.txt.
3. Set up environment variables to access the www.allsports.fit website.
4. Run the Makefile using the commands it contains.
5. Launch allure - allure serves allure_results_chrome or Edge.

#### Summing up General information on the project

* PEP8 guidelines are followed regarding coding style, variable and function naming.
and files. The project structure ensures convenient work and navigation.
* The Git version control system is used. All changes are moved to a separate branch and
then merged into the main branch. The history of changes and commits is available in the project repository.
* User tests cover the main functionality of the www.allsports.fit website
* The Allure Project Report provides easy tracking of test results and helps analyze errors during operations.


Author:<br>
Oleg Atrokhov, Python automation engineer.

Contacts:<br>
email: oleg.a.allsports.fit@gmail.com