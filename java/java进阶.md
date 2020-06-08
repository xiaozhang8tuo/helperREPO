# day01【Object类、常用API】 #

## 第一章 Object类 ##

### Demo01ToString ###

```java
package com.itheima.demo01.Object;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

/*
    java.lang.Object
    类 Object 是类层次结构的根(父)类。
    每个类(Person,Student...)都使用 Object 作为超(父)类。
    所有对象（包括数组）都实现这个类的方法。
 */
public class Demo01ToString{
    public static void main(String[] args) {
        /*
            Person类默认继承了Object类,所以可以使用Object类中的toString方法
            String toString() 返回该对象的字符串表示。
         */
        Person p = new Person("张三",18);
        String s = p.toString();
        System.out.println(s);//com.itheima.demo01.Object.Person@75412c2f | abc | Person{name=张三 ,age=18}

        //直接打印对象的名字,其实就是调用对象的toString  p=p.toString();
        System.out.println(p);//com.itheima.demo01.Object.Person@5f150435 | abc | Person{name=张三 ,age=18}

        //看一个类是否重写了toString,直接打印这个类的对象即可,如果没有重写toString方法那么打印的是对象的地址值
        Random r = new Random();
        System.out.println(r);//java.util.Random@3f3afe78  没有重写toString方法

        Scanner sc = new Scanner(System.in);
        System.out.println(sc);//java.util.Scanner[delimiters=\p{javaWhitespace}+..  重写toString方法

        ArrayList<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);
        System.out.println(list);//[1, 2, 3]  重写toString方法
    }
}

```

### Demo02Equals/Demo03Objects ###

```java
package com.itheima.demo01.Object;

import java.util.Objects;

public class Person {
    private String name;
    private int age;

    public Person() {
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    /*
        直接打印对象的地址值没有意义,需要重写Object类中的toString方法
        打印对象的属性(name,age)
     */
    /*@Override
    public String toString() {
       //return "abc";
       return "Person{name="+name+" ,age="+age+"}";
    }*/
    /*@Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }*/

    /*
        Object类的equals方法,默认比较的是两个对象的地址值,没有意义
        所以我们要重写equals方法,比较两个对象的属性(name,age)
        问题:
            隐含着一个多态
            多态的弊端:无法使用子类特有的内容(属性和方法)
            Object obj = p2 = new Person("古力娜扎",19);
            解决:可以使用向下转型(强转)把obj类型转换为Person
     */
    /*@Override
    public boolean equals(Object obj) {
        //增加一个判断,传递的参数obj如果是this本身,直接返回true,提高程序的效率
        if(obj==this){
            return true;
        }

        //增加一个判断,传递的参数obj如果是null,直接返回false,提高程序的效率
        if(obj==null){
            return false;
        }

        //增加一个判断,防止类型转换一次ClassCastException
        if(obj instanceof Person){
            //使用向下转型,把obj转换为Person类型
            Person p = (Person)obj;
            //比较两个对象的属性,一个对象是this(p1),一个对象是p(obj->p2)
            boolean b = this.name.equals(p.name) && this.age==p.age;
            return b;
        }
        //不是Person类型直接返回false
        return false;
    }*/
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        //getClass() != o.getClass() 使用反射技术,判断o是否是Person类型  等效于 obj instanceof Person
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return age == person.age &&
                Objects.equals(name, person.name);
    }

    @Override
    public int hashCode() {

        return Objects.hash(name, age);
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
}
package com.itheima.demo01.Object;

import java.util.ArrayList;

public class Demo02Equals {
    public static void main(String[] args) {
        /*
            Person类默认继承了Object类,所以可以使用Object类的equals方法
            boolean equals(Object obj) 指示其他某个对象是否与此对象“相等”。
            equals方法源码:
                public boolean equals(Object obj) {
                    return (this == obj);
                }
                参数:
                    Object obj:可以传递任意的对象
                    == 比较运算符,返回的是一个布尔值 true false
                    基本数据类型:比较的是值
                    引用数据类型:比价的是两个对象的地址值
               this是谁?那个对象调用的方法,方法中的this就是那个对象;p1调用的equals方法所以this就是p1
               obj是谁?传递过来的参数p2
               this==obj -->p1==p2
         */
        Person p1 = new Person("迪丽热巴",18);
        //Person p2 = new Person("古力娜扎",19);
        Person p2 = new Person("迪丽热巴",18);
        System.out.println("p1:"+p1);//p1:com.itheima.demo01.Object.Person@58ceff1
        System.out.println("p2:"+p2);//p2:com.itheima.demo01.Object.Person@7c30a502

        //p1=p2;//把p2的地址值赋值给p1
        ArrayList<String> list = new ArrayList<>();

        boolean b = p1.equals(p1);  //p1.equals(p2).var 快捷输入
        System.out.println(b);
    }
}
package com.itheima.demo01.Object;

import java.util.Objects;

public class Demo03Objects {
    public static void main(String[] args) {
        String s1 = "abc";
        //String s1 = null;
        String s2 = "abc";
        //boolean b = s1.equals(s2); // NullPointerException null是不能调用方法的,会抛出空指针异常
        //System.out.println(b);
        /*
            Objects类的equals方法:对两个对象进行比较,防止空指针异常
            public static boolean equals(Object a, Object b) {
                return (a == b) || (a != null && a.equals(b));
            }
         */
        boolean b2 = Objects.equals(s1, s2);
        System.out.println(b2);

    }
}

```

## 第二章 日期时间类 ##

### Demo01Date ###

```JAVA
package com.itheima.demo02.Date;

import java.sql.Date;

/*
    java.util.Date:表示日期和时间的类
    类 Date 表示特定的瞬间，精确到毫秒。
    毫秒:千分之一秒 1000毫秒=1秒
    特定的瞬间:一个时间点,一刹那时间
    2088-08-08 09:55:33:333 瞬间
    2088-08-08 09:55:33:334 瞬间
    2088-08-08 09:55:33:334 瞬间
    ...
    毫秒值的作用:可以对时间和日期进行计算
    2099-01-03 到 2088-01-01 中间一共有多少天
    可以日期转换为毫秒进行计算,计算完毕,在把毫秒转换为日期

    把日期转换为毫秒:
        当前的日期:2088-01-01
        时间原点(0毫秒):1970 年 1 月 1 日 00:00:00(英国格林威治)
        就是计算当前日期到时间原点之间一共经历了多少毫秒 (3742767540068L)
    注意:
        中国属于东八区,会把时间增加8个小时
        1970 年 1 月 1 日 08:00:00

    把毫秒转换为日期:
        1 天 = 24 × 60 × 60 = 86400 秒  = 86400 x 1000 = 86400000毫秒
 */
public class Demo01Date {
    public static void main(String[] args) {
        System.out.println(System.currentTimeMillis());//获取当前系统时间到1970 年 1 月 1 日 00:00:00经历了多少毫秒
    }
}
```

### Demo02Date  ###

```JAVA
package com.itheima.demo02.Date;

import java.util.Date;

public class Demo02Date {
    public static void main(String[] args) {
        demo03();
    }

    /*
        long getTime() 把日期转换为毫秒值(相当于System.currentTimeMillis()方法)
          返回自 1970 年 1 月 1 日 00:00:00 GMT 以来此 Date 对象表示的毫秒数。
     */
    private static void demo03() {
        Date date = new Date();
        long time = date.getTime();
        System.out.println(time);//3742777636267
    }

    /*
        Date类的带参数构造方法
        Date(long date) :传递毫秒值,把毫秒值转换为Date日期
     */
    private static void demo02() {
        Date date = new Date(0L);
        System.out.println(date);// Thu Jan 01 08:00:00 CST 1970

        date = new Date(3742767540068L);
        System.out.println(date);// Sun Aug 08 09:39:00 CST 2088
    }

    /*
        Date类的空参数构造方法
        Date() 获取当前系统的日期和时间
     */
    private static void demo01() {
        Date date = new Date();
        System.out.println(date);//Sun Aug 08 12:23:03 CST 2088
    }
}
```

### Demo01DateFormat ###

```java
package com.itheima.demo03.DateFormat;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

/*
    java.text.DateFormat:是日期/时间格式化子类的抽象类
    作用:
        格式化（也就是日期 -> 文本）、解析（文本-> 日期）
    成员方法:
        String format(Date date)  按照指定的模式,把Date日期,格式化为符合模式的字符串
        Date parse(String source)  把符合模式的字符串,解析为Date日期
    DateFormat类是一个抽象类,无法直接创建对象使用,可以使用DateFormat类的子类

    java.text.SimpleDateFormat extends DateFormat

    构造方法:
        SimpleDateFormat(String pattern)
          用给定的模式和默认语言环境的日期格式符号构造 SimpleDateFormat。
        参数:
             String pattern:传递指定的模式
        模式:区分大小写的
            y   年
            M   月
            d   日
            H   时
            m   分
            s   秒
        写对应的模式,会把模式替换为对应的日期和时间
            "yyyy-MM-dd HH:mm:ss"
        注意:
            模式中的字母不能更改,连接模式的符号可以改变
             "yyyy年MM月dd日 HH时mm分ss秒"

 */
public class Demo01DateFormat {
    public static void main(String[] args) throws ParseException {
        demo01();
    }

    /*
         使用DateFormat类中的方法parse,把文本解析为日期
         使用步骤:
            1.创建SimpleDateFormat对象,构造方法中传递指定的模式
            2.调用SimpleDateFormat对象中的方法parse,把符合构造方法中模式的字符串,解析为Date日期
            注意:
                public Date parse(String source) throws ParseException
                parse方法声明了一个异常叫ParseException
                如果字符串和构造方法的模式不一样,那么程序就会抛出此异常
                调用一个抛出了异常的方法,就必须的处理这个异常,要么throws继续抛出这个异常,要么try catch自己处理
     */
    private static void demo02() throws ParseException {
        //1.创建SimpleDateFormat对象,构造方法中传递指定的模式
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy年MM月dd日 HH时mm分ss秒");
        //2.调用SimpleDateFormat对象中的方法parse,把符合构造方法中模式的字符串,解析为Date日期
        //Date parse(String source)  把符合模式的字符串,解析为Date日期
        Date date = sdf.parse("2088年08月08日 15时51分54秒");
        System.out.println(date);
    }

    /*
        使用DateFormat类中的方法format,把日期格式化为文本
        使用步骤:
            1.创建SimpleDateFormat对象,构造方法中传递指定的模式
            2.调用SimpleDateFormat对象中的方法format,按照构造方法中指定的模式,把Date日期格式化为符合模式的字符串(文本)
     */
    private static void demo01() {
        //1.创建SimpleDateFormat对象,构造方法中传递指定的模式
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy年MM月dd日 HH时mm分ss秒");
        //2.调用SimpleDateFormat对象中的方法format,按照构造方法中指定的模式,把Date日期格式化为符合模式的字符串(文本)
        //String format(Date date)  按照指定的模式,把Date日期,格式化为符合模式的字符串
        Date date = new Date();
        String d = sdf.format(date);
        System.out.println(date);//Sun Aug 08 15:51:54 CST 2088
        System.out.println(d);//2088年08月08日 15时51分54秒
    }
}
```

### Demo02计算出一个人已经出生了多少天 ###

```java
package com.itheima.demo03.DateFormat;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

/*
    练习:
        请使用日期时间相关的API，计算出一个人已经出生了多少天。
    分析:
        1.使用Scanner类中的方法next,获取出生日期
        2.使用DateFormat类中的方法parse,把字符串的出生日期,解析为Date格式的出生日期
        3.把Date格式的出生日期转换为毫秒值
        4.获取当前的日期,转换为毫秒值
        5.使用当前日期的毫秒值-出生日期的毫秒值
        6.把毫秒差值转换为天(s/1000/60/60/24)
 */
public class Demo02Test {
    public static void main(String[] args) throws ParseException {
        //1.使用Scanner类中的方法next,获取出生日期
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入您的出生日期,格式:yyyy-MM-dd");
        String birthdayDateString = sc.next();
        //2.使用DateFormat类中的方法parse,把字符串的出生日期,解析为Date格式的出生日期
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
        Date birthdayDate = sdf.parse(birthdayDateString);
        //3.把Date格式的出生日期转换为毫秒值
        long birthdayDateTime = birthdayDate.getTime();
        //4.获取当前的日期,转换为毫秒值
        long todayTime = new Date().getTime();
        //5.使用当前日期的毫秒值-出生日期的毫秒值
        long time = todayTime-birthdayDateTime;
        //6.把毫秒差值转换为天(s/1000/60/60/24)
        System.out.println(time/1000/60/60/24);
    }
}
```

### Demo03Calendar类 ###

```java
package com.itheima.demo04.Calendar;

import java.util.Calendar;
import java.util.Date;

/*
    Calendar类的常用成员方法:
        public int get(int field)：返回给定日历字段的值。
        public void set(int field, int value)：将给定的日历字段设置为给定值。
        public abstract void add(int field, int amount)：根据日历的规则，为给定的日历字段添加或减去指定的时间量。
        public Date getTime()：返回一个表示此Calendar时间值（从历元到现在的毫秒偏移量）的Date对象。
    成员方法的参数:
        int field:日历类的字段,可以使用Calendar类的静态成员变量获取
            public static final int YEAR = 1;  年
            public static final int MONTH = 2; 月
            public static final int DATE = 5;  月中的某一天
            public static final int DAY_OF_MONTH = 5;月中的某一天
            public static final int HOUR = 10;        时
            public static final int MINUTE = 12;   分
            public static final int SECOND = 13;   秒
 */
public class Demo02Calendar {
    public static void main(String[] args) {
        demo04();
    }

    /*
        public Date getTime()：返回一个表示此Calendar时间值（从历元到现在的毫秒偏移量）的Date对象。
        把日历对象,转换为日期对象
     */
    private static void demo04() {
        //使用getInstance方法获取Calendar对象
        Calendar c = Calendar.getInstance();

        Date date = c.getTime();
        System.out.println(date);
    }

    /*
        public abstract void add(int field, int amount)：根据日历的规则，为给定的日历字段添加或减去指定的时间量。
        把指定的字段增加/减少指定的值
        参数:
            int field:传递指定的日历字段(YEAR,MONTH...)
            int amount:增加/减少指定的值
                正数:增加
                负数:减少
     */
    private static void demo03() {
        //使用getInstance方法获取Calendar对象
        Calendar c = Calendar.getInstance();

        //把年增加2年
        c.add(Calendar.YEAR,2);
        //把月份减少3个月
        c.add(Calendar.MONTH,-3);


        int year = c.get(Calendar.YEAR);
        System.out.println(year);

        int month = c.get(Calendar.MONTH);
        System.out.println(month);//西方的月份0-11 东方:1-12

        //int date = c.get(Calendar.DAY_OF_MONTH);
        int date = c.get(Calendar.DATE);
        System.out.println(date);
    }

    /*
        public void set(int field, int value)：将给定的日历字段设置为给定值。
        参数:
            int field:传递指定的日历字段(YEAR,MONTH...)
            int value:给指定字段设置的值
     */
    private static void demo02() {
        //使用getInstance方法获取Calendar对象
        Calendar c = Calendar.getInstance();

        //设置年为9999
        c.set(Calendar.YEAR,9999);
        //设置月为9月
        c.set(Calendar.MONTH,9);
        //设置日9日
        c.set(Calendar.DATE,9);

        //同时设置年月日,可以使用set的重载方法
        c.set(8888,8,8);

        int year = c.get(Calendar.YEAR);
        System.out.println(year);

        int month = c.get(Calendar.MONTH);
        System.out.println(month);//西方的月份0-11 东方:1-12

        int date = c.get(Calendar.DATE);
        System.out.println(date);
    }

    /*
        public int get(int field)：返回给定日历字段的值。
        参数:传递指定的日历字段(YEAR,MONTH...)
        返回值:日历字段代表的具体的值
     */
    private static void demo01() {
        //使用getInstance方法获取Calendar对象
        Calendar c = Calendar.getInstance();
        int year = c.get(Calendar.YEAR);
        System.out.println(year);

        int month = c.get(Calendar.MONTH);
        System.out.println(month);//西方的月份0-11 东方:1-12

        //int date = c.get(Calendar.DAY_OF_MONTH);
        int date = c.get(Calendar.DATE);
        System.out.println(date);
    }
}
```

## 第三章 System类 ##

### Demo01System ArrayCopy/currentTimeMillis ###

```java
package com.itheima.demo05.System;

import java.util.Arrays;

/*
    java.lang.System类中提供了大量的静态方法，可以获取与系统相关的信息或系统级操作，在System类的API文档中，常用的方法有：
        public static long currentTimeMillis()：返回以毫秒为单位的当前时间。
        public static void arraycopy(Object src, int srcPos, Object dest, int destPos, int length)：将数组中指定的数据拷贝到另一个数组中。
 */
public class Demo01System {
    public static void main(String[] args) {
        demo02();
        StringBuilder sb = new StringBuilder();
    }

    /*
        public static void arraycopy(Object src, int srcPos, Object dest, int destPos, int length)：将数组中指定的数据拷贝到另一个数组中。
        参数:
            src - 源数组。
            srcPos - 源数组中的起始位置(起始索引)。
            dest - 目标数组。
            destPos - 目标数据中的起始位置。
            length - 要复制的数组元素的数量。
        练习:
            将src数组中前3个元素，复制到dest数组的前3个位置上
                复制元素前：
                src数组元素[1,2,3,4,5]，dest数组元素[6,7,8,9,10]
                复制元素后：
                src数组元素[1,2,3,4,5]，dest数组元素[1,2,3,9,10]
     */
    private static void demo02() {
        //定义源数组
        int[] src = {1,2,3,4,5};
        //定义目标数组
        int[] dest = {6,7,8,9,10};
        System.out.println("复制前:"+ Arrays.toString(dest));
        //使用System类中的arraycopy把源数组的前3个元素复制到目标数组的前3个位置上
        System.arraycopy(src,0,dest,0,3);
        System.out.println("复制后:"+ Arrays.toString(dest));
    }

    /*
        public static long currentTimeMillis()：返回以毫秒为单位的当前时间。
        用来程序的效率
        验证for循环打印数字1-9999所需要使用的时间（毫秒）
     */
    private static void demo01() {
        //程序执行前,获取一次毫秒值
        long s = System.currentTimeMillis();
        //执行for循环
        for (int i = 1; i <=9999 ; i++) {
            System.out.println(i);
        }
        //程序执行后,获取一次毫秒值
        long e = System.currentTimeMillis();
        System.out.println("程序共耗时:"+(e-s)+"毫秒");//程序共耗时:106毫秒
    }
}
```

## 第四章 StringBuilder类 ##

### Demo01StringBuilder ###

```java
package com.itheima.demo06StringBuilder;
/*
    java.lang.StringBuilder类:字符串缓冲区,可以提高字符串的效率
    构造方法:
        StringBuilder() 构造一个不带任何字符的字符串生成器，其初始容量为 16 个字符。
        StringBuilder(String str) 构造一个字符串生成器，并初始化为指定的字符串内容。
 */
public class Demo01StringBuilder {
    public static void main(String[] args) {
        //空参数构造方法
        StringBuilder bu1 = new StringBuilder();
        System.out.println("bu1:"+bu1);//bu1:""

        //带字符串的构造方法
        StringBuilder bu2 = new StringBuilder("abc");
        System.out.println("bu2:"+bu2);//bu2:abc
    }
}
package com.itheima.demo06StringBuilder;
/*
    StringBuilder的常用方法:
        public StringBuilder append(...)：添加任意类型数据的字符串形式，并返回当前对象自身。
 */
public class Demo02StringBuilder {
    public static void main(String[] args) {
        //创建StringBuilder对象
        StringBuilder bu = new StringBuilder();
        //使用append方法往StringBuilder中添加数据
        //append方法返回的是this,调用方法的对象bu,this==bu
        //StringBuilder bu2 = bu.append("abc");//把bu的地址赋值给了bu2
        //System.out.println(bu);//"abc"
        //System.out.println(bu2);//"abc"
        //System.out.println(bu==bu2);//比较的是地址 true

        //使用append方法无需接收返回值
//        bu.append("abc");
//        bu.append(1);
//        bu.append(true);
//        bu.append(8.8);
//        bu.append('中');
//        System.out.println(bu);//abc1true8.8中

        /*
            链式编程:方法返回值是一个对象,可以继续调用方法
         */
        System.out.println("abc".toUpperCase().toLowerCase().toUpperCase().toLowerCase());
        bu.append("abc").append(1).append(true).append(8.8).append('中');
        System.out.println(bu);//abc1true8.8中

    }
}
package com.itheima.demo06StringBuilder;
/*
    StringBuilder和String可以相互转换:
        String->StringBuilder:可以使用StringBuilder的构造方法
            StringBuilder(String str) 构造一个字符串生成器，并初始化为指定的字符串内容。
        StringBuilder->String:可以使用StringBuilder中的toString方法
            public String toString()：将当前StringBuilder对象转换为String对象。
 */
public class Demo03StringBuilder {
    public static void main(String[] args) {
        //String->StringBuilder
        String str = "hello";
        System.out.println("str:"+str);
        StringBuilder bu = new StringBuilder(str);
        //往StringBuilder中添加数据
        bu.append("world");
        System.out.println("bu:"+bu);

        //StringBuilder->String
        String s = bu.toString();
        System.out.println("s:"+s);
    }
}

```

## 第五章 包装类 ##

### Demo01Integer ###

```java
package com.itheima.demo07Integer;
/*
    装箱:把基本类型的数据,包装到包装类中(基本类型的数据->包装类)
        构造方法:
            Integer(int value) 构造一个新分配的 Integer 对象，它表示指定的 int 值。
            Integer(String s) 构造一个新分配的 Integer 对象，它表示 String 参数所指示的 int 值。
                传递的字符串,必须是基本类型的字符串,否则会抛出异常 "100" 正确  "a" 抛异常
        静态方法:
            static Integer valueOf(int i) 返回一个表示指定的 int 值的 Integer 实例。
            static Integer valueOf(String s) 返回保存指定的 String 的值的 Integer 对象。
    拆箱:在包装类中取出基本类型的数据(包装类->基本类型的数据)
        成员方法:
            int intValue() 以 int 类型返回该 Integer 的值。
 */
public class Demo01Integer {
    public static void main(String[] args) {
        //装箱:把基本类型的数据,包装到包装类中(基本类型的数据->包装类)
        //构造方法
        Integer in1 = new Integer(1);//方法上有横线,说明方法过时了
        System.out.println(in1);//1 重写了toString方法

        Integer in2 = new Integer("1");
        System.out.println(in2);//1

        //静态方法
        Integer in3 = Integer.valueOf(1);
        System.out.println(in3);

        //Integer in4 = Integer.valueOf("a");//NumberFormatException数字格式化异常
        Integer in4 = Integer.valueOf("1");
        System.out.println(in4);

        //拆箱:在包装类中取出基本类型的数据(包装类->基本类型的数据)
        int i = in1.intValue();
        System.out.println(i);
    }
}
package com.itheima.demo07Integer;

import java.util.ArrayList;

/*
    自动装箱与自动拆箱:基本类型的数据和包装类之间可以自动的相互转换
    JDK1.5之后出现的新特性
 */
public class Demo02Ineger {
    public static void main(String[] args) {
        /*
            自动装箱:直接把int类型的整数赋值包装类
            Integer in = 1; 就相当于 Integer in = new Integer(1);
         */
        Integer in = 1;

        /*
            自动拆箱:in是包装类,无法直接参与运算,可以自动转换为基本数据类型,在进行计算
            in+2;就相当于 in.intVale() + 2 = 3
            in = in.intVale() + 2 = 3 又是一个自动装箱
         */
        in = in+2;

        ArrayList<Integer> list = new ArrayList<>();
        /*
            ArrayList集合无法直接存储整数,可以存储Integer包装类
         */
        list.add(1); //-->自动装箱 list.add(new Integer(1));

        int a = list.get(0); //-->自动拆箱  list.get(0).intValue();
    }
}
package com.itheima.demo07Integer;
/*
    基本类型与字符串类型之间的相互转换
    基本类型->字符串(String)
        1.基本类型的值+""  最简单的方法(工作中常用)
        2.包装类的静态方法toString(参数),不是Object类的toString() 重载
            static String toString(int i) 返回一个表示指定整数的 String 对象。
        3.String类的静态方法valueOf(参数)
            static String valueOf(int i) 返回 int 参数的字符串表示形式。
    字符串(String)->基本类型
        使用包装类的静态方法parseXXX("字符串");
            Integer类: static int parseInt(String s)
            Double类: static double parseDouble(String s)
 */
public class Demo03Integer {
    public static void main(String[] args) {
        //基本类型->字符串(String)
        int i1 = 100;
        String s1 = i1+"";
        System.out.println(s1+200);//100200

        String s2 = Integer.toString(100);
        System.out.println(s2+200);//100200

        String s3 = String.valueOf(100);
        System.out.println(s3+200);//100200

        //字符串(String)->基本类型
        int i = Integer.parseInt(s1);
        System.out.println(i-10);

        int a = Integer.parseInt("a");//NumberFormatException
        System.out.println(a);
    }
}

```

# day02【Collection、泛型】 #

## 第一章 Collection集合 ##

### Demo01Collection ###

```java
package com.itheima.demo01.Collection;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;

/*
    java.util.Collection接口
        所有单列集合的最顶层的接口,里边定义了所有单列集合共性的方法
        任意的单列集合都可以使用Collection接口中的方法


    共性的方法:
      public boolean add(E e)：  把给定的对象添加到当前集合中 。
      public void clear() :清空集合中所有的元素。
      public boolean remove(E e): 把给定的对象在当前集合中删除。
      public boolean contains(E e): 判断当前集合中是否包含给定的对象。
      public boolean isEmpty(): 判断当前集合是否为空。
      public int size(): 返回集合中元素的个数。
      public Object[] toArray(): 把集合中的元素，存储到数组中。
 */
public class Demo01Collection {
    public static void main(String[] args) {
        //创建集合对象,可以使用多态
        //Collection<String> coll = new ArrayList<>();
        Collection<String> coll = new HashSet<>();
        System.out.println(coll);//重写了toString方法  []

        /*
            public boolean add(E e)：  把给定的对象添加到当前集合中 。
            返回值是一个boolean值,一般都返回true,所以可以不用接收
         */
        boolean b1 = coll.add("张三");
        System.out.println("b1:"+b1);//b1:true
        System.out.println(coll);//[张三]
        coll.add("李四");
        coll.add("李四");
        coll.add("赵六");
        coll.add("田七");
        System.out.println(coll);//[张三, 李四, 赵六, 田七]

        /*
            public boolean remove(E e): 把给定的对象在当前集合中删除。
            返回值是一个boolean值,集合中存在元素,删除元素,返回true
                                集合中不存在元素,删除失败,返回false
         */
        boolean b2 = coll.remove("赵六");
        System.out.println("b2:"+b2);//b2:true

        boolean b3 = coll.remove("赵四");
        System.out.println("b3:"+b3);//b3:false
        System.out.println(coll);//[张三, 李四, 田七]

        /*
            public boolean contains(E e): 判断当前集合中是否包含给定的对象。
            包含返回true
            不包含返回false
         */
        boolean b4 = coll.contains("李四");
        System.out.println("b4:"+b4);//b4:true

        boolean b5 = coll.contains("赵四");
        System.out.println("b5:"+b5);//b5:false

        //public boolean isEmpty(): 判断当前集合是否为空。 集合为空返回true,集合不为空返回false
        boolean b6 = coll.isEmpty();
        System.out.println("b6:"+b6);//b6:false

        //public int size(): 返回集合中元素的个数。
        int size = coll.size();
        System.out.println("size:"+size);//size:3

        //public Object[] toArray(): 把集合中的元素，存储到数组中。
        Object[] arr = coll.toArray();
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }

        //public void clear() :清空集合中所有的元素。但是不删除集合,集合还存在
        coll.clear();
        System.out.println(coll);//[]
        System.out.println(coll.isEmpty());//true
    }
}
```

## 第二章 Iterator迭代器 ##

### Demo01Iterator ###

```java
package com.itheima.demo02.Iterator;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;

/*
    java.util.Iterator接口:迭代器(对集合进行遍历)
    有两个常用的方法
        boolean hasNext() 如果仍有元素可以迭代，则返回 true。
            判断集合中还有没有下一个元素,有就返回true,没有就返回false
        E next() 返回迭代的下一个元素。
            取出集合中的下一个元素
    Iterator迭代器,是一个接口,我们无法直接使用,需要使用Iterator接口的实现类对象,获取实现类的方式比较特殊
    Collection接口中有一个方法,叫iterator(),这个方法返回的就是迭代器的实现类对象
        Iterator<E> iterator() 返回在此 collection 的元素上进行迭代的迭代器。

    迭代器的使用步骤(重点):
        1.使用集合中的方法iterator()获取迭代器的实现类对象,使用Iterator接口接收(多态)
        2.使用Iterator接口中的方法hasNext判断还有没有下一个元素
        3.使用Iterator接口中的方法next取出集合中的下一个元素
 */
public class Demo01Iterator {
    public static void main(String[] args) {
        //创建一个集合对象
        Collection<String> coll = new ArrayList<>();
        //往集合中添加元素
        coll.add("姚明");
        coll.add("科比");
        coll.add("麦迪");
        coll.add("詹姆斯");
        coll.add("艾弗森");

        /*
            1.使用集合中的方法iterator()获取迭代器的实现类对象,使用Iterator接口接收(多态)
            注意:
                Iterator<E>接口也是有泛型的,迭代器的泛型跟着集合走,集合是什么泛型,迭代器就是什么泛型
         */
        //多态  接口            实现类对象
        Iterator<String> it = coll.iterator();


        /*
            发现使用迭代器取出集合中元素的代码,是一个重复的过程
            所以我们可以使用循环优化
            不知道集合中有多少元素,使用while循环
            循环结束的条件,hasNext方法返回false
         */
        while(it.hasNext()){
            String e = it.next();
            System.out.println(e);
        }
        System.out.println("----------------------");//.next()会自动步进
        for(Iterator<String> it2 = coll.iterator();it2.hasNext();){
            String e = it2.next();
            System.out.println(e);
        }


       /* //2.使用Iterator接口中的方法hasNext判断还有没有下一个元素
        boolean b = it.hasNext();
        System.out.println(b);//true
        //3.使用Iterator接口中的方法next取出集合中的下一个元素
        String s = it.next();
        System.out.println(s);//姚明

        b = it.hasNext();
        System.out.println(b);
        s = it.next();
        System.out.println(s);

        b = it.hasNext();
        System.out.println(b);
        s = it.next();
        System.out.println(s);

        b = it.hasNext();
        System.out.println(b);
        s = it.next();
        System.out.println(s);

        b = it.hasNext();
        System.out.println(b);
        s = it.next();
        System.out.println(s);

        b = it.hasNext();
        System.out.println(b);//没有元素,返回false
        s = it.next();//没有元素,在取出元素会抛出NoSuchElementException没有元素异常
        System.out.println(s);*/
    }
}
```

### Demo02ForEach增强for循环 ###

```java
package com.itheima.demo02.Iterator;

import java.util.ArrayList;

/*
    增强for循环:底层使用的也是迭代器,使用for循环的格式,简化了迭代器的书写
    是JDK1.5之后出现的新特性
    Collection<E>extends Iterable<E>:所有的单列集合都可以使用增强for
    public interface Iterable<T>实现这个接口允许对象成为 "foreach" 语句的目标。

    增强for循环:用来遍历集合和数组

    格式:
        for(集合/数组的数据类型 变量名: 集合名/数组名){
            sout(变量名);
        }
 */
public class Demo02ForEach {
    public static void main(String[] args) {
        demo02();
    }

    //使用增强for循环遍历集合
    private static void demo02() {
        ArrayList<String> list = new ArrayList<>();
        list.add("aaa");
        list.add("bbb");
        list.add("ccc");
        list.add("ddd");
        for(String s : list){
            System.out.println(s);
        }
    }

    //使用增强for循环遍历数组
    private static void demo01() {
        int[] arr = {1,2,3,4,5};
        for(int i:arr){
            System.out.println(i);
        }
    }
}
```

## 第三章 泛型Generic ##

### Demo01Generic ###

```java
package com.itheima.demo03.Generic;

import java.util.ArrayList;
import java.util.Iterator;

public class Demo01Generic {
    public static void main(String[] args) {
        show01();
    }

    /*
        创建集合对象,使用泛型
        好处:
            1.避免了类型转换的麻烦,存储的是什么类型,取出的就是什么类型
            2.把运行期异常(代码运行之后会抛出的异常),提升到了编译期(写代码的时候会报错)
         弊端:
            泛型是什么类型,只能存储什么类型的数据
     */
    private static void show02() {
        ArrayList<String> list = new ArrayList<>();
        list.add("abc");
        //list.add(1);//add(java.lang.String)in ArrayList cannot be applied to (int)

        //使用迭代器遍历list集合
        Iterator<String> it = list.iterator();
        while(it.hasNext()){
            String s = it.next();
            System.out.println(s+"->"+s.length());
        }
    }

    /*
        创建集合对象,不使用泛型
        好处:
            集合不使用泛型,默认的类型就是Object类型,可以存储任意类型的数据
        弊端:
            不安全,会引发异常
     */
    private static void show01() {
        ArrayList list = new ArrayList();
        list.add("abc");
        list.add(1);

        //使用迭代器遍历list集合
        //获取迭代器
        Iterator it = list.iterator();
        //使用迭代器中的方法hasNext和next遍历集合
        while(it.hasNext()){
            //取出元素也是Object类型
            Object obj = it.next();
            System.out.println(obj);

            //想要使用String类特有的方法,length获取字符串的长度;不能使用  多态 Object obj = "abc";
            //需要向下转型
            //会抛出ClassCastException类型转换异常,不能把Integer类型转换为String类型
            String s = (String)obj;
            System.out.println(s.length());
        }
    }
}
```

### Demo02GenericClass ###

```java
package com.itheima.demo03.Generic;
/*
    定义一个含有泛型的类,模拟ArrayList集合
    泛型是一个未知的数据类型,当我们不确定什么什么数据类型的时候,可以使用泛型
    泛型可以接收任意的数据类型,可以使用Integer,String,Student...
    创建对象的时候确定泛型的数据类型
 */
public class GenericClass<E> {
    private E name;

    public E getName() {
        return name;
    }

    public void setName(E name) {
        this.name = name;
    }
}
package com.itheima.demo03.Generic;

public class Demo02GenericClass {
    public static void main(String[] args) {
        //不写泛型默认为Object类型
        GenericClass gc = new GenericClass();
        gc.setName("只能是字符串");
        Object obj = gc.getName();

        //创建GenericClass对象,泛型使用Integer类型
        GenericClass<Integer> gc2 = new GenericClass<>();
        gc2.setName(1);

        Integer name = gc2.getName();
        System.out.println(name);

        //创建GenericClass对象,泛型使用String类型
        GenericClass<String> gc3 = new GenericClass<>();
        gc3.setName("小明");
        String name1 = gc3.getName();
        System.out.println(name1);
    }
}

```

### Demo03GenericMethod ###

```java
package com.itheima.demo03.Generic;
/*
    定义含有泛型的方法:泛型定义在方法的修饰符和返回值类型之间

    格式:
        修饰符 <泛型> 返回值类型 方法名(参数列表(使用泛型)){
            方法体;
        }

    含有泛型的方法,在调用方法的时候确定泛型的数据类型
    传递什么类型的参数,泛型就是什么类型
 */
public class GenericMethod {
    //定义一个含有泛型的方法
    public <M> void method01(M m){
        System.out.println(m);
    }

    //定义一个含有泛型的静态方法
    public static <S> void method02(S s){
        System.out.println(s);
    }
}
package com.itheima.demo03.Generic;
/*
    测试含有泛型的方法
 */
public class Demo03GenericMethod {
    public static void main(String[] args) {
        //创建GenericMethod对象
        GenericMethod gm = new GenericMethod();

        /*
            调用含有泛型的方法method01
            传递什么类型,泛型就是什么类型
         */
        gm.method01(10);
        gm.method01("abc");
        gm.method01(8.8);
        gm.method01(true);

        gm.method02("静态方法,不建议创建对象使用");

        //静态方法,通过类名.方法名(参数)可以直接使用
        GenericMethod.method02("静态方法");
        GenericMethod.method02(1);
    }
}
```

### Demo04GenericInterface ###

```java
package com.itheima.demo03.Generic;
/*
    定义含有泛型的接口
 */
public interface GenericInterface<I> {
    public abstract void method(I i);
}

package com.itheima.demo03.Generic;
/*
    含有泛型的接口,第一种使用方式:定义接口的实现类,实现接口,指定接口的泛型
    public interface Iterator<E> {
        E next();
    }
    Scanner类实现了Iterator接口,并指定接口的泛型为String,所以重写的next方法泛型默认就是String
    public final class Scanner implements Iterator<String>{
        public String next() {}
    }
 */
public class GenericInterfaceImpl1 implements GenericInterface<String>{
    @Override
    public void method(String s) {
        System.out.println(s);
    }
}
package com.itheima.demo03.Generic;

/*
    含有泛型的接口第二种使用方式:接口使用什么泛型,实现类就使用什么泛型,类跟着接口走
    就相当于定义了一个含有泛型的类,创建对象的时候确定泛型的类型
    public interface List<E>{
        boolean add(E e);
        E get(int index);
    }
    public class ArrayList<E> implements List<E>{
        public boolean add(E e) {}
        public E get(int index) {}
    }
 */
public class GenericInterfaceImpl2<I> implements GenericInterface<I> {
    @Override
    public void method(I i) {
        System.out.println(i);
    }
}
package com.itheima.demo03.Generic;
/*
    测试含有泛型的接口
 */
public class Demo04GenericInterface {
    public static void main(String[] args) {
        //创建GenericInterfaceImpl1对象
        GenericInterfaceImpl1 gi1 = new GenericInterfaceImpl1();
        gi1.method("字符串");

        //创建GenericInterfaceImpl2对象
        GenericInterfaceImpl2<Integer> gi2 = new GenericInterfaceImpl2<>();
        gi2.method(10);

        GenericInterfaceImpl2<Double> gi3 = new GenericInterfaceImpl2<>();
        gi3.method(8.8);
    }
}
```

### Demo05Generic  ?泛型通配符 ###

```java
package com.itheima.demo03.Generic;

import java.util.ArrayList;
import java.util.Iterator;

/*
    泛型的通配符:
        ?:代表任意的数据类型
    使用方式:
        不能创建对象使用
        只能作为方法的参数使用
 */
public class Demo05Generic {
    public static void main(String[] args) {
        ArrayList<Integer> list01 = new ArrayList<>();
        list01.add(1);
        list01.add(2);

        ArrayList<String> list02 = new ArrayList<>();
        list02.add("a");
        list02.add("b");

        printArray(list01);
        printArray(list02);

        //ArrayList<?> list03 = new ArrayList<?>();//不能创建对象使用
    }

    /*
        定义一个方法,能遍历所有类型的ArrayList集合
        这时候我们不知道ArrayList集合使用什么数据类型,可以泛型的通配符?来接收数据类型
        注意:
            泛型没有继承概念的
     */
    public static void printArray(ArrayList<?> list){
        //使用迭代器遍历集合
        Iterator<?> it = list.iterator();
        while(it.hasNext()){
            //it.next()方法,取出的元素是Object,可以接收任意的数据类型
            Object o = it.next();
            System.out.println(o);
        }
    }
}
```

### Demo06Generic泛型通配符的上下限限定 ###

```java
package com.itheima.demo03.Generic;

import java.util.ArrayList;
import java.util.Collection;

/*
    泛型的上限限定: ? extends E  代表使用的泛型只能是E类型的子类/本身
    泛型的下限限定: ? super E    代表使用的泛型只能是E类型的父类/本身
 */
public class Demo06Generic {
    public static void main(String[] args) {
        Collection<Integer> list1 = new ArrayList<Integer>();
        Collection<String> list2 = new ArrayList<String>();
        Collection<Number> list3 = new ArrayList<Number>();
        Collection<Object> list4 = new ArrayList<Object>();

        getElement1(list1);
        //getElement1(list2);//报错
        getElement1(list3);
        //getElement1(list4);//报错

        //getElement2(list1);//报错
        //getElement2(list2);//报错
        getElement2(list3);
        getElement2(list4);

        /*
            类与类之间的继承关系
            Integer extends Number extends Object
            String extends Object
         */

    }
    // 泛型的上限：此时的泛型?，必须是Number类型或者Number类型的子类
    public static void getElement1(Collection<? extends Number> coll){}
    // 泛型的下限：此时的泛型?，必须是Number类型或者Number类型的父类
    public static void getElement2(Collection<? super Number> coll){}
}
```

## 第四章 集合综合案例-斗地主 ##

### 斗地主 ###

```java
package com.itheima.demo04.Test;

import java.util.ArrayList;
import java.util.Collections;

/*
    斗地主综合案例:
        1.准备牌
        2.洗牌
        3.发牌
        4.看牌
 */
public class DouDiZhu {
    public static void main(String[] args) {
        //1.准备牌
        //定义一个存储54张牌的ArrayList集合,泛型使用String
        ArrayList<String> poker = new ArrayList<>();
        //定义两个数组,一个数组存储牌的花色,一个数组存储牌的序号
        String[] colors = {"♠","♥","♣","♦"};
        String[] numbers = {"2","A","K","Q","J","10","9","8","7","6","5","4","3"};
        //先把大王和小王存储到poker集合中
        poker.add("大王");
        poker.add("小王");
        //循环嵌套遍历两个数组,组装52张牌
        for(String number : numbers){
            for (String color : colors) {
                //System.out.println(color+number);
                //把组装好的牌存储到poker集合中
                poker.add(color+number);
            }
        }
        //System.out.println(poker);

        /*
            2.洗牌
            使用集合的工具类Collections中的方法
            static void shuffle(List<?> list) 使用默认随机源对指定列表进行置换。
         */
        Collections.shuffle(poker);
        //System.out.println(poker);

        /*
            3.发牌
         */
        //定义4个集合,存储玩家的牌和底牌
        ArrayList<String> player01 = new ArrayList<>();
        ArrayList<String> player02 = new ArrayList<>();
        ArrayList<String> player03 = new ArrayList<>();
        ArrayList<String> diPai = new ArrayList<>();

        /*
            遍历poker集合,获取每一张牌
            使用poker集合的索引%3给3个玩家轮流发牌
            剩余3张牌给底牌
            注意:
                先判断底牌(i>=51),否则牌就发没了
         */
        for (int i = 0; i < poker.size() ; i++) {
            //获取每一张牌
            String p = poker.get(i);
            //轮流发牌
            if(i>=51){
                //给底牌发牌
                diPai.add(p);
            }else if(i%3==0){
                //给玩家1发牌
                player01.add(p);
            }else if(i%3==1){
                //给玩家2发牌
                player02.add(p);
            }else if(i%3==2){
                //给玩家3发牌
                player03.add(p);
            }
        }

        //4.看牌
        System.out.println("刘德华:"+player01);
        System.out.println("周润发:"+player02);
        System.out.println("周星驰:"+player03);
        System.out.println("底牌:"+diPai);
    }
}
```

# day03 【List、Set、数据结构、Collections】 #

## 第二章 List集合 ##

### Demo01List ###

```java
package com.itheima.demo01.List;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/*
    java.util.List接口 extends Collection接口
    List接口的特点:
        1.有序的集合,存储元素和取出元素的顺序是一致的(存储123 取出123)
        2.有索引,包含了一些带索引的方法
        3.允许存储重复的元素

    List接口中带索引的方法(特有)
        - public void add(int index, E element): 将指定的元素，添加到该集合中的指定位置上。
        - public E get(int index):返回集合中指定位置的元素。
        - public E remove(int index): 移除列表中指定位置的元素, 返回的是被移除的元素。
        - public E set(int index, E element):用指定元素替换集合中指定位置的元素,返回值的更新前的元素。
    注意:
        操作索引的时候,一定要防止索引越界异常
        IndexOutOfBoundsException:索引越界异常,集合会报
        ArrayIndexOutOfBoundsException:数组索引越界异常
        StringIndexOutOfBoundsException:字符串索引越界异常
 */
public class Demo01List {
    public static void main(String[] args) {
        //创建一个List集合对象,多态
        List<String> list = new ArrayList<>();
        //使用add方法往集合中添加元素
        list.add("a");
        list.add("b");
        list.add("c");
        list.add("d");
        list.add("a");
        //打印集合
        System.out.println(list);//[a, b, c, d, a]  不是地址重写了toString

        //public void add(int index, E element): 将指定的元素，添加到该集合中的指定位置上。
        //在c和d之间添加一个itheima
        list.add(3,"itheima");//[a, b, c, itheima, d, a]
        System.out.println(list);

        //public E remove(int index): 移除列表中指定位置的元素, 返回的是被移除的元素。
        //移除元素
        String removeE = list.remove(2);
        System.out.println("被移除的元素:"+removeE);//被移除的元素:c
        System.out.println(list);//[a, b, itheima, d, a]

        //public E set(int index, E element):用指定元素替换集合中指定位置的元素,返回值的更新前的元素。
        //把最后一个a,替换为A
        String setE = list.set(4, "A");
        System.out.println("被替换的元素:"+setE);//被替换的元素:a
        System.out.println(list);//[a, b, itheima, d, A]

        //List集合遍历有3种方式
        //使用普通的for循环
        for(int i=0; i<list.size(); i++){
            //public E get(int index):返回集合中指定位置的元素。
            String s = list.get(i);
            System.out.println(s);
        }
        System.out.println("-----------------");
        //使用迭代器
        Iterator<String> it = list.iterator();
        while(it.hasNext()){
            String s = it.next();
            System.out.println(s);
        }
        System.out.println("-----------------");
        //使用增强for
        for (String s : list) {
            System.out.println(s);
        }

        String r = list.get(5);//IndexOutOfBoundsException: Index 5 out-of-bounds for length 5
        System.out.println(r);

    }
}
```

## 第三章 List的子类 ##

### Demo02LinkedList ###

```java
package com.itheima.demo01.List;

import java.util.LinkedList;

/*
    java.util.LinkedList集合 implements List接口
    LinkedList集合的特点:
        1.底层是一个链表结构:查询慢,增删快
        2.里边包含了大量操作首尾元素的方法
        注意:使用LinkedList集合特有的方法,不能使用多态

        - public void addFirst(E e):将指定元素插入此列表的开头。
        - public void addLast(E e):将指定元素添加到此列表的结尾。
        - public void push(E e):将元素推入此列表所表示的堆栈。

        - public E getFirst():返回此列表的第一个元素。
        - public E getLast():返回此列表的最后一个元素。

        - public E removeFirst():移除并返回此列表的第一个元素。
        - public E removeLast():移除并返回此列表的最后一个元素。
        - public E pop():从此列表所表示的堆栈处弹出一个元素。

        - public boolean isEmpty()：如果列表不包含元素，则返回true。

 */
public class Demo02LinkedList {
    public static void main(String[] args) {
        show03();
    }

    /*
        - public E removeFirst():移除并返回此列表的第一个元素。
        - public E removeLast():移除并返回此列表的最后一个元素。
        - public E pop():从此列表所表示的堆栈处弹出一个元素。此方法相当于 removeFirst
     */
    private static void show03() {
        //创建LinkedList集合对象
        LinkedList<String> linked = new LinkedList<>();
        //使用add方法往集合中添加元素
        linked.add("a");
        linked.add("b");
        linked.add("c");
        System.out.println(linked);//[a, b, c]

        //String first = linked.removeFirst();
        String first = linked.pop();
        System.out.println("被移除的第一个元素:"+first);
        String last = linked.removeLast();
        System.out.println("被移除的最后一个元素:"+last);
        System.out.println(linked);//[b]
    }

    /*
        - public E getFirst():返回此列表的第一个元素。
        - public E getLast():返回此列表的最后一个元素。
     */
    private static void show02() {
        //创建LinkedList集合对象
        LinkedList<String> linked = new LinkedList<>();
        //使用add方法往集合中添加元素
        linked.add("a");
        linked.add("b");
        linked.add("c");

        //linked.clear();//清空集合中的元素 在获取集合中的元素会抛出NoSuchElementException

        //public boolean isEmpty()：如果列表不包含元素，则返回true。
        if(!linked.isEmpty()){
            String first = linked.getFirst();
            System.out.println(first);//a
            String last = linked.getLast();
            System.out.println(last);//c
        }
    }

    /*
        - public void addFirst(E e):将指定元素插入此列表的开头。
        - public void addLast(E e):将指定元素添加到此列表的结尾。
        - public void push(E e):将元素推入此列表所表示的堆栈。此方法等效于 addFirst(E)。
     */
    private static void show01() {
        //创建LinkedList集合对象
        LinkedList<String> linked = new LinkedList<>();
        //使用add方法往集合中添加元素
        linked.add("a");
        linked.add("b");
        linked.add("c");
        System.out.println(linked);//[a, b, c]

        //public void addFirst(E e):将指定元素插入此列表的开头。
        //linked.addFirst("www");
        linked.push("www");
        System.out.println(linked);//[www, a, b, c]

        //public void addLast(E e):将指定元素添加到此列表的结尾。此方法等效于 add()
        linked.addLast("com");
        System.out.println(linked);//[www, a, b, c, com]
    }
}
```

## 第四章 Set接口 ##

### Demo01Set ###

```java
package com.itheima.demo02.Set;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

/*
    java.util.Set接口 extends Collection接口
    Set接口的特点:
        1.不允许存储重复的元素
        2.没有索引,没有带索引的方法,也不能使用普通的for循环遍历
    java.util.HashSet集合 implements Set接口
    HashSet特点:
         1.不允许存储重复的元素
         2.没有索引,没有带索引的方法,也不能使用普通的for循环遍历
         3.是一个无序的集合,存储元素和取出元素的顺序有可能不一致
         4.底层是一个哈希表结构(查询的速度非常的快)
 */
public class Demo01Set {
    public static void main(String[] args) {
        Set<Integer> set = new HashSet<>();
        //使用add方法往集合中添加元素
        set.add(1);
        set.add(3);
        set.add(2);
        set.add(1);
        //使用迭代器遍历set集合
        Iterator<Integer> it = set.iterator();
        while (it.hasNext()){
            Integer n = it.next();
            System.out.println(n);//1,2,3
        }
        //使用增强for遍历set集合
        System.out.println("-----------------");
        for (Integer i : set) {
            System.out.println(i);
        }
    }
}
```

### Demo01HashCode ###

```java
package com.itheima.demo03.hashCode;

public class Person extends  Object{
    //重写hashCode方法

    @Override
    public int hashCode() {
        return  1;
    }
}
package com.itheima.demo03.hashCode;
/*
    哈希值:是一个十进制的整数,由系统随机给出(就是对象的地址值,是一个逻辑地址,是模拟出来得到地址,不是数据实际存储的物理地址)
    在Object类有一个方法,可以获取对象的哈希值
    int hashCode() 返回该对象的哈希码值。
    hashCode方法的源码:
        public native int hashCode();
        native:代表该方法调用的是本地操作系统的方法
 */
public class Demo01HashCode {
    public static void main(String[] args) {
        //Person类继承了Object类,所以可以使用Object类的hashCode方法
        Person p1 = new Person();
        int h1 = p1.hashCode();
        System.out.println(h1);//1967205423  | 1

        Person p2 = new Person();
        int h2 = p2.hashCode();
        System.out.println(h2);//42121758   |  1

        /*
            toString方法的源码:
                return getClass().getName() + "@" + Integer.toHexString(hashCode());
         */
        System.out.println(p1);
        //com.itheima.demo03.hashCode.Person@75412c2f(16) ==  1967205423 (10)
        System.out.println(p2);
        //com.itheima.demo03.hashCode.Person@282ba1e
        System.out.println(p1==p2);//false

        /*
            String类的哈希值
                String类重写Obejct类的hashCode方法
         */
        String s1 = new String("abc");
        String s2 = new String("abc");
        System.out.println(s1.hashCode());//96354
        System.out.println(s2.hashCode());//96354

        System.out.println("重地".hashCode());//1179395
        System.out.println("通话".hashCode());//1179395
    }
}

```

### Demo02HashSetSaveString ###

```java
package com.itheima.demo02.Set;

import java.util.HashSet;

/*
    Set集合不允许存储重复元素的原理
 */
public class Demo02HashSetSaveString {
    public static void main(String[] args) {
        //创建HashSet集合对象
        HashSet<String> set = new HashSet<>();
        String s1 = new String("abc");
        String s2 = new String("abc");
        set.add(s1);
        set.add(s2);
        set.add("重地");
        set.add("通话");
        set.add("abc");
        System.out.println(set);//[重地, 通话, abc]
    }

}
```

### Demo03HashSetSavePerson 自定义类的hashCode和equals ###

```java
package com.itheima.demo02.Set;

import java.util.Objects;

public class Person {
    private String name;
    private int age;

    public Person() {
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return age == person.age &&
                Objects.equals(name, person.name);
    }

    @Override
    public int hashCode() {

        return Objects.hash(name, age);
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
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
}
package com.itheima.demo02.Set;

import java.util.HashSet;

/*
    HashSet存储自定义类型元素

    set集合报错元素唯一:
        存储的元素(String,Integer,...Student,Person...),必须重写hashCode方法和equals方法

    要求:
        同名同年龄的人,视为同一个人,只能存储一次
 */
public class Demo03HashSetSavePerson {
    public static void main(String[] args) {
        //创建HashSet集合存储Person
        HashSet<Person> set = new HashSet<>();
        Person p1 = new Person("小美女",18);
        Person p2 = new Person("小美女",18);
        Person p3 = new Person("小美女",19);
        System.out.println(p1.hashCode());//1967205423
        System.out.println(p2.hashCode());//42121758

        System.out.println(p1==p2);//false
        System.out.println(p1.equals(p2));//false
        set.add(p1);
        set.add(p2);
        set.add(p3);
        System.out.println(set);
    }

}
```

### Demo04LinkedHashSet ###

```java
package com.itheima.demo02.Set;

import java.util.HashSet;
import java.util.LinkedHashSet;

/*
    java.util.LinkedHashSet集合 extends HashSet集合
    LinkedHashSet集合特点:
        底层是一个哈希表(数组+链表/红黑树)+链表:多了一条链表(记录元素的存储顺序),保证元素有序
 */
public class Demo04LinkedHashSet {
    public static void main(String[] args) {
        HashSet<String> set = new HashSet<>();
        set.add("www");
        set.add("abc");
        set.add("abc");
        set.add("itcast");
        System.out.println(set);//[abc, www, itcast] 无序,不允许重复

        LinkedHashSet<String> linked = new LinkedHashSet<>();
        linked.add("www");
        linked.add("abc");
        linked.add("abc");
        linked.add("itcast");
        System.out.println(linked);//[www, abc, itcast] 有序,不允许重复
    }
}
```

### Demo01VarArgs 可变参数Object...obj ###

```java
package com.itheima.demo04.VarArgs;
/*
    可变参数:是JDK1.5之后出现的新特性
    使用前提:
        当方法的参数列表数据类型已经确定,但是参数的个数不确定,就可以使用可变参数.
    使用格式:定义方法时使用
        修饰符 返回值类型 方法名(数据类型...变量名){}
    可变参数的原理:
        可变参数底层就是一个数组,根据传递参数个数不同,会创建不同长度的数组,来存储这些参数
        传递的参数个数,可以是0个(不传递),1,2...多个

 */
public class Demo01VarArgs {
    public static void main(String[] args) {
        //int i = add();
        //int i = add(10);
        int i = add(10,20);
        //int i = add(10,20,30,40,50,60,70,80,90,100);
        System.out.println(i);

        method("abc",5.5,10,1,2,3,4);
    }

    /*
        可变参数的注意事项
            1.一个方法的参数列表,只能有一个可变参数
            2.如果方法的参数有多个,那么可变参数必须写在参数列表的末尾
     */
    /*public static void method(int...a,String...b){

    }*/

    /*public static void method(String b,double c,int d,int...a){
    }*/

    //可变参数的特殊(终极)写法
    public static void method(Object...obj){

    }

    /*
        定义计算(0-n)整数和的方法
        已知:计算整数的和,数据类型已经确定int
        但是参数的个数不确定,不知道要计算几个整数的和,就可以使用可变参数
        add(); 就会创建一个长度为0的数组, new int[0]
        add(10); 就会创建一个长度为1的数组,存储传递来过的参数 new int[]{10};
        add(10,20); 就会创建一个长度为2的数组,存储传递来过的参数 new int[]{10,20};
        add(10,20,30,40,50,60,70,80,90,100); 就会创建一个长度为2的数组,存储传递来过的参数 new int[]{10,20,30,40,50,60,70,80,90,100};
     */
    public static int add(int...arr){
        //System.out.println(arr);//[I@2ac1fdc4 底层是一个数组
        //System.out.println(arr.length);//0,1,2,10
        int sum = 0;
        //遍历数组,获取数组中的每一个元素
        for (int i : arr) {
            //累加求和
            sum += i;
        }
        return sum;
    }

    //定义一个方法,计算两个int类型整数的和
    /*public static int add(int a,int b){
        return a+b;
    }*/
}
```

## 第五章  Collections ##

### Demo01Collections  addAll/shuffle ###

```java
package com.itheima.demo05.Collections;

import java.util.ArrayList;
import java.util.Collections;

/*
    - java.utils.Collections是集合工具类，用来对集合进行操作。部分方法如下：
        - public static <T> boolean addAll(Collection<T> c, T... elements):往集合中添加一些元素。
        - public static void shuffle(List<?> list) 打乱顺序:打乱集合顺序。
 */
public class Demo01Collections {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        //往集合中添加多个元素
        /*list.add("a");
        list.add("b");
        list.add("c");
        list.add("d");
        list.add("e");*/

        //public static <T> boolean addAll(Collection<T> c, T... elements):往集合中添加一些元素。
        Collections.addAll(list,"a","b","c","d","e");

        System.out.println(list);//[a, b, c, d, e]

        //public static void shuffle(List<?> list) 打乱顺序:打乱集合顺序。
        Collections.shuffle(list);
        System.out.println(list);//[b, d, c, a, e], [b, d, c, a, e]
    }
}
```

### Demo02Sort  实现Comparable接口,重写compareTo方法 ###

```java
package com.itheima.demo05.Collections;

import java.util.ArrayList;
import java.util.Collections;

/*
    - java.utils.Collections是集合工具类，用来对集合进行操作。部分方法如下：
        public static <T> void sort(List<T> list):将集合中元素按照默认规则排序。

    注意:
         sort(List<T> list)使用前提
         被排序的集合里边存储的元素,必须实现Comparable,重写接口中的方法compareTo定义排序的规则

    Comparable接口的排序规则:
        自己(this)-参数:升序
 */
public class Demo02Sort {
    public static void main(String[] args) {
        ArrayList<Integer> list01 = new ArrayList<>();
        list01.add(1);
        list01.add(3);
        list01.add(2);
        System.out.println(list01);//[1, 3, 2]

        //public static <T> void sort(List<T> list):将集合中元素按照默认规则排序。
        Collections.sort(list01);//默认是升序

        System.out.println(list01);//[1, 2, 3]

        ArrayList<String> list02 = new ArrayList<>();
        list02.add("a");
        list02.add("c");
        list02.add("b");
        System.out.println(list02);//[a, c, b]

        Collections.sort(list02);
        System.out.println(list02);//[a, b, c]

        ArrayList<Person> list03 = new ArrayList<>();
        list03.add(new Person("张三",18));
        list03.add(new Person("李四",20));
        list03.add(new Person("王五",15));
        System.out.println(list03);//[Person{name='张三', age=18}, Person{name='李四', age=20}, Person{name='王五', age=15}]

        Collections.sort(list03);
        System.out.println(list03);
    }
}
package com.itheima.demo05.Collections;

public class Person implements Comparable<Person>{
    private String name;
    private int age;

    public Person() {
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
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

    //重写排序的规则
    @Override
    public int compareTo(Person o) {
        //return 0;//认为元素都是相同的
        //自定义比较的规则,比较两个人的年龄(this,参数Person)
        //return this.getAge() - o.getAge();//年龄升序排序
        return o.getAge() - this.getAge();//年龄升序排序
    }
}
```

### Demo03Sort  重写Comparator比较的规则 匿名内部类 ###

```java
package com.itheima.demo05.Collections;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

/*
    - java.utils.Collections是集合工具类，用来对集合进行操作。部分方法如下：
        public static <T> void sort(List<T> list，Comparator<? super T> ):将集合中元素按照指定规则排序。

     Comparator和Comparable的区别
        Comparable:自己(this)和别人(参数)比较,自己需要实现Comparable接口,重写比较的规则compareTo方法
        Comparator:相当于找一个第三方的裁判,比较两个

    Comparator的排序规则:
        o1-o2:升序
 */
public class Demo03Sort {
    public static void main(String[] args) {
        ArrayList<Integer> list01 = new ArrayList<>();
        list01.add(1);
        list01.add(3);
        list01.add(2);
        System.out.println(list01);//[1, 3, 2]

        Collections.sort(list01, new Comparator<Integer>() {
            //重写比较的规则 匿名内部类
            @Override
            public int compare(Integer o1, Integer o2) {
                //return o1-o2;//升序
                return o2-o1;//降序
            }
        });

        System.out.println(list01);

        ArrayList<Student> list02 = new ArrayList<>();
        list02.add(new Student("a迪丽热巴",18));
        list02.add(new Student("古力娜扎",20));
        list02.add(new Student("杨幂",17));
        list02.add(new Student("b杨幂",18));
        System.out.println(list02);

        /*Collections.sort(list02, new Comparator<Student>() {
            @Override
            public int compare(Student o1, Student o2) {
                //按照年龄升序排序
                return o1.getAge()-o2.getAge();
            }
        });*/

        //扩展:了解
        Collections.sort(list02, new Comparator<Student>() {
            @Override
            public int compare(Student o1, Student o2) {
                //按照年龄升序排序
                int result =  o1.getAge()-o2.getAge();
                //如果两个人年龄相同,再使用姓名的第一个字比较
                if(result==0){
                    result =  o1.getName().charAt(0)-o2.getName().charAt(0);
                }
                return  result;
            }

        });

        System.out.println(list02);
    }
}
```

# day04 【Map】 #

## 第一章 Map集合 ##

### Demo01Map 基操put/get/remove/containsKey ###

```java
package com.itheima.demo01.Map;

import java.util.HashMap;
import java.util.Map;

/*
    java.util.Map<k,v>集合
    Map集合的特点:
        1.Map集合是一个双列集合,一个元素包含两个值(一个key,一个value)
        2.Map集合中的元素,key和value的数据类型可以相同,也可以不同
        3.Map集合中的元素,key是不允许重复的,value是可以重复的
        4.Map集合中的元素,key和value是一一对应
    java.util.HashMap<k,v>集合 implements Map<k,v>接口
    HashMap集合的特点:
        1.HashMap集合底层是哈希表:查询的速度特别的快
            JDK1.8之前:数组+单向链表
            JDK1.8之后:数组+单向链表|红黑树(链表的长度超过8):提高查询的速度
        2.hashMap集合是一个无序的集合,存储元素和取出元素的顺序有可能不一致
   java.util.LinkedHashMap<k,v>集合 extends HashMap<k,v>集合
   LinkedHashMap的特点:
        1.LinkedHashMap集合底层是哈希表+链表(保证迭代的顺序)
        2.LinkedHashMap集合是一个有序的集合,存储元素和取出元素的顺序是一致的
 */
public class Demo01Map {
    public static void main(String[] args) {
        show04();
    }

    /*
        boolean containsKey(Object key) 判断集合中是否包含指定的键。
        包含返回true,不包含返回false
     */
    private static void show04() {
        //创建Map集合对象
        Map<String,Integer> map = new HashMap<>();
        map.put("赵丽颖",168);
        map.put("杨颖",165);
        map.put("林志玲",178);

        boolean b1 = map.containsKey("赵丽颖");
        System.out.println("b1:"+b1);//b1:true
        map.remove("赵丽颖");
        b1 = map.containsKey("赵丽颖");
        System.out.println("b1:"+b1);//b1:false

        boolean b2 = map.containsKey("赵颖");
        System.out.println("b2:"+b2);//b2:false
    }

    /*
        public V get(Object key) 根据指定的键，在Map集合中获取对应的值。
            返回值:
                key存在,返回对应的value值
                key不存在,返回null
     */
    private static void show03() {
        //创建Map集合对象
        Map<String,Integer> map = new HashMap<>();
        map.put("赵丽颖",168);
        map.put("杨颖",165);
        map.put("林志玲",178);

        Integer v1 = map.get("杨颖");
        System.out.println("v1:"+v1);//v1:165

        Integer v2 = map.get("迪丽热巴");
        System.out.println("v2:"+v2);//v2:null
    }

    /*
        public V remove(Object key): 把指定的键 所对应的键值对元素 在Map集合中删除，返回被删除元素的值。
            返回值:V
                key存在,v返回被删除的值
                key不存在,v返回null
     */
    private static void show02() {
        //创建Map集合对象
        Map<String,Integer> map = new HashMap<>();
        map.put("赵丽颖",168);
        map.put("杨颖",165);
        map.put("林志玲",178);
        System.out.println(map);//{林志玲=178, 赵丽颖=168, 杨颖=165}

        Integer v1 = map.remove("林志玲");
        System.out.println("v1:"+v1);//v1:178

        System.out.println(map);//{赵丽颖=168, 杨颖=165}

        //int v2 = map.remove("林志颖");//自动拆箱  NullPointerException
        Integer v2 = map.remove("林志颖");
        System.out.println("v2:"+v2);//v2:null

        System.out.println(map);//{赵丽颖=168, 杨颖=165}
    }

    /*
        public V put(K key, V value):  把指定的键与指定的值添加到Map集合中。
            返回值:v
                存储键值对的时候,key不重复,返回值V是null
                存储键值对的时候,key重复,会使用新的value替换map中重复的value,返回被替换的value值
     */
    private static void show01() {
        //创建Map集合对象,多态
        Map<String,String> map = new HashMap<>();

        String v1 = map.put("李晨", "范冰冰1");
        System.out.println("v1:"+v1);//v1:null

        String v2 = map.put("李晨", "范冰冰2");
        System.out.println("v2:"+v2);//v2:范冰冰1

        System.out.println(map);//{李晨=范冰冰2}

        map.put("冷锋","龙小云");
        map.put("杨过","小龙女");
        map.put("尹志平","小龙女");
        System.out.println(map);//{杨过=小龙女, 尹志平=小龙女, 李晨=范冰冰2, 冷锋=龙小云}
    }
}
```

### Demo02KeySet 遍历map:键找值 ###

```java
package com.itheima.demo01.Map;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

/*
    Map集合的第一种遍历方式:通过键找值的方式
    Map集合中的方法:
         Set<K> keySet() 返回此映射中包含的键的 Set 视图。
    实现步骤:
        1.使用Map集合中的方法keySet(),把Map集合所有的key取出来,存储到一个Set集合中
        2.遍历set集合,获取Map集合中的每一个key
        3.通过Map集合中的方法get(key),通过key找到value
 */
public class Demo02KeySet {
    public static void main(String[] args) {
        //创建Map集合对象
        Map<String,Integer> map = new HashMap<>();
        map.put("赵丽颖",168);
        map.put("杨颖",165);
        map.put("林志玲",178);

        //1.使用Map集合中的方法keySet(),把Map集合所有的key取出来,存储到一个Set集合中
        Set<String> set = map.keySet();

        //2.遍历set集合,获取Map集合中的每一个key
        //使用迭代器遍历Set集合
        Iterator<String> it = set.iterator();
        while (it.hasNext()){
            String key = it.next();
            //3.通过Map集合中的方法get(key),通过key找到value
            Integer value = map.get(key);
            System.out.println(key+"="+value);
        }
        System.out.println("-------------------");
        //使用增强for遍历Set集合
        for(String key : set){
            //3.通过Map集合中的方法get(key),通过key找到value
            Integer value = map.get(key);
            System.out.println(key+"="+value);
        }
        System.out.println("-------------------");
        //使用增强for遍历Set集合
        for(String key : map.keySet()){
            //3.通过Map集合中的方法get(key),通过key找到value
            Integer value = map.get(key);
            System.out.println(key+"="+value);
        }
    }
}
```

### Demo03EntrySet EntrySet遍历map(键值对对象) ###

```java
package com.itheima.demo01.Map;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

/*
    Map集合遍历的第二种方式:使用Entry对象遍历

    Map集合中的方法:
        Set<Map.Entry<K,V>> entrySet() 返回此映射中包含的映射关系的 Set 视图。

    实现步骤:
        1.使用Map集合中的方法entrySet(),把Map集合中多个Entry对象取出来,存储到一个Set集合中
        2.遍历Set集合,获取每一个Entry对象
        3.使用Entry对象中的方法getKey()和getValue()获取键与值
 */
public class Demo03EntrySet {
    public static void main(String[] args) {
        //创建Map集合对象
        Map<String,Integer> map = new HashMap<>();
        map.put("赵丽颖",168);
        map.put("杨颖",165);
        map.put("林志玲",178);

        //1.使用Map集合中的方法entrySet(),把Map集合中多个Entry对象取出来,存储到一个Set集合中
        Set<Map.Entry<String, Integer>> set = map.entrySet();

        //2.遍历Set集合,获取每一个Entry对象
        //使用迭代器遍历Set集合
        Iterator<Map.Entry<String, Integer>> it = set.iterator();
        while(it.hasNext()){
            Map.Entry<String, Integer> entry = it.next();
            //3.使用Entry对象中的方法getKey()和getValue()获取键与值
            String key = entry.getKey();
            Integer value = entry.getValue();
            System.out.println(key+"="+value);
        }
        System.out.println("-----------------------");
        for(Map.Entry<String,Integer> entry:set){
            //3.使用Entry对象中的方法getKey()和getValue()获取键与值
            String key = entry.getKey();
            Integer value = entry.getValue();
            System.out.println(key+"="+value);
        }
    }
}
```

### Demo01HashMapSavePerson 自定义类的hashCode和equals ###

```java
package com.itheima.demo02.Map;

import java.util.Objects;

public class Person {
    private String name;
    private  int age;

    public Person() {
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return age == person.age &&
                Objects.equals(name, person.name);
    }

    @Override
    public int hashCode() {

        return Objects.hash(name, age);
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
}
package com.itheima.demo02.Map;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

/*
    HashMap存储自定义类型键值
    Map集合保证key是唯一的:
        作为key的元素,必须重写hashCode方法和equals方法,以保证key唯一
 */
public class Demo01HashMapSavePerson {
    public static void main(String[] args) {
        show01();
    }

    /*
        HashMap存储自定义类型键值
        key:Person类型
            Person类就必须重写hashCode方法和equals方法,以保证key唯一
        value:String类型
            可以重复
     */
    private static void show02() {
        //创建HashMap集合
        HashMap<Person,String> map = new HashMap<>();
        //往集合中添加元素
        map.put(new Person("女王",18),"英国");
        map.put(new Person("秦始皇",18),"秦国");
        map.put(new Person("普京",30),"俄罗斯");
        map.put(new Person("女王",18),"毛里求斯");
        //使用entrySet和增强for遍历Map集合
        Set<Map.Entry<Person, String>> set = map.entrySet();
        for (Map.Entry<Person, String> entry : set) {
            Person key = entry.getKey();
            String value = entry.getValue();
            System.out.println(key+"-->"+value);
        }
    }

    /*
        HashMap存储自定义类型键值
        key:String类型
            String类重写hashCode方法和equals方法,可以保证key唯一
        value:Person类型
            value可以重复(同名同年龄的人视为同一个)
     */
    private static void show01() {
        //创建HashMap集合
        HashMap<String,Person> map = new HashMap<>();
        //往集合中添加元素
        map.put("北京",new Person("张三",18));
        map.put("上海",new Person("李四",19));
        map.put("广州",new Person("王五",20));
        map.put("北京",new Person("赵六",18));
        //使用keySet加增强for遍历Map集合
        Set<String> set = map.keySet();
        for (String key : set) {
            Person value = map.get(key);
            System.out.println(key+"-->"+value);
        }
    }
}
```

### Demo01LinkedHashMap ###

```java
package com.itheima.demo03.Map;

import java.util.HashMap;
import java.util.LinkedHashMap;

/*
    java.util.LinkedHashMap<K,V> entends HashMap<K,V>
    Map 接口的哈希表和链接列表实现，具有可预知的迭代顺序。
    底层原理:
        哈希表+链表(记录元素的顺序)
 */
public class Demo01LinkedHashMap {
    public static void main(String[] args) {
        HashMap<String,String> map = new HashMap<>();
        map.put("a","a");
        map.put("c","c");
        map.put("b","b");
        map.put("a","d");
        System.out.println(map);// key不允许重复,无序 {a=d, b=b, c=c}

        LinkedHashMap<String,String> linked = new LinkedHashMap<>();
        linked.put("a","a");
        linked.put("c","c");
        linked.put("b","b");
        linked.put("a","d");
        System.out.println(linked);// key不允许重复,有序 {a=d, c=c, b=b}
    }
}

```

### Demo02Hashtable ###

```java
package com.itheima.demo03.Map;

import java.util.HashMap;
import java.util.Hashtable;

/*
    java.util.Hashtable<K,V>集合 implements Map<K,V>接口

    Hashtable:底层也是一个哈希表,是一个线程安全的集合,是单线程集合,速度慢
    HashMap:底层是一个哈希表,是一个线程不安全的集合,是多线程的集合,速度快

    HashMap集合(之前学的所有的集合):可以存储null值,null键
    Hashtable集合,不能存储null值,null键

    Hashtable和Vector集合一样,在jdk1.2版本之后被更先进的集合(HashMap,ArrayList)取代了
    Hashtable的子类Properties依然活跃在历史舞台
    Properties集合是一个唯一和IO流相结合的集合
 */
public class Demo02Hashtable {
    public static void main(String[] args) {
        HashMap<String,String> map = new HashMap<>();
        map.put(null,"a");
        map.put("b",null);
        map.put(null,null);
        System.out.println(map);//{null=null, b=null}

        Hashtable<String,String> table = new Hashtable<>();
        //table.put(null,"a");//NullPointerException
        //table.put("b",null);//NullPointerException
        table.put(null,null);//NullPointerException
    }
}

```

### Demo03MapTest 对字符串counter ###

```java
package com.itheima.demo03.Map;

import java.util.HashMap;
import java.util.Scanner;

/*
    练习:
        计算一个字符串中每个字符出现次数

    分析:
        1.使用Scanner获取用户输入的字符串
        2.创建Map集合,key是字符串中的字符,value是字符的个数
        3.遍历字符串,获取每一个字符
        4.使用获取到的字符,去Map集合判断key是否存在
            key存在:
                通过字符(key),获取value(字符个数)
                value++
                put(key,value)把新的value存储到Map集合中
            key不存在:
                put(key,1)
        5.遍历Map集合,输出结果
 */
public class Demo03MapTest {
    public static void main(String[] args) {
        //1.使用Scanner获取用户输入的字符串
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入一个字符串:");
        String str = sc.next();
        //2.创建Map集合,key是字符串中的字符,value是字符的个数
        HashMap<Character,Integer> map = new HashMap<>();
        //3.遍历字符串,获取每一个字符
        for(char c :str.toCharArray()){
            //4.使用获取到的字符,去Map集合判断key是否存在
            if(map.containsKey(c)){
                //key存在
                Integer value = map.get(c);
                value++;
                map.put(c,value);
            }else{
                //key不存在
                map.put(c,1);
            }
        }
        //5.遍历Map集合,输出结果
        for(Character key :map.keySet()){
            Integer value = map.get(key);
            System.out.println(key+"="+value);
        }
    }
}
```

### Demo01JDK9 静态的方法of,返回值不能改变 ###

```java
package com.itheima.demo04.JDK9;

import java.util.List;
import java.util.Map;
import java.util.Set;

/*
    JDK9的新特性:
        List接口,Set接口,Map接口:里边增加了一个静态的方法of,可以给集合一次性添加多个元素
        static <E> List<E> of​(E... elements)
        使用前提:
            当集合中存储的元素的个数已经确定了,不在改变时使用
     注意:
        1.of方法只适用于List接口,Set接口,Map接口,不适用于接接口的实现类
        2.of方法的返回值是一个不能改变的集合,集合不能再使用add,put方法添加元素,会抛出异常
        3.Set接口和Map接口在调用of方法的时候,不能有重复的元素,否则会抛出异常
 */
public class Demo01JDK9 {
    public static void main(String[] args) {
        List<String> list = List.of("a", "b", "a", "c", "d");
        System.out.println(list);//[a, b, a, c, d]
        //list.add("w");//UnsupportedOperationException:不支持操作异常

        //Set<String> set = Set.of("a", "b", "a", "c", "d");//IllegalArgumentException:非法参数异常,有重复的元素
        Set<String> set = Set.of("a", "b", "c", "d");
        System.out.println(set);
        //set.add("w");//UnsupportedOperationException:不支持操作异常

        //Map<String, Integer> map = Map.of("张三", 18, "李四", 19, "王五", 20,"张三",19);////IllegalArgumentException:非法参数异常,有重复的元素
        Map<String, Integer> map = Map.of("张三", 18, "李四", 19, "王五", 20);
        System.out.println(map);//{王五=20, 李四=19, 张三=18}
        //map.put("赵四",30);//UnsupportedOperationException:不支持操作异常
    }
}
```

## 第二章-综合案例 ##

### 斗地主 ###

```java
package com.itheima.demo06.Test;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

/*
    斗地主综合案例:有序版本
    1.准备牌
    2.洗牌
    3.发牌
    4.排序
    5.看牌
 */
public class DouDiZhu {
    public static void main(String[] args) {
        //1.准备牌
        //创建一个Map集合,存储牌的索引和组装好的牌
        HashMap<Integer,String> poker = new HashMap<>();
        //创建一个List集合,存储牌的索引
        ArrayList<Integer> pokerIndex = new ArrayList<>();
        //定义两个集合,存储花色和牌的序号
        List<String> colors = List.of("♠", "♥", "♣", "♦");
        List<String> numbers = List.of("2", "A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3");
        //把大王和小王存储到集合中
        //定义一个牌的索引
        int index = 0;
        poker.put(index,"大王");
        pokerIndex.add(index);
        index++;
        poker.put(index,"小王");
        pokerIndex.add(index);
        index++;
        //循环嵌套遍历两个集合,组装52张牌,存储到集合中
        for (String number : numbers) {
            for (String color : colors) {
                poker.put(index,color+number);
                pokerIndex.add(index);
                index++;
            }
        }
        //System.out.println(poker);
        //System.out.println(pokerIndex);

        /*
            2.洗牌
            使用Collections中的方法shuffle(List)
         */
        Collections.shuffle(pokerIndex);
        //System.out.println(pokerIndex);

        /*
            3.发牌
         */
        //定义4个集合,存储玩家牌的索引,和底牌的索引
        ArrayList<Integer> player01 = new ArrayList<>();
        ArrayList<Integer> player02 = new ArrayList<>();
        ArrayList<Integer> player03 = new ArrayList<>();
        ArrayList<Integer> diPai = new ArrayList<>();
        //遍历存储牌索引的List集合,获取每一个牌的索引
        for (int i = 0; i <pokerIndex.size() ; i++) {
            Integer in = pokerIndex.get(i);
            //先判断底牌
            if(i>=51){
                //给底牌发牌
                diPai.add(in);
            }else if(i%3==0){
                //给玩家1发牌
                player01.add(in);
            }else if(i%3==1){
                //给玩家2发牌
                player02.add(in);
            }else if(i%3==2){
                //给玩家3发牌
                player03.add(in);
            }
        }

        /*
            4.排序
            使用Collections中的方法sort(List)
            默认是升序排序
         */
        Collections.sort(player01);
        Collections.sort(player02);
        Collections.sort(player03);
        Collections.sort(diPai);

        /*
            5.看牌
            调用看牌的方法
         */
        lookPoker("刘德华",poker,player01);
        lookPoker("周润发",poker,player02);
        lookPoker("周星驰",poker,player03);
        lookPoker("底牌",poker,diPai);
    }

    /*
        定义一个看牌的方法,提高代码的复用性
        参数:
            String name:玩家名称
            HashMap<Integer,String> poker:存储牌的poker集合
            ArrayList<Integer> list:存储玩家和底牌的List集合
        查表法:
             遍历玩家或者底牌集合,获取牌的索引
             使用牌的索引,去Map集合中,找到对应的牌
     */
    public static void lookPoker(String name,HashMap<Integer,String> poker,ArrayList<Integer> list){
        //输出玩家名称,不换行
        System.out.print(name+":");
        //遍历玩家或者底牌集合,获取牌的索引
        for (Integer key : list) {
            //使用牌的索引,去Map集合中,找到对应的牌
            String value = poker.get(key);
            System.out.print(value+" ");
        }
        System.out.println();//打印完每一个玩家的牌,换行
    }

}
```

# day05 【异常、线程】-笔记 #

## 第一章    异常 ##

### Demo01Exception ###

```java
package com.itheima.demo01.Exception;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

/*
    java.lang.Throwable:类是 Java 语言中所有错误或异常的超类。
        Exception:编译期异常,进行编译(写代码)java程序出现的问题
            RuntimeException:运行期异常,java程序运行过程中出现的问题
            异常就相当于程序得了一个小毛病(感冒,发烧),把异常处理掉,程序可以继续执行(吃点药,继续革命工作)
        Error:错误
            错误就相当于程序得了一个无法治愈的毛病(非典,艾滋).必须修改源代码,程序才能继续执行
 */
public class Demo01Exception {
    public static void main(String[] args) /*throws ParseException*/ {
        //Exception:编译期异常,进行编译(写代码)java程序出现的问题
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");//用来格式化日期
        Date date = null;
        try {
            date = sdf.parse("1999-0909");//把字符串格式的日期,解析为Date格式的日期
        } catch (ParseException e) {
            e.printStackTrace();
        }
        System.out.println(date);

        //RuntimeException:运行期异常,java程序运行过程中出现的问题
        int[] arr = {1,2,3};
        System.out.println(arr[0]);
        try {
            //可能会出现异常的代码
            System.out.println(arr[3]);
        }catch(Exception e){
            //异常的处理逻辑
            System.out.println(e);
        }

        /*
            Error:错误
            OutOfMemoryError: Java heap space
            内存溢出的错误,创建的数组太大了,超出了给JVM分配的内存
         */
        int[] arr = new int[1024*1024*1024];
        //必须修改代码,创建的数组小一点
        int[] arr = new int[1024*1024];
        System.out.println("后续代码");
    }
}
```

## 第二章 异常的处理 ##

### Demo03Throw throw关键字 ###

```java
package com.itheima.demo01.Exception;
/*
    throw关键字
    作用:
        可以使用throw关键字在指定的方法中抛出指定的异常
    使用格式:
        throw new xxxException("异常产生的原因");
    注意:
        1.throw关键字必须写在方法的内部
        2.throw关键字后边new的对象必须是Exception或者Exception的子类对象
        3.throw关键字抛出指定的异常对象,我们就必须处理这个异常对象
            throw关键字后边创建的是RuntimeException或者是 RuntimeException的子类对象,我们可以不处理,默认交给JVM处理(打印异常对象,中断程序)
            throw关键字后边创建的是编译异常(写代码的时候报错),我们就必须处理这个异常,要么throws,要么try...catch
 */
public class Demo03Throw {
    public static void main(String[] args) {
        //int[] arr = null;
        int[] arr = new int[3];
        int e = getElement(arr,3);
        System.out.println(e);
    }
    /*
        定义一个方法,获取数组指定索引处的元素
        参数:
            int[] arr
            int index
        以后(工作中)我们首先必须对方法传递过来的参数进行合法性校验
        如果参数不合法,那么我们就必须使用抛出异常的方式,告知方法的调用者,传递的参数有问题
        注意:
            NullPointerException是一个运行期异常,我们不用处理,默认交给JVM处理
            ArrayIndexOutOfBoundsException是一个运行期异常,我们不用处理,默认交给JVM处理
     */
    public static int getElement(int[] arr,int index){
        /*
            我们可以对传递过来的参数数组,进行合法性校验
            如果数组arr的值是null
            那么我们就抛出空指针异常,告知方法的调用者"传递的数组的值是null"
         */
        if(arr == null){
            throw new NullPointerException("传递的数组的值是null");
        }

        /*
            我们可以对传递过来的参数index进行合法性校验
            如果index的范围不在数组的索引范围内
            那么我们就抛出数组索引越界异常,告知方法的调用者"传递的索引超出了数组的使用范围"
         */
        if(index<0 || index>arr.length-1){
            throw new ArrayIndexOutOfBoundsException("传递的索引超出了数组的使用范围");
        }

        in ele = arr[index];
        return ele;
    }
}
```

### Demo04Objects Objects.requireNonNull非空判断 ###

```java
package com.itheima.demo01.Exception;

import java.util.Objects;

/*
    Obects类中的静态方法
    public static <T> T requireNonNull(T obj):查看指定引用对象不是null。
    源码:
        public static <T> T requireNonNull(T obj) {
            if (obj == null)
                throw new NullPointerException();
            return obj;
        }
 */
public class Demo04Objects {
    public static void main(String[] args) {
        method(null);
    }

    public static void method(Object obj){
        //对传递过来的参数进行合法性判断,判断是否为null
        /*if(obj == null){
            throw new NullPointerException("传递的对象的值是null");
        }*/

        //Objects.requireNonNull(obj);
        Objects.requireNonNull(obj,"传递的对象的值是null");
    }
}
```

### Demo05Throws  声明异常throws关键字 ###

```java
package com.itheima.demo01.Exception;

import java.io.FileNotFoundException;
import java.io.IOException;

/*
    throws关键字:异常处理的第一种方式,交给别人处理
    作用:
        当方法内部抛出异常对象的时候,那么我们就必须处理这个异常对象
        可以使用throws关键字处理异常对象,会把异常对象声明抛出给方法的调用者处理(自己不处理,给别人处理),最终交给JVM处理-->中断处理
    使用格式:在方法声明时使用
        修饰符 返回值类型 方法名(参数列表) throws AAAExcepiton,BBBExcepiton...{
            throw new AAAExcepiton("产生原因");
            throw new BBBExcepiton("产生原因");
            ...
        }
     注意:
        1.throws关键字必须写在方法声明处
        2.throws关键字后边声明的异常必须是Exception或者是Exception的子类
        3.方法内部如果抛出了多个异常对象,那么throws后边必须也声明多个异常
            如果抛出的多个异常对象有子父类关系,那么直接声明父类异常即可
        4.调用了一个声明抛出异常的方法,我们就必须的处理声明的异常
            要么继续使用throws声明抛出,交给方法的调用者处理,最终交给JVM
            要么try...catch自己处理异常
 */
public class Demo05Throws {
    /*
        FileNotFoundException extends IOException extends Excepiton
        如果抛出的多个异常对象有子父类关系,那么直接声明父类异常即可
     */
    //public static void main(String[] args) throws FileNotFoundException,IOException {
    //public static void main(String[] args) throws IOException {
    public static void main(String[] args) throws Exception {
        readFile("c:\\a.tx");

        System.out.println("后续代码");
    }

    /*
        定义一个方法,对传递的文件路径进行合法性判断
        如果路径不是"c:\\a.txt",那么我们就抛出文件找不到异常对象,告知方法的调用者
        注意:
            FileNotFoundException是编译异常,抛出了编译异常,就必须处理这个异常
            可以使用throws继续声明抛出FileNotFoundException这个异常对象,让方法的调用者处理
     */
    public static void readFile(String fileName) throws FileNotFoundException,IOException{
        if(!fileName.equals("c:\\a.txt")){
            throw new FileNotFoundException("传递的文件路径不是c:\\a.txt");
        }

        /*
            如果传递的路径,不是.txt结尾
            那么我们就抛出IO异常对象,告知方法的调用者,文件的后缀名不对

         */
        if(!fileName.endsWith(".txt")){
            throw new IOException("文件的后缀名不对");
        }

        System.out.println("路径没有问题,读取文件");
    }
}
```

### Demo01 TryCatch关键字 ###

```java
package com.itheima.demo02.Exception;

import java.io.IOException;

/*
    try...catch:异常处理的第二种方式,自己处理异常
    格式:
        try{
            可能产生异常的代码
        }catch(定义一个异常的变量,用来接收try中抛出的异常对象){
            异常的处理逻辑,异常异常对象之后,怎么处理异常对象
            一般在工作中,会把异常的信息记录到一个日志中
        }
        ...
        catch(异常类名 变量名){

        }
    注意:
        1.try中可能会抛出多个异常对象,那么就可以使用多个catch来处理这些异常对象
        2.如果try中产生了异常,那么就会执行catch中的异常处理逻辑,执行完毕catch中的处理逻辑,继续执行try...catch之后的代码
          如果try中没有产生异常,那么就不会执行catch中异常的处理逻辑,执行完try中的代码,继续执行try...catch之后的代码
 */
public class Demo01TryCatch {
    public static void main(String[] args) {
        try{
            //可能产生异常的代码
            readFile("d:\\a.tx");
            System.out.println("资源释放");
        }catch (IOException e){//try中抛出什么异常对象,catch就定义什么异常变量,用来接收这个异常对象
            //异常的处理逻辑,异常异常对象之后,怎么处理异常对象
            //System.out.println("catch - 传递的文件后缀不是.txt");

            /*
                Throwable类中定义了3个异常处理的方法
                 String getMessage() 返回此 throwable 的简短描述。
                 String toString() 返回此 throwable 的详细消息字符串。
                 void printStackTrace()  JVM打印异常对象,默认此方法,打印的异常信息是最全面的
             */
//            System.out.println(e.getMessage());//文件的后缀名不对
//            System.out.println(e.toString());//重写Object类的toString java.io.IOException: 文件的后缀名不对
//            System.out.println(e);//java.io.IOException: 文件的后缀名不对

            /*
                java.io.IOException: 文件的后缀名不对
                    at com.itheima.demo02.Exception.Demo01TryCatch.readFile(Demo01TryCatch.java:55)
                    at com.itheima.demo02.Exception.Demo01TryCatch.main(Demo01TryCatch.java:27)
             */
            e.printStackTrace();
        }
        System.out.println("后续代码");
    }

    /*
       如果传递的路径,不是.txt结尾
       那么我们就抛出IO异常对象,告知方法的调用者,文件的后缀名不对

    */
    public static void readFile(String fileName) throws IOException {

        if(!fileName.endsWith(".txt")){
            throw new IOException("文件的后缀名不对");
        }

        System.out.println("路径没有问题,读取文件");
    }
}

```

### Demo02 Finally关键字 ###

```java
package com.itheima.demo02.Exception;

import java.io.IOException;
import java.text.ParseException;

/*
    finally代码块
     格式:
        try{
            可能产生异常的代码
        }catch(定义一个异常的变量,用来接收try中抛出的异常对象){
            异常的处理逻辑,异常异常对象之后,怎么处理异常对象
            一般在工作中,会把异常的信息记录到一个日志中
        }
        ...
        catch(异常类名 变量名){

        }finally{
            无论是否出现异常都会执行
        }
     注意:
        1.finally不能单独使用,必须和try一起使用
        2.finally一般用于资源释放(资源回收),无论程序是否出现异常,最后都要资源释放(IO)
 */
public class Demo02TryCatchFinally {
    public static void main(String[] args) {
        try {
            //可能会产生异常的代码
            readFile("c:\\a.tx");
        } catch (IOException e) {
            //异常的处理逻辑
            e.printStackTrace();
        } finally {
            //无论是否出现异常,都会执行
            System.out.println("资源释放");
        }
    }

    /*
       如果传递的路径,不是.txt结尾
       那么我们就抛出IO异常对象,告知方法的调用者,文件的后缀名不对

    */
    public static void readFile(String fileName) throws IOException {

        if(!fileName.endsWith(".txt")){
            throw new IOException("文件的后缀名不对");
        }

        System.out.println("路径没有问题,读取文件");
    }
}
```

### Demo01 多个异常使用捕获 ###

```java
package com.itheima.demo03.Exception;

import java.util.List;

/*
    异常的注意事项
 */
public class Demo01Exception {
    public static void main(String[] args) {
        /*
            多个异常使用捕获又该如何处理呢？
            1. 多个异常分别处理。
            2. 多个异常一次捕获，多次处理。
            3. 多个异常一次捕获一次处理。
         */

        //1. 多个异常分别处理。
       /* try {
            int[] arr = {1,2,3};
            System.out.println(arr[3]);//ArrayIndexOutOfBoundsException: 3
        }catch (ArrayIndexOutOfBoundsException e){
            System.out.println(e);
        }

        try{
            List<Integer> list = List.of(1, 2, 3);
            System.out.println(list.get(3));//IndexOutOfBoundsException: Index 3 out-of-bounds for length 3
        }catch (IndexOutOfBoundsException e){
            System.out.println(e);
        }*/

        //2. 多个异常一次捕获，多次处理。
        /*try {
            int[] arr = {1,2,3};
            //System.out.println(arr[3]);//ArrayIndexOutOfBoundsException: 3
            List<Integer> list = List.of(1, 2, 3);
            System.out.println(list.get(3));//IndexOutOfBoundsException: Index 3 out-of-bounds for length 3
        }catch (ArrayIndexOutOfBoundsException e){
            System.out.println(e);
        }catch (IndexOutOfBoundsException e){
            System.out.println(e);
        }*/

        /*
            一个try多个catch注意事项:
                catch里边定义的异常变量,如果有子父类关系,那么子类的异常变量必须写在上边,否则就会报错
                ArrayIndexOutOfBoundsException extends IndexOutOfBoundsException

        //3. 多个异常一次捕获一次处理。
        /*try {
            int[] arr = {1,2,3};
            //System.out.println(arr[3]);//ArrayIndexOutOfBoundsException: 3
            List<Integer> list = List.of(1, 2, 3);
            System.out.println(list.get(3));//IndexOutOfBoundsException: Index 3 out-of-bounds for length 3
        }catch (Exception e){
            System.out.println(e);
        }*/

        //运行时异常被抛出可以不处理。即不捕获也不声明抛出。
        //默认给虚拟机处理,终止程序,什么时候不抛出运行时异常了,在来继续执行程序
        int[] arr = {1,2,3};
        System.out.println(arr[3]);//ArrayIndexOutOfBoundsException: 3
        List<Integer> list = List.of(1, 2, 3);
        System.out.println(list.get(3));//IndexOutOfBoundsException: Index 3 out-of-bounds for length 3

        System.out.println("后续代码!");
    }
}
```

### Demo02 finally中避免return语句 ###

```java
package com.itheima.demo03.Exception;
/*
    如果finally有return语句,永远返回finally中的结果,避免该情况.
 */
public class Demo02Exception {
    public static void main(String[] args) {
        int a = getA();
        System.out.println(a);
    }

    //定义一个方法,返回变量a的值
    public static int getA(){
        int a = 10;
        try{
            return a;
        }catch (Exception e){
            System.out.println(e);
        }finally {
            //一定会执行的代码
            a = 100;
            return a;
        }

    }
}
```

### 子父类的异常 ###

```java
package com.itheima.demo03.Exception;
/*
    子父类的异常:
        - 如果父类抛出了多个异常,子类重写父类方法时,抛出和父类相同的异常或者是父类异常的子类或者不抛出异常。
        - 父类方法没有抛出异常，子类重写父类该方法时也不可抛出异常。此时子类产生该异常，只能捕获处理，不能声明抛出
    注意:
        父类异常时什么样,子类异常就什么样
 */
public class Fu {
    public void show01() throws NullPointerException,ClassCastException{}
    public void show02() throws IndexOutOfBoundsException{}
    public void show03() throws IndexOutOfBoundsException{}
    public void show04() {}
}

class Zi extends Fu{
    //子类重写父类方法时,抛出和父类相同的异常
    public void show01() throws NullPointerException,ClassCastException{}
    //子类重写父类方法时,抛出父类异常的子类
    public void show02() throws ArrayIndexOutOfBoundsException{}
    //子类重写父类方法时,不抛出异常
    public void show03() {}

    /*
        父类方法没有抛出异常，子类重写父类该方法时也不可抛出异常。

     */
    //public void show04() throws Exception{}

    //此时子类产生该异常，只能捕获处理，不能声明抛出
    public void show04()  {
        try {
            throw  new Exception("编译期异常");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

## 第三章 自定义异常 ##

### 编译期异常(try-catch) 和 运行期异常(无需处理) ###

```java
package com.itheima.demo04.MyException;
/*
    自定义异常类:
        java提供的异常类,不够我们使用,需要自己定义一些异常类
    格式:
        public class XXXExcepiton extends Exception | RuntimeException{
            添加一个空参数的构造方法
            添加一个带异常信息的构造方法
        }
     注意:
        1.自定义异常类一般都是以Exception结尾,说明该类是一个异常类
        2.自定义异常类,必须的继承Exception或者RuntimeException
            继承Exception:那么自定义的异常类就是一个编译期异常,如果方法内部抛出了编译期异常,就必须处理这个异常,要么throws,要么try...catch
            继承RuntimeException:那么自定义的异常类就是一个运行期异常,无需处理,交给虚拟机处理(中断处理)
 */
public class RegisterException extends /*Exception*/ RuntimeException{
    //添加一个空参数的构造方法
    public RegisterException(){
        super();
    }

    /*
        添加一个带异常信息的构造方法
        查看源码发现,所有的异常类都会有一个带异常信息的构造方法,方法内部会调用父类带异常信息的构造方法,让父类来处理这个异常信息
     */
    public RegisterException(String message){
        super(message);
    }
}
package com.itheima.demo04.MyException;

import java.util.Scanner;

/*
    要求：我们模拟注册操作，如果用户名已存在，则抛出异常并提示：亲，该用户名已经被注册。

    分析:
        1.使用数组保存已经注册过的用户名(数据库)
        2.使用Scanner获取用户输入的注册的用户名(前端,页面)
        3.定义一个方法,对用户输入的中注册的用户名进行判断
            遍历存储已经注册过用户名的数组,获取每一个用户名
            使用获取到的用户名和用户输入的用户名比较
                true:
                    用户名已经存在,抛出RegisterException异常,告知用户"亲，该用户名已经被注册";
                false:
                    继续遍历比较
            如果循环结束了,还没有找到重复的用户名,提示用户"恭喜您,注册成功!";
 */
public class Demo01RegisterException {
    // 1.使用数组保存已经注册过的用户名(数据库)
    static String[] usernames = {"张三","李四","王五"};

    public static void main(String[] args) /*throws RegisterException*/ {
        //2.使用Scanner获取用户输入的注册的用户名(前端,页面)
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入您要注册的用户名:");
        String username = sc.next();
        checkUsername(username);

    }

    //3.定义一个方法,对用户输入的中注册的用户名进行判断
    public static void checkUsername(String username) /*throws RegisterException*/ {
        //遍历存储已经注册过用户名的数组,获取每一个用户名
        for (String name : usernames) {
            //使用获取到的用户名和用户输入的用户名比较
            if(name.equals(username)){
                //true:用户名已经存在,抛出RegisterException异常,告知用户"亲，该用户名已经被注册";
                try {
                    throw new RegisterException("亲，该用户名已经被注册");
                } catch (RegisterException e) {
                    e.printStackTrace();
                    return; //结束方法
                }
            }
        }

        //如果循环结束了,还没有找到重复的用户名,提示用户"恭喜您,注册成功!";
        System.out.println("恭喜您,注册成功!");
    }
}


package com.itheima.demo04.MyException;

import java.util.Scanner;

public class Demo02RegisterException {
    // 1.使用数组保存已经注册过的用户名(数据库)
    static String[] usernames = {"张三","李四","王五"};

    public static void main(String[] args) {
        //2.使用Scanner获取用户输入的注册的用户名(前端,页面)
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入您要注册的用户名:");
        String username = sc.next();
        checkUsername(username);

    }

    //3.定义一个方法,对用户输入的中注册的用户名进行判断
    public static void checkUsername(String username)  {
        //遍历存储已经注册过用户名的数组,获取每一个用户名
        for (String name : usernames) {
            //使用获取到的用户名和用户输入的用户名比较
            if(name.equals(username)){
                //true:用户名已经存在,抛出RegisterException异常,告知用户"亲，该用户名已经被注册";
                throw new RegisterException("亲，该用户名已经被注册");//抛出运行期异常,无需处理,交给JVM处理,中断处理
            }
        }

        //如果循环结束了,还没有找到重复的用户名,提示用户"恭喜您,注册成功!";
        System.out.println("恭喜您,注册成功!");
    }
}
```

## 第四章 多线程 ##

### Demo01MainThread 主线程 ###

```java
package com.itheima.demo05.Thread;
/*
    主线程:执行主(main)方法的线程

    单线程程序:java程序中只有一个线程
    执行从main方法开始,从上到下依次执行

    JVM执行main方法,main方法会进入到栈内存
    JVM会找操作系统开辟一条main方法通向cpu的执行路径
    cpu就可以通过这个路径来执行main方法
    而这个路径有一个名字,叫main(主)线程
 */
public class Demo01MainThread {
    public static void main(String[] args) {
        Person p1 = new Person("小强");
        p1.run();
        System.out.println(0/0);
        //Exception in thread "main" java.lang.ArithmeticException: / by zero
        Person p2 = new Person("旺财");//主线程中断后的剩余语句无法执行
        p2.run();
    }
}

```

### Demo01Thread 多线程的随机执行结果 ###

```java
package com.itheima.demo06.Thread;
//1.创建一个Thread类的子类
public class MyThread extends Thread{
    //2.在Thread类的子类中重写Thread类中的run方法,设置线程任务(开启线程要做什么?)
    @Override
    public void run() {
        for (int i = 0; i <20 ; i++) {
            System.out.println("run:"+i);
        }
    }
}
package com.itheima.demo06.Thread;
/*
    创建多线程程序的第一种方式:创建Thread类的子类
    java.lang.Thread类:是描述线程的类,我们想要实现多线程程序,就必须继承Thread类

    实现步骤:
        1.创建一个Thread类的子类
        2.在Thread类的子类中重写Thread类中的run方法,设置线程任务(开启线程要做什么?)
        3.创建Thread类的子类对象
        4.调用Thread类中的方法start方法,开启新的线程,执行run方法
             void start() 使该线程开始执行；Java 虚拟机调用该线程的 run 方法。
             结果是两个线程并发地运行；当前线程（main线程）和另一个线程（创建的新线程,执行其 run 方法）。
             多次启动一个线程是非法的。特别是当线程已经结束执行后，不能再重新启动。
    java程序属于抢占式调度,那个线程的优先级高,那个线程优先执行;同一个优先级,随机选择一个执行
 */
public class Demo01Thread {
    public static void main(String[] args) {
        //3.创建Thread类的子类对象
        MyThread mt = new MyThread();
        //4.调用Thread类中的方法start方法,开启新的线程,执行run方法
        mt.start();

        for (int i = 0; i <20 ; i++) {
            System.out.println("main:"+i);
        }
    }
}
```

# day06 【线程、同步】-笔记 #

## 第一章 线程 ##

### Demo01GetThreadName 获取当前线程名称 ###

```java
package com.itheima.demo01.getName;
/*
    获取线程的名称:
        1.使用Thread类中的方法getName()
            String getName() 返回该线程的名称。
        2.可以先获取到当前正在执行的线程,使用线程中的方法getName()获取线程的名称
            static Thread currentThread() 返回对当前正在执行的线程对象的引用。
 */
// 定义一个Thread类的子类
public class MyThread extends Thread{
    //重写Thread类中的run方法,设置线程任务
    @Override
    public void run() {
        //获取线程名称
        //String name = getName();
        //System.out.println(name);

        //Thread t = Thread.currentThread();
        //System.out.println(t);//Thread[Thread-0,5,main]
        //String name = t.getName();
        //System.out.println(name);

        //链式编程
        System.out.println(Thread.currentThread().getName());
    }
}
package com.itheima.demo01.getName;
/*
    线程的名称:
        主线程: main
        新线程: Thread-0,Thread-1,Thread-2
 */
public class Demo01GetThreadName {
    public static void main(String[] args) {
        //创建Thread类的子类对象
        MyThread mt = new MyThread();
        //调用start方法,开启新线程,执行run方法
        mt.start();

        new MyThread().start();
        new MyThread().start();

        //链式编程
        System.out.println(Thread.currentThread().getName());
    }
}
```

### Demo01SetThreadName 设置线程名称 ###

```java
package com.itheima.demo02.setName;
/*
    设置线程的名称:(了解)
        1.使用Thread类中的方法setName(名字)
            void setName(String name) 改变线程名称，使之与参数 name 相同。
        2.创建一个带参数的构造方法,参数传递线程的名称;调用父类的带参构造方法,把线程名称传递给父类,让父类(Thread)给子线程起一个名字
            Thread(String name) 分配新的 Thread 对象。
 */
public class MyThread extends Thread{

    public MyThread(){}

    public MyThread(String name){
        super(name);//把线程名称传递给父类,让父类(Thread)给子线程起一个名字
    }

    @Override
    public void run() {
        //获取线程的名称
        System.out.println(Thread.currentThread().getName());
    }
}
package com.itheima.demo02.setName;

public class Demo01SetThreadName {
    public static void main(String[] args) {
        //开启多线程
        MyThread mt = new MyThread();
        mt.setName("小强");
        mt.start();

        //开启多线程
        new MyThread("旺财").start();
    }
}
```

### Demo01Sleep 线程暂时休眠 ###

```java
package com.itheima.demo03.sleep;
/*
    public static void sleep(long millis):使当前正在执行的线程以指定的毫秒数暂停（暂时停止执行）。
    毫秒数结束之后,线程继续执行
 */
public class Demo01Sleep {
    public static void main(String[] args) {
        //模拟秒表
        for (int i = 1; i <=60 ; i++) {
            System.out.println(i);

            //使用Thread类的sleep方法让程序睡眠1秒钟
            try {
                Thread.sleep(1000);//sleep方法本身是有异常的，需要throws/ try-catch
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

### Demo01 Runnable接口创建多线程 ###

```java
package com.itheima.demo04.Runnable;
//1.创建一个Runnable接口的实现类
public class RunnableImpl implements Runnable{
    //2.在实现类中重写Runnable接口的run方法,设置线程任务
    @Override
    public void run() {
        for (int i = 0; i <20 ; i++) {
            System.out.println(Thread.currentThread().getName()+"-->"+i);
        }
    }
}
package com.itheima.demo04.Runnable;
//1.创建一个Runnable接口的实现类
public class RunnableImpl2 implements Runnable{
    //2.在实现类中重写Runnable接口的run方法,设置线程任务
    @Override
    public void run() {
        for (int i = 0; i <20 ; i++) {
            System.out.println("HelloWorld"+i);
        }
    }
}
package com.itheima.demo04.Runnable;
/*
    创建多线程程序的第二种方式:实现Runnable接口
    java.lang.Runnable
        Runnable 接口应该由那些打算通过某一线程执行其实例的类来实现。类必须定义一个称为 run 的无参数方法。
    java.lang.Thread类的构造方法
        Thread(Runnable target) 分配新的 Thread 对象。
        Thread(Runnable target, String name) 分配新的 Thread 对象。

    实现步骤:
        1.创建一个Runnable接口的实现类
        2.在实现类中重写Runnable接口的run方法,设置线程任务
        3.创建一个Runnable接口的实现类对象
        4.创建Thread类对象,构造方法中传递Runnable接口的实现类对象
        5.调用Thread类中的start方法,开启新的线程执行run方法

    实现Runnable接口创建多线程程序的好处:
        1.避免了单继承的局限性
            一个类只能继承一个类(一个人只能有一个亲爹),类继承了Thread类就不能继承其他的类
            实现了Runnable接口,还可以继承其他的类,实现其他的接口
        2.增强了程序的扩展性,降低了程序的耦合性(解耦)
            实现Runnable接口的方式,把设置线程任务和开启新线程进行了分离(解耦)run1/run2
            实现类中,重写了run方法:用来设置线程任务
            创建Thread类对象,调用start方法:用来开启新线程
 */
public class Demo01Runnable {
    public static void main(String[] args) {
        //3.创建一个Runnable接口的实现类对象
        RunnableImpl run = new RunnableImpl();
        //4.创建Thread类对象,构造方法中传递Runnable接口的实现类对象
        //Thread t = new Thread(run);//打印线程名称
        Thread t = new Thread(new RunnableImpl2());//打印HelloWorld
        //5.调用Thread类中的start方法,开启新的线程执行run方法
        t.start();

        for (int i = 0; i <20 ; i++) {
            System.out.println(Thread.currentThread().getName()+"-->"+i);
        }
    }
}
```

### Demo01InnerClassThread 匿名内部类方式实现线程 ###

```java
package com.itheima.demo05.InnerClassThread;
/*
    匿名内部类方式实现线程的创建

    匿名:没有名字
    内部类:写在其他类内部的类

    匿名内部类作用:简化代码
        把子类继承父类,重写父类的方法,创建子类对象合一步完成
        把实现类实现类接口,重写接口中的方法,创建实现类对象合成一步完成
    匿名内部类的最终产物:子类/实现类对象,而这个类没有名字

    格式:
        new 父类/接口(){
            重复父类/接口中的方法
        };
 */
public class Demo01InnerClassThread {
    public static void main(String[] args) {
        //线程的父类是Thread
        // new MyThread().start();
        new Thread(){
            //重写run方法,设置线程任务
            @Override
            public void run() {
                for (int i = 0; i <20 ; i++) {
                    System.out.println(Thread.currentThread().getName()+"-->"+"黑马");
                }
            }
        }.start();

        //线程的接口Runnable
        //Runnable r = new RunnableImpl();//多态
        Runnable r = new Runnable(){
            //重写run方法,设置线程任务
            @Override
            public void run() {
                for (int i = 0; i <20 ; i++) {
                    System.out.println(Thread.currentThread().getName()+"-->"+"程序员");
                }
            }
        };
        new Thread(r).start();

        //简化接口的方式
        new Thread(new Runnable(){
            //重写run方法,设置线程任务
            @Override
            public void run() {
                for (int i = 0; i <20 ; i++) {
                    System.out.println(Thread.currentThread().getName()+"-->"+"传智播客");
                }
            }
        }).start();
    }
}
```

## 第二章 线程安全 ##

### Demo01Ticket 多个线程共享数据不同步导致的安全问题 ###

```java
package com.itheima.demo06.ThreadSafe;
/*
    实现卖票案例
 */
public class RunnableImpl implements Runnable{
    //定义一个多个线程共享的票源
    private  int ticket = 100;


    //设置线程任务:卖票
    @Override
    public void run() {
        //使用死循环,让卖票操作重复执行
        while(true){
            //先判断票是否存在
            if(ticket>0){
                //提高安全问题出现的概率,让程序睡眠
                try {
                    Thread.sleep(10);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

                //票存在,卖票 ticket--
                System.out.println(Thread.currentThread().getName()+"-->正在卖第"+ticket+"张票");
                ticket--;
            }
        }
    }
}
package com.itheima.demo06.ThreadSafe;
/*
    模拟卖票案例
    创建3个线程,同时开启,对共享的票进行出售
 */
public class Demo01Ticket {
    public static void main(String[] args) {
        //创建Runnable接口的实现类对象
        RunnableImpl run = new RunnableImpl();
        //创建Thread类对象,构造方法中传递Runnable接口的实现类对象
        Thread t0 = new Thread(run);
        Thread t1 = new Thread(run);
        Thread t2 = new Thread(run);
        //调用start方法开启多线程
        t0.start();
        t1.start();
        t2.start();
    }
}
```

### 法1 同步代码块synchronized ###

```java
package com.itheima.demo07.Synchronized;
/*
    卖票案例出现了线程安全问题
    卖出了不存在的票和重复的票

    解决线程安全问题的一种方案:使用同步代码块
    格式:
        synchronized(锁对象){
            可能会出现线程安全问题的代码(访问了共享数据的代码)
        }

    注意:
        1.通过代码块中的锁对象,可以使用任意的对象
        2.但是必须保证多个线程使用的锁对象是同一个 声明在run()方法外部
        3.锁对象作用:
            把同步代码块锁住,只让一个线程在同步代码块中执行
 */
public class RunnableImpl implements Runnable{
    //定义一个多个线程共享的票源
    private  int ticket = 100;

    //创建一个锁对象
    Object obj = new Object();

    //设置线程任务:卖票
    @Override
    public void run() {
        //使用死循环,让卖票操作重复执行
        while(true){
           //同步代码块
            synchronized (obj){
                //先判断票是否存在
                if(ticket>0){
                    //提高安全问题出现的概率,让程序睡眠
                    try {
                        Thread.sleep(10);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                    //票存在,卖票 ticket--
                    System.out.println(Thread.currentThread().getName()+"-->正在卖第"+ticket+"张票");
                    ticket--;
                }
            }
        }
    }
}
```

### 法2 同步方法(锁对象是实现类对象) ###

```java
package com.itheima.demo08.Synchronized;
/*
    卖票案例出现了线程安全问题
    卖出了不存在的票和重复的票

    解决线程安全问题的二种方案:使用同步方法
    使用步骤:
        1.把访问了共享数据的代码抽取出来,放到一个方法中
        2.在方法上添加synchronized修饰符

    格式:定义方法的格式
    修饰符 synchronized 返回值类型 方法名(参数列表){
        可能会出现线程安全问题的代码(访问了共享数据的代码)
    }
 */
public class RunnableImpl implements Runnable{
    //定义一个多个线程共享的票源
    private int ticket = 100;


    //设置线程任务:卖票
    @Override
    public void run() {
        System.out.println("this:"+this);//this:com.itheima.demo08.Synchronized.RunnableImpl@58ceff1
        //使用死循环,让卖票操作重复执行
        while(true){
            payTicket();
        }
    }

    /*
        定义一个同步方法
        同步方法也会把方法内部的代码锁住
        只让一个线程执行
        同步方法的锁对象是谁?
        就是实现类对象 new RunnableImpl()
        也是就是this
     */
    public synchronized void payTicket(){
        //synchronized (this){
            //先判断票是否存在
            if(ticket>0){
                //提高安全问题出现的概率,让程序睡眠
                try {
                    Thread.sleep(10);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

                //票存在,卖票 ticket--
                System.out.println(Thread.currentThread().getName()+"-->正在卖第"+ticket+"张票");
                ticket--;
            }
        //}

    }
}
```

### 法2 静态同步方法(锁对象是本类的class属性)了解 ###

```java
package com.itheima.demo08.Synchronized;

public class RunnableImpl implements Runnable{
    //定义一个多个线程共享的票源
    private static int ticket = 100;

    //设置线程任务:卖票
    @Override
    public void run() {
        System.out.println("this:"+this);//this:com.itheima.demo08.Synchronized.RunnableImpl@58ceff1
        //使用死循环,让卖票操作重复执行
        while(true){
            payTicket();
        }
    }

    /*
        静态的同步方法
        锁对象是谁?
        不能是this
        this是创建对象之后产生的,静态方法优先于对象
        静态方法的锁对象是本类的class属性-->class文件对象(反射)
     */
    public static synchronized void payTicketStatic(){
        //synchronized (RunnableImpl.class){
            //先判断票是否存在
            if(ticket>0){
                //提高安全问题出现的概率,让程序睡眠
                try {
                    Thread.sleep(10);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

                //票存在,卖票 ticket--
                System.out.println(Thread.currentThread().getName()+"-->正在卖第"+ticket+"张票");
                ticket--;
            }
        //}

    }
}
```

### 法3 lock🔒 ###

```java
package com.itheima.demo09.Lock;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/*
    卖票案例出现了线程安全问题
    卖出了不存在的票和重复的票

    解决线程安全问题的三种方案:使用Lock锁
    java.util.concurrent.locks.Lock接口
    Lock 实现提供了比使用 synchronized 方法和语句可获得的更广泛的锁定操作。
    Lock接口中的方法:
        void lock()获取锁。
        void unlock()  释放锁。
    java.util.concurrent.locks.ReentrantLock implements Lock接口


    使用步骤:
        1.在成员位置创建一个ReentrantLock对象
        2.在可能会出现安全问题的代码前调用Lock接口中的方法lock获取锁
        3.在可能会出现安全问题的代码后调用Lock接口中的方法unlock释放锁
 */
public class RunnableImpl implements Runnable{
    //定义一个多个线程共享的票源
    private  int ticket = 100;

    //1.在成员位置创建一个ReentrantLock对象
    Lock l = new ReentrantLock();

    //设置线程任务:卖票
    @Override
    public void run() {
        //使用死循环,让卖票操作重复执行
        while(true){
            //2.在可能会出现安全问题的代码前调用Lock接口中的方法lock获取锁
            l.lock();

            //先判断票是否存在
            if(ticket>0){
                //提高安全问题出现的概率,让程序睡眠
                try {
                    Thread.sleep(10);
                    //票存在,卖票 ticket--
                    System.out.println(Thread.currentThread().getName()+"-->正在卖第"+ticket+"张票");
                    ticket--;
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }finally {
                    //3.在可能会出现安全问题的代码后调用Lock接口中的方法unlock释放锁
                    l.unlock();//无论程序是否异常,都会把锁释放
                }
            }
        }
    }

    /*//设置线程任务:卖票
    @Override
    public void run() {
        //使用死循环,让卖票操作重复执行
        while(true){
           //2.在可能会出现安全问题的代码前调用Lock接口中的方法lock获取锁
           l.lock();

            //先判断票是否存在
            if(ticket>0){
                //提高安全问题出现的概率,让程序睡眠
                try {
                    Thread.sleep(10);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }

                //票存在,卖票 ticket--
                System.out.println(Thread.currentThread().getName()+"-->正在卖第"+ticket+"张票");
                ticket--;
            }

            //3.在可能会出现安全问题的代码后调用Lock接口中的方法unlock释放锁
            l.unlock();
        }
    }*/
}
```

## 第三章 线程状态 ##

### Demo01obj.wait()/obj.notify()进程的等待和唤醒 ###

```java
package com.itheima.demo10.WaitAndNotify;
/*
    等待唤醒案例:线程之间的通信
        创建一个顾客线程(消费者):告知老板要的包子的种类和数量,调用wait方法,放弃cpu的执行,进入到WAITING状态(无限等待)
        创建一个老板线程(生产者):花了5秒做包子,做好包子之后,调用notify方法,唤醒顾客吃包子

    注意:
        顾客和老板线程必须使用同步代码块包裹起来,保证等待和唤醒只能有一个在执行
        同步使用的锁对象必须保证唯一
        只有锁对象才能调用wait和notify方法

    Obejct类中的方法
    void wait()
          在其他线程调用此对象的 notify() 方法或 notifyAll() 方法前，导致当前线程等待。
    void notify()
          唤醒在此对象监视器上等待的单个线程。
          会继续执行wait方法之后的代码
 */
public class Demo01WaitAndNotify {
    public static void main(String[] args) {
        //创建锁对象,保证唯一
        Object obj = new Object();
        // 创建一个顾客线程(消费者)
        new Thread(){
            @Override
            public void run() {
               //一直等着买包子
               while(true){
                   //保证等待和唤醒的线程只能有一个执行,需要使用同步技术
                   synchronized (obj){
                       System.out.println("告知老板要的包子的种类和数量");
                       //调用wait方法,放弃cpu的执行,进入到WAITING状态(无限等待)
                       try {
                           obj.wait();
                       } catch (InterruptedException e) {
                           e.printStackTrace();
                       }
                       //唤醒之后执行的代码
                       System.out.println("包子已经做好了,开吃!");
                       System.out.println("---------------------------------------");
                   }
               }
            }
        }.start();

        //创建一个老板线程(生产者)
        new Thread(){
            @Override
            public void run() {
                //一直做包子
                while (true){
                    //花了5秒做包子
                    try {
                        Thread.sleep(5000);//花5秒钟做包子
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                    //保证等待和唤醒的线程只能有一个执行,需要使用同步技术
                    synchronized (obj){
                        System.out.println("老板5秒钟之后做好包子,告知顾客,可以吃包子了");
                        //做好包子之后,调用notify方法,唤醒顾客吃包子
                        obj.notify();
                    }
                }
            }
        }.start();
    }
}
```

### Demo02 obj.wait(m)/obj.notifyAll()多个进程同时唤醒 ###

```java
package com.itheima.demo10.WaitAndNotify;
/*
    进入到TimeWaiting(计时等待)有两种方式
    1.使用Thread.sleep(long m)方法,在毫秒值结束之后,线程睡醒进入到Runnable/Blocked状态
    2.使用obj.wait(long m)方法,wait方法如果在毫秒值结束之后,还没有被notify唤醒,就会自动醒来,线程睡醒进入到Runnable/Blocked状态
    //规定时间的wait(long m),规定之间内等notify,时间过了就睡醒  PS: 1个小时后还没有结果就炸了城门楼

    唤醒的方法:
         void notify() 唤醒在此对象监视器上等待的单个线程。
         void notifyAll() 唤醒在此对象监视器上等待的所有线程。
 */
public class Demo02WaitAndNotify {
    public static void main(String[] args) {
        //创建锁对象,保证唯一
        Object obj = new Object();
        // 创建一个顾客线程(消费者)
        new Thread(){
            @Override
            public void run() {
                //一直等着买包子
                while(true){
                    //保证等待和唤醒的线程只能有一个执行,需要使用同步技术
                    synchronized (obj){
                        System.out.println("顾客1告知老板要的包子的种类和数量");
                        //调用wait方法,放弃cpu的执行,进入到WAITING状态(无限等待)
                        try {
                            obj.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                        //唤醒之后执行的代码
                        System.out.println("包子已经做好了,顾客1开吃!");
                        System.out.println("---------------------------------------");
                    }
                }
            }
        }.start();

        // 创建一个顾客线程(消费者)
        new Thread(){
            @Override
            public void run() {
                //一直等着买包子
                while(true){
                    //保证等待和唤醒的线程只能有一个执行,需要使用同步技术
                    synchronized (obj){
                        System.out.println("顾客2告知老板要的包子的种类和数量");
                        //调用wait方法,放弃cpu的执行,进入到WAITING状态(无限等待)
                        try {
                            obj.wait();
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                        //唤醒之后执行的代码
                        System.out.println("包子已经做好了,顾客2开吃!");
                        System.out.println("---------------------------------------");
                    }
                }
            }
        }.start();

        //创建一个老板线程(生产者)
        new Thread(){
            @Override
            public void run() {
                //一直做包子
                while (true){
                    //花了5秒做包子
                    try {
                        Thread.sleep(5000);//花5秒钟做包子
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                    //保证等待和唤醒的线程只能有一个执行,需要使用同步技术
                    synchronized (obj){
                        System.out.println("老板5秒钟之后做好包子,告知顾客,可以吃包子了");
                        //做好包子之后,调用notify方法,唤醒顾客吃包子
                        //obj.notify();//如果有多个等待线程,随机唤醒一个
                        obj.notifyAll();//唤醒所有等待的线程
                    }
                }
            }
        }.start();
    }
}
```

# day07【线程池、Lambda表达式】 #

## 第一章 等待唤醒机制 ##

### Demo 包子铺 ###

```java
package com.itheima.demo01.WaitAndNotify;
/*
    资源类:包子类
	设置包子的属性
		皮
		陷
		包子的状态: 有 true,没有 false
 */
public class BaoZi {
    //皮
    String pi;
    //陷
    String xian;
    //包子的状态: 有 true,没有 false,设置初始值为false没有包子
    boolean flag = false;

}

package com.itheima.demo01.WaitAndNotify;
/*
    消费者(吃货)类:是一个线程类,可以继承Thread
	设置线程任务(run):吃包子
	对包子的状态进行判断
	false:没有包子
		吃货调用wait方法进入等待状态
	true:有包子
		吃货吃包子
		吃货吃完包子
		修改包子的状态为false没有
		吃货唤醒包子铺线程,生产包子
 */
public class ChiHuo extends Thread{
    //1.需要在成员位置创建一个包子变量
    private BaoZi bz;

    //2.使用带参数构造方法,为这个包子变量赋值
    public ChiHuo(BaoZi bz) {
        this.bz = bz;
    }
    //设置线程任务(run):吃包子
    @Override
    public void run() {
        //使用死循环,让吃货一直吃包子
        while (true){
            //必须同时同步技术保证两个线程只能有一个在执行
            synchronized (bz){
                //对包子的状态进行判断
                if(bz.flag==false){
                    //吃货调用wait方法进入等待状态
                    try {
                        bz.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }

                //被唤醒之后执行的代码,吃包子
                System.out.println("吃货正在吃:"+bz.pi+bz.xian+"的包子");
                //吃货吃完包子
                //修改包子的状态为false没有
                bz.flag = false;
                //吃货唤醒包子铺线程,生产包子
                bz.notify();
                System.out.println("吃货已经把:"+bz.pi+bz.xian+"的包子吃完了,包子铺开始生产包子");
                System.out.println("----------------------------------------------------");
            }
        }
    }
}

package com.itheima.demo01.WaitAndNotify;
/*
    生产者(包子铺)类:是一个线程类,可以继承Thread
	设置线程任务(run):生产包子
	对包子的状态进行判断
	true:有包子
		包子铺调用wait方法进入等待状态
	false:没有包子
		包子铺生产包子
		增加一些趣味性:交替生产两种包子
			有两种状态(i%2==0)
		包子铺生产好了包子
		修改包子的状态为true有
		唤醒吃货线程,让吃货线程吃包子

	注意:
	    包子铺线程和包子线程关系-->通信(互斥)
	    必须同时同步技术保证两个线程只能有一个在执行
	    锁对象必须保证唯一,可以使用包子对象作为锁对象
	    包子铺类和吃货的类就需要把包子对象作为参数传递进来
	        1.需要在成员位置创建一个包子变量
	        2.使用带参数构造方法,为这个包子变量赋值
 */
public class BaoZiPu extends Thread{
    //1.需要在成员位置创建一个包子变量
    private BaoZi bz;

    //2.使用带参数构造方法,为这个包子变量赋值
    public BaoZiPu(BaoZi bz) {
        this.bz = bz;
    }

    //设置线程任务(run):生产包子
    @Override
    public void run() {
        //定义一个变量
        int count = 0;
        //让包子铺一直生产包子
        while(true){
            //必须同时同步技术保证两个线程只能有一个在执行
            synchronized (bz){
                //对包子的状态进行判断
                if(bz.flag==true){
                    //包子铺调用wait方法进入等待状态
                    try {
                        bz.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }

                //被唤醒之后执行,包子铺生产包子
                //增加一些趣味性:交替生产两种包子
                if(count%2==0){
                    //生产 薄皮三鲜馅包子
                    bz.pi = "薄皮";
                    bz.xian = "三鲜馅";
                }else{
                    //生产 冰皮 牛肉大葱陷
                    bz.pi = "冰皮";
                    bz.xian = "牛肉大葱陷";

                }
                count++;
                System.out.println("包子铺正在生产:"+bz.pi+bz.xian+"包子");
                //生产包子需要3秒钟
                try {
                    Thread.sleep(3000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                //包子铺生产好了包子
                //修改包子的状态为true有
                bz.flag = true;
                //唤醒吃货线程,让吃货线程吃包子
                bz.notify();
                System.out.println("包子铺已经生产好了:"+bz.pi+bz.xian+"包子,吃货可以开始吃了");
            }
        }
    }
}

package com.itheima.demo01.WaitAndNotify;
/*
    测试类:
	包含main方法,程序执行的入口,启动程序
	创建包子对象;
	创建包子铺线程,开启,生产包子;
	创建吃货线程,开启,吃包子;
 */
public class Demo {
    public static void main(String[] args) {
        //创建包子对象;
        BaoZi bz =new BaoZi();
        //创建包子铺线程,开启,生产包子;
        new BaoZiPu(bz).start();
        //创建吃货线程,开启,吃包子;
        new ChiHuo(bz).start();
    }
}
```

## 第二章 线程池 ##

### Demo01ThreadPool 线程池 ###

```java
package com.itheima.demo02.ThreadPool;
/*
    2.创建一个类,实现Runnable接口,重写run方法,设置线程任务
 */
public class RunnableImpl implements Runnable{
    @Override
    public void run() {
        System.out.println(Thread.currentThread().getName()+"创建了一个新的线程执行");
    }
}
package com.itheima.demo02.ThreadPool;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/*
    线程池:JDK1.5之后提供的
    java.util.concurrent.Executors:线程池的工厂类,用来生成线程池
    Executors类中的静态方法:
        static ExecutorService newFixedThreadPool(int nThreads) 创建一个可重用固定线程数的线程池
        参数:
            int nThreads:创建线程池中包含的线程数量
        返回值:
            ExecutorService接口,返回的是ExecutorService接口的实现类对象,我们可以使用ExecutorService接口接收(面向接口编程)
    java.util.concurrent.ExecutorService:线程池接口
        用来从线程池中获取线程,调用start方法,执行线程任务
            submit(Runnable task) 提交一个 Runnable 任务用于执行
        关闭/销毁线程池的方法
            void shutdown()
    线程池的使用步骤:
        1.使用线程池的工厂类Executors里边提供的静态方法newFixedThreadPool生产一个指定线程数量的线程池
        2.创建一个类,实现Runnable接口,重写run方法,设置线程任务
        3.调用ExecutorService中的方法submit,传递线程任务(实现类),开启线程,执行run方法
        4.调用ExecutorService中的方法shutdown销毁线程池(不建议执行)
 */
public class Demo01ThreadPool {
    public static void main(String[] args) {
        //1.使用线程池的工厂类Executors里边提供的静态方法newFixedThreadPool生产一个指定线程数量的线程池
        ExecutorService es = Executors.newFixedThreadPool(2);
        //3.调用ExecutorService中的方法submit,传递线程任务(实现类),开启线程,执行run方法
        es.submit(new RunnableImpl());//pool-1-thread-1创建了一个新的线程执行
        //线程池会一直开启,使用完了线程,会自动把线程归还给线程池,线程可以继续使用
        es.submit(new RunnableImpl());
        //pool-1-thread-1创建了一个新的线程执行(再次使用thread1)
        es.submit(new RunnableImpl());//pool-1-thread-2创建了一个新的线程执行

        //4.调用ExecutorService中的方法shutdown销毁线程池(不建议执行)
        es.shutdown();

        es.submit(new RunnableImpl());//抛异常,线程池都没有了,就不能获取线程了
    }

}
```

## 第三章 Lambda表达式 ##

### Demo02Lambda 实现多线程程序(runnable接口) ###

```java
package com.itheima.demo03.Lambda;
/*
    使用实现Runnable接口的方式实现多线程程序
 */
public class Demo01Runnable {
    public static void main(String[] args) {
        //创建Runnable接口的实现类对象
        RunnableImpl run = new RunnableImpl();
        //创建Thread类对象,构造方法中传递Runnable接口的实现类
        Thread t = new Thread(run);
        //调用start方法开启新线程,执行run方法
        t.start();

        //简化代码,使用匿名内部类,实现多线程程序
        Runnable r = new Runnable(){
            @Override
            public void run() {
                System.out.println(Thread.currentThread().getName()+" 新线程创建了");
            }
        };
        new Thread(r).start();

        //简化代码
        new Thread(new Runnable(){
            @Override
            public void run() {
                System.out.println(Thread.currentThread().getName()+" 新线程创建了");
            }
        }).start();
    }
}
package com.itheima.demo03.Lambda;
/*
    Lambda表达式的标准格式:
        由三部分组成:
            a.一些参数
            b.一个箭头
            c.一段代码
        格式:
            (参数列表) -> {一些重写方法的代码};
        解释说明格式:
            ():接口中抽象方法的参数列表,没有参数,就空着;有参数就写出参数,多个参数使用逗号分隔
            ->:传递的意思,把参数传递给方法体{}
            {}:重写接口的抽象方法的方法体
 */
public class Demo02Lambda {
    public static void main(String[] args) {
        //使用匿名内部类的方式,实现多线程
        new Thread(new Runnable(){
            @Override
            public void run() {
                System.out.println(Thread.currentThread().getName()+" 新线程创建了");
            }
        }).start();

        //使用Lambda表达式,实现多线程
        new Thread(()->{
                System.out.println(Thread.currentThread().getName()+" 新线程创建了");
            }
        ).start();

        //优化省略Lambda
        new Thread(()->System.out.println(Thread.currentThread().getName()+" 新线程创建了")).start();
    }
}
```

### Demo01Cook Lambda 实现其他接口的重写 ###

```java
package com.itheima.demo04.Lambda;
/*
    定一个厨子Cook接口，内含唯一的抽象方法makeFood
 */
public interface Cook {
    //定义无参数无返回值的方法makeFood
    public abstract void makeFood();
}
package com.itheima.demo04.Lambda;
/*
    需求:
        给定一个厨子Cook接口，内含唯一的抽象方法makeFood，且无参数、无返回值。
        使用Lambda的标准格式调用invokeCook方法，打印输出“吃饭啦！”字样
 */
public class Demo01Cook {
    public static void main(String[] args) {
        //调用invokeCook方法,参数是Cook接口,传递Cook接口的匿名内部类对象
        invokeCook(new Cook() {
            @Override
            public void makeFood() {
                System.out.println("吃饭了");
            }
        });

        //使用Lambda表达式,简化匿名内部类的书写
        invokeCook(()->{
            System.out.println("吃饭了");
        });

        //优化省略Lambda
        invokeCook(()-> System.out.println("吃饭了"));
    }

    //定义一个方法,参数传递Cook接口,方法内部调用Cook接口中的方法makeFood
    public static void invokeCook(Cook cook){
        cook.makeFood();
    }
}

```

### Demo01 Lambda表达式有参数有返回值 ###

```java
package com.itheima.demo05.Lambda;

import java.util.Arrays;

/*
    Lambda表达式有参数有返回值的练习
    需求:
        使用数组存储多个Person对象
        对数组中的Person对象使用Arrays的sort方法通过年龄进行升序排序
 */
public class Demo01Arrays {
    public static void main(String[] args) {
        //使用数组存储多个Person对象
        Person[] arr = {
                new Person("柳岩",38),
                new Person("迪丽热巴",18),
                new Person("古力娜扎",19)
        };

        //对数组中的Person对象使用Arrays的sort方法通过年龄进行升序(前边-后边)排序
        /*Arrays.sort(arr, new Comparator<Person>() {
            @Override
            public int compare(Person o1, Person o2) {
                return o1.getAge()-o2.getAge();
            }
        });*/

        //使用Lambda表达式,简化匿名内部类
        Arrays.sort(arr,(Person o1, Person o2)->{
            return o1.getAge()-o2.getAge();
        });

        //优化省略Lambda
        Arrays.sort(arr,(o1, o2)->o1.getAge()-o2.getAge());

        //遍历数组
        for (Person p : arr) {
            System.out.println(p);
        }
    }
}
```

### Demo01Calculator Lambda表达式有参数有返回值 ###

```java
package com.itheima.demo06.Lambda;
/*
    给定一个计算器Calculator接口，内含抽象方法calc可以将两个int数字相加得到和值
 */
public interface Calculator {
    //定义一个计算两个int整数和的方法并返回结果
    public abstract int calc(int a,int b);
}
package com.itheima.demo06.Lambda;

/*
    Lambda表达式有参数有返回值的练习
    需求:
        给定一个计算器Calculator接口，内含抽象方法calc可以将两个int数字相加得到和值
        使用Lambda的标准格式调用invokeCalc方法，完成120和130的相加计算
 */
public class Demo01Calculator {
    public static void main(String[] args) {
        //调用invokeCalc方法,方法的参数是一个接口,可以使用匿名内部类
        invokeCalc(10, 20, new Calculator() {
            @Override
            public int calc(int a, int b) {
                return a+b;
            }
        });

        //使用Lambda表达式简化匿名内部类的书写
        invokeCalc(120,130,(int a,int b)->{
            return a + b;
        });

        //优化省略Lambda
        invokeCalc(120,130,(a,b)-> a + b);
    }

    /*
        定义一个方法
        参数传递两个int类型的整数
        参数传递Calculator接口
        方法内部调用Calculator中的方法calc计算两个整数的和
     */
    public static void invokeCalc(int a,int b,Calculator c){
        int sum = c.calc(a,b);
        System.out.println(sum);
    }
}
```

### Demo01  lambda推导出来的内容,都可以省略书写 ###

```java
package com.itheima.demo07.Lambda;

import java.util.ArrayList;

/*
    Lambda表达式:是可推导,可以省略
    凡是根据上下文推导出来的内容,都可以省略书写
    可以省略的内容:
        1.(参数列表):括号中参数列表的数据类型,可以省略不写
        2.(参数列表):括号中的参数如果只有一个,那么类型和()都可以省略
        3.{一些代码}:如果{}中的代码只有一行,无论是否有返回值,都可以省略({},return,分号)
            注意:要省略{},return,分号必须一起省略
 */
public class Demo01ArrayList {
    public static void main(String[] args) {
        //JDK1.7版本之前,创建集合对象必须把前后的泛型都写上
        ArrayList<String> list01 = new ArrayList<String>();

        //JDK1.7版本之后,=号后边的泛型可以省略,后边的泛型可以根据前边的泛型推导出来
        ArrayList<String> list02 = new ArrayList<>();
    }
}
```

# day08【File类、递归】 #

## 第一章 File类 ##

### Demo01File ###

```java
package com.itheima.demo01.File;

import java.io.File;

/*
    java.io.File类
    文件和目录路径名的抽象表示形式。
    java把电脑中的文件和文件夹(目录)封装为了一个File类,我们可以使用File类对文件和文件夹进行操作
    我们可以使用File类的方法
        创建一个文件/文件夹
        删除文件/文件夹
        获取文件/文件夹
        判断文件/文件夹是否存在
        对文件夹进行遍历
        获取文件的大小
    File类是一个与系统无关的类,任何的操作系统都可以使用这个类中的方法

    重点:记住这三个单词
        file:文件
        directory:文件夹/目录
        path:路径
 */
public class Demo01File {
    public static void main(String[] args) {
        /*
            static String pathSeparator 与系统有关的路径分隔符，为了方便，它被表示为一个字符串。
            static char pathSeparatorChar 与系统有关的路径分隔符。

            static String separator 与系统有关的默认名称分隔符，为了方便，它被表示为一个字符串。
            static char separatorChar 与系统有关的默认名称分隔符。

            操作路径:路径不能写死了
            C:\develop\a\a.txt  windows
            C:/develop/a/a.txt  linux
            "C:"+File.separator+"develop"+File.separator+"a"+File.separator+"a.txt"
         */
        String pathSeparator = File.pathSeparator;
        System.out.println(pathSeparator);//路径分隔符 windows:分号;  linux:冒号:

        String separator = File.separator;
        System.out.println(separator);// 文件名称分隔符 windows:反斜杠\  linux:正斜杠/
    }

}
```

### Demo02 File类的构造方法 ###

```java
package com.itheima.demo01.File;

import java.io.File;

/*
    路径:
        绝对路径:是一个完整的路径
            以盘符(c:,D:)开始的路径
                c:\\a.txt
                C:\\Users\itcast\\IdeaProjects\\shungyuan\\123.txt
                D:\\demo\\b.txt
        相对路径:是一个简化的路径
            相对指的是相对于当前项目的根目录(C:\\Users\itcast\\IdeaProjects\\shungyuan)
            如果使用当前项目的根目录,路径可以简化书写
            C:\\Users\itcast\\IdeaProjects\\shungyuan\\123.txt-->简化为: 123.txt(可以省略项目的根目录)
        注意:
            1.路径是不区分大小写
            2.路径中的文件名称分隔符windows使用反斜杠,反斜杠是转义字符,两个反斜杠代表一个普通的反斜杠
 */
public class Demo02File {
    public static void main(String[] args) {
        /*
            File类的构造方法
         */
        //show02("c:\\","a.txt");//c:\a.txt
        //show02("d:\\","a.txt");//d:\a.txt
        //show03();

        File f = new File("C:\\Users\\itcast\\IdeaProjects\\shungyuan");
        long length = f.length();
        System.out.println(length);
    }

    /*
        File(File parent, String child) 根据 parent 抽象路径名和 child 路径名字符串创建一个新 File 实例。
        参数:把路径分成了两部分
            File parent:父路径
            String child:子路径
        好处:
             父路径和子路径,可以单独书写,使用起来非常灵活;父路径和子路径都可以变化
             父路径是File类型,可以使用File的方法对路径进行一些操作,再使用路径创建对象
     */
    private static void show03() {
        File parent = new File("c:\\");
        File file = new File(parent,"hello.java");
        System.out.println(file);//c:\hello.java
    }

    /*
        File(String parent, String child) 根据 parent 路径名字符串和 child 路径名字符串创建一个新 File 实例。
        参数:把路径分成了两部分
            String parent:父路径
            String child:子路径
        好处:
            父路径和子路径,可以单独书写,使用起来非常灵活;父路径和子路径都可以变化
     */
    private static void show02(String parent, String child) {
        File file = new File(parent,child);
        System.out.println(file);//c:\a.txt
    }

    /*
        File(String pathname) 通过将给定路径名字符串转换为抽象路径名来创建一个新 File 实例。
        参数:
            String pathname:字符串的路径名称
            路径可以是以文件结尾,也可以是以文件夹结尾
            路径可以是相对路径,也可以是绝对路径
            路径可以是存在,也可以是不存在
            创建File对象,只是把字符串路径封装为File对象,不考虑路径的真假情况
     */
    private static void show01() {
        File f1 = new File("C:\\Users\\itcast\\IdeaProjects\\shungyuan\\a.txt");
        System.out.println(f1);//重写了Object类的toString方法 C:\Users\itcast\IdeaProjects\shungyuan\a.txt

        File f2 = new File("C:\\Users\\itcast\\IdeaProjects\\shungyuan");
        System.out.println(f2);//C:\Users\itcast\IdeaProjects\shungyuan

        File f3 = new File("b.txt");
        System.out.println(f3);//b.txt
    }
}
```

### Demo03 File类获取功能的方法 ###

```java
package com.itheima.demo01.File;

import java.io.File;

/*
    File类获取功能的方法
        - public String getAbsolutePath() ：返回此File的绝对路径名字符串。
        - public String getPath() ：将此File转换为路径名字符串。
        - public String getName()  ：返回由此File表示的文件或目录的名称。
        - public long length()  ：返回由此File表示的文件的长度。
 */
public class Demo03File {
    public static void main(String[] args) {
        show04();
    }

    /*
        public long length()  ：返回由此File表示的文件的长度。
        获取的是构造方法指定的文件的大小,以字节为单位
        注意:
            文件夹是没有大小概念的,不能获取文件夹的大小
            如果构造方法中给出的路径不存在,那么length方法返回0
     */
    private static void show04() {
        File f1 = new File("C:\\develop\\a\\1.jpg");
        long l1 = f1.length();
        System.out.println(l1);//780831字节

        File f2 = new File("C:\\develop\\a\\2.jpg");
        System.out.println(f2.length());//0

        File f3 = new File("C:\\develop\\a");
        System.out.println(f3.length());//0 文件夹没有大小概念的
    }

    /*
        public String getName()  ：返回由此File表示的文件或目录的名称。
        获取的就是构造方法传递路径的结尾部分(文件/文件夹)
     */
    private static void show03() {
        File f1 = new File("C:\\Users\\itcast\\IdeaProjects\\shungyuan\\a.txt");
        String name1 = f1.getName();
        System.out.println(name1);//a.txt

        File f2 = new File("C:\\Users\\itcast\\IdeaProjects\\shungyuan");
        String name2 = f2.getName();
        System.out.println(name2);//shungyuan
    }

    /*
        public String getPath() ：将此File转换为路径名字符串。
        获取的构造方法中传递的路径

        toString方法调用的就是getPath方法
        源码:
            public String toString() {
                return getPath();
            }
     */
    private static void show02() {
        File f1 = new File("C:\\Users\\itcast\\IdeaProjects\\shungyuan\\a.txt");
        File f2 = new File("a.txt");
        String path1 = f1.getPath();
        System.out.println(path1);//C:\Users\itcast\IdeaProjects\shungyuan\a.txt
        String path2 = f2.getPath();
        System.out.println(path2);//a.txt

        System.out.println(f1);//C:\Users\itcast\IdeaProjects\shungyuan\a.txt
        System.out.println(f1.toString());//C:\Users\itcast\IdeaProjects\shungyuan\a.txt
    }

    /*
        public String getAbsolutePath() ：返回此File的绝对路径名字符串。
        获取的构造方法中传递的路径
        无论路径是绝对的还是相对的,getAbsolutePath方法返回的都是绝对路径
     */
    private static void show01() {
        File f1 = new File("C:\\Users\\itcast\\IdeaProjects\\shungyuan\\a.txt");
        String absolutePath1 = f1.getAbsolutePath();
        System.out.println(absolutePath1);//C:\Users\itcast\IdeaProjects\shungyuan\a.txt

        File f2 = new File("a.txt");
        String absolutePath2 = f2.getAbsolutePath();
        System.out.println(absolutePath2);//C:\Users\itcast\IdeaProjects\shungyuan\a.txt
    }
}
```

### Demo04 File类判断功能的方法 ###

```java
package com.itheima.demo01.File;

import java.io.File;

/*
    File类判断功能的方法
        - public boolean exists() ：此File表示的文件或目录是否实际存在。
        - public boolean isDirectory() ：此File表示的是否为目录。
        - public boolean isFile() ：此File表示的是否为文件。
 */
public class Demo04File {
    public static void main(String[] args) {
        show02();
    }

    /*
        public boolean isDirectory() ：此File表示的是否为目录。
            用于判断构造方法中给定的路径是否以文件夹结尾
                是:true
                否:false
        public boolean isFile() ：此File表示的是否为文件。
            用于判断构造方法中给定的路径是否以文件结尾
                是:true
                否:false
        注意:
            电脑的硬盘中只有文件/文件夹,两个方法是互斥
            这两个方法使用前提,路径必须是存在的,否则都返回false
     */
    private static void show02() {
        File f1 = new File("C:\\Users\\itcast\\IdeaProjects\\shung");

        //不存在,就没有必要获取
        if(f1.exists()){
            System.out.println(f1.isDirectory());
            System.out.println(f1.isFile());
        }

        File f2 = new File("C:\\Users\\itcast\\IdeaProjects\\shungyuan");
        if(f2.exists()){
            System.out.println(f2.isDirectory());//true
            System.out.println(f2.isFile());//false
        }

        File f3 = new File("C:\\Users\\itcast\\IdeaProjects\\shungyuan\\shungyuan.iml");
        if(f3.exists()){
            System.out.println(f3.isDirectory());//false
            System.out.println(f3.isFile());//true
        }
    }

    /*
        public boolean exists() ：此File表示的文件或目录是否实际存在。
        用于判断构造方法中的路径是否存在
            存在:true
            不存在:false
     */
    private static void show01() {
        File f1 = new File("C:\\Users\\itcast\\IdeaProjects\\shungyuan");
        System.out.println(f1.exists());//true

        File f2 = new File("C:\\Users\\itcast\\IdeaProjects\\shung");
        System.out.println(f2.exists());//false

        File f3 = new File("shungyuan.iml");//相对路径 C:\Users\itcast\IdeaProjects\shungyuan\shungyuan.iml
        System.out.println(f3.exists());//true

        File f4 = new File("a.txt");
        System.out.println(f4.exists());//false
    }
}
```

### Demo05 File类创建删除功能的方法 ###

```java
package com.itheima.demo01.File;

import java.io.File;
import java.io.IOException;

/*
    File类创建删除功能的方法
        - public boolean createNewFile() ：当且仅当具有该名称的文件尚不存在时，创建一个新的空文件。
        - public boolean delete() ：删除由此File表示的文件或目录。
        - public boolean mkdir() ：创建由此File表示的目录。
        - public boolean mkdirs() ：创建由此File表示的目录，包括任何必需但不存在的父目录。
 */
public class Demo05File {
    public static void main(String[] args) throws IOException {
        show03();
    }

    /*
        public boolean delete() ：删除由此File表示的文件或目录。
        此方法,可以删除构造方法路径中给出的文件/文件夹
        返回值:布尔值
            true:文件/文件夹删除成功,返回true
            false:1 文件夹中有内容,不会删除返回false;2 构造方法中路径不存在false
        注意:
            delete方法是直接在硬盘删除文件/文件夹,不走回收站,删除要谨慎
     */
    private static void show03() {
        File f1 = new File("08_FileAndRecursion\\新建文件夹");
        boolean b1 = f1.delete();
        System.out.println("b1:"+b1);

        File f2 = new File("08_FileAndRecursion\\abc.txt");
        System.out.println(f2.delete());
    }

    /*
       public boolean mkdir() ：创建单级空文件夹
       public boolean mkdirs() ：既可以创建单级空文件夹,也可以创建多级文件夹
       创建文件夹的路径和名称在构造方法中给出(构造方法的参数)
        返回值:布尔值
            true:文件夹不存在,创建文件夹,返回true
            false:文件夹存在,不会创建,返回false;构造方法中给出的路径不存在返回false
        注意:
            1.此方法只能创建文件夹,不能创建文件
     */
    private static void show02() {
        File f1 = new File("08_FileAndRecursion\\aaa");
        boolean b1 = f1.mkdir();
        System.out.println("b1:"+b1);

        File f2 = new File("08_FileAndRecursion\\111\\222\\333\\444");
        boolean b2 = f2.mkdirs();
        System.out.println("b2:"+b2);

        File f3 = new File("08_FileAndRecursion\\abc.txt");
        boolean b3 = f3.mkdirs();//看类型,是一个文件
        System.out.println("b3:"+b3);

        File f4 = new File("08_F\\ccc");
        boolean b4 = f4.mkdirs();//不会抛出异常,路径不存在,不会创建
        System.out.println("b4:"+b4);
    }

    /*
        public boolean createNewFile() ：当且仅当具有该名称的文件尚不存在时，创建一个新的空文件。
        创建文件的路径和名称在构造方法中给出(构造方法的参数)
        返回值:布尔值
            true:文件不存在,创建文件,返回true
            false:文件存在,不会创建,返回false
        注意:
            1.此方法只能创建文件,不能创建文件夹
            2.创建文件的路径必须存在,否则会抛出异常

        public boolean createNewFile() throws IOException
        createNewFile声明抛出了IOException,我们调用这个方法,就必须的处理这个异常,要么throws,要么trycatch
     */
    private static void show01() throws IOException {
        File f1 = new File("G:\\IdeaProjects\\advanced-code\\08_FileAndRecursion\\1.txt");
        boolean b1 = f1.createNewFile();
        System.out.println("b1:"+b1);

        File f2 = new File("08_FileAndRecursion\\2.txt");
        System.out.println(f2.createNewFile());

        File f3 = new File("08_FileAndRecursion\\新建文件夹");
        System.out.println(f3.createNewFile());//不要被名称迷糊,要看类型

        File f4 = new File("0111_FileAndRecursi\\3.txt");
        System.out.println(f4.createNewFile());//路径不存在,抛出IOException
    }
}
```

### Demo06 File类遍历(文件夹)目录功能 ###

```java
package com.itheima.demo01.File;

import java.io.File;

/*
    File类遍历(文件夹)目录功能
        - public String[] list() ：返回一个String数组，表示该File目录中的所有子文件或目录。
        - public File[] listFiles() ：返回一个File数组，表示该File目录中的所有的子文件或目录。

    注意:
        list方法和listFiles方法遍历的是构造方法中给出的目录
        如果构造方法中给出的目录的路径不存在,会抛出空指针异常
        如果构造方法中给出的路径不是一个目录,也会抛出空指针异常
 */
public class Demo06File {
    public static void main(String[] args) {
        show02();
    }

    /*
        public File[] listFiles() ：返回一个File数组，表示该File目录中的所有的子文件或目录。
        遍历构造方法中给出的目录,会获取目录中所有的文件/文件夹,把文件/文件夹封装为File对象,多个File对象存储到File数组中
     */
    private static void show02() {
        File file = new File("C:\\Users\\itcast\\IdeaProjects\\shungyuan\\08_FileAndRecursion");
        File[] files = file.listFiles();
        for (File f : files) {
            System.out.println(f);
        }
    }

    /*
        public String[] list() ：返回一个String数组，表示该File目录中的所有子文件或目录。
        遍历构造方法中给出的目录,会获取目录中所有文件/文件夹的名称,把获取到的多个名称存储到一个String类型的数组中
     */
    private static void show01() {
        //File file = new File("C:\\Users\\itcast\\IdeaProjects\\shungyuan\\08_FileAndRecursion\\1.txt");//NullPointerException
        //File file = new File("C:\\Users\\itcast\\IdeaProjects\\shungyuan\\08_Fi");//NullPointerException
        File file = new File("C:\\Users\\itcast\\IdeaProjects\\shungyuan\\08_FileAndRecursion");
        String[] arr = file.list();
        for (String fileName : arr) {
            System.out.println(fileName);
        }
    }
}
```

## 第二章 递归 ##

### Demo01Recurison ###

```java
package com.itheima.demo02.Recursion;
/*
    递归:方法自己调用自己
    - 递归的分类:
      - 递归分为两种，直接递归和间接递归。
      - 直接递归称为方法自身调用自己。
      - 间接递归可以A方法调用B方法，B方法调用C方法，C方法调用A方法。
    - 注意事项：
      - 递归一定要有条件限定，保证递归能够停止下来，否则会发生栈内存溢出。
      - 在递归中虽然有限定条件，但是递归次数不能太多。否则也会发生栈内存溢出。
      - 构造方法,禁止递归
    递归的使用前提:
        当调用方法的时候,方法的主体不变,每次调用方法的参数不同,可以使用递归
 */
public class Demo01Recurison {
    public static void main(String[] args) {
        //a();
        b(1);
    }

    /*
        构造方法,禁止递归
            编译报错:构造方法是创建对象使用的,一直递归会导致内存中有无数多个对象,直接编译报错
     */
    public Demo01Recurison() {
        //Demo01Recurison();
    }

    /*
            在递归中虽然有限定条件，但是递归次数不能太多。否则也会发生栈内存溢出。
            11157
                Exception in thread "main" java.lang.StackOverflowError
         */
    private static void b(int i) {
        System.out.println(i);
        if(i==20000){
            return; //结束方法
        }
        b(++i);
    }

    /*
        递归一定要有条件限定，保证递归能够停止下来，否则会发生栈内存溢出。
        Exception in thread "main" java.lang.StackOverflowError
     */
    private static void a() {
        System.out.println("a方法!");
        a();
    }
}
```

### Demo02 递归计算1-n之间的和 ###

```java
package com.itheima.demo02.Recursion;
/*
    练习:
        使用递归计算1-n之间的和
 */
public class Demo02Recurison {
    public static void main(String[] args) {
        int s = sum(3);
        System.out.println(s);
    }

    /*
        定义一个方法,使用递归计算1-n之间的和
        1+2+3+...+n
        n+(n-1)+(n-2)+...+1
        已知:
            最大值:n
            最小值:1
        使用递归必须明确:
            1.递归的结束条件
                获取到1的时候结束
            2.递归的目的
                获取下一个被加的数字(n-1)
     */
    public static int sum(int n){
        //获取到1的时候结束
        if(n==1){
            return 1;
        }

        //获取下一个被加的数字(n-1)
        return n + sum(n-1);
    }
}
```

### Demo04Recurison 递归打印文件目录 ###

```java
package com.itheima.demo02.Recursion;

import java.io.File;

/*
    练习:
        递归打印多级目录
    需求:
        遍历c:\\abc文件夹,及abc文件夹的子文件夹
        c:\\abc
        c:\\abc\\abc.txt
        c:\\abc\\abc.java
        c:\\abc\\a
        c:\\abc\\a\\a.jpg
        c:\\abc\\a\\a.java
        c:\\abc\\b
        c:\\abc\\b\\b.java
        c:\\abc\\b\\b.txt
 */
public class Demo04Recurison {
    public static void main(String[] args) {
        File file = new File("G:\\IdeaProjects\\advanced-code\\08_FileAndRecursion");
        getAllFile(file);
    }

    /*
        定义一个方法,参数传递File类型的目录
        方法中对目录进行遍历
     */
    public static void getAllFile(File dir){
        System.out.println(dir);//打印被遍历的目录名称
        File[] files = dir.listFiles();
        for (File f : files) {
            //对遍历得到的File对象f进行判断,判断是否是文件夹
            if(f.isDirectory()){
                //f是一个文件夹,则继续遍历这个文件夹
                //我们发现getAllFile方法就是传递文件夹,遍历文件夹的方法
                //所以直接调用getAllFile方法即可:递归(自己调用自己)
                getAllFile(f);
            }else{
                //f是一个文件,直接打印即可
                System.out.println(f);
            }
        }
    }
}
```

### Demo05 递归打印.java ###

```java
package com.itheima.demo02.Recursion;

import java.io.File;

/*
    练习:
        递归打印多级目录
    需求:
        遍历c:\\abc文件夹,及abc文件夹的子文件夹
        只要.java结尾的文件
        c:\\abc
        c:\\abc\\abc.txt
        c:\\abc\\abc.java
        c:\\abc\\a
        c:\\abc\\a\\a.jpg
        c:\\abc\\a\\a.java
        c:\\abc\\b
        c:\\abc\\b\\b.java
        c:\\abc\\b\\b.txt
 */
public class Demo05Recurison {
    public static void main(String[] args) {
        File file = new File("G:\\IdeaProjects\\advanced-code\\08_FileAndRecursion");
        getAllFile(file);
    }

    /*
        定义一个方法,参数传递File类型的目录
        方法中对目录进行遍历
     */
    public static void getAllFile(File dir){
        //System.out.println(dir);//打印被遍历的目录名称
        File[] files = dir.listFiles();
        for (File f : files) {
            //对遍历得到的File对象f进行判断,判断是否是文件夹
            if(f.isDirectory()){
                //f是一个文件夹,则继续遍历这个文件夹
                //我们发现getAllFile方法就是传递文件夹,遍历文件夹的方法
                //所以直接调用getAllFile方法即可:递归(自己调用自己)
                getAllFile(f);
            }else{
                //f是一个文件,直接打印即可
                /*
                    c:\\abc\\abc.java
                    只要.java结尾的文件
                    1.把File对象f,转为字符串对象
                 */
                //String name = f.getName();//abc.java
                //String path = f.getPath();//c:\\abc\\abc.java
                //String s = f.toString();//c:\\abc\\abc.java

                //把字符串,转换为小写
                //s = s.toLowerCase();

                //2.调用String类中的方法endsWith判断字符串是否是以.java结尾
                //boolean b = s.endsWith(".java");

                //3.如果是以.java结尾的文件,则输出
                /*if(b){
                    System.out.println(f);
                }*/

                if(f.getName().toLowerCase().endsWith(".java")){
                    System.out.println(f.getName());
                }
            }
        }
    }
}
```

### Demo01 文件过滤器优化 ###

```java
package com.itheima.demo03Filter;

import java.io.File;

/*
    我们可以使用过滤器来实现
    在File类中有两个和ListFiles重载的方法,方法的参数传递的就是过滤器
    File[] listFiles(FileFilter filter)
    java.io.FileFilter接口:用于抽象路径名(File对象)的过滤器。
        作用:用来过滤文件(File对象)
        抽象方法:用来过滤文件的方法
            boolean accept(File pathname) 测试指定抽象路径名是否应该包含在某个路径名列表中。
            参数:
                File pathname:使用ListFiles方法遍历目录,得到的每一个文件对象
    File[] listFiles(FilenameFilter filter)
    java.io.FilenameFilter接口:实现此接口的类实例可用于过滤器文件名。
        作用:用于过滤文件名称
        抽象方法:用来过滤文件的方法
            boolean accept(File dir, String name) 测试指定文件是否应该包含在某一文件列表中。
            参数:
                File dir:构造方法中传递的被遍历的目录
                String name:使用ListFiles方法遍历目录,获取的每一个文件/文件夹的名称
    注意:
        两个过滤器接口是没有实现类的,需要我们自己写实现类,重写过滤的方法accept,在方法中自己定义过滤的规则
 */
public class Demo01Filter {
    public static void main(String[] args) {
        File file = new File("G:\\IdeaProjects\\advanced-code\\08_FileAndRecursion");
        getAllFile(file);
    }

    /*
        定义一个方法,参数传递File类型的目录
        方法中对目录进行遍历
     */
    public static void getAllFile(File dir){
        File[] files = dir.listFiles(new FileFilterImpl());//传递过滤器对象
        for (File f : files) {
            //对遍历得到的File对象f进行判断,判断是否是文件夹
            if(f.isDirectory()){
                //f是一个文件夹,则继续遍历这个文件夹
                //我们发现getAllFile方法就是传递文件夹,遍历文件夹的方法
                //所以直接调用getAllFile方法即可:递归(自己调用自己)
                getAllFile(f);
            }else{
                //f是一个文件,直接打印即可
                System.out.println(f);
            }
        }
    }
}
package com.itheima.demo03Filter;

import java.io.File;
import java.io.FileFilter;

/*
    创建过滤器FileFilter的实现类,重写过滤方法accept,定义过滤规则
 */
public class FileFilterImpl implements FileFilter{
    @Override
    public boolean accept(File pathname) {
        /*
            过滤的规则:
            在accept方法中,判断File对象是否是以.java结尾
            是就返回true
            不是就返回false
         */
        //如果pathname是一个文件夹,返回true,继续遍历这个文件夹
        if(pathname.isDirectory()){
            return true;
        }

        return pathname.getName().toLowerCase().endsWith(".java");
    }
}
```

### Demo01 文件过滤器的lambda优化 ###

```java
javapackage com.itheima.demo03Filter;

import java.io.File;

public class Demo02Filter {
    public static void main(String[] args) {
        File file = new File("c:\\abc");
        getAllFile(file);
    }

    /*
        定义一个方法,参数传递File类型的目录
        方法中对目录进行遍历
     */
    public static void getAllFile(File dir){
        //传递过滤器对象 使用匿名内部类
        /*File[] files = dir.listFiles(new FileFilter() {
            @Override
            public boolean accept(File pathname) {
                //过滤规则,pathname是文件夹或者是.java结尾的文件返回true
                return pathname.isDirectory() || pathname.getName().toLowerCase().endsWith(".java");
            }
        });*/

        //使用Lambda表达式优化匿名内部类(接口中只有一个抽象方法)
        /*File[] files = dir.listFiles((File pathname)->{
            return pathname.isDirectory() || pathname.getName().toLowerCase().endsWith(".java");
        });*/

        File[] files = dir.listFiles(pathname->pathname.isDirectory() || pathname.getName().toLowerCase().endsWith(".java"));

        /*File[] files = dir.listFiles(new FilenameFilter() {
            @Override
            public boolean accept(File dir, String name) {
                //过滤规则,pathname是文件夹或者是.java结尾的文件返回true
                return new File(dir,name).isDirectory() || name.toLowerCase().endsWith(".java");
            }
        });*/

        //使用Lambda表达式优化匿名内部类(接口中只有一个抽象方法)
        /*File[] files = dir.listFiles((File d, String name)->{
            //过滤规则,pathname是文件夹或者是.java结尾的文件返回true
            return new File(d,name).isDirectory() || name.toLowerCase().endsWith(".java");
        });*/

        //File[] files = dir.listFiles((d,name)->new File(d,name).isDirectory() || name.toLowerCase().endsWith(".java"));

        for (File f : files) {
            //对遍历得到的File对象f进行判断,判断是否是文件夹
            if(f.isDirectory()){
                //f是一个文件夹,则继续遍历这个文件夹
                //我们发现getAllFile方法就是传递文件夹,遍历文件夹的方法
                //所以直接调用getAllFile方法即可:递归(自己调用自己)
                getAllFile(f);
            }else{
                //f是一个文件,直接打印即可
                System.out.println(f);
            }
        }
    }
}
```

# day09【字节流、字符流】 #

## 第二章 字节流 ##

### Demo01FileOutputStream  字节输出流/一次写一个字节 ###

```java
package com.itheima.demo01.OutputStream;

import java.io.FileOutputStream;
import java.io.IOException;

/*
    java.io.OutputStream:字节输出流
        此抽象类是表示输出字节流的所有类的超类。

    定义了一些子类共性的成员方法:
        - public void close() ：关闭此输出流并释放与此流相关联的任何系统资源。
        - public void flush() ：刷新此输出流并强制任何缓冲的输出字节被写出。
        - public void write(byte[] b)：将 b.length字节从指定的字节数组写入此输出流。
        - public void write(byte[] b, int off, int len) ：从指定的字节数组写入 len字节，从偏移量 off开始输出到此输出流。
        - public abstract void write(int b) ：将指定的字节输出流。

    java.io.FileOutputStream extends OutputStream
    FileOutputStream:文件字节输出流
    作用:把内存中的数据写入到硬盘的文件中

    构造方法:
        FileOutputStream(String name)创建一个向具有指定名称的文件中写入数据的输出文件流。
        FileOutputStream(File file) 创建一个向指定 File 对象表示的文件中写入数据的文件输出流。
        参数:写入数据的目的
            String name:目的地是一个文件的路径
            File file:目的地是一个文件
        构造方法的作用:
            1.创建一个FileOutputStream对象
            2.会根据构造方法中传递的文件/文件路径,创建一个空的文件
            3.会把FileOutputStream对象指向创建好的文件

    写入数据的原理(内存-->硬盘)
        java程序-->JVM(java虚拟机)-->OS(操作系统)-->OS调用写数据的方法-->把数据写入到文件中

    字节输出流的使用步骤(重点):
        1.创建一个FileOutputStream对象,构造方法中传递写入数据的目的地
        2.调用FileOutputStream对象中的方法write,把数据写入到文件中
        3.释放资源(流使用会占用一定的内存,使用完毕要把内存清空,提供程序的效率)
 */
public class Demo01OutputStream {
    public static void main(String[] args) throws IOException {
        //1.创建一个FileOutputStream对象,构造方法中传递写入数据的目的地
        FileOutputStream fos = new FileOutputStream("09_IOAndProperties\\a.txt");
        //2.调用FileOutputStream对象中的方法write,把数据写入到文件中
        //public abstract void write(int b) ：将指定的字节输出流。
        fos.write(97);
        //3.释放资源(流使用会占用一定的内存,使用完毕要把内存清空,提供程序的效率)
        fos.close();
    }
}
```

### Demo02FileOutputStream 一次写多个字节 ###

```java
jpackage com.itheima.demo01.OutputStream;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Arrays;

/*
    一次写多个字节的方法:
        - public void write(byte[] b)：将 b.length字节从指定的字节数组写入此输出流。
        - public void write(byte[] b, int off, int len) ：从指定的字节数组写入 len字节，从偏移量 off开始输出到此输出流。
 */
public class Demo02OutputStream {
    public static void main(String[] args) throws IOException {
        //创建FileOutputStream对象,构造方法中绑定要写入数据的目的地
        FileOutputStream fos = new FileOutputStream(new File("09_IOAndProperties\\b.txt"));
        //调用FileOutputStream对象中的方法write,把数据写入到文件中
        //在文件中显示100,写个字节
        fos.write(49);
        fos.write(48);
        fos.write(48);

        /*
            public void write(byte[] b)：将 b.length字节从指定的字节数组写入此输出流。
            一次写多个字节:
                如果写的第一个字节是正数(0-127),那么显示的时候会查询ASCII表
                如果写的第一个字节是负数,那第一个字节会和第二个字节,两个字节组成一个中文显示,查询系统默认码表(GBK)
                utf-8中3个字节是一个中文,GBK中两个字节是一个中文
         */
        byte[] bytes = {65,66,67,68,69};//ABCDE
        //byte[] bytes = {-65,-66,-67,68,69};//烤紻E
        fos.write(bytes);

        /*
            public void write(byte[] b, int off, int len) ：把字节数组的一部分写入到文件中
                int off:数组的开始索引
                int len:写几个字节
         */
        fos.write(bytes,1,2);//BC

        /*
            写入字符的方法:可以使用String类中的方法把字符串,转换为字节数组
                byte[] getBytes()  把字符串转换为字节数组
         */
        byte[] bytes2 = "你好".getBytes();
        System.out.println(Arrays.toString(bytes2));//[-28, -67, -96, -27, -91, -67]
        fos.write(bytes2);

        //释放资源
        fos.close();
    }
}
```

### Demo03OutputStream 续写/换行写 ###

```java
package com.itheima.demo01.OutputStream;

import java.io.FileOutputStream;
import java.io.IOException;

/*
    追加写/续写:使用两个参数的构造方法
        FileOutputStream(String name, boolean append)创建一个向具有指定 name 的文件中写入数据的输出文件流。
        FileOutputStream(File file, boolean append) 创建一个向指定 File 对象表示的文件中写入数据的文件输出流。
        参数:
           String name,File file:写入数据的目的地
           boolean append:追加写开关
            true:创建对象不会覆盖源文件,继续在文件的末尾追加写数据
            false:创建一个新文件,覆盖源文件
    写换行:写换行符号
        windows:\r\n
        linux:/n
        mac:/r
 */
public class Demo03OutputStream {
    public static void main(String[] args) throws IOException {
        FileOutputStream fos = new FileOutputStream("09_IOAndProperties\\c.txt",true);
        for (int i = 1; i <=10 ; i++) {
            fos.write("你好".getBytes());
            fos.write("\r\n".getBytes());
        }

        fos.close();
    }
}
```

### Demo01InputStream 字节输入流/读取一个字节 ###

```java
package com.itheima.demo02.InputStream;

import java.io.FileInputStream;
import java.io.IOException;

/*
    java.io.InputStream:字节输入流
    此抽象类是表示字节输入流的所有类的超类。

    定义了所有子类共性的方法: 
    	 read()返回读取字节/read(byte[] b)返回读取有效字节的个数
         int read()从输入流中读取数据的下一个字节。
         int read(byte[] b) 从输入流中读取一定数量的字节，并将其存储在缓冲区数组 b 中。
         void close() 关闭此输入流并释放与该流关联的所有系统资源。

    java.io.FileInputStream extends InputStream
    FileInputStream:文件字节输入流
    作用:把硬盘文件中的数据,读取到内存中使用

    构造方法:
        FileInputStream(String name)
        FileInputStream(File file)
        参数:读取文件的数据源
            String name:文件的路径
            File file:文件
        构造方法的作用:
            1.会创建一个FileInputStream对象
            2.会把FileInputStream对象指定构造方法中要读取的文件

    读取数据的原理(硬盘-->内存)
        java程序-->JVM-->OS-->OS读取数据的方法-->读取文件

    字节输入流的使用步骤(重点):
        1.创建FileInputStream对象,构造方法中绑定要读取的数据源
        2.使用FileInputStream对象中的方法read,读取文件
        3.释放资源
 */
public class Demo01InputStream {
    public static void main(String[] args) throws IOException {
        //1.创建FileInputStream对象,构造方法中绑定要读取的数据源
        FileInputStream fis = new FileInputStream("09_IOAndProperties\\c.txt");
        //2.使用FileInputStream对象中的方法read,读取文件
        //int read()读取文件中的一个字节并返回,读取到文件的末尾返回-1
        /*int len = fis.read();
        System.out.println(len);//97 a

        len = fis.read();
        System.out.println(len);// 98 b

        len = fis.read();
        System.out.println(len);//99 c

        len = fis.read();
        System.out.println(len);//-1

        len = fis.read();
        System.out.println(len);//-1*/

        /*
            发现以上读取文件是一个重复的过程,所以可以使用循环优化
            不知道文件中有多少字节,使用while循环
            while循环结束条件,读取到-1的时候结束

            布尔表达式(len = fis.read())!=-1
                1.fis.read():读取一个字节
                2.len = fis.read():把读取到的字节赋值给变量len
                3.(len = fis.read())!=-1:判断变量len是否不等于-1
         */
        int len = 0; //记录读取到的字节
        while((len = fis.read())!=-1){
            System.out.print(len);//abc
        }
        //3.释放资源
        fis.close();
    }
}
```

### Demo02InputStream 字节输入流/读取多个字节 ###

```java
package com.itheima.demo02.InputStream;

import java.io.FileInputStream;
import java.io.IOException;

/*
    字节输入流一次读取多个字节的方法:
        int read(byte[] b) 从输入流中读取一定数量的字节，并将其存储在缓冲区数组 b 中。
    明确两件事情:
        1.方法的参数byte[]的作用?
            起到缓冲作用,存储每次读取到的多个字节
            数组的长度一把定义为1024(1kb)或者1024的整数倍
        2.方法的返回值int是什么?
            每次读取的有效字节个数

    String类的构造方法
        String(byte[] bytes) :把字节数组转换为字符串
        String(byte[] bytes, int offset, int length) 把字节数组的一部分转换为字符串 offset:数组的开始索引 length:转换的字节个数
 */
public class Demo02InputStream {
    public static void main(String[] args) throws IOException {
        //创建FileInputStream对象,构造方法中绑定要读取的数据源
        FileInputStream fis = new FileInputStream("09_IOAndProperties\\b.txt");
        //使用FileInputStream对象中的方法read读取文件
        //int read(byte[] b) 从输入流中读取一定数量的字节，并将其存储在缓冲区数组 b 中。
        /*byte[] bytes = new byte[2];
        int len = fis.read(bytes);
        System.out.println(len);//2
        //System.out.println(Arrays.toString(bytes));//[65, 66]
        System.out.println(new String(bytes));//AB

        len = fis.read(bytes);
        System.out.println(len);//2
        System.out.println(new String(bytes));//CD

        len = fis.read(bytes);
        System.out.println(len);//1
        System.out.println(new String(bytes));//ED

        len = fis.read(bytes);
        System.out.println(len);//-1
        System.out.println(new String(bytes));//ED*/

        /*
            发现以上读取时一个重复的过程,可以使用循环优化
            不知道文件中有多少字节,所以使用while循环
            while循环结束的条件,读取到-1结束
         */
        byte[] bytes = new byte[1024];//存储读取到的多个字节
        int len = 0; //记录每次读取的有效字节个数
        while((len = fis.read(bytes))!=-1){
            //String(byte[] bytes, int offset, int length) 把字节数组的一部分转换为字符串 offset:数组的开始索引 length:转换的字节个数
            System.out.println(new String(bytes,0,len));//只循环了一次 1024很大
            System.out.println(len); 

        }

        //释放资源
        fis.close();
    }
}
```

### Demo01CopyFile 输入输出流复制文件 ###

```java
package com.itheima.demo03.CopyFile;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

/*
    文件复制练习:一读一写

    明确:
        数据源: c:\\1.jpg
        数据的目的地: d:\\1.jpg

    文件复制的步骤:
        1.创建一个字节输入流对象,构造方法中绑定要读取的数据源
        2.创建一个字节输出流对象,构造方法中绑定要写入的目的地
        3.使用字节输入流对象中的方法read读取文件
        4.使用字节输出流中的方法write,把读取到的字节写入到目的地的文件中
        5.释放资源
 */
public class Demo01CopyFile {
    public static void main(String[] args) throws IOException {
        long s = System.currentTimeMillis();
        //1.创建一个字节输入流对象,构造方法中绑定要读取的数据源
        FileInputStream fis = new FileInputStream("09_IOAndProperties\\1.bmp");
        //2.创建一个字节输出流对象,构造方法中绑定要写入的目的地
        FileOutputStream fos = new FileOutputStream("09_IOAndProperties\\2.jpg");
        //一次读取一个字节写入一个字节的方式
        //3.使用字节输入流对象中的方法read读取文件
        /*int len = 0;
        while((len = fis.read())!=-1){
            //4.使用字节输出流中的方法write,把读取到的字节写入到目的地的文件中
            fos.write(len);
        }*/
        //使用数组缓冲读取多个字节,写入多个字节
        byte[] bytes = new byte[1024];
        //3.使用字节输入流对象中的方法read读取文件
        int len = 0;//每次读取的有效字节个数
        while((len = fis.read(bytes))!=-1){
            //4.使用字节输出流中的方法write,把读取到的字节写入到目的地的文件中
            fos.write(bytes,0,len);
        }
        //5.释放资源(先关写的,后关闭读的;如果写完了,肯定读取完毕了)
        fos.close();
        fis.close();
        long e = System.currentTimeMillis();
        System.out.println("复制文件共耗时:"+(e-s)+"毫秒");
    }
}
```

## 第三章 字符流 ##

### Demo02FileReader 字符输入流/一次读取一个字节 ###

```java
package com.itheima.Demo04.Reader;

import java.io.FileReader;
import java.io.IOException;

/*
    java.io.Reader:字符输入流,是字符输入流的最顶层的父类,定义了一些共性的成员方法,是一个抽象类

    共性的成员方法:
        int read() 读取单个字符并返回。
        int read(char[] cbuf)一次读取多个字符,将字符读入数组。
        void close() 关闭该流并释放与之关联的所有资源。

    java.io.FileReader extends InputStreamReader extends Reader
    FileReader:文件字符输入流
    作用:把硬盘文件中的数据以字符的方式读取到内存中

    构造方法:
        FileReader(String fileName)
        FileReader(File file)
        参数:读取文件的数据源
            String fileName:文件的路径
            File file:一个文件
        FileReader构造方法的作用:
            1.创建一个FileReader对象
            2.会把FileReader对象指向要读取的文件
    字符输入流的使用步骤:
        1.创建FileReader对象,构造方法中绑定要读取的数据源
        2.使用FileReader对象中的方法read读取文件
        3.释放资源
 */
public class Demo02Reader {
    public static void main(String[] args) throws IOException {
        //1.创建FileReader对象,构造方法中绑定要读取的数据源
        FileReader fr = new FileReader("09_IOAndProperties\\c.txt");
        //2.使用FileReader对象中的方法read读取文件
        //int read() 读取单个字符并返回。
        /*int len = 0;
        while((len = fr.read())!=-1){
            System.out.print((char)len);
        }*/

        //int read(char[] cbuf)一次读取多个字符,将字符读入数组。
        char[] cs = new char[1024];//存储读取到的多个字符
        int len = 0;//记录的是每次读取的有效字符个数
        while((len = fr.read(cs))!=-1){
            /*
                String类的构造方法
                String(char[] value) 把字符数组转换为字符串
                String(char[] value, int offset, int count) 把字符数组的一部分转换为字符串 offset数组的开始索引 count转换的个数
             */
            System.out.println(new String(cs,0,len));
        }

        //3.释放资源
        fr.close();
    }
}
```

### Demo01FileWriter 字符输出流/不同于字节先写内存后flush ###

```java
package com.itheima.Demo05Writer;

import java.io.FileWriter;
import java.io.IOException;

/*
    java.io.Writer:字符输出流,是所有字符输出流的最顶层的父类,是一个抽象类

    共性的成员方法:
        - void write(int c) 写入单个字符。
        - void write(char[] cbuf)写入字符数组。
        - abstract  void write(char[] cbuf, int off, int len)写入字符数组的某一部分,off数组的开始索引,len写的字符个数。
        - void write(String str)写入字符串。
        - void write(String str, int off, int len) 写入字符串的某一部分,off字符串的开始索引,len写的字符个数。
        - void flush()刷新该流的缓冲。
        - void close() 关闭此流，但要先刷新它。

    java.io.FileWriter extends OutputStreamWriter extends Writer
    FileWriter:文件字符输出流
    作用:把内存中字符数据写入到文件中

    构造方法:
        FileWriter(File file)根据给定的 File 对象构造一个 FileWriter 对象。
        FileWriter(String fileName) 根据给定的文件名构造一个 FileWriter 对象。
        参数:写入数据的目的地
            String fileName:文件的路径
            File file:是一个文件
        构造方法的作用:
            1.会创建一个FileWriter对象
            2.会根据构造方法中传递的文件/文件的路径,创建文件
            3.会把FileWriter对象指向创建好的文件

    字符输出流的使用步骤(重点):
        1.创建FileWriter对象,构造方法中绑定要写入数据的目的地
        2.使用FileWriter中的方法write,把数据写入到内存缓冲区中(字符转换为字节的过程)
        3.使用FileWriter中的方法flush,把内存缓冲区中的数据,刷新到文件中
        4.释放资源(会先把内存缓冲区中的数据刷新到文件中)
 */
public class Demo01Writer {
    public static void main(String[] args) throws IOException {
        //1.创建FileWriter对象,构造方法中绑定要写入数据的目的地
        FileWriter fw = new FileWriter("09_IOAndProperties\\d.txt");
        //2.使用FileWriter中的方法write,把数据写入到内存缓冲区中(字符转换为字节的过程)
        //void write(int c) 写入单个字符。
        fw.write(97);
        //3.使用FileWriter中的方法flush,把内存缓冲区中的数据,刷新到文件中
        //fw.flush();
        //4.释放资源(会先把内存缓冲区中的数据刷新到文件中)
        fw.close();
    }
}
```

### Demo02CloseAndFlush 的区别 ###

```java
jpackage com.itheima.Demo05Writer;

import java.io.FileWriter;
import java.io.IOException;

/*
    flush方法和close方法的区别
        - flush ：刷新缓冲区，流对象可以继续使用。
        - close:  先刷新缓冲区，然后通知系统释放资源。流对象不可以再被使用了。
 */
public class Demo02CloseAndFlush {
    public static void main(String[] args) throws IOException {
        //1.创建FileWriter对象,构造方法中绑定要写入数据的目的地
        FileWriter fw = new FileWriter("09_IOAndProperties\\e.txt");
        //2.使用FileWriter中的方法write,把数据写入到内存缓冲区中(字符转换为字节的过程)
        //void write(int c) 写入单个字符。
        fw.write(97);
        fw.write(97);
        //3.使用FileWriter中的方法flush,把内存缓冲区中的数据,刷新到文件中
        fw.flush();
        //刷新之后流可以继续使用
        fw.write(98);

        //4.释放资源(会先把内存缓冲区中的数据刷新到文件中)
        fw.close();

        //close方法之后流已经关闭了,已经从内存中消失了,流就不能再使用了
        fw.write(99);//IOException: Stream closed
    }
}
```

### Demo03Writer 字符输出流写数据的其他方法 ###

```java
package com.itheima.Demo05Writer;

import java.io.FileWriter;
import java.io.IOException;

/*
    字符输出流写数据的其他方法
        - void write(char[] cbuf)写入字符数组。
        - abstract  void write(char[] cbuf, int off, int len)写入字符数组的某一部分,off数组的开始索引,len写的字符个数。
        - void write(String str)写入字符串。
        - void write(String str, int off, int len) 写入字符串的某一部分,off字符串的开始索引,len写的字符个数。
 */
public class Demo03Writer {
    public static void main(String[] args) throws IOException {
        FileWriter fw = new FileWriter("09_IOAndProperties\\f.txt");
        char[] cs = {'a','b','c','d','e'};
        //void write(char[] cbuf)写入字符数组。
        fw.write(cs);//abcde

        //void write(char[] cbuf, int off, int len)写入字符数组的某一部分,off数组的开始索引,len写的字符个数。
        fw.write(cs,1,3);//bcd

        //void write(String str)写入字符串。
        fw.write("传智播客");//传智播客

        //void write(String str, int off, int len) 写入字符串的某一部分,off字符串的开始索引,len写的字符个数。
        fw.write("黑马程序员",2,3);//程序员

        fw.close();
    }
}
```

### Demo04Writer 续写/换行 ###

```java
j'apackage com.itheima.Demo05Writer;

import java.io.FileWriter;
import java.io.IOException;

/*
    续写和换行
    续写,追加写:使用两个参数的构造方法
        FileWriter(String fileName, boolean append)
        FileWriter(File file, boolean append)
        参数:
            String fileName,File file:写入数据的目的地
            boolean append:续写开关 true:不会创建新的文件覆盖源文件,可以续写; false:创建新的文件覆盖源文件
     换行:换行符号
        windows:\r\n
        linux:/n
        mac:/r
 */
public class Demo04Writer {
    public static void main(String[] args) throws IOException {
        FileWriter fw = new FileWriter("09_IOAndProperties\\g.txt",true);
        for (int i = 0; i <10 ; i++) {
            fw.write("HelloWorld"+i+"\r\n");
        }

        fw.close();
    }
}
```

## 第四章 IO异常的处理 ##

### Demo01 Try Catch处理异常 ###

```java
package com.itheima.demo06.trycatch;

import java.io.FileWriter;
import java.io.IOException;

/*
    在jdk1.7之前使用try catch finally 处理流中的异常
    格式:
        try{
            可能会产出异常的代码
        }catch(异常类变量 变量名){
            异常的处理逻辑
        }finally{
            一定会指定的代码
            资源释放
        }
 */
public class Demo01TryCatch {
    public static void main(String[] args) {
        //提高变量fw的作用域,让finally可以使用
        //变量在定义的时候,可以没有值,但是使用的时候必须有值
        //fw = new FileWriter("09_IOAndProperties\\g.txt",true); 执行失败,fw没有值,fw.close会报错 给一个初始化的null
        FileWriter fw = null;
        try{
            //可能会产出异常的代码
            fw = new FileWriter("09_IOAndProperties\\g.txt",true);
            for (int i = 0; i <10 ; i++) {
                fw.write("HelloWorld"+i+"\r\n");
            }
        }catch(IOException e){
            //异常的处理逻辑
            System.out.println(e);
        }finally {
            //一定会指定的代码
            //创建对象失败了,fw的默认值就是null,null是不能调用方法的,会抛出NullPointerException,需要增加一个判断,不是null在把资源释放
            if(fw!=null){
                try {
                    //fw.close方法声明抛出了IOException异常对象,所以我们就的处理这个异常对象,要么throws,要么try catch
                    fw.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

### Demo02   JDK7/JDK9的新特性 ###

```java
package com.itheima.demo06.trycatch;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

/*
    JDK7的新特性
    在try的后边可以增加一个(),在括号中可以定义流对象
    那么这个流对象的作用域就在try中有效
    try中的代码执行完毕,会自动把流对象释放,不用写finally
    格式:
        try(定义流对象;定义流对象....){
            可能会产出异常的代码
        }catch(异常类变量 变量名){
            异常的处理逻辑
        }
 */
public class Demo02JDK7 {
    public static void main(String[] args) {
        try(//1.创建一个字节输入流对象,构造方法中绑定要读取的数据源
            FileInputStream fis = new FileInputStream("c:\\1.jpg");
            //2.创建一个字节输出流对象,构造方法中绑定要写入的目的地
            FileOutputStream fos = new FileOutputStream("d:\\1.jpg");){

            //可能会产出异常的代码
            //一次读取一个字节写入一个字节的方式
            //3.使用字节输入流对象中的方法read读取文件
            int len = 0;
            while((len = fis.read())!=-1){
                //4.使用字节输出流中的方法write,把读取到的字节写入到目的地的文件中
                fos.write(len);
            }

        }catch (IOException e){
            //异常的处理逻辑
            System.out.println(e);
        }
    }
}
package com.itheima.demo06.trycatch;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

/*
    JDK9新特性
    try的前边可以定义流对象
    在try后边的()中可以直接引入流对象的名称(变量名)
    在try代码执行完毕之后,流对象也可以释放掉,不用写finally
    格式:
        A a = new A();
        B b = new B();
        try(a,b){
            可能会产出异常的代码
        }catch(异常类变量 变量名){
            异常的处理逻辑
        }
 */
public class Demo03JDK9 {
    public static void main(String[] args) throws IOException {
        //1.创建一个字节输入流对象,构造方法中绑定要读取的数据源
        FileInputStream fis = new FileInputStream("c:\\1.jpg");
        //2.创建一个字节输出流对象,构造方法中绑定要写入的目的地
        FileOutputStream fos = new FileOutputStream("d:\\1.jpg");

        try(fis;fos){
            //一次读取一个字节写入一个字节的方式
            //3.使用字节输入流对象中的方法read读取文件
            int len = 0;
            while((len = fis.read())!=-1){
                //4.使用字节输出流中的方法write,把读取到的字节写入到目的地的文件中
                fos.write(len);
            }
        }catch (IOException e){
            System.out.println(e);
        }

        //fos.write(1);//Stream Closed

    }
}
```

## 第五章 属性集 ##

### Demo01 Properties集合是一个唯一和IO流相结合的集合 ###

```java
package com.itheima.demo07.Prop;

import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;
import java.util.Set;

/*
    java.util.Properties集合 extends Hashtable<k,v> implements Map<k,v>
    Properties 类表示了一个持久的属性集。Properties 可保存在流中或从流中加载。
    Properties集合是一个唯一和IO流相结合的集合
        可以使用Properties集合中的方法store,把集合中的临时数据,持久化写入到硬盘中存储
        可以使用Properties集合中的方法load,把硬盘中保存的文件(键值对),读取到集合中使用

    属性列表中每个键及其对应值都是一个字符串。
        Properties集合是一个双列集合,key和value默认都是字符串
 */
public class Demo01Properties {
    public static void main(String[] args) throws IOException {
        show03();
    }

    /*
        可以使用Properties集合中的方法load,把硬盘中保存的文件(键值对),读取到集合中使用
        void load(InputStream inStream)
        void load(Reader reader)
        参数:
            InputStream inStream:字节输入流,不能读取含有中文的键值对
            Reader reader:字符输入流,能读取含有中文的键值对
        使用步骤:
            1.创建Properties集合对象
            2.使用Properties集合对象中的方法load读取保存键值对的文件
            3.遍历Properties集合
        注意:
            1.存储键值对的文件中,键与值默认的连接符号可以使用=,空格(其他符号)
            2.存储键值对的文件中,可以使用#进行注释,被注释的键值对不会再被读取
            3.存储键值对的文件中,键与值默认都是字符串,不用再加引号
     */
//    #save data
//    #Sun Aug 08 07:39:28 CST 2088
//    赵丽颖=168
//    迪丽热巴 165
//    #古力娜扎=160
    private static void show03() throws IOException {
        //1.创建Properties集合对象
        Properties prop = new Properties();
        //2.使用Properties集合对象中的方法load读取保存键值对的文件
        prop.load(new FileReader("09_IOAndProperties\\prop.txt"));
        //prop.load(new FileInputStream("09_IOAndProperties\\prop.txt"));
        //3.遍历Properties集合
        Set<String> set = prop.stringPropertyNames();
        for (String key : set) {
            String value = prop.getProperty(key);
            System.out.println(key+"="+value);//赵丽颖=168 迪丽热巴 165
        }
    }

    /*
        可以使用Properties集合中的方法store,把集合中的临时数据,持久化写入到硬盘中存储
        void store(OutputStream out, String comments)
        void store(Writer writer, String comments)
        参数:
            OutputStream out:字节输出流,不能写入中文
            Writer writer:字符输出流,可以写中文
            String comments:注释,用来解释说明保存的文件是做什么用的
                    不能使用中文,会产生乱码,默认是Unicode编码
                    一般使用""空字符串

        使用步骤:
            1.创建Properties集合对象,添加数据
            2.创建字节输出流/字符输出流对象,构造方法中绑定要输出的目的地
            3.使用Properties集合中的方法store,把集合中的临时数据,持久化写入到硬盘中存储
            4.释放资源
     */
    private static void show02() throws IOException {
        //1.创建Properties集合对象,添加数据
        Properties prop = new Properties();
        prop.setProperty("赵丽颖","168");
        prop.setProperty("迪丽热巴","165");
        prop.setProperty("古力娜扎","160");

        //2.创建字节输出流/字符输出流对象,构造方法中绑定要输出的目的地
        //FileWriter fw = new FileWriter("09_IOAndProperties\\prop.txt");

        //3.使用Properties集合中的方法store,把集合中的临时数据,持久化写入到硬盘中存储
        //prop.store(fw,"save data");

        //4.释放资源
        //fw.close();

        prop.store(new FileOutputStream("09_IOAndProperties\\prop2.txt"),"");
    }

    /*
        使用Properties集合存储数据,遍历取出Properties集合中的数据
        Properties集合是一个双列集合,key和value默认都是字符串
        Properties集合有一些操作字符串的特有方法
            Object setProperty(String key, String value) 调用 Hashtable 的方法 put。
            String getProperty(String key) 通过key找到value值,此方法相当于Map集合中的get(key)方法
            Set<String> stringPropertyNames() 返回此属性列表中的键集，其中该键及其对应值是字符串,此方法相当于Map集合中的keySet方法
     */
    private static void show01() {
        //创建Properties集合对象
        Properties prop = new Properties();
        //使用setProperty往集合中添加数据
        prop.setProperty("赵丽颖","168");
        prop.setProperty("迪丽热巴","165");
        prop.setProperty("古力娜扎","160");
        //prop.put(1,true);

        //使用stringPropertyNames把Properties集合中的键取出,存储到一个Set集合中
        Set<String> set = prop.stringPropertyNames();

        //遍历Set集合,取出Properties集合的每一个键
        for (String key : set) {
            //使用getProperty方法通过key获取value
            String value = prop.getProperty(key);
            System.out.println(key+"="+value);
        }
    }
}
```

# day10【缓冲流、转换流、序列化流】 #

## 第一章 缓冲流 ##

### Demo01BufferedOutputStream 字节缓冲输出流 ###

```java
package com.itheima.demo01.BufferedStream;

import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;

/*
    java.io.BufferedOutputStream extends OutputStream
    BufferedOutputStream:字节缓冲输出流

    继承自父类的共性成员方法:
        - public void close() ：关闭此输出流并释放与此流相关联的任何系统资源。
        - public void flush() ：刷新此输出流并强制任何缓冲的输出字节被写出。
        - public void write(byte[] b)：将 b.length字节从指定的字节数组写入此输出流。
        - public void write(byte[] b, int off, int len) ：从指定的字节数组写入 len字节，从偏移量 off开始输出到此输出流。
        - public abstract void write(int b) ：将指定的字节输出流。

     构造方法:
        BufferedOutputStream(OutputStream out)  创建一个新的缓冲输出流，以将数据写入指定的底层输出流。
        BufferedOutputStream(OutputStream out, int size)  创建一个新的缓冲输出流，以将具有指定缓冲区大小的数据写入指定的底层输出流。
        参数:
           OutputStream out:字节输出流
                我们可以传递FileOutputStream,缓冲流会给FileOutputStream增加一个缓冲区,提高FileOutputStream的写入效率
           int size:指定缓冲流内部缓冲区的大小,不指定默认
     使用步骤(重点)
        1.创建FileOutputStream对象,构造方法中绑定要输出的目的地
        2.创建BufferedOutputStream对象,构造方法中传递FileOutputStream对象对象,提高FileOutputStream对象效率
        3.使用BufferedOutputStream对象中的方法write,把数据写入到内部缓冲区中
        4.使用BufferedOutputStream对象中的方法flush,把内部缓冲区中的数据,刷新到文件中
        5.释放资源(会先调用flush方法刷新数据,第4部可以省略)
 */
public class Demo01BufferedOutputStream {
    public static void main(String[] args) throws IOException {
        //1.创建FileOutputStream对象,构造方法中绑定要输出的目的地
        FileOutputStream fos = new FileOutputStream("10_IO\\a.txt");
        //2.创建BufferedOutputStream对象,构造方法中传递FileOutputStream对象对象,提高FileOutputStream对象效率
        BufferedOutputStream bos = new BufferedOutputStream(fos);
        //3.使用BufferedOutputStream对象中的方法write,把数据写入到内部缓冲区中
        bos.write("我把数据写入到内部缓冲区中".getBytes());
        //4.使用BufferedOutputStream对象中的方法flush,把内部缓冲区中的数据,刷新到文件中
        bos.flush();
        //5.释放资源(会先调用flush方法刷新数据,第4部可以省略)
        bos.close();
    }

}
```

### Demo02BufferedInputStream 字节缓冲输入流 ###

```java
package com.itheima.demo01.BufferedStream;

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.IOException;

/*
    java.io.BufferedInputStream extends InputStream
    BufferedInputStream:字节缓冲输入流

    继承自父类的成员方法:
        int read()从输入流中读取数据的下一个字节。
        int read(byte[] b) 从输入流中读取一定数量的字节，并将其存储在缓冲区数组 b 中。
        void close() 关闭此输入流并释放与该流关联的所有系统资源。

    构造方法:
        BufferedInputStream(InputStream in) 创建一个 BufferedInputStream 并保存其参数，即输入流 in，以便将来使用。
        BufferedInputStream(InputStream in, int size) 创建具有指定缓冲区大小的 BufferedInputStream 并保存其参数，即输入流 in，以便将来使用。
        参数:
            InputStream in:字节输入流
                我们可以传递FileInputStream,缓冲流会给FileInputStream增加一个缓冲区,提高FileInputStream的读取效率
            int size:指定缓冲流内部缓冲区的大小,不指定默认

    使用步骤(重点):
        1.创建FileInputStream对象,构造方法中绑定要读取的数据源
        2.创建BufferedInputStream对象,构造方法中传递FileInputStream对象,提高FileInputStream对象的读取效率
        3.使用BufferedInputStream对象中的方法read,读取文件
        4.释放资源
 */
public class Demo02BufferedInputStream {
    public static void main(String[] args) throws IOException {
        //1.创建FileInputStream对象,构造方法中绑定要读取的数据源
        FileInputStream fis = new FileInputStream("10_IO\\a.txt");
        //2.创建BufferedInputStream对象,构造方法中传递FileInputStream对象,提高FileInputStream对象的读取效率
        BufferedInputStream bis = new BufferedInputStream(fis);
        //3.使用BufferedInputStream对象中的方法read,读取文件
        //int read()从输入流中读取数据的下一个字节。
        /*int len = 0;//记录每次读取到的字节
        while((len = bis.read())!=-1){
            System.out.println(len);
        }*/

        //int read(byte[] b) 从输入流中读取一定数量的字节，并将其存储在缓冲区数组 b 中。
        byte[] bytes =new byte[1024];//存储每次读取的数据
        int len = 0; //记录每次读取的有效字节个数
        while((len = bis.read(bytes))!=-1){
            System.out.println(new String(bytes,0,len));
        }

        //4.释放资源
        bis.close();
    }
}
```

### Demo02CopyFile 缓冲输入输出复制文件 ###

```java
package com.itheima.demo02.CopyFile;

import java.io.*;

/*
    文件复制练习:一读一写

    明确:
        数据源: c:\\1.jpg
        数据的目的地: d:\\1.jpg
    文件复制的步骤:
        1.创建字节缓冲输入流对象,构造方法中传递字节输入流
        2.创建字节缓冲输出流对象,构造方法中传递字节输出流
        3.使用字节缓冲输入流对象中的方法read,读取文件
        4.使用字节缓冲输出流中的方法write,把读取的数据写入到内部缓冲区中
        5.释放资源(会先把缓冲区中的数据,刷新到文件中)

    文件的大小:780,831 字节
    一次读写一个字节:32毫秒
    使用数组缓冲读取多个字节,写入多个字节:5毫秒
 */
public class Demo02CopyFile {
    public static void main(String[] args) throws IOException {
        long s = System.currentTimeMillis();
        //1.创建字节缓冲输入流对象,构造方法中传递字节输入流
        BufferedInputStream bis = new BufferedInputStream(new FileInputStream("09_IOAndProperties\\1.jpg"));
        //2.创建字节缓冲输出流对象,构造方法中传递字节输出流
        BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream("09_IOAndProperties\\2.jpg"));
        //3.使用字节缓冲输入流对象中的方法read,读取文件
        //一次读取一个字节写入一个字节的方式
        /*int len = 0;
        while((len = bis.read())!=-1){
            bos.write(len);
        }*/

        //使用数组缓冲读取多个字节,写入多个字节
        byte[] bytes = new byte[1024];
        int len = 0;
        while((len = bis.read(bytes))!=-1){
            bos.write(bytes,0,len);
        }

        bos.close();
        bis.close();

        long e = System.currentTimeMillis();
        System.out.println("复制文件共耗时:"+(e-s)+"毫秒");
    }
}
```

### Demo03BufferedWriter 字符缓冲输出流 ###

```java
package com.itheima.demo01.BufferedStream;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

/*
    java.io.BufferedWriter extends Writer
    BufferedWriter:字符缓冲输出流

    继承自父类的共性成员方法:
        - void write(int c) 写入单个字符。
        - void write(char[] cbuf)写入字符数组。
        - abstract  void write(char[] cbuf, int off, int len)写入字符数组的某一部分,off数组的开始索引,len写的字符个数。
        - void write(String str)写入字符串。
        - void write(String str, int off, int len) 写入字符串的某一部分,off字符串的开始索引,len写的字符个数。
        - void flush()刷新该流的缓冲。
        - void close() 关闭此流，但要先刷新它。

    构造方法:
        BufferedWriter(Writer out) 创建一个使用默认大小输出缓冲区的缓冲字符输出流。
        BufferedWriter(Writer out, int sz) 创建一个使用给定大小输出缓冲区的新缓冲字符输出流。
        参数:
            Writer out:字符输出流
                我们可以传递FileWriter,缓冲流会给FileWriter增加一个缓冲区,提高FileWriter的写入效率
            int sz:指定缓冲区的大小,不写默认大小

    特有的成员方法:
        void newLine() 写入一个行分隔符。会根据不同的操作系统,获取不同的行分隔符
        换行:换行符号
        windows:\r\n
        linux:/n
        mac:/r
     使用步骤:
        1.创建字符缓冲输出流对象,构造方法中传递字符输出流
        2.调用字符缓冲输出流中的方法write,把数据写入到内存缓冲区中
        3.调用字符缓冲输出流中的方法flush,把内存缓冲区中的数据,刷新到文件中
        4.释放资源
 */
public class Demo03BufferedWriter {
    public static void main(String[] args) throws IOException {
        //System.out.println();
        //1.创建字符缓冲输出流对象,构造方法中传递字符输出流
        BufferedWriter bw = new BufferedWriter(new FileWriter("10_IO\\c.txt"));
        //2.调用字符缓冲输出流中的方法write,把数据写入到内存缓冲区中
        for (int i = 0; i <10 ; i++) {
            bw.write("传智播客");
            //bw.write("\r\n");
            bw.newLine();
        }
        //3.调用字符缓冲输出流中的方法flush,把内存缓冲区中的数据,刷新到文件中
        bw.flush();
        //4.释放资源
        bw.close();
    }
}
```

### Demo04BufferedReader 字符缓冲输入流 ###

```java
package com.itheima.demo01.BufferedStream;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/*
    java.io.BufferedReader extends Reader
    BufferedReader:字符缓冲输入流

    继承自父类的共性成员方法:
        int read() 读取单个字符并返回。
        int read(char[] cbuf)一次读取多个字符,将字符读入数组。
        void close() 关闭该流并释放与之关联的所有资源。

     构造方法:
        BufferedReader(Reader in)  创建一个使用默认大小输入缓冲区的缓冲字符输入流。
        BufferedReader(Reader in, int sz)     创建一个使用指定大小输入缓冲区的缓冲字符输入流。
        参数:
            Reader in:字符输入流
                我们可以传递FileReader,缓冲流会给FileReader增加一个缓冲区,提高FileReader的读取效率
     特有的成员方法:
        String readLine() 读取一个文本行。读取一行数据
            行的终止符号:通过下列字符之一即可认为某行已终止：换行 ('\n')、回车 ('\r') 或回车后直接跟着换行(\r\n)。
        返回值:
            包含该行内容的字符串，不包含任何行终止符，如果已到达流末尾，则返回 null

     使用步骤:
        1.创建字符缓冲输入流对象,构造方法中传递字符输入流
        2.使用字符缓冲输入流对象中的方法read/readLine读取文本
        3.释放资源
 */
public class Demo04BufferedReader {
    public static void main(String[] args) throws IOException {
        //1.创建字符缓冲输入流对象,构造方法中传递字符输入流
        BufferedReader br = new BufferedReader(new FileReader("10_IO\\c.txt"));

        //2.使用字符缓冲输入流对象中的方法read/readLine读取文本
        /*String line = br.readLine();
        System.out.println(line);

        line = br.readLine();
        System.out.println(line);*/
        /*
            发下以上读取是一个重复的过程,所以可以使用循环优化
            不知道文件中有多少行数据,所以使用while循环
            while的结束条件,读取到null结束
         */
        String line;
        while((line = br.readLine())!=null){
            System.out.println(line);
        }

        //3.释放资源
        br.close();
    }
}
```

### Demo05Test 文本排序 ###

```java
package com.itheima.demo01.BufferedStream;

import java.io.*;
import java.util.HashMap;

/*
    练习:
        对文本的内容进行排序
        按照(1,2,3....)顺序排序
    分析:
        1.创建一个HashMap集合对象,可以:存储每行文本的序号(1,2,3,..);value:存储每行的文本
        2.创建字符缓冲输入流对象,构造方法中绑定字符输入流
        3.创建字符缓冲输出流对象,构造方法中绑定字符输出流
        4.使用字符缓冲输入流中的方法readline,逐行读取文本
        5.对读取到的文本进行切割,获取行中的序号和文本内容
        6.把切割好的序号和文本的内容存储到HashMap集合中(key序号是有序的,会自动排序1,2,3,4..)
        7.遍历HashMap集合,获取每一个键值对
        8.把每一个键值对,拼接为一个文本行
        9.把拼接好的文本,使用字符缓冲输出流中的方法write,写入到文件中
        10.释放资源
 */
public class Demo05Test {
    public static void main(String[] args) throws IOException {
        //1.创建一个HashMap集合对象,可以:存储每行文本的序号(1,2,3,..);value:存储每行的文本
        HashMap<String,String> map = new HashMap<>();
        //2.创建字符缓冲输入流对象,构造方法中绑定字符输入流
        BufferedReader br = new BufferedReader(new FileReader("10_IO\\in.txt"));
        //3.创建字符缓冲输出流对象,构造方法中绑定字符输出流
        BufferedWriter bw = new BufferedWriter(new FileWriter("10_IO\\out.txt"));
        //4.使用字符缓冲输入流中的方法readline,逐行读取文本
        String line;
        while((line = br.readLine())!=null){
            //5.对读取到的文本进行切割,获取行中的序号和文本内容
            String[] arr = line.split("\\.");
            //6.把切割好的序号和文本的内容存储到HashMap集合中(key序号是有序的,会自动排序1,2,3,4..)
            map.put(arr[0],arr[1]);
        }

        //7.遍历HashMap集合,获取每一个键值对
        for(String key : map.keySet()){
            String value = map.get(key);
            //8.把每一个键值对,拼接为一个文本行
            line = key + "." + value;
            //9.把拼接好的文本,使用字符缓冲输出流中的方法write,写入到文件中
            bw.write(line);
            bw.newLine();//写换行
        }
        //10.释放资源
        bw.close();
        br.close();
    }
}
```

## 第二章 转换流 ##

### Demo02 OutputStreamWriter编码 指定编码表 ###

```java
j'a'vpackage com.itheima.demo03.ReverseStream;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;

/*
    java.io.OutputStreamWriter extends Writer
    OutputStreamWriter: 是字符流通向字节流的桥梁：可使用指定的 charset 将要写入流中的字符编码成字节。(编码:把能看懂的变成看不懂)

    继续自父类的共性成员方法:
        - void write(int c) 写入单个字符。
        - void write(char[] cbuf)写入字符数组。
        - abstract  void write(char[] cbuf, int off, int len)写入字符数组的某一部分,off数组的开始索引,len写的字符个数。
        - void write(String str)写入字符串。
        - void write(String str, int off, int len) 写入字符串的某一部分,off字符串的开始索引,len写的字符个数。
        - void flush()刷新该流的缓冲。
        - void close() 关闭此流，但要先刷新它。
    构造方法:
        OutputStreamWriter(OutputStream out)创建使用默认字符编码的 OutputStreamWriter。
        OutputStreamWriter(OutputStream out, String charsetName) 创建使用指定字符集的 OutputStreamWriter。
        参数:
            OutputStream out:字节输出流,可以用来写转换之后的字节到文件中
            String charsetName:指定的编码表名称,不区分大小写,可以是utf-8/UTF-8,gbk/GBK,...不指定默认使用UTF-8
    使用步骤:
        1.创建OutputStreamWriter对象,构造方法中传递字节输出流和指定的编码表名称
        2.使用OutputStreamWriter对象中的方法write,把字符转换为字节存储缓冲区中(编码)
        3.使用OutputStreamWriter对象中的方法flush,把内存缓冲区中的字节刷新到文件中(使用字节流写字节的过程)
        4.释放资源
 */
public class Demo02OutputStreamWriter {
    public static void main(String[] args) throws IOException {
        //write_utf_8();
        write_gbk();
    }

    /*
       使用转换流OutputStreamWriter写GBK格式的文件
    */
    private static void write_gbk() throws IOException {
        //1.创建OutputStreamWriter对象,构造方法中传递字节输出流和指定的编码表名称
        OutputStreamWriter osw = new OutputStreamWriter(new FileOutputStream("10_IO\\gbk.txt"),"GBK");
        //2.使用OutputStreamWriter对象中的方法write,把字符转换为字节存储缓冲区中(编码)
        osw.write("你好");
        //3.使用OutputStreamWriter对象中的方法flush,把内存缓冲区中的字节刷新到文件中(使用字节流写字节的过程)
        osw.flush();
        //4.释放资源
        osw.close();
    }

    /*
        使用转换流OutputStreamWriter写UTF-8格式的文件
     */
    private static void write_utf_8() throws IOException {
        //1.创建OutputStreamWriter对象,构造方法中传递字节输出流和指定的编码表名称
        //OutputStreamWriter osw = new OutputStreamWriter(new FileOutputStream("10_IO\\utf_8.txt"),"utf-8");
        OutputStreamWriter osw = new OutputStreamWriter(new FileOutputStream("10_IO\\utf_8.txt"));//不指定默认使用UTF-8
        //2.使用OutputStreamWriter对象中的方法write,把字符转换为字节存储缓冲区中(编码)
        osw.write("你好");
        //3.使用OutputStreamWriter对象中的方法flush,把内存缓冲区中的字节刷新到文件中(使用字节流写字节的过程)
        osw.flush();
        //4.释放资源
        osw.close();
    }
}
```

### Demo03 InputStreamReader解码 指定编码表 ###

```java
javapackage com.itheima.demo03.ReverseStream;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

/*
    java.io.InputStreamReader extends Reader
    InputStreamReader:是字节流通向字符流的桥梁：它使用指定的 charset 读取字节并将其解码为字符。(解码:把看不懂的变成能看懂的)

    继承自父类的共性成员方法:
        int read() 读取单个字符并返回。
        int read(char[] cbuf)一次读取多个字符,将字符读入数组。
        void close() 关闭该流并释放与之关联的所有资源。
    构造方法:
        InputStreamReader(InputStream in) 创建一个使用默认字符集的 InputStreamReader。
        InputStreamReader(InputStream in, String charsetName) 创建使用指定字符集的 InputStreamReader。
        参数:
            InputStream in:字节输入流,用来读取文件中保存的字节
            String charsetName:指定的编码表名称,不区分大小写,可以是utf-8/UTF-8,gbk/GBK,...不指定默认使用UTF-8
     使用步骤:
        1.创建InputStreamReader对象,构造方法中传递字节输入流和指定的编码表名称
        2.使用InputStreamReader对象中的方法read读取文件
        3.释放资源
     注意事项:
        构造方法中指定的编码表名称要和文件的编码相同,否则会发生乱码
 */
public class Demo03InputStreamReader {
    public static void main(String[] args) throws IOException {
        //read_utf_8();
        read_gbk();
    }


    /*
        使用InputStreamReader读取GBK格式的文件
     */
    private static void read_gbk() throws IOException {
        //1.创建InputStreamReader对象,构造方法中传递字节输入流和指定的编码表名称
        //InputStreamReader isr = new InputStreamReader(new FileInputStream("10_IO\\gbk.txt"),"UTF-8");//???
        InputStreamReader isr = new InputStreamReader(new FileInputStream("10_IO\\gbk.txt"),"GBK");//你好

        //2.使用InputStreamReader对象中的方法read读取文件
        int len = 0;
        while((len = isr.read())!=-1){
            System.out.println((char)len);
        }
        //3.释放资源
        isr.close();
    }

    /*
        使用InputStreamReader读取UTF-8格式的文件
     */
    private static void read_utf_8() throws IOException {
        //1.创建InputStreamReader对象,构造方法中传递字节输入流和指定的编码表名称
        //InputStreamReader isr = new InputStreamReader(new FileInputStream("10_IO\\utf_8.txt"),"UTF-8");
        InputStreamReader isr = new InputStreamReader(new FileInputStream("10_IO\\utf_8.txt"));//不指定默认使用UTF-8
        //2.使用InputStreamReader对象中的方法read读取文件
        int len = 0;
        while((len = isr.read())!=-1){
            System.out.println((char)len);
        }
        //3.释放资源
        isr.close();
    }
}
```

### Demo04Test 转换文件编码 ###

```JAVA
package com.itheima.demo03.ReverseStream;

import java.io.*;

/*
    练习：转换文件编码
        将GBK编码的文本文件，转换为UTF-8编码的文本文件。

    分析:
        1.创建InputStreamReader对象,构造方法中传递字节输入流和指定的编码表名称GBK
        2.创建OutputStreamWriter对象,构造方法中传递字节输出流和指定的编码表名称UTF-8
        3.使用InputStreamReader对象中的方法read读取文件
        4.使用OutputStreamWriter对象中的方法write,把读取的数据写入到文件中
        5.释放资源
 */
public class Demo04Test {
    public static void main(String[] args) throws IOException {
        //1.创建InputStreamReader对象,构造方法中传递字节输入流和指定的编码表名称GBK
        InputStreamReader isr = new InputStreamReader(new FileInputStream("10_IO\\我是GBK格式的文本.txt"),"GBK");
        //2.创建OutputStreamWriter对象,构造方法中传递字节输出流和指定的编码表名称UTF-8
        OutputStreamWriter osw = new OutputStreamWriter(new FileOutputStream("10_IO\\我是utf_8格式的文件.txt"),"UTF-8");
        //3.使用InputStreamReader对象中的方法read读取文件

        //BufferedReader isr = new BufferedReader(new InputStreamReader(new FileInputStream("10_IO\\我是GBK格式的文本.txt"),"GBK"));
        //BufferedWriter osw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("10_IO\\我是utf_8格式的文件.txt"),"UTF-8")); 更快

        int len = 0;
        while((len = isr.read())!=-1){
            //4.使用OutputStreamWriter对象中的方法write,把读取的数据写入到文件中
            osw.write(len);
        }
        //5.释放资源
        osw.close();
        isr.close();
    }
}
```

## 第三章 序列化 ##

###  ###

```java
package com.itheima.demo04.ObjectStream;

import java.io.Serializable;

/*
    序列化和反序列化的时候,会抛出NotSerializableException没有序列化异常
    类通过实现 java.io.Serializable 接口以启用其序列化功能。未实现此接口的类将无法使其任何状态序列化或反序列化。
    Serializable接口也叫标记型接口
        要进行序列化和反序列化的类必须实现Serializable接口,就会给类添加一个标记
        当我们进行序列化和反序列化的时候,就会检测类上是否有这个标记
            有:就可以序列化和反序列化
            没有:就会抛出 NotSerializableException异常
    去市场买肉-->肉上有一个蓝色章(检测合格)-->放心购买-->买回来怎么吃随意


    static关键字:静态关键字
        静态优先于非静态加载到内存中(静态优先于对象进入到内存中)
        被static修饰的成员变量不能被序列化的,序列化的都是对象
        private static int age;
        oos.writeObject(new Person("小美女",18));
        Object o = ois.readObject();
        Person{name='小美女', age=0}

    transient关键字:瞬态关键字(用于一些不是静态但又不想被序列化的变量)
        被transient修饰成员变量,不能被序列化
        private transient int age;
        oos.writeObject(new Person("小美女",18));
        Object o = ois.readObject();
        Person{name='小美女', age=0}
        
    static final long serialVersionUID = 1L;
		class类序列化后有修改，反序列化会导致class的版本不同报错，提前声明
		serialVersionUID不会报错
 */
public class Person implements Serializable{
    private static final long serialVersionUID = 1L;
    private String name;
    //private static int age;
    //private transient int age;
    public int age;

    public Person() {
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
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
}
```

### ObjectOutputStream/ObjectInputStream 来序列化的读写对象 ###

```java
package com.itheima.demo04.ObjectStream;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;

/*
    java.io.ObjectOutputStream extends OutputStream
    ObjectOutputStream:对象的序列化流
    作用:把对象以流的方式写入到文件中保存

    构造方法:
        ObjectOutputStream(OutputStream out) 创建写入指定 OutputStream 的 ObjectOutputStream。
        参数:
            OutputStream out:字节输出流
    特有的成员方法:
        void writeObject(Object obj) 将指定的对象写入 ObjectOutputStream。

    使用步骤:
        1.创建ObjectOutputStream对象,构造方法中传递字节输出流
        2.使用ObjectOutputStream对象中的方法writeObject,把对象写入到文件中
        3.释放资源
 */
public class Demo01ObjectOutputStream {
    public static void main(String[] args) throws IOException {
        //1.创建ObjectOutputStream对象,构造方法中传递字节输出流
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("10_IO\\person.txt"));
        //2.使用ObjectOutputStream对象中的方法writeObject,把对象写入到文件中
        oos.writeObject(new Person("小美女",18));
        //3.释放资源
        oos.close();
    }
}
package com.itheima.demo04.ObjectStream;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

/*
    java.io.ObjectInputStream extends InputStream
    ObjectInputStream:对象的反序列化流
    作用:把文件中保存的对象,以流的方式读取出来使用

    构造方法:
        ObjectInputStream(InputStream in) 创建从指定 InputStream 读取的 ObjectInputStream。
        参数:
            InputStream in:字节输入流
    特有的成员方法:
        Object readObject() 从 ObjectInputStream 读取对象。

    使用步骤:
        1.创建ObjectInputStream对象,构造方法中传递字节输入流
        2.使用ObjectInputStream对象中的方法readObject读取保存对象的文件
        3.释放资源
        4.使用读取出来的对象(打印)

     readObject方法声明抛出了ClassNotFoundException(class文件找不到异常)
     当不存在对象的class文件时抛出此异常
     反序列化的前提:
        1.类必须实现Serializable
        2.必须存在类对应的class文件
 */
public class Demo02ObjectInputStream {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        //1.创建ObjectInputStream对象,构造方法中传递字节输入流
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("10_IO\\person.txt"));
        //2.使用ObjectInputStream对象中的方法readObject读取保存对象的文件
        Object o = ois.readObject();
        //3.释放资源
        ois.close();
        //4.使用读取出来的对象(打印)
        System.out.println(o);
        Person p = (Person)o;
        System.out.println(p.getName()+p.getAge());
    }

}
```

### Demo03Test 序列化集合 ###

```java
package com.itheima.demo04.ObjectStream;

import java.io.*;
import java.util.ArrayList;

/*
    练习：序列化集合
        当我们想在文件中保存多个对象的时候
        可以把多个对象存储到一个集合中
        对集合进序列化和反序列化
    分析:
        1.定义一个存储Person对象的ArrayList集合
        2.往ArrayList集合中存储Person对象
        3.创建一个序列化流ObjectOutputStream对象
        4.使用ObjectOutputStream对象中的方法writeObject,对集合进行序列化
        5.创建一个反序列化ObjectInputStream对象
        6.使用ObjectInputStream对象中的方法readObject读取文件中保存的集合
        7.把Object类型的集合转换为ArrayList类型
        8.遍历ArrayList集合
        9.释放资源
 */
public class Demo03Test {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        //1.定义一个存储Person对象的ArrayList集合
        ArrayList<Person> list = new ArrayList<>();
        //2.往ArrayList集合中存储Person对象
        list.add(new Person("张三",18));
        list.add(new Person("李四",19));
        list.add(new Person("王五",20));
        //3.创建一个序列化流ObjectOutputStream对象
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("10_IO\\list.txt"));
        //4.使用ObjectOutputStream对象中的方法writeObject,对集合进行序列化
        oos.writeObject(list);
        //5.创建一个反序列化ObjectInputStream对象
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream("10_IO\\list.txt"));
        //6.使用ObjectInputStream对象中的方法readObject读取文件中保存的集合
        Object o = ois.readObject();
        //7.把Object类型的集合转换为ArrayList类型
        ArrayList<Person> list2 = (ArrayList<Person>)o;
        //8.遍历ArrayList集合
        for (Person p : list2) {
            System.out.println(p);
        }
        //9.释放资源
        ois.close();
        oos.close();
    }
}
```

## 第四章 打印流 ##

### Demo01PrintStream ###

```java
package com.itheima.demo05.PrintStream;

import java.io.FileNotFoundException;
import java.io.PrintStream;

/*
    java.io.PrintStream:打印流
        PrintStream 为其他输出流添加了功能，使它们能够方便地打印各种数据值表示形式。
    PrintStream特点:
        1.只负责数据的输出,不负责数据的读取
        2.与其他输出流不同，PrintStream 永远不会抛出 IOException
        3.有特有的方法,print,println
            void print(任意类型的值)
            void println(任意类型的值并换行)
    构造方法:
        PrintStream(File file):输出的目的地是一个文件
        PrintStream(OutputStream out):输出的目的地是一个字节输出流
        PrintStream(String fileName) :输出的目的地是一个文件路径
    PrintStream extends OutputStream
    继承自父类的成员方法:
        - public void close() ：关闭此输出流并释放与此流相关联的任何系统资源。
        - public void flush() ：刷新此输出流并强制任何缓冲的输出字节被写出。
        - public void write(byte[] b)：将 b.length字节从指定的字节数组写入此输出流。
        - public void write(byte[] b, int off, int len) ：从指定的字节数组写入 len字节，从偏移量 off开始输出到此输出流。
        - public abstract void write(int b) ：将指定的字节输出流。
    注意:
        如果使用继承自父类的write方法写数据,那么查看数据的时候会查询编码表 97->a
        如果使用自己特有的方法print/println方法写数据,写的数据原样输出 97->97
 */
public class Demo01PrintStream {
    public static void main(String[] args) throws FileNotFoundException {
        //System.out.println("HelloWorld");

        //创建打印流PrintStream对象,构造方法中绑定要输出的目的地
        PrintStream ps = new PrintStream("10_IO\\print.txt");
        //如果使用继承自父类的write方法写数据,那么查看数据的时候会查询编码表 97->a
        ps.write(97);
        //如果使用自己特有的方法print/println方法写数据,写的数据原样输出 97->97
        ps.println(97);
        ps.println(8.8);
        ps.println('a');
        ps.println("HelloWorld");
        ps.println(true);

        //释放资源
        ps.close();
    }
}
```

### Demo02PrintStream 改变输出语句的目的地(打印流的流向) log ###

```java
package com.itheima.demo05.PrintStream;

import java.io.FileNotFoundException;
import java.io.PrintStream;

/*
    可以改变输出语句的目的地(打印流的流向)
    输出语句,默认在控制台输出
    使用System.setOut方法改变输出语句的目的地改为参数中传递的打印流的目的地
        static void setOut(PrintStream out)
          重新分配“标准”输出流。
 */
public class Demo02PrintStream {
    public static void main(String[] args) throws FileNotFoundException {
        System.out.println("我是在控制台输出");

        PrintStream ps = new PrintStream("10_IO\\目的地是打印流.txt");
        System.setOut(ps);//把输出语句的目的地改变为打印流的目的地
        System.out.println("我在打印流的目的地中输出");

        ps.close();
    }
}
```

# day11【网络编程】 #

## 第二章 TCP通信程序 ##

### DemoTCP 客户端和服务器进行简单交互 ###

```java
package com.itheima.demo01.TCP;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

/*
    TCP通信的服务器端:接收客户端的请求,读取客户端发送的数据,给客户端回写数据
    表示服务器的类:
        java.net.ServerSocket:此类实现服务器套接字。

    构造方法:
        ServerSocket(int port) 创建绑定到特定端口的服务器套接字。

    服务器端必须明确一件事情,必须的知道是哪个客户端请求的服务器
    所以可以使用accept方法获取到请求的客户端对象Socket
    成员方法:
        Socket accept() 侦听并接受到此套接字的连接。

    服务器的实现步骤:
        1.创建服务器ServerSocket对象和系统要指定的端口号
        2.使用ServerSocket对象中的方法accept,获取到请求的客户端对象Socket
        3.使用Socket对象中的方法getInputStream()获取网络字节输入流InputStream对象
        4.使用网络字节输入流InputStream对象中的方法read,读取客户端发送的数据
        5.使用Socket对象中的方法getOutputStream()获取网络字节输出流OutputStream对象
        6.使用网络字节输出流OutputStream对象中的方法write,给客户端回写数据
        7.释放资源(Socket,ServerSocket)
 */
public class TCPServer {
    public static void main(String[] args) throws IOException {
        //1.创建服务器ServerSocket对象和系统要指定的端口号
        ServerSocket server = new ServerSocket(8888);
        //2.使用ServerSocket对象中的方法accept,获取到请求的客户端对象Socket
        Socket socket = server.accept();
        //3.使用Socket对象中的方法getInputStream()获取网络字节输入流InputStream对象
        InputStream is = socket.getInputStream();
        //4.使用网络字节输入流InputStream对象中的方法read,读取客户端发送的数据
        byte[] bytes = new byte[1024];
        int len = is.read(bytes);
        System.out.println(new String(bytes,0,len));
        //5.使用Socket对象中的方法getOutputStream()获取网络字节输出流OutputStream对象
        OutputStream os = socket.getOutputStream();
        //6.使用网络字节输出流OutputStream对象中的方法write,给客户端回写数据
        os.write("收到谢谢".getBytes());
        //7.释放资源(Socket,ServerSocket)
        socket.close();
        server.close();
    }
}

package com.itheima.demo01.TCP;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

/*
    TCP通信的客户端:向服务器发送连接请求,给服务器发送数据,读取服务器回写的数据
    表示客户端的类:
        java.net.Socket:此类实现客户端套接字（也可以就叫“套接字”）。套接字是两台机器间通信的端点。
        套接字:包含了IP地址和端口号的网络单位

    构造方法:
        Socket(String host, int port) 创建一个流套接字并将其连接到指定主机上的指定端口号。
        参数:
            String host:服务器主机的名称/服务器的IP地址
            int port:服务器的端口号

    成员方法:
        OutputStream getOutputStream() 返回此套接字的输出流。
        InputStream getInputStream() 返回此套接字的输入流。
        void close() 关闭此套接字。

    实现步骤:
        1.创建一个客户端对象Socket,构造方法绑定服务器的IP地址和端口号
        2.使用Socket对象中的方法getOutputStream()获取网络字节输出流OutputStream对象
        3.使用网络字节输出流OutputStream对象中的方法write,给服务器发送数据
        4.使用Socket对象中的方法getInputStream()获取网络字节输入流InputStream对象
        5.使用网络字节输入流InputStream对象中的方法read,读取服务器回写的数据
        6.释放资源(Socket)
     注意:
        1.客户端和服务器端进行交互,必须使用Socket中提供的网络流,不能使用自己创建的流对象
        2.当我们创建客户端对象Socket的时候,就会去请求服务器和服务器经过3次握手建立连接通路
            这时如果服务器没有启动,那么就会抛出异常ConnectException: Connection refused: connect
            如果服务器已经启动,那么就可以进行交互了
 */
public class TCPClient {
    public static void main(String[] args) throws IOException {
        //1.创建一个客户端对象Socket,构造方法绑定服务器的IP地址和端口号
        Socket socket = new Socket("127.0.0.1",8888);
        //2.使用Socket对象中的方法getOutputStream()获取网络字节输出流OutputStream对象
        OutputStream os = socket.getOutputStream();
        //3.使用网络字节输出流OutputStream对象中的方法write,给服务器发送数据
        os.write("你好服务器".getBytes());

        //4.使用Socket对象中的方法getInputStream()获取网络字节输入流InputStream对象
        InputStream is = socket.getInputStream();

        //5.使用网络字节输入流InputStream对象中的方法read,读取服务器回写的数据
        byte[] bytes = new byte[1024];
        int len = is.read(bytes);
        System.out.println(new String(bytes,0,len));

        //6.释放资源(Socket)
        socket.close();
    }
}
```

## 第三章 综合案例 ##

### 文件上传案例 ###

#### Demo 客户端上传文件到服务器 本地字节流和网络字节流/shutdownOutput ####

```java
package com.itheima.demo02.FileUpload;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;

/*
    文件上传案例服务器端:读取客户端上传的文件,保存到服务器的硬盘,给客户端回写"上传成功"

    明确:
        数据源:客户端上传的文件
        目的地:服务器的硬盘 d:\\upload\\1.jpg

    实现步骤:
        1.创建一个服务器ServerSocket对象,和系统要指定的端口号
        2.使用ServerSocket对象中的方法accept,获取到请求的客户端Socket对象
        3.使用Socket对象中的方法getInputStream,获取到网络字节输入流InputStream对象
        4.判断d:\\upload文件夹是否存在,不存在则创建
        5.创建一个本地字节输出流FileOutputStream对象,构造方法中绑定要输出的目的地
        6.使用网络字节输入流InputStream对象中的方法read,读取客户端上传的文件
        7.使用本地字节输出流FileOutputStream对象中的方法write,把读取到的文件保存到服务器的硬盘上
        8.使用Socket对象中的方法getOutputStream,获取到网络字节输出流OutputStream对象
        9.使用网络字节输出流OutputStream对象中的方法write,给客户端回写"上传成功"
        10.释放资源(FileOutputStream,Socket,ServerSocket)
 */
public class TCPServer {
    public static void main(String[] args) throws IOException {
        //1.创建一个服务器ServerSocket对象,和系统要指定的端口号
        ServerSocket server = new ServerSocket(8888);
        //2.使用ServerSocket对象中的方法accept,获取到请求的客户端Socket对象
        Socket socket = server.accept();
        //3.使用Socket对象中的方法getInputStream,获取到网络字节输入流InputStream对象
        InputStream is = socket.getInputStream();
        //4.判断d:\\upload文件夹是否存在,不存在则创建
        File file =  new File("10_IO");
        if(!file.exists()){
            file.mkdirs();
            System.out.println("路径不存在，创建新路径");
        }


        //5.创建一个本地字节输出流FileOutputStream对象,构造方法中绑定要输出的目的地
        FileOutputStream fos = new FileOutputStream(file+"\\123.txt");
        //6.使用网络字节输入流InputStream对象中的方法read,读取客户端上传的文件

        System.out.println("11111111111111111111");

        int len =0;
        byte[] bytes = new byte[1024];
        while((len = is.read(bytes))!=-1){
            //7.使用本地字节输出流FileOutputStream对象中的方法write,把读取到的文件保存到服务器的硬盘上
            fos.write(bytes,0,len);
        }

        System.out.println("22222222222222222222222  while死循环打印不到");

        //8.使用Socket对象中的方法getOutputStream,获取到网络字节输出流OutputStream对象
        //9.使用网络字节输出流OutputStream对象中的方法write,给客户端回写"上传成功"
        socket.getOutputStream().write("上传成功".getBytes());
        //10.释放资源(FileOutputStream,Socket,ServerSocket)
        fos.close();
        socket.close();
        server.close();
    }
}

package com.itheima.demo02.FileUpload;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

/*
    文件上传案例的客户端:读取本地文件,上传到服务器,读取服务器回写的数据

    明确:
        数据源:c:\\1.jpg
        目的地:服务器

    实现步骤:
        1.创建一个本地字节输入流FileInputStream对象,构造方法中绑定要读取的数据源
        2.创建一个客户端Socket对象,构造方法中绑定服务器的IP地址和端口号
        3.使用Socket中的方法getOutputStream,获取网络字节输出流OutputStream对象
        4.使用本地字节输入流FileInputStream对象中的方法read,读取本地文件
        5.使用网络字节输出流OutputStream对象中的方法write,把读取到的文件上传到服务器
        6.使用Socket中的方法getInputStream,获取网络字节输入流InputStream对象
        7.使用网络字节输入流InputStream对象中的方法read读取服务回写的数据
        8.释放资源(FileInputStream,Socket)
 */
public class TCPClient {
    public static void main(String[] args) throws IOException {
        //1.创建一个本地字节输入流FileInputStream对象,构造方法中绑定要读取的数据源
        FileInputStream fis = new FileInputStream("10_IO\\a.txt");
        //2.创建一个客户端Socket对象,构造方法中绑定服务器的IP地址和端口号
        Socket socket = new Socket("127.0.0.1",8888);
        //3.使用Socket中的方法getOutputStream,获取网络字节输出流OutputStream对象
        OutputStream os = socket.getOutputStream();
        //4.使用本地字节输入流FileInputStream对象中的方法read,读取本地文件
        int len = 0;
        byte[] bytes = new byte[1024];
        while((len = fis.read(bytes))!=-1){
            //5.使用网络字节输出流OutputStream对象中的方法write,把读取到的文件上传到服务器
            os.write(bytes,0,len);
        }

        /*
            解决:上传完文件,给服务器写一个结束标记
            void shutdownOutput() 禁用此套接字的输出流。
            对于 TCP 套接字，任何以前写入的数据都将被发送，并且后跟 TCP 的正常连接终止序列。
         */
        socket.shutdownOutput();

        //6.使用Socket中的方法getInputStream,获取网络字节输入流InputStream对象
        InputStream is = socket.getInputStream();

        System.out.println("333333333333333333333");

        //7.使用网络字节输入流InputStream对象中的方法read读取服务回写的数据
        while((len = is.read(bytes))!=-1){
            System.out.println(new String(bytes,0,len));
        }

        System.out.println("444444444444444444  while死循环打印不到");

        //8.释放资源(FileInputStream,Socket)
        fis.close();
        socket.close();
    }
}
```

#### Demo  多线程技术优化上传 ####

```java
package com.itheima.demo03.FileUpload;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Random;


public class TCPServer {
    public static void main(String[] args) throws IOException {

        ServerSocket server = new ServerSocket(8888);

        /*
            让服务器一直处于监听状态(死循环accept方法)
            有一个客户端上传文件,就保存一个文件
         */
        while(true){
            Socket socket = server.accept();

            /*
                使用多线程技术,提高程序的效率
                有一个客户端上传文件,就开启一个线程,完成文件的上传
             */
            new Thread(new Runnable() {
                //完成文件的上传
                @Override
                public void run() {
                   try {
                       InputStream is = socket.getInputStream();
                       File file =  new File("10_IO");
                       if(!file.exists()){
                           file.mkdirs();
                       }

                    /*
                        自定义一个文件的命名规则:防止同名的文件被覆盖
                        规则:域名+毫秒值+随机数
                     */
                       String fileName = "itcast"+System.currentTimeMillis()+new Random().nextInt(999999)+".jpg";

                       FileOutputStream fos = new FileOutputStream(file+"\\"+fileName);
                       int len =0;
                       byte[] bytes = new byte[1024];
                       while((len = is.read(bytes))!=-1){

                           fos.write(bytes,0,len);
                       }
                       socket.getOutputStream().write("上传成功".getBytes());
                       fos.close();
                       socket.close();
                   }catch (IOException e){
                       System.out.println(e);
                   }
                }
            }).start();
        }
        //服务器就不用关闭
        //server.close();
    }
}
```

### 模拟B\S服务器 ###

http://127.0.0.1:8080/11_Net/web/index.html

#### 浏览器和服务器间通讯  图片无法加载 ####

```java
package com.itheima.demo04.BSTCP;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

/*
    创建BS版本TCP服务器
 */
public class TCPServer {
    public static void main(String[] args) throws IOException {
        //创建一个服务器ServerSocket,和系统要指定的端口号
        ServerSocket server = new ServerSocket(8080);
        //使用accept方法获取到请求的客户端对象(浏览器)
        Socket socket = server.accept();
        //使用Socket对象中的方法getInputStream,获取到网络字节输入流InputStream对象
        InputStream is = socket.getInputStream();
        //使用网络字节输入流InputStream对象中的方法read读取客户端的请求信息
        /*byte[] bytes = new byte[1024];
        int len = 0;
        while((len = is.read(bytes))!=-1){
            System.out.println(new String(bytes,0,len));
        }*/

        //把is网络字节输入流对象,转换为字符缓冲输入流
        BufferedReader br = new BufferedReader(new InputStreamReader(is));
        //把客户端请求信息的第一行读取出来 GET /11_Net/web/index.html HTTP/1.1
        String line = br.readLine();
        //把读取的信息进行切割,只要中间部分 /11_Net/web/index.html
        String[] arr = line.split(" ");
        //把路径前边的/去掉,进行截取 11_Net/web/index.html
        String htmlpath = arr[1].substring(1);
        System.out.println(htmlpath);

        //创建一个本地字节输入流,构造方法中绑定要读取的html路径
        FileInputStream fis = new FileInputStream(htmlpath);
        //使用Socket中的方法getOutputStream获取网络字节输出流OutputStream对象
        OutputStream os = socket.getOutputStream();

        // 写入HTTP协议响应头,固定写法
        os.write("HTTP/1.1 200 OK\r\n".getBytes());
        os.write("Content-Type:text/html\r\n".getBytes());
        // 必须要写入空行,否则浏览器不解析
        os.write("\r\n".getBytes());

        //一读一写复制文件,把服务读取的html文件回写到客户端
        int len = 0;
        byte[] bytes = new byte[1024];
        while((len = fis.read(bytes))!=-1){
            os.write(bytes,0,len);
        }

        //释放资源
        fis.close();
//        socket.close();
//        server.close();
    }
}
```

#### 加载图片开启另一个线程/多线程技术 ####

```java
package com.itheima.demo04.BSTCP;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

/*
    创建BS版本TCP服务器
 */
public class TCPServerThread {
    public static void main(String[] args) throws IOException {
        //创建一个服务器ServerSocket,和系统要指定的端口号
        ServerSocket server = new ServerSocket(8080);

        /*
            浏览器解析服务器回写的html页面,页面中如果有图片,那么浏览器就会单独的开启一个线程,读取服务器的图片
            我们就得让服务器一直处于监听状态,客户端请求一次,服务器就回写一次
         */
        while(true){
            //使用accept方法获取到请求的客户端对象(浏览器)
            Socket socket = server.accept();

            new Thread(new Runnable() {
                @Override
                public void run() {
                    try {
                        //使用Socket对象中的方法getInputStream,获取到网络字节输入流InputStream对象
                        InputStream is = socket.getInputStream();
                        //使用网络字节输入流InputStream对象中的方法read读取客户端的请求信息
                        /*byte[] bytes = new byte[1024];
                        int len = 0;
                        while((len = is.read(bytes))!=-1){
                            System.out.println(new String(bytes,0,len));
                        }*/

                        //把is网络字节输入流对象,转换为字符缓冲输入流
                        BufferedReader br = new BufferedReader(new InputStreamReader(is));
                        //把客户端请求信息的第一行读取出来 GET /11_Net/web/index.html HTTP/1.1
                        String line = br.readLine();
                        System.out.println(line);
                        //把读取的信息进行切割,只要中间部分 /11_Net/web/index.html
                        String[] arr = line.split(" ");
                        //把路径前边的/去掉,进行截取 11_Net/web/index.html
                        String htmlpath = arr[1].substring(1);
                        System.out.println("解析返回地址"+htmlpath+"\r\n");
                        //创建一个本地字节输入流,构造方法中绑定要读取的html路径
                        FileInputStream fis = new FileInputStream(htmlpath);
                        //使用Socket中的方法getOutputStream获取网络字节输出流OutputStream对象
                        OutputStream os = socket.getOutputStream();

                        // 写入HTTP协议响应头,固定写法
                        os.write("HTTP/1.1 200 OK\r\n".getBytes());
                        os.write("Content-Type:text/html\r\n".getBytes());
                        // 必须要写入空行,否则浏览器不解析
                        os.write("\r\n".getBytes());

                        //一读一写复制文件,把服务读取的html文件回写到客户端
                        int len = 0;
                        byte[] bytes = new byte[1024];
                        while((len = fis.read(bytes))!=-1){
                            os.write(bytes,0,len);
                        }

                        //释放资源
                        fis.close();
                        socket.close();
                    }catch (IOException e){
                        e.printStackTrace();
                    }
                }
            }).start();


        }


        //server.close();
    }
}
/*
GET /11_Net/web/index.html HTTP/1.1
解析返回地址11_Net/web/index.html

GET /11_Net/web/img/logo2.png HTTP/1.1
GET /11_Net/web/img/header.jpg HTTP/1.1
解析返回地址11_Net/web/img/logo2.png

解析返回地址11_Net/web/img/header.jpg

GET /11_Net/web/img/1.jpg HTTP/1.1
解析返回地址11_Net/web/img/1.jpg

GET /11_Net/web/img/title2.jpg HTTP/1.1
GET /11_Net/web/img/big01.jpg HTTP/1.1
解析返回地址11_Net/web/img/big01.jpg

解析返回地址11_Net/web/img/title2.jpg

GET /11_Net/web/img/middle01.jpg HTTP/1.1
解析返回地址11_Net/web/img/middle01.jpg

GET /11_Net/web/img/ad.jpg HTTP/1.1
解析返回地址11_Net/web/img/ad.jpg

GET /11_Net/web/img/small03.jpg HTTP/1.1
解析返回地址11_Net/web/img/small03.jpg

GET /11_Net/web/img/footer.jpg HTTP/1.1
解析返回地址11_Net/web/img/footer.jpg

*/
```

# day12【函数式接口】 #

## 第一章 函数式接口 ##

### @FunctionalInterface注解 检测是否是函数式接口 ###

```java
package com.itheima.demo01.FunctionalInterface;
/*
    函数式接口:有且只有一个抽象方法的接口,称之为函数式接口
    当然接口中可以包含其他的方法(默认,静态,私有)

    @FunctionalInterface注解
    作用:可以检测接口是否是一个函数式接口
        是:编译成功
        否:编译失败(接口中没有抽象方法抽象方法的个数多余1个)
 */
@FunctionalInterface
public interface MyFunctionalInterface {
    //定义一个抽象方法
    public abstract void method();
    public static void others(){
        
    }
}
package com.itheima.demo01.FunctionalInterface;
/*
    函数式接口的使用:一般可以作为方法的参数和返回值类型
 */
public class Demo {
    //定义一个方法,参数使用函数式接口MyFunctionalInterface
    public static void show(MyFunctionalInterface myInter){
        myInter.method();
    }

    public static void main(String[] args) {
        //1 调用show方法,方法的参数是一个接口,所以可以传递接口的实现类对象
        show(new MyFunctionalInterfaceImpl());

        //2 调用show方法,方法的参数是一个接口,所以我们可以传递接口的匿名内部类
        show(new MyFunctionalInterface() {
            @Override
            public void method() {
                System.out.println("使用匿名内部类重写接口中的抽象方法");
            }
        });
		//lambda编译不会生成额外的匿名class文件(相比匿名内部类要节约空间)
        //3 调用show方法,方法的参数是一个函数式接口,所以我们可以Lambda表达式
        show(()->{
            System.out.println("使用Lambda表达式重写接口中的抽象方法");
        });

        //4 简化Lambda表达式
        show(() -> System.out.println("使用Lambda表达式重写接口中的抽象方法"));
    }
}
```

## 第二章 函数式编程 ##

### lambda性能优化：延迟执行，不满足条件不执行语句，不会浪费 ###

```java
package com.itheima.demo02.Lambda;

@FunctionalInterface
public interface MessageBuilder {
    //定义一个拼接消息的抽象方法,返回被拼接的消息
    public abstract String builderMessage();
}
package com.itheima.demo02.Lambda;
/*
    日志案例

    发现以下代码存在的一些性能浪费的问题
    调用showLog方法,传递的第二个参数是一个拼接后的字符串
    先把字符串拼接好,然后在调用showLog方法
    showLog方法中如果传递的日志等级不是1级
    那么就不会是如此拼接后的字符串
    所以感觉字符串就白拼接了,存在了浪费
 */
public class Demo01Logger {
    //定义一个根据日志的级别,显示日志信息的方法
    public static void showLog(int level, String message){
        //对日志的等级进行判断,如果是1级别,那么输出日志信息
        if(level==1){
            System.out.println(message);
        }
    }

    public static void main(String[] args) {
        //定义三个日志信息
        String msg1 = "Hello";
        String msg2 = "World";
        String msg3 = "Java";

        //调用showLog方法,传递日志级别和日志信息
        showLog(2,msg1+msg2+msg3);

    }
}
package com.itheima.demo02.Lambda;
/*
    使用Lambda优化日志案例
    Lambda的特点:延迟加载
    Lambda的使用前提,必须存在函数式接口
 */
public class Demo02Lambda {
    //定义一个显示日志的方法,方法的参数传递日志的等级和MessageBuilder接口
    public static void showLog(int level, MessageBuilder mb){
        //对日志的等级进行判断,如果是1级,则调用MessageBuilder接口中的builderMessage方法
        if(level==1){
            System.out.println(mb.builderMessage());
        }
    }

    public static void main(String[] args) {
        //定义三个日志信息
        String msg1 = "Hello";
        String msg2 = "World";
        String msg3 = "Java";

        //调用showLog方法,参数MessageBuilder是一个函数式接口,所以可以传递Lambda表达式
        /*showLog(2,()->{
            //返回一个拼接好的字符串
            return  msg1+msg2+msg3;
        });*/

        /*
            使用Lambda表达式作为参数传递,仅仅是把参数传递到showLog方法中
            只有满足条件,日志的等级是1级
                才会调用接口MessageBuilder中的方法builderMessage
                才会进行字符串的拼接
            如果条件不满足,日志的等级不是1级
                那么MessageBuilder接口中的方法builderMessage也不会执行
                所以拼接字符串的代码也不会执行
            所以不会存在性能的浪费
         */
        showLog(2,()->{
            //等级不是1，在showlog中就不会继续调用接口中的抽象方法，不会拼接字符串,节约
            System.out.println("不满足条件不执行");
            //返回一个拼接好的字符串 
            return  msg1+msg2+msg3;
        });
    }
}
```

### Demo01Runnable 函数式接口作为方法的参数 ###

```java
package com.itheima.demo03.LambdaTest;
/*
    例如java.lang.Runnable接口就是一个函数式接口，
    假设有一个startThread方法使用该接口作为参数，那么就可以使用Lambda进行传参。
    这种情况其实和Thread类的构造方法参数为Runnable没有本质区别。
 */
public class Demo01Runnable {
    //定义一个方法startThread,方法的参数使用函数式接口Runnable
    public static void startThread(Runnable run){
        //开启多线程
        new Thread(run).start();
    }

    public static void main(String[] args) {
        //调用startThread方法,方法的参数是一个接口,那么我们可以传递这个接口的匿名内部类
        startThread(new Runnable() {
            @Override
            public void run() {
                System.out.println(Thread.currentThread().getName()+"-->"+"线程启动了");
            }
        });

        //调用startThread方法,方法的参数是一个函数式接口,所以可以传递Lambda表达式
        startThread(()->{
            System.out.println(Thread.currentThread().getName()+"-->"+"线程启动了");
        });

        //优化Lambda表达式
        startThread(()->System.out.println(Thread.currentThread().getName()+"-->"+"线程启动了"));
    }
}
```

### Demo02Comparator 函数式接口作为方法的参数 ###

```java
package com.itheima.demo03.LambdaTest;

import java.util.Arrays;
import java.util.Comparator;

/*
    如果一个方法的返回值类型是一个函数式接口，那么就可以直接返回一个Lambda表达式。
    当需要通过一个方法来获取一个java.util.Comparator接口类型的对象作为排序器时,就可以调该方法获取。
 */
public class Demo02Comparator {
    //定义一个方法,方法的返回值类型使用函数式接口Comparator
    public static Comparator<String> getComparator(){
        //方法的返回值类型是一个接口,那么我们可以返回这个接口的匿名内部类
        /*return new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                //按照字符串的降序排序
                return o2.length()-o1.length();
            }
        };*/

        //方法的返回值类型是一个函数式接口,所有我们可以返回一个Lambda表达式
        /*return (String o1, String o2)->{
            //按照字符串的降序排序
            return o2.length()-o1.length();
        };*/

        //继续优化Lambda表达式
        return (o1, o2)->o2.length()-o1.length();
    }

    public static void main(String[] args) {
        //创建一个字符串数组
        String[] arr = {"aaa","b","cccccc","dddddddddddd"};
        //输出排序前的数组
        System.out.println(Arrays.toString(arr));//[aaa, b, cccccc, dddddddddddd]
        //调用Arrays中的sort方法,对字符串数组进行排序
        Arrays.sort(arr,getComparator());
        //输出排序后的数组
        System.out.println(Arrays.toString(arr));//[dddddddddddd, cccccc, aaa, b]
    }

}
```

## 第三章 常用函数式接口 ##

### Supplier接口(get) ###

```java
package com.itheima.demo04.Supplier;

import java.util.function.Supplier;

/*
    常用的函数式接口
    java.util.function.Supplier<T>接口仅包含一个无参的方法：T get()。用来获取一个泛型参数指定类型的对象数据。

    Supplier<T>接口被称之为生产型接口,指定接口的泛型是什么类型,那么接口中的get方法就会生产什么类型的数据
 */
public class Demo01Supplier {
    //定义一个方法,方法的参数传递Supplier<T>接口,泛型执行String,get方法就会返回一个String
    public static String getString(Supplier<String> sup){
        return sup.get();
    }

    public static void main(String[] args) {
        //调用getString方法,方法的参数Supplier是一个函数式接口,所以可以传递Lambda表达式
        String s = getString(()->{
            //生产一个字符串,并返回
            return "胡歌";
        });
        System.out.println(s);

        //优化Lambda表达式
        String s2 = getString(()->"胡歌");
        System.out.println(s2);
    }
}

package com.itheima.demo04.Supplier;


import java.util.function.Supplier;

/*
    练习：求数组元素最大值
        使用Supplier接口作为方法参数类型，通过Lambda表达式求出int数组中的最大值。
        提示：接口的泛型请使用java.lang.Integer类。
 */
public class Demo02Test {
   //定义一个方法,用于获取int类型数组中元素的最大值,方法的参数传递Supplier接口,泛型使用Integer
   public static int getMax(Supplier<Integer> sup){
       return sup.get();
   }

    public static void main(String[] args) {
        //定义一个int类型的数组,并赋值
        int[] arr = {100,0,-50,880,99,33,-30};
        //调用getMax方法,方法的参数Supplier是一个函数式接口,所以可以传递Lambda表达式
        int maxValue = getMax(()->{
            //获取数组的最大值,并返回
            //定义一个变量,把数组中的第一个元素赋值给该变量,记录数组中元素的最大值
            int max = arr[0];
            //遍历数组,获取数组中的其他元素
            for (int i : arr) {
                //使用其他的元素和最大值比较
                if(i>max){
                    //如果i大于max,则替换max作为最大值
                    max = i;
                }
            }
            //返回最大值
            return max;
        });
        System.out.println("数组中元素的最大值是:"+maxValue);
    }
}
```

### Consumer接口(accept)/默认方法andThen() ###

```java
package com.itheima.demo05.Consumer;

import java.util.function.Consumer;

/*
    java.util.function.Consumer<T>接口则正好与Supplier接口相反，
        它不是生产一个数据，而是消费一个数据，其数据类型由泛型决定。
    Consumer接口中包含抽象方法void accept(T t)，意为消费一个指定泛型的数据。

   Consumer接口是一个消费型接口,泛型执行什么类型,就可以使用accept方法消费什么类型的数据
   至于具体怎么消费(使用),需要自定义(输出,计算....)
 */
public class Demo01Consumer {
    /*
        定义一个方法
        方法的参数传递一个字符串的姓名
        方法的参数传递Consumer接口,泛型使用String
        可以使用Consumer接口消费字符串的姓名
     */
    public static void method(String name, Consumer<String> con){
        con.accept(name);
    }

    public static void main(String[] args) {
        //调用method方法,传递字符串姓名,方法的另一个参数是Consumer接口,是一个函数式接口,所以可以传递Lambda表达式
        method("赵丽颖",(String name)->{
            //对传递的字符串进行消费
            //消费方式:直接输出字符串
            //System.out.println(name);

            //消费方式:把字符串进行反转输出
            String reName = new StringBuffer(name).reverse().toString();
            System.out.println(reName);
        });
    }
}
package com.itheima.demo05.Consumer;

import java.util.function.Consumer;

/*
   Consumer接口的默认方法andThen
   作用:需要两个Consumer接口,可以把两个Consumer接口组合到一起,在对数据进行消费

   例如:
    Consumer<String> con1
    Consumer<String> con2
    String s = "hello";
    con1.accept(s);
    con2.accept(s);
    连接两个Consumer接口  再进行消费
    con1.andThen(con2).accept(s); 谁写前边谁先消费
*/
public class Demo02AndThen {
    //定义一个方法,方法的参数传递一个字符串和两个Consumer接口,Consumer接口的泛型使用字符串
    public static void method(String s, Consumer<String> con1 ,Consumer<String> con2){
        //con1.accept(s);
        //con2.accept(s);
        //使用andThen方法,把两个Consumer接口连接到一起,在消费数据
        con1.andThen(con2).accept(s);//con1连接con2,先执行con1消费数据,在执行con2消费数据
    }

    public static void main(String[] args) {
        //调用method方法,传递一个字符串,两个Lambda表达式
        method("Hello",
                (t)->{
                    //消费方式:把字符串转换为大写输出
                    System.out.println(t.toUpperCase());
                },
                (t)->{
                    //消费方式:把字符串转换为小写输出
                    System.out.println(t.toLowerCase());
                });
    }
}
//public interface MyConsumer {
//    public void accept(Object o);
//
//    default MyConsumer andThen(MyConsumer after){
//        return new MyConsumer() {
//            @Override
//            public void accept(Object o) {
//                MyConsumer.this.accept(o);
//                after.accept(o);
//            }
//        };
//    }
//}
//default Consumer<T> andThen(Consumer<? super T> after) {
//    Objects.requireNonNull(after);
//    return (T t) -> { accept(t); after.accept(t); };
package com.itheima.demo05.Consumer;

import java.util.function.Consumer;

/*
    练习:
        字符串数组当中存有多条信息，请按照格式“姓名：XX。性别：XX。”的格式将信息打印出来。
        要求将打印姓名的动作作为第一个Consumer接口的Lambda实例，
        将打印性别的动作作为第二个Consumer接口的Lambda实例，
        将两个Consumer接口按照顺序“拼接”到一起。
 */
public class Demo03Test {
    //定义一个方法,参数传递String类型的数组和两个Consumer接口,泛型使用String
    public static void printInfo(String[] arr, Consumer<String> con1,Consumer<String> con2){
        //遍历字符串数组
        for (String message : arr) {
            //使用andThen方法连接两个Consumer接口,消费字符串
            con1.andThen(con2).accept(message);
        }
    }

    public static void main(String[] args) {
        //定义一个字符串类型的数组
        String[] arr = { "迪丽热巴,女", "古力娜扎,女", "马尔扎哈,男" };

        //调用printInfo方法,传递一个字符串数组,和两个Lambda表达式
        printInfo(arr,(message)->{
            //消费方式:对message进行切割,获取姓名,按照指定的格式输出
            String name = message.split(",")[0];
            System.out.print("姓名: "+name);
        },(message)->{
            //消费方式:对message进行切割,获取年龄,按照指定的格式输出
            String age = message.split(",")[1];
            System.out.println("。年龄: "+age+"。");
        });
    }
}
//上下界通配符 PECS
//PECS是"Producer Extends,Consumer Super"（生产者用Extends，消费者用Super）的缩写。
//https://blog.csdn.net/lzufeng/article/details/83589665
```

### Predicate接口(test)/默认方法and/or/negate ###

```java
package com.itheima.demo06.Predicate;

import java.util.function.Predicate;

/*
    java.util.function.Predicate<T>接口
    作用:对某种数据类型的数据进行判断,结果返回一个boolean值

    Predicate接口中包含一个抽象方法：
        boolean test(T t):用来对指定数据类型数据进行判断的方法
            结果:
                符合条件,返回true
                不符合条件,返回false
*/
public class Demo01Predicate {
    /*
        定义一个方法
        参数传递一个String类型的字符串
        传递一个Predicate接口,泛型使用String
        使用Predicate中的方法test对字符串进行判断,并把判断的结果返回
     */
    public static boolean checkString(String s, Predicate<String> pre){
        return  pre.test(s);
    }

    public static void main(String[] args) {
        //定义一个字符串
        String s = "abcdef";

        //调用checkString方法对字符串进行校验,参数传递字符串和Lambda表达式
        /*boolean b = checkString(s,(String str)->{
            //对参数传递的字符串进行判断,判断字符串的长度是否大于5,并把判断的结果返回
            return str.length()>5;
        });*/

        //优化Lambda表达式
        boolean b = checkString(s,str->str.length()>5);
        System.out.println(b);
    }
}
package com.itheima.demo06.Predicate;

import java.util.function.Predicate;

/*
    逻辑表达式:可以连接多个判断的条件
    &&:与运算符,有false则false
    ||:或运算符,有true则true
    !:非(取反)运算符,非真则假,非假则真

    需求:判断一个字符串,有两个判断的条件
        1.判断字符串的长度是否大于5
        2.判断字符串中是否包含a
    两个条件必须同时满足,我们就可以使用&&运算符连接两个条件

    Predicate接口中有一个方法and,表示并且关系,也可以用于连接两个判断条件
    default Predicate<T> and(Predicate<? super T> other) {
        Objects.requireNonNull(other);
        return (t) -> this.test(t) && other.test(t);
    }
    方法内部的两个判断条件,也是使用&&运算符连接起来的
 */
public class Demo02Predicate_and {
    /*
        定义一个方法,方法的参数,传递一个字符串
        传递两个Predicate接口
            一个用于判断字符串的长度是否大于5
            一个用于判断字符串中是否包含a
            两个条件必须同时满足
     */
    public static boolean checkString(String s, Predicate<String> pre1,Predicate<String> pre2){
        //return pre1.test(s) && pre2.test(s);
        return pre1.and(pre2).test(s);//等价于return pre1.test(s) && pre2.test(s);
    }

    public static void main(String[] args) {
        //定义一个字符串
        String s = "abcdef";
        //调用checkString方法,参数传递字符串和两个Lambda表达式
        boolean b = checkString(s,(String str)->{
            //判断字符串的长度是否大于5
            return str.length()>5;
        },(String str)->{
            //判断字符串中是否包含a
            return str.contains("a");
        });
        System.out.println(b);
    }
}package com.itheima.demo06.Predicate;

import java.util.function.Predicate;

/*
     需求:判断一个字符串,有两个判断的条件
        1.判断字符串的长度是否大于5
        2.判断字符串中是否包含a
    满足一个条件即可,我们就可以使用||运算符连接两个条件

    Predicate接口中有一个方法or,表示或者关系,也可以用于连接两个判断条件
    default Predicate<T> or(Predicate<? super T> other) {
        Objects.requireNonNull(other);
        return (t) -> test(t) || other.test(t);
    }
    方法内部的两个判断条件,也是使用||运算符连接起来的
 */
public class Demo03Predicate_or {
    /*
            定义一个方法,方法的参数,传递一个字符串
            传递两个Predicate接口
                一个用于判断字符串的长度是否大于5
                一个用于判断字符串中是否包含a
                满足一个条件即可
         */
    public static boolean checkString(String s, Predicate<String> pre1, Predicate<String> pre2){
        //return pre1.test(s) || pre2.test(s);
        return  pre1.or(pre2).test(s);//等价于return pre1.test(s) || pre2.test(s);
    }

    public static void main(String[] args) {
        //定义一个字符串
        String s = "bc";
        //调用checkString方法,参数传递字符串和两个Lambda表达式
        boolean b = checkString(s,(String str)->{
            //判断字符串的长度是否大于5
            return str.length()>5;
        },(String str)->{
            //判断字符串中是否包含a
            return str.contains("a");
        });
        System.out.println(b);
    }
}

package com.itheima.demo06.Predicate;

import java.util.function.Predicate;

/*
     需求:判断一个字符串,有两个判断的条件
        1.判断字符串的长度是否大于5
        2.判断字符串中是否包含a
    满足一个条件即可,我们就可以使用||运算符连接两个条件

    Predicate接口中有一个方法or,表示或者关系,也可以用于连接两个判断条件
    default Predicate<T> or(Predicate<? super T> other) {
        Objects.requireNonNull(other);
        return (t) -> test(t) || other.test(t);
    }
    方法内部的两个判断条件,也是使用||运算符连接起来的
 */
public class Demo03Predicate_or {
    /*
            定义一个方法,方法的参数,传递一个字符串
            传递两个Predicate接口
                一个用于判断字符串的长度是否大于5
                一个用于判断字符串中是否包含a
                满足一个条件即可
         */
    public static boolean checkString(String s, Predicate<String> pre1, Predicate<String> pre2){
        //return pre1.test(s) || pre2.test(s);
        return  pre1.or(pre2).test(s);//等价于return pre1.test(s) || pre2.test(s);
    }

    public static void main(String[] args) {
        //定义一个字符串
        String s = "bc";
        //调用checkString方法,参数传递字符串和两个Lambda表达式
        boolean b = checkString(s,(String str)->{
            //判断字符串的长度是否大于5
            return str.length()>5;
        },(String str)->{
            //判断字符串中是否包含a
            return str.contains("a");
        });
        System.out.println(b);
    }
}
package com.itheima.demo06.Predicate;

import java.util.function.Predicate;

/*
    需求:判断一个字符串长度是否小于等于5
        如果字符串的长度大于5,那返回false
        如果字符串的长度不大于5,那么返回true
    所以我们可以使用取反符号!对判断的结果进行取反

    Predicate接口中有一个方法negate,也表示取反的意思
    default Predicate<T> negate() {
        return (t) -> !test(t);
    }
 */
public class Demo04Predicate_negate {
    /*
           定义一个方法,方法的参数,传递一个字符串
           使用Predicate接口判断字符串的长度是否小于等于5
    */
    public static boolean checkString(String s, Predicate<String> pre){
        //return !pre.test(s);
        return  pre.negate().test(s);//等效于return !pre.test(s);
    }

    public static void main(String[] args) {
        //定义一个字符串
        String s = "abc";
        //调用checkString方法,参数传递字符串和Lambda表达式
        boolean b = checkString(s,(String str)->{
            //判断字符串的长度是否大于5,并返回结果
            return str.length()>5;
        });
        System.out.println(b);
    }
}
```

#### Test Predicate练习 ####

```java
package com.itheima.demo06.Predicate;

import java.util.ArrayList;
import java.util.function.Predicate;

/*
    练习：集合信息筛选
    数组当中有多条“姓名+性别”的信息如下，
    String[] array = { "迪丽热巴,女", "古力娜扎,女", "马尔扎哈,男", "赵丽颖,女" };
    请通过Predicate接口的拼装将符合要求的字符串筛选到集合ArrayList中，
    需要同时满足两个条件：
        1. 必须为女生；
        2. 姓名为4个字。

    分析:
        1.有两个判断条件,所以需要使用两个Predicate接口,对条件进行判断
        2.必须同时满足两个条件,所以可以使用and方法连接两个判断条件
 */
public class Demo05Test {
    /*
        定义一个方法
        方法的参数传递一个包含人员信息的数组
        传递两个Predicate接口,用于对数组中的信息进行过滤
        把满足条件的信息存到ArrayList集合中并返回
     */
    public static ArrayList<String> filter(String[] arr,Predicate<String> pre1,Predicate<String> pre2){
        //定义一个ArrayList集合,存储过滤之后的信息
        ArrayList<String> list = new ArrayList<>();
        //遍历数组,获取数组中的每一条信息
        for (String s : arr) {
            //使用Predicate接口中的方法test对获取到的字符串进行判断
            boolean b = pre1.and(pre2).test(s);
            //对得到的布尔值进行判断
            if(b){
                //条件成立,两个条件都满足,把信息存储到ArrayList集合中
                list.add(s);
            }
        }
        //把集合返回
        return list;
    }

    public static void main(String[] args) {
        //定义一个储存字符串的数组
        String[] array = { "迪丽热巴,女", "古力娜扎,女", "马尔扎哈,男", "赵丽颖,女" };
        //调用filter方法,传递字符串数组和两个Lambda表达式
        ArrayList<String> list = filter(array,(String s)->{
            //获取字符串中的性别,判断是否为女
           return s.split(",")[1].equals("女");
        },(String s)->{
            //获取字符串中的姓名,判断长度是否为4个字符
           return s.split(",")[0].length()==4;
        });
        //遍历集合
        for (String s : list) {
            System.out.println(s);
        }
    }
}
```

### Function接口(apply)/默认方法andThen ###

```java
package com.itheima.demo07.Function;

import java.util.function.Function;

/*
    java.util.function.Function<T,R>接口用来根据一个类型的数据得到另一个类型的数据，
        前者称为前置条件，后者称为后置条件。
    Function接口中最主要的抽象方法为：R apply(T t)，根据类型T的参数获取类型R的结果。
        使用的场景例如：将String类型转换为Integer类型。
 */
public class Demo01Function {
    /*
        定义一个方法
        方法的参数传递一个字符串类型的整数
        方法的参数传递一个Function接口,泛型使用<String,Integer>
        使用Function接口中的方法apply,把字符串类型的整数,转换为Integer类型的整数
     */
    public static void change(String s, Function<String,Integer> fun){
        //Integer in = fun.apply(s);
        int in = fun.apply(s);//自动拆箱 Integer->int
        System.out.println(in);
    }

    public static void main(String[] args) {
        //定义一个字符串类型的整数
        String s = "1234";
        //调用change方法,传递字符串类型的整数,和Lambda表达式
        change(s,(String str)->{
            //把字符串类型的整数,转换为Integer类型的整数返回
            return Integer.parseInt(str);
        });
        //优化Lambda
        change(s,str->Integer.parseInt(str));
    }
}
package com.itheima.demo07.Function;

import java.util.function.Function;

/*
    Function接口中的默认方法andThen:用来进行组合操作

    需求:
        把String类型的"123",转换为Inteter类型,把转换后的结果加10
        把增加之后的Integer类型的数据,转换为String类型

    分析:
        转换了两次
        第一次是把String类型转换为了Integer类型
            所以我们可以使用Function<String,Integer> fun1
                Integer i = fun1.apply("123")+10;
        第二次是把Integer类型转换为String类型
            所以我们可以使用Function<Integer,String> fun2
                String s = fun2.apply(i);
        我们可以使用andThen方法,把两次转换组合在一起使用
            String s = fun1.andThen(fun2).apply("123");
            fun1先调用apply方法,把字符串转换为Integer
            fun2再调用apply方法,把Integer转换为字符串
 */
public class Demo02Function_andThen {
    /*
        定义一个方法
        参数串一个字符串类型的整数
        参数再传递两个Function接口
            一个泛型使用Function<String,Integer>
            一个泛型使用Function<Integer,String>
     */
    public static void change(String s, Function<String,Integer> fun1,Function<Integer,String> fun2){
        String ss = fun1.andThen(fun2).apply(s);
        System.out.println(ss);
    }

    public static void main(String[] args) {
        //定义一个字符串类型的整数
        String s = "123";
        //调用change方法,传递字符串和两个Lambda表达式
        change(s,(String str)->{
            //把字符串转换为整数+10
            return Integer.parseInt(str)+10;
        },(Integer i)->{
            //把整数转换为字符串
            return i+"";
        });

        //优化Lambda表达式
        change(s,str->Integer.parseInt(str)+10,i->i+"");
    }
}
package com.itheima.demo07.Function;

import java.util.function.Function;

/*
    练习：自定义函数模型拼接
    题目
    请使用Function进行函数模型的拼接，按照顺序需要执行的多个函数操作为：
        String str = "赵丽颖,20";

    分析:
    1. 将字符串截取数字年龄部分，得到字符串；
        Function<String,String> "赵丽颖,20"->"20"
    2. 将上一步的字符串转换成为int类型的数字；
        Function<String,Integer> "20"->20
    3. 将上一步的int数字累加100，得到结果int数字。
        Function<Integer,Integer> 20->120
 */
public class Demo03Test {
    /*
        定义一个方法
        参数传递包含姓名和年龄的字符串
        参数再传递3个Function接口用于类型转换
     */
    public static int change(String s, Function<String,String> fun1,
                             Function<String,Integer> fun2,Function<Integer,Integer> fun3){
        //使用andThen方法把三个转换组合到一起
        return fun1.andThen(fun2).andThen(fun3).apply(s);
    }

    public static void main(String[] args) {
        //定义一个字符串
        String str = "赵丽颖,20";
        //调用change方法,参数传递字符串和3个Lambda表达式
        int num = change(str,(String s)->{
            //"赵丽颖,20"->"20"
           return s.split(",")[1];
        },(String s)->{
            //"20"->20
            return Integer.parseInt(s);
        },(Integer i)->{
            //20->120
            return i+100;
        });
        System.out.println(num);
    }
}
```

# day13【Stream流、方法引用】 #

## 第一章 Stream流 ##

### 使用Stream流的方式,遍历集合,对集合中的数据进行过滤 ###

```java
package com.itheima.demo01.Stream;

import java.util.ArrayList;
import java.util.List;

/*
    使用传统的方式,遍历集合,对集合中的数据进行过滤
 */
public class Demo01List {
    public static void main(String[] args) {
        //创建一个List集合,存储姓名
        List<String> list = new ArrayList<>();
        list.add("张无忌");
        list.add("周芷若");
        list.add("赵敏");
        list.add("张强");
        list.add("张三丰");

        //对list集合中的元素进行过滤,只要以张开头的元素,存储到一个新的集合中
        List<String> listA = new ArrayList<>();
        for(String s : list){
            if(s.startsWith("张")){
                listA.add(s);
            }
        }

        //对listA集合进行过滤,只要姓名长度为3的人,存储到一个新集合中
        List<String> listB = new ArrayList<>();
        for (String s : listA) {
            if(s.length()==3){
                listB.add(s);
            }
        }

        //遍历listB集合
        for (String s : listB) {
            System.out.println(s);
        }
    }
}
package com.itheima.demo01.Stream;

import java.util.ArrayList;
import java.util.List;

/*
    使用Stream流的方式,遍历集合,对集合中的数据进行过滤
    Stream流是JDK1.8之后出现的
    关注的是做什么,而不是怎么做
 */
public class Demo02Stream {
    public static void main(String[] args) {
        //创建一个List集合,存储姓名
        List<String> list = new ArrayList<>();
        list.add("张无忌");
        list.add("周芷若");
        list.add("赵敏");
        list.add("张强");
        list.add("张三丰");

        //对list集合中的元素进行过滤,只要以张开头的元素,存储到一个新的集合中
        //对listA集合进行过滤,只要姓名长度为3的人,存储到一个新集合中
        //遍历listB集合
        list.stream()
                .filter(name->name.startsWith("张"))
            .filter(name->name.length()==3)
            .forEach(name-> System.out.println(name));
}
}
```

### 获取流的方法 静态方法/默认方法 ###

```java
package com.itheima.demo02.Stream;

import java.util.*;
import java.util.stream.Stream;

/*
    java.util.stream.Stream<T>是Java 8新加入的最常用的流接口。（这并不是一个函数式接口。）
    获取一个流非常简单，有以下几种常用的方式：
        - 所有的Collection集合都可以通过stream默认方法获取流；
            default Stream<E> stream()
        - Stream接口的静态方法of可以获取数组对应的流。
            static <T> Stream<T> of(T... values)
            参数是一个可变参数,那么我们就可以传递一个数组
 */
public class Demo01GetStream {
    public static void main(String[] args) {
        //把集合转换为Stream流
        List<String> list = new ArrayList<>();
        Stream<String> stream1 = list.stream();

        Set<String> set = new HashSet<>();
        Stream<String> stream2 = set.stream();

        Map<String,String> map = new HashMap<>();
        //获取键,存储到一个Set集合中
        Set<String> keySet = map.keySet();
        Stream<String> stream3 = keySet.stream();

        //获取值,存储到一个Collection集合中
        Collection<String> values = map.values();
        Stream<String> stream4 = values.stream();

        //获取键值对(键与值的映射关系 entrySet)
        Set<Map.Entry<String, String>> entries = map.entrySet();
        Stream<Map.Entry<String, String>> stream5 = entries.stream();

        //把数组转换为Stream流
        Stream<Integer> stream6 = Stream.of(1, 2, 3, 4, 5);

        //可变参数可以传递数组
        Integer[] arr = {1,2,3,4,5};
        Stream<Integer> stream7 = Stream.of(arr);
        String[] arr2 = {"a","bb","ccc"};
        Stream<String> stream8 = Stream.of(arr2);
    }
}
```

### Stream流中的常用方法_forEach ###

```java
package com.itheima.demo02.Stream;

import java.util.stream.Stream;

/*
    Stream流中的常用方法_forEach
    void forEach(Consumer<? super T> action);
    该方法接收一个Consumer接口函数，会将每一个流元素交给该函数进行处理。
    Consumer接口是一个消费型的函数式接口,可以传递Lambda表达式,消费数据

    简单记:
        forEach方法,用来遍历流中的数据
        是一个终结方法,遍历之后就不能继续调用Stream流中的其他方法
 */
public class Demo02Stream_forEach {
    public static void main(String[] args) {
        //获取一个Stream流
        Stream<String> stream = Stream.of("张三", "李四", "王五", "赵六", "田七");
        //使用Stream流中的方法forEach对Stream流中的数据进行遍历
        /*stream.forEach((String name)->{
            System.out.println(name);
        });*/

        stream.forEach(name->System.out.println(name));
    }
}
```

### Stream流中的常用方法_filter ###

```java
package com.itheima.demo02.Stream;

import java.util.stream.Stream;

/*
    Stream流中的常用方法_filter:用于对Stream流中的数据进行过滤
    Stream<T> filter(Predicate<? super T> predicate);
    filter方法的参数Predicate是一个函数式接口,所以可以传递Lambda表达式,对数据进行过滤
    Predicate中的抽象方法:
        boolean test(T t);
 */
public class Demo03Stream_filter {
    public static void main(String[] args) {
        //创建一个Stream流
        Stream<String> stream = Stream.of("张三丰", "张翠山", "赵敏", "周芷若", "张无忌");
        //对Stream流中的元素进行过滤,只要姓张的人
        Stream<String> stream2 = stream.filter((String name)->{return name.startsWith("张");});
        //遍历stream2流
        stream2.forEach(name-> System.out.println(name));

        /*
            Stream流属于管道流,只能被消费(使用)一次
            第一个Stream流调用完毕方法,数据就会流转到下一个Stream上
            而这时第一个Stream流已经使用完毕,就会关闭了
            所以第一个Stream流就不能再调用方法了
            IllegalStateException: stream has already been operated upon or closed
         */
        //遍历stream流
        stream.forEach(name-> System.out.println(name));
    }
}
```

### Stream流中的常用方法_map ###

```java
package com.itheima.demo02.Stream;

import java.util.stream.Stream;

/*
    Stream流中的常用方法_map:用于类型转换
    如果需要将流中的元素映射到另一个流中，可以使用map方法.
    <R> Stream<R> map(Function<? super T, ? extends R> mapper);
    该接口需要一个Function函数式接口参数，可以将当前流中的T类型数据转换为另一种R类型的流。
    Function中的抽象方法:
        R apply(T t);
 */
public class Demo04Stream_map {
    public static void main(String[] args) {
        //获取一个String类型的Stream流
        Stream<String> stream = Stream.of("1", "2", "3", "4");
        //使用map方法,把字符串类型的整数,转换(映射)为Integer类型的整数
        Stream<Integer> stream2 = stream.map((String s)->{
            return Integer.parseInt(s);
        });
        //遍历Stream2流
        stream2.forEach(i-> System.out.println(i));
    }
}
```

### Stream流中的常用方法_count ###

```java
package com.itheima.demo02.Stream;

import java.util.ArrayList;
import java.util.stream.Stream;

/*
    Stream流中的常用方法_count:用于统计Stream流中元素的个数
    long count();
    count方法是一个终结方法,返回值是一个long类型的整数
    所以不能再继续调用Stream流中的其他方法了
 */
public class Demo05Stream_count {
    public static void main(String[] args) {
        //获取一个Stream流
        ArrayList<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);
        list.add(5);
        list.add(6);
        list.add(7);
        Stream<Integer> stream = list.stream();
        long count = stream.count();
        System.out.println(count);//7
    }
}
```

### Stream流中的常用方法_limit ###

```java
package com.itheima.demo02.Stream;

import java.util.stream.Stream;

/*
    Stream流中的常用方法_limit:用于截取流中的元素
    limit方法可以对流进行截取，只取用前n个。方法签名：
    Stream<T> limit(long maxSize);
        参数是一个long型，如果集合当前长度大于参数则进行截取；否则不进行操作
    limit方法是一个延迟方法,只是对流中的元素进行截取,返回的是一个新的流,所以可以继续调用Stream流中的其他方法
 */
public class Demo06Stream_limit {
    public static void main(String[] args) {
        //获取一个Stream流
        String[] arr = {"美羊羊","喜洋洋","懒洋洋","灰太狼","红太狼"};
        Stream<String> stream = Stream.of(arr);
        //使用limit对Stream流中的元素进行截取,只要前3个元素
        Stream<String> stream2 = stream.limit(3);
        //遍历stream2流
        stream2.forEach(name-> System.out.println(name));
    }
}
```

### Stream流中的常用方法_skip ###

```java
package com.itheima.demo02.Stream;

import java.util.stream.Stream;

/*
    Stream流中的常用方法_skip:用于跳过元素
    如果希望跳过前几个元素，可以使用skip方法获取一个截取之后的新流：
    Stream<T> skip(long n);
        如果流的当前长度大于n，则跳过前n个；否则将会得到一个长度为0的空流。
 */
public class Demo07Stream_skip {
    public static void main(String[] args) {
        //获取一个Stream流
        String[] arr = {"美羊羊","喜洋洋","懒洋洋","灰太狼","红太狼"};
        Stream<String> stream = Stream.of(arr);
        //使用skip方法跳过前3个元素
        Stream<String> stream2 = stream.skip(3);
        //遍历stream2流
        stream2.forEach(name-> System.out.println(name));
    }
}
```

### Stream流中的常用方法_concat ###

```java
package com.itheima.demo02.Stream;

import java.util.stream.Stream;

/*
    Stream流中的常用方法_concat:用于把流组合到一起
    如果有两个流，希望合并成为一个流，那么可以使用Stream接口的静态方法concat
    static <T> Stream<T> concat(Stream<? extends T> a, Stream<? extends T> b)
 */
public class Demo08Stream_concat {
    public static void main(String[] args) {
        //创建一个Stream流
        Stream<String> stream1 = Stream.of("张三丰", "张翠山", "赵敏", "周芷若", "张无忌");
        //获取一个Stream流
        String[] arr = {"美羊羊","喜洋洋","懒洋洋","灰太狼","红太狼"};
        Stream<String> stream2 = Stream.of(arr);
        //把以上两个流组合为一个流
        Stream<String> concat = Stream.concat(stream1, stream2);
        //遍历concat流
        concat.forEach(name-> System.out.println(name));
    }
}
```

### 集合元素处理 传统/stream流 ###

```java
package com.itheima.demo03.Stream;

import java.util.ArrayList;

/*
    练习:集合元素处理（传统方式）
        现在有两个ArrayList集合存储队伍当中的多个成员姓名，要求使用传统的for循环（或增强for循环）依次进行以下若干操作步骤：
        1. 第一个队伍只要名字为3个字的成员姓名；存储到一个新集合中。
        2. 第一个队伍筛选之后只要前3个人；存储到一个新集合中。
        3. 第二个队伍只要姓张的成员姓名；存储到一个新集合中。
        4. 第二个队伍筛选之后不要前2个人；存储到一个新集合中。
        5. 将两个队伍合并为一个队伍；存储到一个新集合中。
        6. 根据姓名创建Person对象；存储到一个新集合中。
        7. 打印整个队伍的Person对象信息。
 */
public class Demo01StreamTest {
    public static void main(String[] args) {
        //第一支队伍
        ArrayList<String> one = new ArrayList<>();
        one.add("迪丽热巴");
        one.add("宋远桥");
        one.add("苏星河");
        one.add("石破天");
        one.add("石中玉");
        one.add("老子");
        one.add("庄子");
        one.add("洪七公");
        //1. 第一个队伍只要名字为3个字的成员姓名；存储到一个新集合中。
        ArrayList<String> one1 = new ArrayList<>();
        for (String name : one) {
            if(name.length()==3){
                one1.add(name);
            }
        }
        //2. 第一个队伍筛选之后只要前3个人；存储到一个新集合中。
        ArrayList<String> one2 = new ArrayList<>();
        for (int i = 0; i <3 ; i++) {
            one2.add(one1.get(i));//i = 0,1,2
        }

        //第二支队伍
        ArrayList<String> two = new ArrayList<>();
        two.add("古力娜扎");
        two.add("张无忌");
        two.add("赵丽颖");
        two.add("张三丰");
        two.add("尼古拉斯赵四");
        two.add("张天爱");
        two.add("张二狗");
        //3. 第二个队伍只要姓张的成员姓名；存储到一个新集合中。
        ArrayList<String> two1 = new ArrayList<>();
        for (String name : two) {
            if(name.startsWith("张")){
                two1.add(name);
            }
        }
        //4. 第二个队伍筛选之后不要前2个人；存储到一个新集合中。
        ArrayList<String> two2 = new ArrayList<>();
        for (int i = 2; i <two1.size() ; i++) {
            two2.add(two1.get(i)); //i 不包含0 1
        }

        //5. 将两个队伍合并为一个队伍；存储到一个新集合中。
        ArrayList<String> all = new ArrayList<>();
        all.addAll(one2);
        all.addAll(two2);

        //6. 根据姓名创建Person对象；存储到一个新集合中。
        ArrayList<Person> list = new ArrayList<>();
        for (String name : all) {
            list.add(new Person(name));
        }

        //7. 打印整个队伍的Person对象信息。
        for (Person person : list) {
            System.out.println(person);
        }
    }
}
//————————————————————————————————————————————————————————————————————————————
package com.itheima.demo03.Stream;

import java.util.ArrayList;
import java.util.stream.Stream;

/*
    练习：集合元素处理（Stream方式）
    将上一题当中的传统for循环写法更换为Stream流式处理方式。
    两个集合的初始内容不变，Person类的定义也不变。
 */
public class Demo02StreamTest {
    public static void main(String[] args) {
        //第一支队伍
        ArrayList<String> one = new ArrayList<>();
        one.add("迪丽热巴");
        one.add("宋远桥");
        one.add("苏星河");
        one.add("石破天");
        one.add("石中玉");
        one.add("老子");
        one.add("庄子");
        one.add("洪七公");
        //1. 第一个队伍只要名字为3个字的成员姓名；存储到一个新集合中。
        //2. 第一个队伍筛选之后只要前3个人；存储到一个新集合中。
        Stream<String> oneStream = one.stream().filter(name -> name.length() == 3).limit(3);

        //第二支队伍
        ArrayList<String> two = new ArrayList<>();
        two.add("古力娜扎");
        two.add("张无忌");
        two.add("赵丽颖");
        two.add("张三丰");
        two.add("尼古拉斯赵四");
        two.add("张天爱");
        two.add("张二狗");
        //3. 第二个队伍只要姓张的成员姓名；存储到一个新集合中。
        //4. 第二个队伍筛选之后不要前2个人；存储到一个新集合中。
        Stream<String> twoStream = two.stream().filter(name -> name.startsWith("张")).skip(2);

        //5. 将两个队伍合并为一个队伍；存储到一个新集合中。
        //6. 根据姓名创建Person对象；存储到一个新集合中。
        //7. 打印整个队伍的Person对象信息。
        Stream.concat(oneStream,twoStream).map(name->new Person(name)).forEach(p-> System.out.println(p));
        ArrayList<Person> all = new ArrayList<>();
        Stream.concat(oneStream,twoStream).map(name->new Person(name)).forEach(p->all.add(p));
        for (Person person : all) {
            System.out.println(person);
        }
    }
}
```

## 第二章 方法引用 ##

### lambda本身就是匿名函数，如果已经有现成的函数 ###

```java
package com.itheima.demo04.MethodReference;

public class Demo01Printable {
    public static void printString(Printable p,String name) {
        p.print(name);
    }

    public static void main(String[] args) {       
        printString((s) -> {
            System.out.println(s);
        },"123");
        printString(System.out::println,"123");
    }
}

package com.itheima.demo04.MethodReference;

public class Demo01Printable {
    //定义一个方法,参数传递Printable接口,对字符串进行打印
    public static void printString(Printable p) {
        p.print("HelloWorld");
    }

    public static void main(String[] args) {
        //调用printString方法,方法的参数Printable是一个函数式接口,所以可以传递Lambda
        printString((s) -> {
            System.out.println(s);
        });

        /*
            分析:
                Lambda表达式的目的,打印参数传递的字符串
                把参数s,传递给了System.out对象,调用out对象中的方法println对字符串进行了输出
                注意:
                    1.System.out对象是已经存在的
                    2.println方法也是已经存在的
                所以我们可以使用方法引用来优化Lambda表达式
                可以使用System.out方法直接引用(调用)println方法
         */
        printString(System.out::println);
    }
}
```

### 方法引用：通过对象名引用成员方法 ###

```java
package com.itheima.demo05.ObjectMethodReference;
/*
    定义一个打印的函数式接口
 */
@FunctionalInterface
public interface Printable {
    //定义字符串的抽象方法
    void print(String s);
}
package com.itheima.demo05.ObjectMethodReference;

public class MethodRerObject {
    //定义一个成员方法,传递字符串,把字符串按照大写输出
    public void printUpperCaseString(String str){
        System.out.println(str.toUpperCase());
    }
}
package com.itheima.demo05.ObjectMethodReference;
/*
    通过对象名引用成员方法
    使用前提是对象名是已经存在的,成员方法也是已经存在
    就可以使用对象名来引用成员方法
 */
public class Demo01ObjectMethodReference {
    //定义一个方法,方法的参数传递Printable接口
    public static void printString(Printable p){
        p.print("Hello");
    }

    public static void main(String[] args) {
        //调用printString方法,方法的参数Printable是一个函数式接口,所以可以传递Lambda表达式
        printString((s)->{
            //创建MethodRerObject对象
            MethodRerObject obj = new MethodRerObject();
            //调用MethodRerObject对象中的成员方法printUpperCaseString,把字符串按照大写输出
            obj.printUpperCaseString(s);
        });

        /*
            使用方法引用优化Lambda
            对象是已经存在的MethodRerObject
            成员方法也是已经存在的printUpperCaseString
            所以我们可以使用对象名引用成员方法
         */
        //创建MethodRerObject对象
        MethodRerObject obj = new MethodRerObject();
        printString(obj::printUpperCaseString);
    }
}
```

### 方法引用：通过类名称引用静态方法 ###

```java
package com.itheima.demo06.StaticMethodReference;

@FunctionalInterface
public interface Calcable {
    //定义一个抽象方法,传递一个整数,对整数进行绝对值计算并返回
    int calsAbs(int number);
}
package com.itheima.demo06.StaticMethodReference;

/*
    通过类名引用静态成员方法
    类已经存在,静态成员方法也已经存在
    就可以通过类名直接引用静态成员方法
 */
public class Demo01StaticMethodReference {
    //定义一个方法,方法的参数传递要计算绝对值的整数,和函数式接口Calcable
    public static int method(int number,Calcable c){
       return c.calsAbs(number);
    }

    public static void main(String[] args) {
        //调用method方法,传递计算绝对值得整数,和Lambda表达式
        int number = method(-10,(n)->{
            //对参数进行绝对值得计算并返回结果
            return Math.abs(n);
        });
        System.out.println(number);

        /*
            使用方法引用优化Lambda表达式
            Math类是存在的
            abs计算绝对值的静态方法也是已经存在的
            所以我们可以直接通过类名引用静态方法
         */
        int number2 = method(-10,Math::abs);
        System.out.println(number2);
    }
}
```

### 方法引用：通过super引用父类的成员方法 ###

```java
package com.itheima.demo07.SuperMethodReference;
/*
    定义见面的函数式接口
 */
@FunctionalInterface
public interface Greetable {
    //定义一个见面的方法
    void greet();
}
package com.itheima.demo07.SuperMethodReference;
/*
    定义父类
 */
public class Human {
    //定义一个sayHello的方法
    public void sayHello(){
        System.out.println("Hello 我是Human!");
    }
}
package com.itheima.demo07.SuperMethodReference;
/*
    定义子类
 */
public class Man extends Human{
    //子类重写父类sayHello的方法
    @Override
    public void sayHello() {
        System.out.println("Hello 我是Man!");
    }

    //定义一个方法参数传递Greetable接口
    public void method(Greetable g){
        g.greet();
    }

    public void show(){
        //调用method方法,方法的参数Greetable是一个函数式接口,所以可以传递Lambda
        /*method(()->{
            //创建父类Human对象
            Human h = new Human();
            //调用父类的sayHello方法
            h.sayHello();
        });*/

        //因为有子父类关系,所以存在的一个关键字super,代表父类,所以我们可以直接使用super调用父类的成员方法
       /* method(()->{
            super.sayHello();
        });*/

      /*
           使用super引用类的成员方法
           super是已经存在的
           父类的成员方法sayHello也是已经存在的
           所以我们可以直接使用super引用父类的成员方法
       */
      method(super::sayHello);
    }

    public static void main(String[] args) {
        new Man().show();
    }
}
```

### 方法引用：通过this引用本类成员方法 ###

```java
package com.itheima.demo08.ThisMethodReference;
/*
    定义一个富有的函数式接口
 */
@FunctionalInterface
public interface Richable {
    //定义一个想买什么就买什么的方法
    void buy();
}
package com.itheima.demo08.ThisMethodReference;
/*
    使用this引用本类的成员方法
 */
public class Husband {
    //定义一个买房子的方法
    public void buyHouse(){
        System.out.println("北京二环内买一套四合院!");
    }

    //定义一个结婚的方法,参数传递Richable接口
    public void marry(Richable r){
        r.buy();
    }

    //定义一个非常高兴的方法
    public void soHappy(){
        //调用结婚的方法,方法的参数Richable是一个函数式接口,传递Lambda表达式
       /* marry(()->{
            //使用this.成员方法,调用本类买房子的方法
            this.buyHouse();
        });*/

        /*
            使用方法引用优化Lambda表达式
            this是已经存在的
            本类的成员方法buyHouse也是已经存在的
            所以我们可以直接使用this引用本类的成员方法buyHouse
         */
        marry(this::buyHouse);
    }

    public static void main(String[] args) {
        new Husband().soHappy();
    }
}
```

###  方法引用：通过类的构造器(构造方法)引用 ###

```java
package com.itheima.demo09.ConstructorMethodReference;
/*
    定义一个创建Person对象的函数式接口
 */
@FunctionalInterface
public interface PersonBuilder {
    //定义一个方法,根据传递的姓名,创建Person对象返回
    Person builderPerson(String name);
}
package com.itheima.demo09.ConstructorMethodReference;

public class Person {
    private String name;

    public Person() {
        System.out.println("无参构造被调用");
    }

    public Person(String name) {
        this.name = name;
        System.out.println("有参构造被调用");
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
package com.itheima.demo09.ConstructorMethodReference;
/*
    类的构造器(构造方法)引用
 */
public class Demo {
    //定义一个方法,参数传递姓名和PersonBuilder接口,方法中通过姓名创建Person对象
    public static void printName(String name,PersonBuilder pb){
        Person person = pb.builderPerson(name);
        System.out.println(person.getName());
    }

    public static void main(String[] args) {
        //调用printName方法,方法的参数PersonBuilder接口是一个函数式接口,可以传递Lambda
        printName("迪丽热巴",(String name)->{
            return new Person(name);
        });

        /*
            使用方法引用优化Lambda表达式
            构造方法new Person(String name) 已知
            创建对象已知 new
            就可以使用Person引用new创建对象
         */
        printName("古力娜扎",Person::new);//使用Person类的带参构造方法,通过传递的姓名创建对象
    }
}
```

### 方法引用：通过数组的构造器引用 ###

```java
package com.itheima.demo10.ArrayMethodReference;
/*
    定义一个创建数组的函数式接口
 */
@FunctionalInterface
public interface ArrayBuilder {
    //定义一个创建int类型数组的方法,参数传递数组的长度,返回创建好的int类型数组
    int[] builderArray(int length);
}

package com.itheima.demo10.ArrayMethodReference;

import java.util.Arrays;

/*
    数组的构造器引用
 */
public class Demo {
    /*
        定义一个方法
        方法的参数传递创建数组的长度和ArrayBuilder接口
        方法内部根据传递的长度使用ArrayBuilder中的方法创建数组并返回
     */
    public static int[] createArray(int length, ArrayBuilder ab){
        return  ab.builderArray(length);
    }

    public static void main(String[] args) {
        //调用createArray方法,传递数组的长度和Lambda表达式
        int[] arr1 = createArray(10,(len)->{
            //根据数组的长度,创建数组并返回
            return new int[len];
        });
        System.out.println(arr1.length);//10

        /*
            使用方法引用优化Lambda表达式
            已知创建的就是int[]数组
            数组的长度也是已知的
            就可以使用方法引用
            int[]引用new,根据参数传递的长度来创建数组
         */
        int[] arr2 =createArray(10,int[]::new);
        System.out.println(Arrays.toString(arr2));
        System.out.println(arr2.length);//10
    }
}
```