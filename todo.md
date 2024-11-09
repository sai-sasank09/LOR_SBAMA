# TODO


### Frontend stuff

- [x] ~~Login page -> Credentials do not match~~
- [x] ~~About us~~
- [x] ~~Interlink login and signup pages and logout button~~
- [x] ~~Make login as parent root~~
- [x] ~~CSRF protection~~
- [x] ~~Force number inputs in application form~~
- [x] ~~Messages in signup page~~
- [x] ~~HTML page for 404, unauthorized etc~~
- [x] ~~Password fields~~
- [x] ~~Error page go back does not work~~
- [x] ~~Header footer in error pages~~
- [x] ~~Page titles~~
- [x] ~~Favicon~~
- [x] ~~CSRF error page~~
- [x] ~~Remove internal styles~~
- [x] ~~Countries in dropdown~~
- [x] ~~Logout button~~
- [x] ~~/application staffs in same row, exams in same row and docs in same row~~
- [x] ~~Footer in /application~~
- [x] ~~/application form not matching with backend~~
- [x] ~~Missing fields in application.html~~
- [x] ~~Social media links~~
- [x] ~~Fix year of grad in signu~~
- [x] ~~Country field -> Return names instead of country codes~~    
- [x] ~~Country field -> Return names instead of country codes~~
- [x] ~~Messages in signup~~
- [x] ~~Take to home on click "Sathyabama LOR"~~
- [x] ~~Signup confirm password check JS~~
- [x] ~~Social media links~~
- [x] ~~Add contact details in footer and remove contact from nav~~
- [x] ~~student/dashboard.html~~
- [x] ~~Footer 2023~~
- [x] ~~Add name in nav if logged in~~
- [x] ~~Dean dashboard tables column changes?~~
- [x] ~~Add modal for dean dashboard~~
- [x] ~~Dean dashboard view more button color is grey. Change it~~
- [x] ~~url_for all resources~~
- [x] ~~Fix twitter href~~
- [x] ~~Rename images~~
- [x] ~~Fix year of grad in signup~~
- [x] ~~footer line not full width (dashboard, apply)~~
- [x] ~~Pagination center~~
- [x] ~~Prof "thank you for uploading" page~~
- [x] ~~png for sist footer image~~
- [x] ~~Link to go to dashboard from about page~~
- [x] ~~Why does title href to /login~~
- [x] ~~Add link to go to dashoard from about page or other pages~~
- [x] ~~about la name in white text if logged in~~
- [ ] Dean dashboard tables sorting? 
- [ ] Site description for SEO
- [ ] Guidlines add in student.html
- [ ] Change signup to horizontal orientation
- [ ] Reformat application.html
- [ ] Application form message boxes
- [ ] Form validation in signup page
- [ ] Uniform page titles
- [ ] Cache frequently used pictures
- [ ] Dean view more prof name instead of id
- [ ] Search and sort inputs for table
- [ ] Final approve button unlock after prof approvals

---

### Backend stuff

- [x] ~~Test sessions~~
- [x] ~~Update requirements.txt~~
- [x] ~~Figlets~~
- [x] ~~Hash passwords~~
- [x] ~~logout~~
- [x] ~~Cookie encryption while transmission??~~
- [x] ~~Interlink application to student table~~
- [x] ~~File name~~
- [x] ~~Script to create db~~
- [x] ~~Templating~~
- [x] ~~Photos missing here and there~~
- [x] ~~Dept and course in signup~~
- [x] ~~Backref connection bw application and student table (application.student.column_name)~~
- [x] ~~Better way to link student and application rows~~
- [x] ~~Images not loading~~
- [x] ~~Format dates when sending to dashboards~~
- [x] ~~Login -> Dashboard -> application~~
- [x] ~~Do not go back to application page after clicking submit button in /application~~
- [x] ~~Signup phone and mail uniqueness~~
- [x] ~~Add error message for signup fields.~~
- [x] ~~Signup confirm password check~~
- [x] ~~login and signup if else in home page~~
- [x] ~~Fix current user in non auth pages~~
- [x] ~~Delete application~~
- [x] ~~SID and role based login~~
- [x] ~~Package structure~~
- [x] ~~Secure sid hijacking~~
- [x] ~~Mail~~
- [x] ~~Mail credentials -> .env~~
- [x] ~~delete bug~~
- [x] ~~Save docs bug in path~~
- [x] ~~Reload after delete~~
- [x] ~~Define application status values (Create table for it)~~
- [x] ~~Fill env.example~~
- [x] ~~Have a prof table and add relation using id as foreign key in application table~~
- [x] ~~File extention check~~
- [x] ~~Write JS to send post request when clicking approve button~~
- [x] ~~Department and courses into seperate table~~
- [x] ~~About bug~~
- [x] ~~404 bug~~
- [x] ~~Make mailing a non blocking function call~~
- [x] ~~Fix student upload documents names~~
- [x] ~~https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support~~
- [x] ~~Display uploaded docs in dashboard~~
- [x] ~~Forgot password~~
- [x] ~~Why does application.students.name raise error but renders page in prof upload url~~
- [ ] Statistics table
- [ ] Table scalability issues...(Won't rows keep on increasing every year? Diff table for diff batches? Archive tables?)
- [ ] Export stats
- [ ] Map mail acc to prof? Ask prof mail from student? If we store prof mail, give an option to edit it.
- [ ] Radio buttons receive
- [ ] Diff signup page for deans?
- [ ] Design how to store deleted applications (or should we?)
- [ ] Where to store uploaded files?
- [ ] Logout from all devices
- [ ] No sid -> redirect
- [ ] auth.py for auth functions alone
- [ ] Make html for different mail contents and use them instead of fstrings in code?
- [ ] Send mail flag not working in vscode
- [ ] Prof 1 -> 2 -> 3. It should be filled one by one only. Prof 2 ilama prof 3 fill pana koodadhu during application

---

### Fullstack stuff

- [x] ~~Login/logout button changes for pages which can be accessed without login (error pages, about us)~~
- [x] ~~Application status student side~~
- [x] ~~Flowchart?~~
- [x] ~~Logout button missing in dean nav~~
- [x] ~~Show application details for prof upload page~~
- [x] ~~Send mails when a prof uploads a lor~~
- [ ] Edit account student
- [ ] Edit account dean
- [ ] Statistics page
- [ ] Edit application
- [ ] Make "Deans" into "staffs" and add levels like 1, 2, 3 for the staffs (For future expansion maybe)
- [ ] Filter and sorting stuff in tables (dean dashboard)

---

### Security

- [x] ~~Directory traversal?~~
- [ ] Refer: https://www.securecoding.com/blog/flask-security-best-practices/
- [ ] SQL injection -> Sanitize inputs
- [ ] CSRF time limit?
- [ ] Dean signup -> Only a registered dean can create a new dean account?


### Ask Dean of higher studies

- How many students can we expect to use this portal
- How many documents would be submitted by each student
- IELTS, GRE etc before getting LOR or after getting LOR
- IELTS, GRE etc what other exams are there
- What type of exam completion documents are there
- Expiry date of applications




- [ ] Male female thoookanum
- [ ] Dept thookanum
- [ ] Keela kodu student dashboard
- [ ] Form page redesign


Name, reg no, dept, yog
