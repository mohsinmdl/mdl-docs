# Database Migration


## Show all tables in database via concole
ActiveRecord::Base.connection.tables

## Reset Database
rails db:reset

## model without timestamp

rails g model product --no-timestamps
rails g model style --no-timestamps

## Add index to column
rails g migration AddRefNumToProducts ref_num:string:index

rails g migration add_style_to_product style:references

## Add references to column
rails g migration AddStyleToProducts style:references

## Raise activemethod irreversible migration
(Type of exception: in the model down method)
raise ActiveRecord::IrreversibleMigration

## Undo last Migration

rails db:rollback 

## Migrate status 
rails db:migrate:status


## Revert Migration
rails g migration revert_add_style_to_products

```
require_relative '20200612070523_add_style_to_product'
class RevertAddStyleToProducts < ActiveRecord::Migration[6.0]
  def change
    revert AddStyleToProduct
  end
end
```

## Join Table

(mailing_lists and products)

rails g migration create_join_table_products_mailing_lists mailing_lists products


## Control Migration Output
puts "Message"
say "Message", indent:true

say_with_time 'Message' do 
  sleep 5
end

supress_messages do 
  puts 'Hello from puts'
  say "hello from say"
  say "hello from say", true
end

rails db:migrate VERBOSE=false


## Dump the database schema
rails db:schema:dump
rails db:schema:load

rails db:structure:dump
rails db:structure:load

## Define seed data 
  Character.create(name: 'Luke', movie: movies.first)

## CRUD Record with a block

## Create Record with a block

product = Product.create do |p|
  p.name = 'Fancy Couch'
  p.price = 65.34
end
product.save

## Update Record with a block
product.update_attribute(:name, 'xyz')
product.update_attribute(:name => 'xyz')
product.update(:name => 'xyz')


@products.each do |product|
  product.update_attribute(:visible => true)
end 


Class Method
Product.update_all(:visible => true)

## Delete Record with a block
product.destroy
product.delete


@product.each do |product|
  product.destroy
end

Class method

Product.destroy(152)
Product.destroy([152,153,158])

product.outdated.destroy_all
product.outdated.delete_all


*** Touch Record ***

product.touch # updates updated_at
product.touch(:restocked_at) updates restocked_at
product.touch(:restocked_at, :time => 2.minutes.ago)
  
## Toggle attribute value

blog_post = BlogPost.find(123)
blog_post.published?
//false

blog_post.toggle(:published)
blog_post.published?
//true

hint! not changed in database

if you also need to change in database as well you can do it with the bang(!)

blog_post.toggle!(:published)



## Increment and Dec columns values 

product.increment(:qty_sold) # increment by 1
product.increment(:qty_sold, 5) # increment by 5


// fresh copy from database product.reload

to make changes in database
product.increment!(:qty_sold, 5) # increment by 5

## Track changes to Object
product.changed?  # true
product.changed # ["name"]

product.changes # {"name" => ["BlueSHirt", "GreenShirt"]}
product.changed_attribute # {"name" => ["BlueSHirt"]} // only original values


product.save  

*** trach changes to attribute ***
product.name_changed?
product.name_change
product.name_was
 

product.name_changed(:from => "Couch", :to => "Sofa") # true


*** Restore Attributes ***
product.restore_attributes
//similar to : product.name = product.name_was


## Other find Recored

find_by     // return single object insted of array of object like in where clause
find_by_attr

Product.find_by(:name => 'couch')


*** Dynamic Finder ***
Product.find_by_name('Couch') #first match
Product.find_by_name_and_price('Couch', 500) #first match


*** Assign if not find ***
Product.find_or_create_by(:name => 'couch')


#exists?
#any?
#many?

Product.where(:name => 'couch') # array
Product.exists?(:name => 'couch') #boolean

Product.where(:name => 'couch').any? # boolean
Product.where(:name => 'couch').many? # boolean


## Select Partial Record Data (Remaining)

## Join Tables Query

products = Product.joins(:category).all
*** One Query instead of two queries ***
products = Product.joins(:category).where(:categories => {:name => 'Furniture'})
products = Product.joins(:category).where(:categories => {:name => 'Furniture'}).count
products = Product.joins(:category).order('categories.name ASC').all

*** Two Queries  ***
category = Category.find_by_name("Furniture")
products = Product.where(:categery_id => category.id)

## Distinct Record


Product.joins(:category).pluck(:name)
Category.joins(:product).distinct.pluck(:name)
*** Left Outer Joins *** 
Category.lef_outer_joins(:product).distinct.pluck(:name)


## Eager Loading
```
products.each do |product|
  names << product.category.name 
end
```

vs

```
products.includes(:category).all
```


products = Product.includes(:category).where("categer.name = 'Furniture').references(:category)

products = Product.includes(:category).where(:category => {:name => "Furniture"})


## Associations





















