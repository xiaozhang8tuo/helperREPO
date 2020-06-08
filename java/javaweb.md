# day1  【基础加强笔记】 #

## 第一章 Junit单元测试： ##

### Junit单元测试 ###

```java
package cn.itcast.junit;

/**
 * 计算器类
 */
public class Calculator {


    /**
     * 加法
     * @param a
     * @param b
     * @return
     */
    public int add (int a , int b){
        //int i = 3/0;

        return a + b;
    }

    /**
     * 减法
     * @param a
     * @param b
     * @return
     */
    public int sub (int a , int b){
        return a - b;
    }

}
package cn.itcast.test;

import cn.itcast.junit.Calculator;
import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

public class CalculatorTest {
    /**
     * 初始化方法：
     *  用于资源申请，所有测试方法在执行之前都会先执行该方法
     */
    @Before
    public void init(){
        System.out.println("init...");
    }

    /**
     * 释放资源方法：
     *  在所有测试方法执行完后，都会自动执行该方法
     */
    @After
    public void close(){
        System.out.println("close...");
    }


    /**
     * 测试add方法
     */
    @Test
    public void testAdd(){
       // System.out.println("我被执行了");
        //1.创建计算器对象
        System.out.println("testAdd...");
        Calculator c  = new Calculator();
        //2.调用add方法
        int result = c.add(1, 2);
        //System.out.println(result);

        //3.断言  我断言这个结果是3
        Assert.assertEquals(3,result);

    }

    @Test
    public void testSub(){
        //1.创建计算器对象
        Calculator c  = new Calculator();
        int result = c.sub(1, 2);
        System.out.println("testSub....");
        Assert.assertEquals(-1,result);
    }
}
```

## 第二章：反射：框架设计的灵魂 ##

### Person类 ###

```java
package cn.itcast.domain;

public class Person {
    private String name;
    private int age;

    public String a;
    protected String b;
    String c;
    private String d;


    public Person() {
    }

    public Person(String name, int age) {

        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                ", a='" + a + '\'' +
                ", b='" + b + '\'' +
                ", c='" + c + '\'' +
                ", d='" + d + '\'' +
                '}';
    }


    public void eat(){
        System.out.println("eat...");
    }

    public void eat(String food){
        System.out.println("eat..."+food);
    }
}
```

### 1 获取字节码class对象的3种方法 ###

```java
package cn.itcast.reflect;

import cn.itcast.domain.Person;
import cn.itcast.domain.Student;

public class ReflectDemo1 {


    /**
        获取Class对象的方式：
            1. Class.forName("全类名")：将字节码文件加载进内存，返回Class对象
            2. 类名.class：通过类名的属性class获取
            3. 对象.getClass()：getClass()方法在Object类中定义着。

     */
    public static void main(String[] args) throws Exception {

        //1.Class.forName("全类名")
        Class cls1 = Class.forName("cn.itcast.domain.Person");
        System.out.println(cls1);
        //2.类名.class
        Class cls2 = Person.class;
        System.out.println(cls2);
        //3.对象.getClass()
        Person p = new Person();
        Class cls3 = p.getClass();
        System.out.println(cls3);

        //== 比较三个对象
        System.out.println(cls1 == cls2);//true
        System.out.println(cls1 == cls3);//true


        Class c = Student.class;
        System.out.println(c == cls1);

    }
}
```

### 2 Class对象功能--获取成员变量 ###

```java
package cn.itcast.reflect;
import cn.itcast.domain.Person;
import java.lang.reflect.Field;
public class ReflectDemo2 {

    /**
     Class对象功能：
         * 获取功能：
         1. 获取成员变量们
             * Field[] getFields() 获取所有public修饰的成员变量
             * Field getField(String name) 获取指定名称的 public修饰的成员变量

             * Field[] getDeclaredFields() 获取所有的成员变量，不考虑修饰符
             * Field getDeclaredField(String name)
         2. 获取构造方法们
             * Constructor<?>[] getConstructors()
             * Constructor<T> getConstructor(类<?>... parameterTypes)

             * Constructor<T> getDeclaredConstructor(类<?>... parameterTypes)
             * Constructor<?>[] getDeclaredConstructors()
         3. 获取成员方法们：
             * Method[] getMethods() 获取所有public修饰的方法
             * Method getMethod(String name, 类<?>... parameterTypes)

             * Method[] getDeclaredMethods() 获取所有的成员方法，不考虑修饰符
             * Method getDeclaredMethod(String name, 类<?>... parameterTypes)

         4. 获取类名
             * String getName()



     */

    public static void main(String[] args) throws Exception {

        //0.获取Person的Class对象
        Class personClass = Person.class;
        /*
             1. 获取成员变量们
                 * Field[] getFields()
                 * Field getField(String name)

                 * Field[] getDeclaredFields()
                 * Field getDeclaredField(String name)

         */
        //1.Field[] getFields()获取所有public修饰的成员变量
        Field[] fields = personClass.getFields();
        for (Field field : fields) {
            System.out.println(field);
        }

        System.out.println("------------");
        //2.Field getField(String name)
        Field a = personClass.getField("a");
        //获取成员变量a 的值
        Person p = new Person();
        Object value = a.get(p);
        System.out.println(value);
        //设置a的值
        a.set(p,"张三");
        System.out.println(p);

        System.out.println("===================");

        //Field[] getDeclaredFields()：获取所有的成员变量，不考虑修饰符
        Field[] declaredFields = personClass.getDeclaredFields();
        for (Field declaredField : declaredFields) {
            System.out.println(declaredField);
        }
        //Field getDeclaredField(String name)
        Field d = personClass.getDeclaredField("d");
        //忽略访问权限修饰符的安全检查  不加的话 私有成员变量是无法访问的
        d.setAccessible(true);//暴力反射
        Object value2 = d.get(p);
        System.out.println(value2);
    }
}
/*
public java.lang.String cn.itcast.domain.Person.a
------------
null
Person{name='null', age=0, a='张三', b='null', c='null', d='null'}
===================
private java.lang.String cn.itcast.domain.Person.name
private int cn.itcast.domain.Person.age
public java.lang.String cn.itcast.domain.Person.a
protected java.lang.String cn.itcast.domain.Person.b
java.lang.String cn.itcast.domain.Person.c
private java.lang.String cn.itcast.domain.Person.d
null
```

### 3 Class对象功能--获取构造器(构造方法) ###

```java
package cn.itcast.reflect;

import cn.itcast.domain.Person;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;

public class ReflectDemo3 {
    public static void main(String[] args) throws Exception {

        //0.获取Person的Class对象
        Class personClass = Person.class;
        /*
            2. 获取构造方法们
                 * Constructor<?>[] getConstructors()
                 * Constructor<T> getConstructor(类<?>... parameterTypes)

                 * Constructor<T> getDeclaredConstructor(类<?>... parameterTypes)
                 * Constructor<?>[] getDeclaredConstructors()
         */


        //Constructor<T> getConstructor(类<?>... parameterTypes)
        Constructor constructor = personClass.getConstructor(String.class, int.class);
        System.out.println(constructor);
        //创建对象
        Object person = constructor.newInstance("张三", 23);
        System.out.println(person);
        System.out.println("----------");

        Constructor constructor1 = personClass.getConstructor();
        System.out.println(constructor1);
        //创建对象
        Object person1 = constructor1.newInstance();
        System.out.println(person1);
        //创建空参对象可以直接调用类对象的newInstance()，不需要再去调用空参构造器对象的newInstance()
        Object o = personClass.newInstance();
        System.out.println(o);
        //constructor1.setAccessible(true);
    }
}
```

### 4 Class对象功能--获取成员方法.invoke() /获取类名 ###

```java
package cn.itcast.reflect;

import cn.itcast.domain.Person;

import java.lang.reflect.Constructor;
import java.lang.reflect.Method;

public class ReflectDemo4 {

    public static void main(String[] args) throws Exception {

        //0.获取Person的Class对象
        Class personClass = Person.class;
        /*
          3. 获取成员方法们：
             * Method[] getMethods()
             * Method getMethod(String name, 类<?>... parameterTypes)

             * Method[] getDeclaredMethods()
             * Method getDeclaredMethod(String name, 类<?>... parameterTypes)
         */
        //获取指定名称的方法
        Method eat_method = personClass.getMethod("eat");
        Person p = new Person();
        //执行方法
        eat_method.invoke(p);


        Method eat_method2 = personClass.getMethod("eat", String.class);
        //执行方法
        eat_method2.invoke(p,"饭");

        System.out.println("-----------------");

        //获取所有public修饰的方法
        Method[] methods = personClass.getMethods();
        for (Method method : methods) {
            System.out.println(method);
            String name = method.getName();
            System.out.println(name);
            //method.setAccessible(true);
        }
        //获取类名
        String className = personClass.getName();
        System.out.println(className);//cn.itcast.domain.Person
    }
}
```

### 反射实例  框架类（可以创建任意类的对象，可以执行任意方法） ###

```java
package cn.itcast.reflect;

import cn.itcast.domain.Person;
import cn.itcast.domain.Student;

import java.io.IOException;
import java.io.InputStream;
import java.lang.reflect.Method;
import java.util.Properties;

/**
 * 框架类
 */
public class ReflectTest {
    public static void main(String[] args) throws Exception {
        //可以创建任意类的对象，可以执行任意方法

        /*
            前提：不能改变该类的任何代码。可以创建任意类的对象，可以执行任意方法
         */
      /*  Person p = new Person();
        p.eat();*/
/*
        Student stu = new Student();
        stu.sleep();*/

        //1.加载配置文件
        //1.1创建Properties对象
        Properties pro = new Properties();//map中和IO流有关的
        //1.2加载配置文件，转换为一个集合
        //1.2.1获取class目录下的配置文件
        ClassLoader classLoader = ReflectTest.class.getClassLoader();
        InputStream is = classLoader.getResourceAsStream("apple.properties");
        pro.load(is);
        //2.获取配置文件中定义的数据
        String className = pro.getProperty("className");
        //cn.itcast.domain.Person
        String methodName = pro.getProperty("methodName");
        //eat
        //3.加载该类进内存
        Class cls = Class.forName(className);
        //4.创建对象
        Object obj = cls.newInstance();
        //5.获取方法对象
        Method method = cls.getMethod(methodName);
        //6.执行方法
        method.invoke(obj);
    }
}


apple.properties文件内容
className=cn.itcast.domain.Person
methodName=eat
```

## 第三章：注解 ##

①	编写文档：通过代码里标识的注解生成文档【生成文档doc文档】@param @return
javadoc 类 生成类似说明文档的html
②	代码分析：通过代码里标识的注解对代码进行分析【使用反射】
③	编译检查：通过代码里标识的注解让编译器能够实现基本的编译检查   @Override

### JDK自带注解 ###

```java
package cn.itcast.annotation;

import java.util.Date;

/**
 * JDK中预定义的一些注解
 *        * @Override    ：检测被该注解标注的方法是否是继承自父类(接口)的
 *        * @Deprecated：该注解标注的内容，表示已过时
 *        * @SuppressWarnings：压制警告
 */

@SuppressWarnings("all")
public class AnnoDemo2 {

    @Override
    public String toString() {
        return super.toString();
    }

    @Deprecated
    public void show1(){
        //有缺陷
    }

    public void show2(){
        //替代show1方法
    }

    public void demo(){
        show1();
        Date date = new Date();
    }
}
```

### 自定义注解的属性/抽象方法 ###

```java
package cn.itcast.annotation;

//import com.sun.corba.se.spi.orbutil.threadpool.Work;

public @interface MyAnno {

     int value();
     Person per();
     MyAnno2 anno2();
     String[] strs();
     String name() default "张三";
     /*String show2();

     Person per();
     MyAnno2 anno2();

     String[] strs();*/
}

package cn.itcast.annotation;


//int 枚举 注解 数组
@MyAnno(value=12,per = Person.P1,anno2 = @MyAnno2,strs="bbb")
@MyAnno3
public class Worker {
    @MyAnno3
    public String name = "aaa";
    @MyAnno3
    public void show(){
        
    }
}
public enum Person {

    P1,P2;
}
public @interface MyAnno2 {

}
```

### 自定义注解的元注解 ###

```java
package cn.itcast.annotation;

import java.lang.annotation.*;

/**

 元注解：用于描述注解的注解
     * @Target：描述注解能够作用的位置
     * @Retention：描述注解被保留的阶段
     * @Documented：描述注解是否被抽取到api文档中
     * @Inherited：描述注解是否被子类继承
 *
 */

@Target({ElementType.TYPE,ElementType.METHOD,ElementType.FIELD})
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
public @interface MyAnno3 {
}
```

### 反射实例  框架类（可以创建任意类的对象，可以执行任意方法）经过注释改进  通过配置文件实现 ###

```java
package cn.itcast.annotation;

import java.io.InputStream;
import java.lang.reflect.Method;
import java.util.Properties;

/**
 * 框架类
 */

@Pro(className = "cn.itcast.annotation.Demo1",methodName = "show")
public class ReflectTest {
    public static void main(String[] args) throws Exception {

        /*
            前提：不能改变该类的任何代码。可以创建任意类的对象，可以执行任意方法
         */
        //1.解析注解
        //1.1获取该类的字节码文件对象
        Class<ReflectTest> reflectTestClass = ReflectTest.class;
        //2.获取上边的注解对象
        //其实就是在内存中生成了一个该注解接口(Pro)的子类(ProImpl)实现对象(an)
        /*

            public class ProImpl implements Pro{
                public String className(){
                    return "cn.itcast.annotation.Demo1";
                }
                public String methodName(){
                    return "show";
                }
            }
 */
        Pro an = reflectTestClass.getAnnotation(Pro.class);
        //3.调用注解对象中定义的抽象方法，获取返回值
        String className = an.className();
        String methodName = an.methodName();
        System.out.println(className);  //cn.itcast.annotation.Demo1
        System.out.println(methodName); //show
        
        //3.加载该类进内存
        Class cls = Class.forName(className);
        //4.创建对象
        Object obj = cls.newInstance();
        //5.获取方法对象
        Method method = cls.getMethod(methodName);
        //6.执行方法
        method.invoke(obj);
    }
}

package cn.itcast.annotation;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * 描述需要执行的类名，和方法名
 */

@Target({ElementType.TYPE})
@Retention(RetentionPolicy.RUNTIME)
public @interface Pro {

    String className();
    String methodName();
}
```

### 简单的测试框架 @check ###

```java
package cn.itcast.annotation.demo;


/**
 * 小明定义的计算器类
 */
public class Calculator {

    //加法
    @Check
    public void add(){
        String str = null;
        str.toString();
        System.out.println("1 + 0 =" + (1 + 0));
    }
    //减法
    @Check
    public void sub(){
        System.out.println("1 - 0 =" + (1 - 0));
    }
    //乘法
    @Check
    public void mul(){
        System.out.println("1 * 0 =" + (1 * 0));
    }
    //除法
    @Check
    public void div(){
        System.out.println("1 / 0 =" + (1 / 0));
    }

    public void show(){
        System.out.println("永无bug...");
    }
}

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Check {
}

package cn.itcast.annotation.demo;
/**
 * 简单的测试框架
 *
 * 当主方法执行后，会自动自行被检测的所有方法(加了Check注解的方法)，判断方法是否有异常，记录到文件中
 */
public class TestCheck {
    public static void main(String[] args) throws IOException {
        //1.创建计算器对象
        Calculator c = new Calculator();
        //2.获取字节码文件对象
        Class cls = c.getClass();
        //3.获取所有方法
        Method[] methods = cls.getMethods();

        int number = 0;//出现异常的次数
        BufferedWriter bw = new BufferedWriter(new FileWriter("bug.txt"));


        for (Method method : methods) {
            //4.判断方法上是否有Check注解
            if(method.isAnnotationPresent(Check.class)){
                //5.有，执行
                try {
                    method.invoke(c);
                } catch (Exception e) {
                    //6.捕获异常

                    //记录到文件中
                    number ++;

                    bw.write(method.getName()+ " 方法出异常了");
                    bw.newLine();
                    bw.write("异常的名称:" + e.getCause().getClass().getSimpleName());
                    bw.newLine();
                    bw.write("异常的原因:"+e.getCause().getMessage());
                    bw.newLine();
                    bw.write("--------------------------");
                    bw.newLine();
                }
            }
        }
        bw.write("本次测试一共出现 "+number+" 次异常");
        bw.flush();
        bw.close();
    }

}
/*add 方法出异常了
异常的名称:NullPointerException
异常的原因:null
--------------------------
div 方法出异常了
异常的名称:ArithmeticException
异常的原因:/ by zero
--------------------------
本次测试一共出现 2 次异常
```

# day02/03/04【MySQL】 #

### MySQL基础 ###

```sql
DROP TABLE student3;

CREATE TABLE student3(
id INT, -- 编号
NAME VARCHAR(20), -- 姓名
age INT, -- 年龄
sex VARCHAR(5), -- 性别
address VARCHAR(100), -- 地址
math INT, -- 数学
english INT -- 英语
);

DESC student3;
ALTER TABLE student3 CHANGE NAME NAME VARCHAR(20) CHARACTER SET utf8;
ALTER TABLE student3 CHANGE address address VARCHAR(100) CHARACTER SET utf8;
ALTER TABLE student3 CHANGE sex sex VARCHAR(10) CHARACTER SET utf8;


INSERT INTO student3(id,NAME,age,sex,address,math,english) VALUES (1,'马云',55,'男','
杭州',66,78),(2,'马化腾',45,'女','深圳',98,87),(3,'马景涛',55,'男','香港',56,77),(4,'柳岩
',20,'女','湖南',76,65),(5,'柳青',20,'男','湖南',86,NULL),(6,'刘德华',57,'男','香港',99,99),(7,'马德',22,'女','香港',99,99),(8,'德玛西亚',18,'男','南京',56,65);
SELECT * FROM student3;

SELECT NAME,age FROM student3;
SELECT 
	NAME, -- 姓名
	age   -- 年龄
FROM 
	student3;

-- 去除重复
SELECT DISTINCT address FROM student3;

-- null 存在的结果会报错
SELECT NAME, math, english, math+english FROM student3;
SELECT id,NAME, math, english, math+ IFNULL(english,0) FROM student3;
SELECT id,NAME, math, english, math+ IFNULL(english,0) AS 总分 FROM student3;
SELECT id,NAME, math 数学, english 英语, math+ IFNULL(english,0) 总分 FROM student3;

SELECT * FROM student3 WHERE NAME LIKE '_化%'
SELECT * FROM student3 WHERE NAME LIKE '___'
```

### MySQL的约束与设计 ###

```sql
DROP TABLE student3;

CREATE TABLE student3(
id INT, -- 编号
NAME VARCHAR(20), -- 姓名
age INT, -- 年龄
sex VARCHAR(5), -- 性别
address VARCHAR(100), -- 地址
math INT, -- 数学
english INT -- 英语
);

DESC student3;
ALTER TABLE student3 CHANGE NAME NAME VARCHAR(20) CHARACTER SET utf8;
ALTER TABLE student3 CHANGE address address VARCHAR(100) CHARACTER SET utf8;
ALTER TABLE student3 CHANGE sex sex VARCHAR(10) CHARACTER SET utf8;


INSERT INTO student3(id,NAME,age,sex,address,math,english) VALUES (1,'马云',55,'男','
杭州',66,78),(2,'马化腾',45,'女','深圳',98,87),(3,'马景涛',55,'男','香港',56,77),(4,'柳岩
',20,'女','湖南',76,65),(5,'柳青',20,'男','湖南',86,NULL),(6,'刘德华',57,'男','香港',99,99),(7,'马德',22,'女','香港',99,99),(8,'德玛西亚',18,'男','南京',56,65);
SELECT * FROM student3;

SELECT NAME,age FROM student3;
SELECT 
	NAME, -- 姓名
	age   -- 年龄
FROM 
	student3;

-- 去除重复
SELECT DISTINCT address FROM student3;

-- null 存在的结果会报错
SELECT NAME, math, english, math+english FROM student3;
SELECT id,NAME, math, english, math+ IFNULL(english,0) FROM student3;
SELECT id,NAME, math, english, math+ IFNULL(english,0) AS 总分 FROM student3;
SELECT id,NAME, math 数学, english 英语, math+ IFNULL(english,0) 总分 FROM student3;

SELECT * FROM student3 WHERE NAME LIKE '_化%'
SELECT * FROM student3 WHERE NAME LIKE '___'

SELECT * FROM student3 ORDER BY math DESC ,english DESC;

SELECT COUNT(NAME) FROM student3;
SELECT MIN(math) FROM student3;
SELECT AVG(english) FROM student3;
SELECT MIN(english) FROM student3;

SELECT sex , AVG(math), COUNT(id) FROM student3 GROUP BY sex;

SELECT sex , AVG(math),COUNT(id) FROM student3 WHERE math > 70 GROUP BY sex HAVING COUNT(id) > 2;



DROP TABLE stu;
SELECT * FROM stu;
CREATE TABLE stu(
	id INT,
	NAME VARCHAR(20) NOT NULL -- name非空
)DEFAULT CHARACTER SET = utf8;
DESC stu;
INSERT INTO  stu(id,NAME) VALUES(1,"王尼玛");

-- 创建表完后，添加非空约束
ALTER TABLE stu MODIFY NAME VARCHAR(20) NOT NULL;

-- 删除表的非空约束
ALTER TABLE stu MODIFY NAME VARCHAR(20);


DROP TABLE stu;
CREATE TABLE stu(
			id INT,
			phone_number VARCHAR(20) UNIQUE -- 添加了唯一约束
		)DEFAULT CHARACTER SET = utf8;
	
	
DROP TABLE emp;
CREATE TABLE emp(
	id  INT PRIMARY KEY AUTO_INCREMENT,
	NAME VARCHAR(20) ,
	age INT ,
	dep_name  VARCHAR(20) ,
	dep_location  VARCHAR(20) 
)DEFAULT CHARACTER SET = utf8;

INSERT INTO emp( NAME, age, dep_name, dep_location) VALUES('张三',20, '研发部', '广州');
INSERT INTO emp( NAME, age, dep_name, dep_location) VALUES('张一',21, '研发部', '广州');
INSERT INTO emp( NAME, age, dep_name, dep_location) VALUES('张二',22, '研发部', '广州');
INSERT INTO emp( NAME, age, dep_name, dep_location) VALUES('老王',23, '销售部', '深圳');
INSERT INTO emp( NAME, age, dep_name, dep_location) VALUES('老王',25, '销售部', '深圳');
INSERT INTO emp( NAME, age, dep_name, dep_location) VALUES('老王',24, '销售部', '深圳');

SELECT * FROM emp;
-- 数据有冗余
-- 将表拆分，在把工作地址/部门和员工信息关联



-- 解决方案：分成2张表
-- 创建部门表(id,dep_name,dep_location)
-- 一方，主表
CREATE TABLE department(
id INT PRIMARY KEY AUTO_INCREMENT,
dep_name VARCHAR(20),
dep_location VARCHAR(20)
)DEFAULT CHARACTER SET = utf8;

-- 创建员工表(id,name,age,dep_id)
-- 多方，从表
CREATE TABLE employee(
id INT PRIMARY KEY AUTO_INCREMENT,
NAME VARCHAR(20),
age INT,
dep_id INT -- 外键对应主表的主键
)DEFAULT CHARACTER SET = utf8;


-- 添加2个部门`department``employee`
INSERT INTO department VALUES(NULL, '研发部','广州'),(NULL, '销售部', '深圳');



DROP TABLE employee;
DROP TABLE department;

CREATE TABLE department(
	id INT PRIMARY KEY AUTO_INCREMENT,
	dep_name VARCHAR(20),
	dep_location VARCHAR(20)
)DEFAULT CHARACTER SET = utf8;

-- 创建员工表(id,name,age,dep_id)
-- 多方，从表
CREATE TABLE employee(
	id INT PRIMARY KEY AUTO_INCREMENT,
	NAME VARCHAR(20),
	age INT,
	dep_id INT ,-- 外键对应主表的主键
	CONSTRAINT dep_emp_fk FOREIGN KEY (dep_id) REFERENCES department(id)
)DEFAULT CHARACTER SET = utf8;


-- 添加2个部门`department``employee`
INSERT INTO department VALUES(NULL, '研发部','广州'),(NULL, '销售部', '深圳');

INSERT INTO employee (NAME, age, dep_id) VALUES ('张三', 20, 1);
INSERT INTO employee (NAME, age, dep_id) VALUES ('李四', 21, 1);
INSERT INTO employee (NAME, age, dep_id) VALUES ('王五', 20, 1);
INSERT INTO employee (NAME, age, dep_id) VALUES ('老王', 20, 2);
INSERT INTO employee (NAME, age, dep_id) VALUES ('大王', 22, 2);
INSERT INTO employee (NAME, age, dep_id) VALUES ('小王', 18, 2);

SELECT * FROM department;
SELECT * FROM employee;


-- 删除employee表的emp_depid_fk外键
ALTER TABLE employee DROP FOREIGN KEY dep_emp_fk;
-- 在employee表情存在的情况下添加外键
ALTER TABLE employee ADD CONSTRAINT dep_emp_fk
FOREIGN KEY (dep_id) REFERENCES department(id);

-- 在employee表情存在的情况下添加外键,设置级联更新
ALTER TABLE employee ADD CONSTRAINT dep_emp_fk
FOREIGN KEY (dep_id) REFERENCES department(id) ON UPDATE CASCADE;

-- 在employee表情存在的情况下添加外键,设置级联更新,设置级联删除
ALTER TABLE employee ADD CONSTRAINT dep_emp_fk
FOREIGN KEY (dep_id) REFERENCES department(id) ON UPDATE CASCADE ON DELETE CASCADE;

SHOW  CREATE DATABASE test;
ALTER DATABASE test CHARACTER SET utf8;
```

### MySQL的多表查询 ###

```sql
# 创建部门表
CREATE TABLE dept(
id INT PRIMARY KEY AUTO_INCREMENT,
NAME VARCHAR(20)
);
INSERT INTO dept (NAME) VALUES ('开发部'),('市场部'),('财务部');
# 创建员工表

CREATE TABLE emp (
id INT PRIMARY KEY AUTO_INCREMENT,
NAME VARCHAR(10),
gender CHAR(1), -- 性别
salary DOUBLE, -- 工资
join_date DATE, -- 入职日期
dept_id INT,
FOREIGN KEY (dept_id) REFERENCES dept(id) -- 外键，关联部门表(部门表的主键)
);
INSERT INTO emp(NAME,gender,salary,join_date,dept_id) VALUES('孙悟空','男
',7200,'2013-02-24',1);
INSERT INTO emp(NAME,gender,salary,join_date,dept_id) VALUES('猪八戒','男
',3600,'2010-12-02',2);
INSERT INTO emp(NAME,gender,salary,join_date,dept_id) VALUES('唐僧','男',9000,'2008-
08-08',2);
INSERT INTO emp(NAME,gender,salary,join_date,dept_id) VALUES('白骨精','女
',5000,'2015-10-07',3);
INSERT INTO emp(NAME,gender,salary,join_date,dept_id) VALUES('蜘蛛精','女
',4500,'2011-03-14',1);

SELECT * FROM emp,dept;
SELECT * FROM dept;


-- 内连接隐式
SELECT * FROM emp,dept WHERE emp.dept_id = dept.`id`;

SELECT emp.name,gender,dept.name FROM emp,dept WHERE emp.dept_id = dept.`id`;

SELECT 
	t1.`name`,t1.`gender`,t2.`name`
FROM
	emp t1,dept t2
WHERE   
	t1.`dept_id`=t2.`id`
-- 内连接显式
SELECT t1.`name`,t1.`gender`,t2.`name` FROM emp t1 INNER JOIN dept t2 ON t1.dept_id = t2.`id`;


-- 外连接 左外连接
SELECT t1.`name`,t1.`gender`,t2.`name` FROM emp t1 LEFT JOIN dept t2 ON t1.dept_id = t2.`id`;
-- 外连接 右外连接
SELECT t1.`name`,t1.`gender`,t2.`name` FROM dept t2 RIGHT JOIN emp t1 ON t1.dept_id = t2.`id`;


-- 子查询 查询中嵌套查询子查询

-- 单行单列
-- 查询最高薪资
SELECT MAX(salary) FROM emp;
SELECT * FROM emp WHERE emp.`salary`=9000;
SELECT * FROM emp WHERE emp.`salary` = (SELECT MAX(emp.`salary`) FROM emp);
-- 小于平均工资的员工
SELECT * FROM emp WHERE emp.`salary` < (SELECT AVG(emp.`salary`) FROM emp);

-- 多行单列
-- 查询'财务部'和'市场部'所有的员工信息
SELECT id FROM dept WHERE NAME = '财务部' OR NAME = '市场部';
SELECT * FROM emp WHERE dept_id = 3 OR dept_id = 2;
SELECT * FROM emp WHERE dept_id IN (3 ,2);
-- 子查询
SELECT * FROM emp WHERE dept_id IN (SELECT id FROM dept WHERE NAME = '财务部' OR NAME = '市场部');

-- 多行多列
SELECT * FROM dept t1 ,(SELECT * FROM emp WHERE emp.`join_date` > '2011-11-11') t2
WHERE t1.id = t2.dept_id;

```

```
1. 多表查询

2. 事务

3. DCL
```

### 多表查询： ###

```
* 查询语法：
	select
		列名列表
	from
		表名列表
	where....
* 准备sql
	# 创建部门表
	CREATE TABLE dept(
		id INT PRIMARY KEY AUTO_INCREMENT,
		NAME VARCHAR(20)
	);
	INSERT INTO dept (NAME) VALUES ('开发部'),('市场部'),('财务部');
	# 创建员工表
	CREATE TABLE emp (
		id INT PRIMARY KEY AUTO_INCREMENT,
		NAME VARCHAR(10),
		gender CHAR(1), -- 性别
		salary DOUBLE, -- 工资
		join_date DATE, -- 入职日期
		dept_id INT,
		FOREIGN KEY (dept_id) REFERENCES dept(id) -- 外键，关联部门表(部门表的主键)
	);
	INSERT INTO emp(NAME,gender,salary,join_date,dept_id) VALUES('孙悟空','男',7200,'2013-02-24',1);
	INSERT INTO emp(NAME,gender,salary,join_date,dept_id) VALUES('猪八戒','男',3600,'2010-12-02',2);
	INSERT INTO emp(NAME,gender,salary,join_date,dept_id) VALUES('唐僧','男',9000,'2008-08-08',2);
	INSERT INTO emp(NAME,gender,salary,join_date,dept_id) VALUES('白骨精','女',5000,'2015-10-07',3);
	INSERT INTO emp(NAME,gender,salary,join_date,dept_id) VALUES('蜘蛛精','女',4500,'2011-03-14',1);
* 笛卡尔积：
	* 有两个集合A,B .取这两个集合的所有组成情况。
	* 要完成多表查询，需要消除无用的数据
* 多表查询的分类：
	1. 内连接查询：
		1. 隐式内连接：使用where条件消除无用数据
			* 例子：
			-- 查询所有员工信息和对应的部门信息

			SELECT * FROM emp,dept WHERE emp.`dept_id` = dept.`id`;
			
			-- 查询员工表的名称，性别。部门表的名称
			SELECT emp.name,emp.gender,dept.name FROM emp,dept WHERE emp.`dept_id` = dept.`id`;
			
			SELECT 
				t1.name, -- 员工表的姓名
				t1.gender,-- 员工表的性别
				t2.name -- 部门表的名称
			FROM
				emp t1,
				dept t2
			WHERE 
				t1.`dept_id` = t2.`id`;
		2. 显式内连接：
			* 语法： select 字段列表 from 表名1 [inner] join 表名2 on 条件
			* 例如：
				* SELECT * FROM emp INNER JOIN dept ON emp.`dept_id` = dept.`id`;	
				* SELECT * FROM emp JOIN dept ON emp.`dept_id` = dept.`id`;	

		3. 内连接查询：
			1. 从哪些表中查询数据
			2. 条件是什么
			3. 查询哪些字段
```

​	

```
	2. 外链接查询：
		1. 左外连接：
			* 语法：select 字段列表 from 表1 left [outer] join 表2 on 条件；
			* 查询的是左表所有数据以及其交集部分。
			* 例子：
				-- 查询所有员工信息，如果员工有部门，则查询部门名称，没有部门，则不显示部门名称
				SELECT 	t1.*,t2.`name` FROM emp t1 LEFT JOIN dept t2 ON t1.`dept_id` = t2.`id`;
		2. 右外连接：
			* 语法：select 字段列表 from 表1 right [outer] join 表2 on 条件；
			* 查询的是右表所有数据以及其交集部分。
			* 例子：
				SELECT 	* FROM dept t2 RIGHT JOIN emp t1 ON t1.`dept_id` = t2.`id`;
```



```
	3. 子查询：
		* 概念：查询中嵌套查询，称嵌套查询为子查询。
			-- 查询工资最高的员工信息
			-- 1 查询最高的工资是多少 9000
			SELECT MAX(salary) FROM emp;
			
			-- 2 查询员工信息，并且工资等于9000的
			SELECT * FROM emp WHERE emp.`salary` = 9000;
			
			-- 一条sql就完成这个操作。子查询
			SELECT * FROM emp WHERE emp.`salary` = (SELECT MAX(salary) FROM emp);
	
		* 子查询不同情况
			1. 子查询的结果是单行单列的：
				* 子查询可以作为条件，使用运算符去判断。 运算符： > >= < <= =
				* 
				-- 查询员工工资小于平均工资的人
				SELECT * FROM emp WHERE emp.salary < (SELECT AVG(salary) FROM emp);
			2. 子查询的结果是多行单列的：
				* 子查询可以作为条件，使用运算符in来判断
				-- 查询'财务部'和'市场部'所有的员工信息
				SELECT id FROM dept WHERE NAME = '财务部' OR NAME = '市场部';
				SELECT * FROM emp WHERE dept_id = 3 OR dept_id = 2;
				-- 子查询
				SELECT * FROM emp WHERE dept_id IN (SELECT id FROM dept WHERE NAME = '财务部' OR NAME = '市场部');
	
			3. 子查询的结果是多行多列的：
				* 子查询可以作为一张虚拟表参与查询
				-- 查询员工入职日期是2011-11-11日之后的员工信息和部门信息
				-- 子查询
				SELECT * FROM dept t1 ,(SELECT * FROM emp WHERE emp.`join_date` > '2011-11-11') t2
				WHERE t1.id = t2.dept_id;
				
				-- 普通内连接
				SELECT * FROM emp t1,dept t2 WHERE t1.`dept_id` = t2.`id` AND t1.`join_date` >  '2011-11-11'
	
	
```

```
-- 部门表
CREATE TABLE dept (
  id INT PRIMARY KEY PRIMARY KEY, -- 部门id
  dname VARCHAR(50), -- 部门名称
  loc VARCHAR(50) -- 部门所在地
);

-- 添加4个部门
INSERT INTO dept(id,dname,loc) VALUES 
(10,'教研部','北京'),
(20,'学工部','上海'),
(30,'销售部','广州'),
(40,'财务部','深圳');



-- 职务表，职务名称，职务描述
CREATE TABLE job (
  id INT PRIMARY KEY,
  jname VARCHAR(20),
  description VARCHAR(50)
);

-- 添加4个职务
INSERT INTO job (id, jname, description) VALUES
(1, '董事长', '管理整个公司，接单'),
(2, '经理', '管理部门员工'),
(3, '销售员', '向客人推销产品'),
(4, '文员', '使用办公软件');



-- 员工表
CREATE TABLE emp (
  id INT PRIMARY KEY, -- 员工id
  ename VARCHAR(50), -- 员工姓名
  job_id INT, -- 职务id
  mgr INT , -- 上级领导
  joindate DATE, -- 入职日期
  salary DECIMAL(7,2), -- 工资
  bonus DECIMAL(7,2), -- 奖金
  dept_id INT, -- 所在部门编号
  CONSTRAINT emp_jobid_ref_job_id_fk FOREIGN KEY (job_id) REFERENCES job (id),
  CONSTRAINT emp_deptid_ref_dept_id_fk FOREIGN KEY (dept_id) REFERENCES dept (id)
);

-- 添加员工
INSERT INTO emp(id,ename,job_id,mgr,joindate,salary,bonus,dept_id) VALUES 
(1001,'孙悟空',4,1004,'2000-12-17','8000.00',NULL,20),
(1002,'卢俊义',3,1006,'2001-02-20','16000.00','3000.00',30),
(1003,'林冲',3,1006,'2001-02-22','12500.00','5000.00',30),
(1004,'唐僧',2,1009,'2001-04-02','29750.00',NULL,20),
(1005,'李逵',4,1006,'2001-09-28','12500.00','14000.00',30),
(1006,'宋江',2,1009,'2001-05-01','28500.00',NULL,30),
(1007,'刘备',2,1009,'2001-09-01','24500.00',NULL,10),
(1008,'猪八戒',4,1004,'2007-04-19','30000.00',NULL,20),
(1009,'罗贯中',1,NULL,'2001-11-17','50000.00',NULL,10),
(1010,'吴用',3,1006,'2001-09-08','15000.00','0.00',30),
(1011,'沙僧',4,1004,'2007-05-23','11000.00',NULL,20),
(1012,'李逵',4,1006,'2001-12-03','9500.00',NULL,30),
(1013,'小白龙',4,1004,'2001-12-03','30000.00',NULL,20),
(1014,'关羽',4,1007,'2002-01-23','13000.00',NULL,10);



-- 工资等级表
CREATE TABLE salarygrade (
  grade INT PRIMARY KEY,   -- 级别
  losalary INT,  -- 最低工资
  hisalary INT -- 最高工资
);

-- 添加5个工资等级
INSERT INTO salarygrade(grade,losalary,hisalary) VALUES 
(1,7000,12000),
(2,12010,14000),
(3,14010,20000),
(4,20010,30000),
(5,30010,99990);

-- 需求：

-- 1.查询所有员工信息。查询员工编号，员工姓名，工资，职务名称，职务描述

-- 2.查询员工编号，员工姓名，工资，职务名称，职务描述，部门名称，部门位置
   
-- 3.查询员工姓名，工资，工资等级

-- 4.查询员工姓名，工资，职务名称，职务描述，部门名称，部门位置，工资等级

-- 5.查询出部门编号、部门名称、部门位置、部门人数
 
-- 6.查询所有员工的姓名及其直接上级的姓名,没有领导的员工也需要查询

```

#### 1.查询所有员工信息。查询员工编号，员工姓名，工资，职务名称，职务描述											 ####

```
-- 需求：

-- 1.查询所有员工信息。查询员工编号，员工姓名，工资，职务名称，职务描述
/*
	分析：
		1.员工编号，员工姓名，工资，需要查询emp表  职务名称，职务描述 需要查询job表
		2.查询条件 emp.job_id = job.id
*/
SELECT 
	t1.`id`, -- 员工编号
	t1.`ename`, -- 员工姓名
	t1.`salary`,-- 工资
	t2.`jname`, -- 职务名称
	t2.`description` -- 职务描述
FROM 
	emp t1, job t2
WHERE 
	t1.`job_id` = t2.`id`;
```

#### 2.查询员工编号，员工姓名，工资，职务名称，职务描述，部门名称，部门位置	 ####

3.查询员工姓名，工资，工资等级						

```
-- 2.查询员工编号，员工姓名，工资，职务名称，职务描述，部门名称，部门位置
/*
	分析：
		1. 员工编号，员工姓名，工资 emp  职务名称，职务描述 job  部门名称，部门位置 dept
		2. 条件： emp.job_id = job.id and emp.dept_id = dept.id
*/

SELECT 
	t1.`id`, -- 员工编号
	t1.`ename`, -- 员工姓名
	t1.`salary`,-- 工资
	t2.`jname`, -- 职务名称
	t2.`description`, -- 职务描述
	t3.`dname`, -- 部门名称
	t3.`loc` -- 部门位置
FROM 
	emp t1, job t2,dept t3
WHERE 
	t1.`job_id` = t2.`id` AND t1.`dept_id` = t3.`id`;
   
-- 3.查询员工姓名，工资，工资等级
/*
	分析：
		1.员工姓名，工资 emp  工资等级 salarygrade
		2.条件 emp.salary >= salarygrade.losalary and emp.salary <= salarygrade.hisalary
			emp.salary BETWEEN salarygrade.losalary and salarygrade.hisalary
*/
SELECT 
	t1.ename ,
	t1.`salary`,
	t2.*
FROM emp t1, salarygrade t2
WHERE t1.`salary` BETWEEN t2.`losalary` AND t2.`hisalary`;
```

#### 4.查询员工姓名，工资，职务名称，职务描述，部门名称，部门位置，工资等级				 ####

```
-- 4.查询员工姓名，工资，职务名称，职务描述，部门名称，部门位置，工资等级
/*
	分析：
		1. 员工姓名，工资 emp ， 职务名称，职务描述 job 部门名称，部门位置，dept  工资等级 salarygrade
		2. 条件： emp.job_id = job.id and emp.dept_id = dept.id and emp.salary BETWEEN salarygrade.losalary and salarygrade.hisalary
			
*/
SELECT 
	t1.`ename`,
	t1.`salary`,
	t2.`jname`,
	t2.`description`,
	t3.`dname`,
	t3.`loc`,
	t4.`grade`
FROM 
	emp t1,job t2,dept t3,salarygrade t4
WHERE 
	t1.`job_id` = t2.`id` 
	AND t1.`dept_id` = t3.`id`
	AND t1.`salary` BETWEEN t4.`losalary` AND t4.`hisalary`;
```

#### 5.查询出部门编号、部门名称、部门位置、部门人数		 ####

```
-- 5.查询出部门编号、部门名称、部门位置、部门人数

/*
	分析：
		1.部门编号、部门名称、部门位置 dept 表。 部门人数 emp表
		2.使用分组查询。按照emp.dept_id完成分组，查询count(id)
		3.使用子查询将第2步的查询结果和dept表进行关联查询
		
*/
SELECT 
	t1.`id`,t1.`dname`,t1.`loc` , t2.total
FROM 
	dept t1,
	(SELECT
		dept_id,COUNT(id) total
	FROM 
		emp
	GROUP BY dept_id) t2
WHERE t1.`id` = t2.dept_id;
```

#### 6.查询所有员工的姓名及其直接上级的姓名,没有领导的员工也需要查询 ####

```
-- 6.查询所有员工的姓名及其直接上级的姓名,没有领导的员工也需要查询

/*
	分析：
		1.姓名 emp， 直接上级的姓名 emp
			* emp表的id 和 mgr 是自关联
		2.条件 emp.id = emp.mgr
		3.查询左表的所有数据，和 交集数据
			* 使用左外连接查询
	
*/
/*
select
	t1.ename,
	t1.mgr,
	t2.`id`,
	t2.ename
from emp t1, emp t2
where t1.mgr = t2.`id`;

*/

SELECT 
	t1.ename,
	t1.mgr,
	t2.`id`,
	t2.`ename`
FROM emp t1
LEFT JOIN emp t2
ON t1.`mgr` = t2.`id`;
```

### 事务 ###

```
1. 事务的基本介绍
	1. 概念：
		*  如果一个包含多个步骤的业务操作，被事务管理，那么这些操作要么同时成功，要么同时失败。
		
	2. 操作：
		1. 开启事务： start transaction;
		2. 回滚：rollback;
		3. 提交：commit;
	3. 例子：
		CREATE TABLE account (
			id INT PRIMARY KEY AUTO_INCREMENT,
			NAME VARCHAR(10),
			balance DOUBLE
		);
		-- 添加数据
		INSERT INTO account (NAME, balance) VALUES ('zhangsan', 1000), ('lisi', 1000);
```

​			

```
		SELECT * FROM account;
		UPDATE account SET balance = 1000;
		-- 张三给李四转账 500 元
		
		-- 0. 开启事务
		START TRANSACTION;
		-- 1. 张三账户 -500
		
		UPDATE account SET balance = balance - 500 WHERE NAME = 'zhangsan';
		-- 2. 李四账户 +500
		-- 出错了...
		UPDATE account SET balance = balance + 500 WHERE NAME = 'lisi';
		
		-- 发现执行没有问题，提交事务
		COMMIT;
		
		-- 发现出问题了，回滚事务
		ROLLBACK;
	4. MySQL数据库中事务默认自动提交
		
		* 事务提交的两种方式：
			* 自动提交：
				* mysql就是自动提交的
				* 一条DML(增删改)语句会自动提交一次事务。
			* 手动提交：
				* Oracle 数据库默认是手动提交事务
				* 需要先开启事务，再提交
		* 修改事务的默认提交方式：
			* 查看事务的默认提交方式：SELECT @@autocommit; -- 1 代表自动提交  0 代表手动提交
			* 修改默认提交方式： set @@autocommit = 0;
```

```
2. 事务的四大特征：
	1. 原子性：是不可分割的最小操作单位，要么同时成功，要么同时失败。
	2. 持久性：当事务提交或回滚后，数据库会持久化的保存数据。
	3. 隔离性：多个事务之间。相互独立。
	4. 一致性：事务操作前后，数据总量不变
3. 事务的隔离级别（了解）
	* 概念：多个事务之间隔离的，相互独立的。但是如果多个事务操作同一批数据，则会引发一些问题，设置不同的隔离级别就可以解决这些问题。
	* 存在问题：
		1. 脏读：一个事务，读取到另一个事务中没有提交的数据
		2. 不可重复读(虚读)：在同一个事务中，两次读取到的数据不一样。
		3. 幻读：一个事务操作(DML)数据表中所有记录，另一个事务添加了一条数据，则第一个事务查询不到自己的修改。
	* 隔离级别：
		1. read uncommitted：读未提交
			* 产生的问题：脏读、不可重复读、幻读
		2. read committed：读已提交 （Oracle）
			* 产生的问题：不可重复读、幻读
		3. repeatable read：可重复读 （MySQL默认）
			* 产生的问题：幻读
		4. serializable：串行化
			* 可以解决所有的问题

		* 注意：隔离级别从小到大安全性越来越高，但是效率越来越低
		* 数据库查询隔离级别：
			* select @@tx_isolation;
		* 数据库设置隔离级别：
			* set global transaction isolation level  级别字符串;

	* 演示：
		set global transaction isolation level read uncommitted;
		start transaction;
		-- 转账操作
		update account set balance = balance - 500 where id = 1;
		update account set balance = balance + 500 where id = 2;
```

### DCL： ###

```
* SQL分类：
	1. DDL：操作数据库和表
	2. DML：增删改表中数据
	3. DQL：查询表中数据
	4. DCL：管理用户，授权

* DBA：数据库管理员

* DCL：管理用户，授权
	1. 管理用户
		1. 添加用户：
			* 语法：CREATE USER '用户名'@'主机名' IDENTIFIED BY '密码';
		2. 删除用户：
			* 语法：DROP USER '用户名'@'主机名';
		3. 修改用户密码：
			
			UPDATE USER SET PASSWORD = PASSWORD('新密码') WHERE USER = '用户名';
			UPDATE USER SET PASSWORD = PASSWORD('abc') WHERE USER = 'lisi';
			
			SET PASSWORD FOR '用户名'@'主机名' = PASSWORD('新密码');
			SET PASSWORD FOR 'root'@'localhost' = PASSWORD('123');

			* mysql中忘记了root用户的密码？
				1. cmd -- > net stop mysql 停止mysql服务
					* 需要管理员运行该cmd

				2. 使用无验证方式启动mysql服务： mysqld --skip-grant-tables
				3. 打开新的cmd窗口,直接输入mysql命令，敲回车。就可以登录成功
				4. use mysql;
				5. update user set password = password('你的新密码') where user = 'root';
				6. 关闭两个窗口
				7. 打开任务管理器，手动结束mysqld.exe 的进程
				8. 启动mysql服务
				9. 使用新密码登录。
		4. 查询用户：
			-- 1. 切换到mysql数据库
			USE myql;
			-- 2. 查询user表
			SELECT * FROM USER;
			
			* 通配符： % 表示可以在任意主机使用用户登录数据库

	2. 权限管理：
		1. 查询权限：
			-- 查询权限
			SHOW GRANTS FOR '用户名'@'主机名';
			SHOW GRANTS FOR 'lisi'@'%';

		2. 授予权限：
			-- 授予权限
			grant 权限列表 on 数据库名.表名 to '用户名'@'主机名';
			-- 给张三用户授予所有权限，在任意数据库任意表上
			
			GRANT ALL ON *.* TO 'zhangsan'@'localhost';
		3. 撤销权限：
			-- 撤销权限：
			revoke 权限列表 on 数据库名.表名 from '用户名'@'主机名';
			REVOKE UPDATE ON db3.`account` FROM 'lisi'@'%';
```

# day4 【JDBC】 #

###  JDBC快速入门 ###

```java
package cn.itcast.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

/**
 * JDBC快速入门
 */
public class JdbcDemo1 {
    public static void main(String[] args) throws Exception {

        //1. 导入驱动jar包
        //2.注册驱动 告诉程序用的是那个版本(mysal/oracel/)的实现类 把对应的类加载到内存
        //告诉程序该使用哪一个数据库驱动jar
        Class.forName("com.mysql.jdbc.Driver");
        //3.获取数据库连接对象
        Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/db3", "root", "");
        //Connection conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "");
        //4.定义sql语句
        String sql = "update account set balance = -20000 where id = 2";
        //String sql = "update account set balance = 2000";
        //5.获取执行sql的对象 Statement
        Statement stmt = conn.createStatement();
        //6.执行sql
        int count = stmt.executeUpdate(sql);
        //7.处理结果
        System.out.println(count);
        //8.释放资源
        stmt.close();
        conn.close();
    }
}
```

### 添加一条记录 insert 语句（标准格式） ###

```java
package cn.itcast.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * account表 添加一条记录 insert 语句
 */
public class JDBCDemo2 {
    public static void main(String[] args) {
        Statement stmt = null;//finally 找不到作用域
        Connection conn = null;
        try {
            //1. 注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2. 定义sql
            String sql = "insert into account values(null,'王五',3000)";
            //3.获取Connection对象
            conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "");
            //4.获取执行sql的对象 Statement
            stmt = conn.createStatement();
            //5.执行sql
            int count = stmt.executeUpdate(sql);//影响的行数
            //6.处理结果
            System.out.println(count);
            if(count > 0){
                System.out.println("添加成功！");
            }else{
                System.out.println("添加失败！");
            }

        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            //stmt.close();
            //7. 释放资源
            //避免空指针异常
            if(stmt != null){
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }

            if(conn != null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

### 修改记录 update语句 ###

```java
package cn.itcast.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * account表 修改记录
 */
public class JDBCDemo3 {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try {
            //1. 注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取连接对象
            conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "");
            //3.定义sql
            String sql  = "update account set balance = 1500 where id = 3";
            //4.获取执行sql对象
            stmt = conn.createStatement();
            //5.执行sql
            int count = stmt.executeUpdate(sql);
            //6.处理结果
            System.out.println(count);
            if(count > 0){
                System.out.println("修改成功！");
            }else{
                System.out.println("修改失败");
            }

        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            //7.释放资源

            if(stmt != null){
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }

            if(conn != null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

### 删除一条记录 delete语句 ###

```java
package cn.itcast.jdbc;


import cn.itcast.util.JDBCUtils;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * account表 删除一条记录
 */
public class JDBCDemo4 {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try {
            //1. 注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取连接对象
            conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "root");
           //conn = JDBCUtils.getConnection("jdbc:mysql:///db3", "root", "root");
            //3.定义sql
            String sql  = "delete from account where id = 3";
            //4.获取执行sql对象
            stmt = conn.createStatement();
            //5.执行sql
            int count = stmt.executeUpdate(sql);
            //6.处理结果
            System.out.println(count);
            if(count > 0){
                System.out.println("删除成功！");
            }else{
                System.out.println("删除失败");
            }

        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            //7.释放资源

            if(stmt != null){
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }

            if(conn != null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

### 执行DDL语句 ###

```java
package cn.itcast.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * 执行DDL语句
 */
public class JDBCDemo5 {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try {
            //1. 注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取连接对象
            conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "root");
            //3.定义sql
            String sql  = "create table student (id int , name varchar(20))";
            //4.获取执行sql对象
            stmt = conn.createStatement();
            //5.执行sql
            int count = stmt.executeUpdate(sql);
            //6.处理结果
            System.out.println(count);

        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            //7.释放资源

            if(stmt != null){
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }

            if(conn != null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

### 获取数据 resultset.next() ###

```java
package cn.itcast.jdbc;

import java.sql.*;

/**
 * 执行DDL语句
 */
public class JDBCDemo7 {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            //1. 注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取连接对象
            conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "");
            //3.定义sql
            String sql  = "select * from account";
            //4.获取执行sql对象
            stmt = conn.createStatement();
            //5.执行sql
            rs = stmt.executeQuery(sql);
            //6.处理结果
            //循环判断游标是否是最后一行末尾。
            while(rs.next()){

                //获取数据
                //6.2 获取数据
                int id = rs.getInt(1);
                String name = rs.getString("name");
                double balance = rs.getDouble(3);

                System.out.println(id + "---" + name + "---" + balance);
            }
           /* 
           //6.1 让游标向下移动一行
            if(rs.next()){
                //判断是否有数据
                //6.2 获取数据
                int id = rs.getInt(1);
                String name = rs.getString("name");
                double balance = rs.getDouble(3);

                System.out.println(id + "---" + name + "---" + balance);
            }*/

          /*  //6.1 让游标向下移动一行
            rs.next();
            //6.2 获取数据
            int id2 = rs.getInt(1);
            String name2 = rs.getString("name");
            double balance2 = rs.getDouble(3);

            System.out.println(id2 + "---" + name2 + "---" + balance2);

            //6.1 让游标向下移动一行
            rs.next();
            //6.2 获取数据
            int id3 = rs.getInt(1);
            String name3 = rs.getString("name");
            double balance3 = rs.getDouble(3);

            System.out.println(id3 + "---" + name3 + "---" + balance3);*/


        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            //7.释放资源

            if(rs != null){
                try {
                    rs.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }

            if(stmt != null){
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }

            if(conn != null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

### 简化代码抽取JDBC工具类，动态加载配置文件中的数据库信息 ###

```java
package cn.itcast.jdbc;

import cn.itcast.domain.Emp;
import cn.itcast.util.JDBCUtils;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 * * 定义一个方法，查询emp表的数据将其封装为对象，然后装载集合，返回。
 */
public class JDBCDemo8 {

    public static void main(String[] args) {
        List<Emp> list = new JDBCDemo8().findAll();  //非静态方法怎么调用，new JDBCDemo8()
        System.out.println(list);
        System.out.println(list.size());
    }
    /**
     * 查询所有emp对象
     * @return
     */
    public List<Emp> findAll(){
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        List<Emp> list = null;
        try {
            //1.注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取连接
            conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "");
            //3.定义sql
            String sql = "select * from emp";
            //4.获取执行sql的对象
            stmt = conn.createStatement();
            //5.执行sql
            rs = stmt.executeQuery(sql);
            //6.遍历结果集，封装对象，装载集合
            Emp emp = null;
            list = new ArrayList<Emp>();
            while(rs.next()){
                //获取数据
                int id = rs.getInt("id");
                String ename = rs.getString("ename");
                int job_id = rs.getInt("job_id");
                int mgr = rs.getInt("mgr");
                Date joindate = rs.getDate("joindate");
                double salary = rs.getDouble("salary");
                double bonus = rs.getDouble("bonus");
                int dept_id = rs.getInt("dept_id");
                // 创建emp对象,并赋值
                emp = new Emp();
                emp.setId(id);
                emp.setEname(ename);
                emp.setJob_id(job_id);
                emp.setMgr(mgr);
                emp.setJoindate(joindate);
                emp.setSalary(salary);
                emp.setBonus(bonus);
                emp.setDept_id(dept_id);

                //装载集合
                list.add(emp);
            }

        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            if(rs != null){
                try {
                    rs.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }

            if(stmt != null){
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }

            if(conn != null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
        return list;
    }


    /**
     * 演示JDBC工具类
     * @return
     */
    public List<Emp> findAll2(){
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        List<Emp> list = null;
        try {
           /* //1.注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取连接
            conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "root");*/
            conn = JDBCUtils.getConnection();
            //3.定义sql
            String sql = "select * from emp";
            //4.获取执行sql的对象
            stmt = conn.createStatement();
            //5.执行sql
            rs = stmt.executeQuery(sql);
            //6.遍历结果集，封装对象，装载集合
            Emp emp = null;
            list = new ArrayList<Emp>();
            while(rs.next()){
                //获取数据
                int id = rs.getInt("id");
                String ename = rs.getString("ename");
                int job_id = rs.getInt("job_id");
                int mgr = rs.getInt("mgr");
                Date joindate = rs.getDate("joindate");
                double salary = rs.getDouble("salary");
                double bonus = rs.getDouble("bonus");
                int dept_id = rs.getInt("dept_id");
                // 创建emp对象,并赋值
                emp = new Emp();
                emp.setId(id);
                emp.setEname(ename);
                emp.setJob_id(job_id);
                emp.setMgr(mgr);
                emp.setJoindate(joindate);
                emp.setSalary(salary);
                emp.setBonus(bonus);
                emp.setDept_id(dept_id);

                //装载集合
                list.add(emp);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            /*if(rs != null){
                try {
                    rs.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }

            if(stmt != null){
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }

            if(conn != null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }*/

            JDBCUtils.close(rs,stmt,conn);
        }
        return list;
    }

}
```

### JDBC工具类 ###

```java
package cn.itcast.util;

import java.io.FileReader;
import java.io.IOException;
import java.net.URL;
import java.sql.*;
import java.util.Properties;

/**
 * JDBC工具类
 */
public class JDBCUtils {
    private static String url;
    private static String user;
    private static String password;
    private static String driver;
    /**
     * 文件的读取，只需要读取一次即可拿到这些值。使用静态代码块
     */
    static{
        //读取资源文件，获取值。

        try {
            //1. 创建Properties集合类。
            Properties pro = new Properties();

            // 动态 获取src路径下的文件的方式--->ClassLoader 类加载器
            ClassLoader classLoader = JDBCUtils.class.getClassLoader();
            URL res  = classLoader.getResource("jdbc.properties");
            String path = res.getPath();
           // System.out.println(path);///D:/IdeaProjects/itcast/out/production/day04_jdbc/jdbc.properties
            //2. 加载文件
           // pro.load(new FileReader("D:\\IdeaProjects\\itcast\\day04_jdbc\\src\\jdbc.properties"));
            pro.load(new FileReader(path));

            //3. 获取数据，赋值
            url = pro.getProperty("url");
            user = pro.getProperty("user");
            password = pro.getProperty("password");
            driver = pro.getProperty("driver");
            //4. 注册驱动
            Class.forName(driver);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }


    /**
     * 获取连接
     * @return 连接对象
     */
    public static Connection getConnection() throws SQLException {

        return DriverManager.getConnection(url, user, password);
    }

    /**
     * 释放资源
     * @param stmt
     * @param conn
     */
    public static void close(Statement stmt,Connection conn){
        if( stmt != null){
            try {
                stmt.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }

        if( conn != null){
            try {
                conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }


    /**
     * 释放资源
     * @param stmt
     * @param conn
     */
    public static void close(ResultSet rs,Statement stmt, Connection conn){
        if( rs != null){
            try {
                rs.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }

        if( stmt != null){
            try {
                stmt.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }

        if( conn != null){
            try {
                conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
/**
url=jdbc:mysql:///db3
user=root
password=root
driver=com.mysql.jdbc.Driver
```

### 登录案例 ###

```sql
CREATE TABLE USER(
	id INT PRIMARY KEY AUTO_INCREMENT,
	username VARCHAR(32),
	PASSWORD VARCHAR(32)
);
INSERT INTO USER VALUES(NULL,'zhangsan','123');
INSERT INTO USER VALUES(NULL,'lisi','234');

SELECT * FROM USER;
```

### 模拟登录 通过键盘录入用户名和密码 判断用户是否登录成功 ###

```java
package cn.itcast.jdbc;

import cn.itcast.util.JDBCUtils;

import java.sql.*;
import java.util.Scanner;

/**
 * 练习：
 *        * 需求：
 *           1. 通过键盘录入用户名和密码
 *           2. 判断用户是否登录成功
 */
public class JDBCDemo9 {

    public static void main(String[] args) {
        //1.键盘录入，接受用户名和密码
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入用户名：");
        String username = sc.nextLine();
        System.out.println("请输入密码：");
        String password = sc.nextLine();
        //2.调用方法
        boolean flag = new JDBCDemo9().login(username, password);
        //3.判断结果，输出不同语句
        if(flag){
            //登录成功
            System.out.println("登录成功！");
        }else{
            System.out.println("用户名或密码错误！");
        }
    }
    /**
     * 登录方法
     */
    public boolean login(String username ,String password){
        if(username == null || password == null){
            return false;
        }
        //连接数据库判断是否登录成功
        Connection conn = null;
        Statement stmt =  null;
        ResultSet rs = null;
        //1.获取连接
        try {
            conn =  JDBCUtils.getConnection();
            //2.定义sql
            String sql = "select * from user where username = '"+username+"' and password = '"+password+"' ";
            System.out.println(sql);
            //3.获取执行sql的对象
            stmt = conn.createStatement();
            //4.执行查询
            rs = stmt.executeQuery(sql);
            //5.判断
           /* if(rs.next()){//如果有下一行，则返回true
                return true;
            }else{
                return false;
            }*/
           return rs.next();//如果有下一行，则返回true

        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            JDBCUtils.close(rs,stmt,conn);
        }
        return false;
    }
}
```

### 登录方法,使用PreparedStatement实现 解决sql的注入问题，提高安全性  ###

 SELECT * FROM USER WHERE username = 'kjksdlaf' AND PASSWORD = '**a' OR 'a' = 'a**' 

```java
/**
 * 登录方法,使用PreparedStatement实现
 */
public boolean login2(String username ,String password){
    if(username == null || password == null){
        return false;
    }
    //连接数据库判断是否登录成功
    Connection conn = null;
    PreparedStatement pstmt =  null;
    ResultSet rs = null;
    //1.获取连接
    try {
        conn =  JDBCUtils.getConnection();
        //2.定义sql
        String sql = "select * from user where username = ? and password = ?";
        //3.获取执行sql的对象
        pstmt = conn.prepareStatement(sql);
        //给?赋值
        pstmt.setString(1,username);
        pstmt.setString(2,password);
        //4.执行查询,不需要传递sql
        rs = pstmt.executeQuery();
        //5.判断
       /* if(rs.next()){//如果有下一行，则返回true
            return true;
        }else{
            return false;
        }*/
        return rs.next();//如果有下一行，则返回true

    } catch (SQLException e) {
        e.printStackTrace();
    }finally {
        JDBCUtils.close(rs,pstmt,conn);
    }
    return false;
}
```
### JDBC控制事务 ###

```java
package cn.itcast.jdbc;

import cn.itcast.util.JDBCUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

/**
 * 事务操作
 */
public class JDBCDemo10 {
    public static void main(String[] args) {
        Connection conn = null;
        PreparedStatement pstmt1 = null;
        PreparedStatement pstmt2 = null;
        try {
            //1.获取连接
            conn = JDBCUtils.getConnection();
            //开启事务
            conn.setAutoCommit(false);
            //2.定义sql
            //2.1 张三 - 500
            String sql1 = "update account set balance = balance - ? where id = ?";
            //2.2 李四 + 500
            String sql2 = "update account set balance = balance + ? where id = ?";
            //3.获取执行sql对象
            pstmt1 = conn.prepareStatement(sql1);
            pstmt2 = conn.prepareStatement(sql2);
            //4. 设置参数
            pstmt1.setDouble(1,500);
            pstmt1.setInt(2,1);

            pstmt2.setDouble(1,500);
            pstmt2.setInt(2,2);
            //5.执行sql
            pstmt1.executeUpdate();
            // 手动制造异常
            int i = 3/0;
            pstmt2.executeUpdate();
            //提交事务
            conn.commit();
        } catch (Exception e) {
            //事务回滚
            try {
                if(conn != null) {
                    conn.rollback();
                }
            } catch (SQLException e1) {
                e1.printStackTrace();
            }
            e.printStackTrace();
        }finally {
            JDBCUtils.close(pstmt1,conn);
            JDBCUtils.close(pstmt2,null);
        }
    }
}
```

# day05 【JDBC连接池 & JDBCTemplate】 #

## 数据库连接池 ##

### c3p0的演示 ###

```java
package cn.itcast.datasource.c3p0;

import com.mchange.v2.c3p0.ComboPooledDataSource;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.SQLException;

/**
 * c3p0的演示
 */
public class C3P0Demo1 {
    public static void main(String[] args) throws SQLException {
        //1.创建数据库连接池对象
        DataSource ds  = new ComboPooledDataSource();
        //2. 获取连接对象
        Connection conn = ds.getConnection();

        //3. 打印
        System.out.println(conn);
    }
}
```

```xml
<c3p0-config>
  <!-- 使用默认的配置读取连接池对象 -->
  <default-config>
   <!--  连接参数 -->
    <property name="driverClass">com.mysql.jdbc.Driver</property>
    <property name="jdbcUrl">jdbc:mysql://localhost:3306/db4</property>
    <property name="user">root</property>
    <property name="password"></property>
    
    <!-- 连接池参数 -->
    <!--初始化申请的连接数量-->
    <property name="initialPoolSize">5</property>
    <!--最大的连接数量-->
    <property name="maxPoolSize">10</property>
    <!--超时时间-->
    <property name="checkoutTimeout">3000</property>
  </default-config>

  <named-config name="otherc3p0"> 
    <!--  连接参数 -->
    <property name="driverClass">com.mysql.jdbc.Driver</property>
    <property name="jdbcUrl">jdbc:mysql://localhost:3306/db3</property>
    <property name="user">root</property>
    <property name="password"></property>
    
    <!-- 连接池参数 -->
    <property name="initialPoolSize">5</property>
    <property name="maxPoolSize">8</property>
    <property name="checkoutTimeout">1000</property>
  </named-config>
</c3p0-config>
```

```java
package cn.itcast.datasource.c3p0;

import com.mchange.v2.c3p0.ComboPooledDataSource;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.SQLException;

/**
 * c3p0演示 最大连接池演示
 */
public class C3P0Demo2 {

    public static void main(String[] args) throws SQLException {
       /* //1. 获取DataSource，使用默认配置
        DataSource ds  = new ComboPooledDataSource();

        //2.获取连接

        for (int i = 1; i <= 11 ; i++) {
            Connection conn = ds.getConnection();
            System.out.println(i+":"+conn);

            if(i == 5){
                conn.close();//归还连接到连接池中
            }
        }*/

        testNamedConfig();

    }
    public static void testNamedConfig() throws SQLException {
        // 1.1 获取DataSource，使用指定名称配置
        DataSource ds  = new ComboPooledDataSource("otherc3p0");
        //2.获取连接
        for (int i = 1; i <= 10 ; i++) {
            Connection conn = ds.getConnection();
            System.out.println(i+":"+conn);
        }
    }
}
```

### Druid演示 ###

```java
package cn.itcast.datasource.druid;

import com.alibaba.druid.pool.DruidDataSourceFactory;

import javax.sql.DataSource;
import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.util.Properties;

/**
 * Druid演示
 */
public class DruidDemo {
    public static void main(String[] args) throws Exception {
        //1.导入jar包
        //2.定义配置文件
        //3.加载配置文件
        Properties pro = new Properties();
        InputStream is = DruidDemo.class.getClassLoader().getResourceAsStream("druid.properties");
        pro.load(is);
        //4.获取连接池对象
        DataSource ds = DruidDataSourceFactory.createDataSource(pro);
        //5.获取连接
        Connection conn = ds.getConnection();
        System.out.println(conn);

    }
}
```

```java
driverClassName=com.mysql.jdbc.Driver
url=jdbc:mysql:///db3
username=root
password=
# 初始化连接数量
initialSize=5
# 最大连接数
maxActive=10
# 最大等待时间
maxWait=3000
```

### Druid 使用新的工具类 ###

```java
package cn.itcast.datasource.druid;

import cn.itcast.utils.JDBCUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 * 使用新的工具类
 */
public class DruidDemo2 {

    public static void main(String[] args) {
        /*
         * 完成添加操作：给account表添加一条记录
         */
        Connection conn = null;
        PreparedStatement pstmt = null;
        try {
            //1.获取连接
            conn = JDBCUtils.getConnection();
            //2.定义sql
            String sql = "insert into account values(null,?,?)";
            //3.获取pstmt对象
            pstmt = conn.prepareStatement(sql);
            //4.给？赋值
            pstmt.setString(1,"王五");
            pstmt.setDouble(2,3000);
            //5.执行sql
            int count = pstmt.executeUpdate();
            System.out.println(count);
        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            //6. 释放资源
            JDBCUtils.close(pstmt,conn);
        }
    }
}
```

### Druid连接池的工具类 ###

```java
package cn.itcast.utils;

import com.alibaba.druid.pool.DruidDataSourceFactory;

import javax.sql.DataSource;
import java.io.IOException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Properties;

/**
 * Druid连接池的工具类
 */
public class JDBCUtils {

    //1.定义成员变量 DataSource
    private static DataSource ds ;

    static{
        try {
            //1.加载配置文件
            Properties pro = new Properties();
            pro.load(JDBCUtils.class.getClassLoader().getResourceAsStream("druid.properties"));
            //2.获取DataSource
            ds = DruidDataSourceFactory.createDataSource(pro);
        } catch (IOException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * 获取连接
     */
    public static Connection getConnection() throws SQLException {
        return ds.getConnection();
    }

    /**
     * 释放资源
     */
    public static void close(Statement stmt,Connection conn){
       /* if(stmt != null){
            try {
                stmt.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }

        if(conn != null){
            try {
                conn.close();//归还连接
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }*/

       close(null,stmt,conn);
    }


    public static void close(ResultSet rs , Statement stmt, Connection conn){


        if(rs != null){
            try {
                rs.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }


        if(stmt != null){
            try {
                stmt.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }

        if(conn != null){
            try {
                conn.close();//归还连接
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * 获取连接池方法
     */

    public static DataSource getDataSource(){
        return  ds;
    }
}
```

## Spring JDBC ##

### JdbcTemplate入门 ###

```java
package cn.itcast.jdbctemplate;
import cn.itcast.utils.JDBCUtils;
import org.springframework.jdbc.core.JdbcTemplate;

/**
 * JdbcTemplate入门
 */
public class JdbcTemplateDemo1 {

    public static void main(String[] args) {
        //1.导入jar包
        //2.创建JDBCTemplate对象
        JdbcTemplate template = new JdbcTemplate(JDBCUtils.getDataSource());
        //3.调用方法
        String sql = "update account set balance = 5000 where id = ?";
        int count = template.update(sql, 3);
        System.out.println(count);
    }
}
```

### JdbcTemplate对数据库进行操作 ###

```java
package cn.itcast.jdbctemplate;

import cn.itcast.domain.Emp;
import cn.itcast.utils.JDBCUtils;
import org.junit.Test;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;

import java.sql.Date;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;
		  /*1. 修改1号数据的 salary 为 10000
			2. 添加一条记录
			3. 删除刚才添加的记录
			4. 查询id为1的记录，将其封装为Map集合
			5. 查询所有记录，将其封装为List
			6. 查询所有记录，将其封装为Emp对象的List集合
			7. 查询总记录数*/
public class JdbcTemplateDemo2 {

    //Junit单元测试，可以让方法独立执行


    //1. 获取JDBCTemplate对象
    private JdbcTemplate template = new JdbcTemplate(JDBCUtils.getDataSource());
    /**
     * 1. 修改1号数据的 salary 为 10000
     */
    @Test
    public void test1(){

        //2. 定义sql
        String sql = "update emp set salary = 10000 where id = 1001";
        //3. 执行sql
        int count = template.update(sql);
        System.out.println(count);
    }

    /**
     * 2. 添加一条记录
     */
    @Test
    public void test2(){
        String sql = "insert into emp(id,ename,dept_id) values(?,?,?)";
        int count = template.update(sql, 1015, "郭靖", 10);
        System.out.println(count);

    }

    /**
     * 3.删除刚才添加的记录
     */
    @Test
    public void test3(){
        String sql = "delete from emp where id = ?";
        int count = template.update(sql, 1015);
        System.out.println(count);
    }

    /**
     * 4.查询id为1001的记录，将其封装为Map集合
     * 注意：这个方法查询的结果集长度只能是1 0不行2也不行
     */
    @Test
    public void test4(){
        String sql = "select * from emp where id = ? or id = ?";
        Map<String, Object> map = template.queryForMap(sql, 1001,1002);
        System.out.println(map);
        //{id=1001, ename=孙悟空, job_id=4, mgr=1004, joindate=2000-12-17, salary=10000.00, bonus=null, dept_id=20}

    }

    /**
     * 5. 查询所有记录，将其封装为List
     */
    @Test
    public void test5(){
        String sql = "select * from emp";
        List<Map<String, Object>> list = template.queryForList(sql);

        for (Map<String, Object> stringObjectMap : list) {
            System.out.println(stringObjectMap);
        }
    }

    /**
     * 6. 查询所有记录，将其封装为Emp对象的List集合
     */

    @Test
    public void test6(){
        String sql = "select * from emp";
        List<Emp> list = template.query(sql, new RowMapper<Emp>() {

            @Override
            public Emp mapRow(ResultSet rs, int i) throws SQLException {
                Emp emp = new Emp();
                int id = rs.getInt("id");
                String ename = rs.getString("ename");
                int job_id = rs.getInt("job_id");
                int mgr = rs.getInt("mgr");
                Date joindate = rs.getDate("joindate");
                double salary = rs.getDouble("salary");
                double bonus = rs.getDouble("bonus");
                int dept_id = rs.getInt("dept_id");

                emp.setId(id);
                emp.setEname(ename);
                emp.setJob_id(job_id);
                emp.setMgr(mgr);
                emp.setJoindate(joindate);
                emp.setSalary(salary);
                emp.setBonus(bonus);
                emp.setDept_id(dept_id);

                return emp;
            }
        });
        for (Emp emp : list) {
            System.out.println(emp);
        }
    }

    /**
     * 6. 查询所有记录，将其封装为Emp对象的List集合
     */

    @Test
    public void test6_2(){
        String sql = "select * from emp";
        List<Emp> list = template.query(sql, new BeanPropertyRowMapper<Emp>(Emp.class));
        for (Emp emp : list) {
            System.out.println(emp);
        }
    }
    /**
     * 7. 查询总记录数
     */
    @Test
    public void test7(){
        String sql = "select count(id) from emp";
        Long total = template.queryForObject(sql, Long.class);
        System.out.println(total);
    }
}
```