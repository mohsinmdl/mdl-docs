# Examples of Structural pattern in core Java libraries:
***
## Facade Design Pattern

## `javax.faces.context.ExternalContext`

**Java Server Faces (JSF) is a Java-based web application framework intended to simplify development integration of web-based user interfaces**

This class allows the Faces API to be unaware of the nature of its containing application environment. In particular, this class allows JavaServer Faces based appications to run in either a Servlet or a Portlet environment.

> Servlets can render complete web pages, whereas portlets renders html fragments.

```java hl_lines="9 14 18"
/**
 *Returns the servlet context object from the FacesContext
 * 
 * @param context
 * @return
 */
private Object _getServletContextFromFacesContext(FacesContext context)
{
  ExternalContext ec = null;
  Object sc = null;
  
  if (context != null)
  {
    ec = context.getExternalContext();
    
    if (ec != null)
    {
      sc = ec.getContext();
    }
  }
  
  return sc;
}
```


***

## Flyweight Design Pattern

Libraries use flyweight
## `java.lang.Integer.valueOf(int)`

**Also use with
Boolean, Byte, Character, Short, Long, BigDecimal**

>The Flyweight pattern has a single purpose: minimizing memory intake. If your program doesn’t struggle with a shortage of RAM, then you might just ignore this pattern for a while.


If you call the method twice with the same argument, it may return the same object thereby limiting the memory usage. This fits the definition of flyweight pattern.


If we look at the source for valueOf, we can get a hint: Source of java.lang.Integer:

```java 
public static Integer valueOf(int i) {
        assert IntegerCache.high >= 127;
        if (i >= IntegerCache.low && i <= IntegerCache.high)
             return IntegerCache.cache[i + (-IntegerCache.low)];
         return new Integer(i);
}
```

***


## Adapter Design Pattern

Java Libraries use Adapter Design Pattern
<small>
- `java.util.Arrays#asList()`
- `java.util.Collections#list(`)
- `java.util.Collections#enumeration()`
- `java.io.InputStreamReader(InputStream)` (returns a **Reader** object)</small>

> The Adapter pattern is pretty common in Java code. It’s very often used in systems based on some legacy code. In such cases, Adapters make legacy code with modern classes.

**The asList() method of java.util.Arrays class is used to return a fixed-size list backed by the specified array.**

```java
 // creating Arrays of String type 
        String a[] = new String[] { "A", "B", "C", "D" }; 
  
 // getting the list view of Array 
        List<String> list = Arrays.asList(a); 
        
 // printing the list 
        System.out.println("The list is: " + list);
 
```

Output:
>The list is: [A, B, C, D]

***



## Decorator Design Pattern

Decorator in Java

All subclasses of `java.io.InputStream`, `OutputStream`, `Reader` and  `Writer` have constructors that accept objects of their own type.

`java.util.Collections` **methods**
 
 `checkedXXX()`, `synchronizedXXX()` and  `unmodifiableXXX()`.
 
### Checked Collections Examples
The Collections class also provides the checkedXXX() methods that returns a dynamically typesafe view of the specified collection.

Consider an example. The following statements create a checked list and pass it to a third-party library method:

```java
List<String> listNames = Collections.checkedList(new ArrayList<>(), String.class);
 
thirdpartyMethod(listNames);
```

Suppose that the third-party library method is written like this:

```java 
public void thirdpartyMethod(List list) {
    list.add("Tom");    // ok
    list.add("Tom");    // ok
 
    list.add(123);  // throws ClassCastException
}
```
