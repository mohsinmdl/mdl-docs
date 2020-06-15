# Ruby on Rails

**Creating a new Project**
```bash
rails new taski 
rails new myapp --database=postgresql
```

```bash
rails new --help
```

```bash
rake db:create:all
```


**Starting Rails Server**
```bash
rails server
or

rails s
```



**Should you Use Scaffolds or Generators**

- Scaffolds: add pretty much useless code also.
- Generators: We will use Generators.


**Creating Your First Rails Scaffold**
```
rails g scaffold Project title:string description:text percent_complete:decimal
```

```bash
rake db:migrate
```


## Introduction to the Rails Console

```bash
rails c
```

Sandbox Mode (Any modifications you make will be rolled back on exit)

```bash
rails c --sandbox
```


**How to Create Records in the Rails Console**

```bash
10.times do |project|
Project.create!(title: "Projcect #{project}", description:"Test Description")
end
```


**How to Update and Delete Records in the Rails Console**
```
rails c
```

Project.all

Project.count

p = Project.last
p.update!(title:"Super title")

p.delete

## Advanced Database Queries in the Rails Console


**Find single record by ID**

```bash
Project.find(5)

a = Project.find([5,8])
a.each do |rec|
puts rec.description
end
```


**Find Record by String**

```bash
Project.where(title:"Projcect 8")
Project.where.not(title:"Projcect 8")

Project.where("LENGTH(title) > 20")
```

## Introduction to Routes in Ruby on Rails


**RESTful Routing in Rails**

app/controllers/projects_controller.rb

## How to Create a Custom Controller in Rails

```bash
rails g controller Pages contact about home
```

## How to Create Custom Routes for Non CRUD Pages
get 'about', to:'pages#about'

file_path: app/controllers/pages_controller.rb


Defining Instance Variable to be used in views
```bash
def about
    @title = "Muhammad Mohsin Mahmood"
end
```

**How to Set the Homepage for a Rails Application**

root "pages#home"


**How to Integrate Routing Redirects in Rails**

  - get "*path", to:redirect('/error')
  - get "blog", to: redirect("https://mohsinmdl.com/docs")

**Overview of the Master Application Layout File**

**How to Use View Partials**
    <%= render 'shared/nav' %>


file name nav in share/ should be _nav.html.erb(Partial)


## How to Integrate Images into a Rails Application

        <%= image_tag("logos/profile.png", width:"150px")%>


## Rails Controller
!!! note
    Fat Models/Skinny Controllers Rule

## Rails Models

```bash
rails g model task title:string description:text project:references
rake db:migrate


rails g migration add_completed_to_tasks completed:boolean

rails g migration add_stage_to_tasks stage:integer
rake db:migrate

rails g migration change_data_type_for_stage
  def change
    change_column :projects, :stage, :string
    #Ex:- change_column("admin_users", "email", :string, :limit =>25)
  end

```
## Installing the Devise Gem for Authentication

gem 'devise'

```bash
bundle install
```

```bash
rails generate devise:install
```


rails g devise:views

**Creating user Model**
```bash
rails g devise User

rake db:migrate

rake route | grep users
```
## Authorization


gem 'cancan'
gem 'cancancan' 

## Adding Jquery

https://www.botreetechnologies.com/blog/introducing-jquery-in-rails-6-using-webpacker



```html
<% fields_for :project_bugs, @bug.project_bugs do |assign_form|%>
        <%= assign_form.hidden_field :id%>
        <%= assign_form.select_fids :project_id, Project.collect {} %>
<%end%>
```


## Populate select with collection/Database
```html
<%= form.select :project, options_from_collection_for_select(Bug.all, "id", "title"), {},:multiple=> true,:validate=> true,:class=> 'form-control' %>
```

## Databse restart
```bash
sudo service postgresql restart
rake db:reset
```

!!! error
    ActiveRecord::StatementInvalid (PG::UndefinedColumn: ERROR:  column teachers.classroom_id does not exist)
    LINE 1: ...ers".* FROM "teachers" INNER JOIN "classrooms" ON "teachers"...

!!!success ""
    SOlution => belongs_to in join column insted of has_many


!!! error

    NameError (uninitialized constant Student::Teachers)

!!!success ""
    Solution: make object singlular in front of : belogns_to :patient insted of patient(s)

!!! error 
    uninitialized constant Project::ProjectUser

!!!success ""

    Solution: make sure you are using the correct model name in controller
    like the obove error had resolved via changing ProjectUser to Project(s)User

**Find current user id controller to pass in views**

```bash
@current_user ||= User.find_by(id: session[:user_id])
```
**Form select for collection**

```html
<%= form.select :project, options_from_collection_for_select(Bug.all, "id", "title"), {},:multiple=> true,:validate=> true,:class=> 'form-control' %>
```


