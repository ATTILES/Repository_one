#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define max 100

struct person
{
    char NO[20];
    int sex;
    int age;
    char phone[20];
    char address[50];
};

struct book
{
    struct person array[max];
    int size;
};

void showMenu()
{
    printf("***************************\n");
    printf("*****  1,添加学生信息  *****\n");
    printf("*****  2,显示学生信息  *****\n");
    printf("*****  3,删除学生信息  *****\n");
    printf("*****  4,查找学生信息  *****\n");
    printf("*****  5,修改学生信息  *****\n");
    printf("*****  6,   *****\n");
    printf("*****  0，退出 *****\n");
    printf("***************************\n");
}

void add(struct book* abs)
{
    if (abs->size == max)
    {
        printf("已满\n");
    }
    else
    {
        printf("请输入学号\n");
        scanf("%s", abs->array[abs->size].NO);

        printf("输入0 女\n");
        printf("输入1 男\n");
        while (1)
        {
            scanf("%d", &abs->array[abs->size].sex);
            if (abs->array[abs->size].sex == 1 || abs->array[abs->size].sex == 0)
            {
                break;
            }
            printf("错误\n");
        }

        printf("请输入年龄\n");
        scanf("%d", &abs->array[abs->size].age);

        printf("请输入电话\n");
        scanf("%s", abs->array[abs->size].phone);

        printf("请输入地址\n");
        scanf("%s", abs->array[abs->size].address);

        abs->size++;
        printf("添加成功\n");
    }
}

void find(struct book* abs)
{
    if (abs->size == 0)
    {
        printf("null\n");
    }
    for (int i = 0; i < abs->size; i++)
    {
        printf("学号：%s\t", abs->array[i].NO);
        printf("性别：%s\t", (abs->array[i].sex == 1 ? "男" : "女"));
        printf("年龄：%d\t", abs->array[i].age);
        printf("电话：%s\t", abs->array[i].phone);
        printf("地址：%s\n", abs->array[i].address);
    }
}

void deleted(struct book* abs)
{
    // 删除学生信息的代码
}

int main()
{
    struct book abs;
    abs.size = 0;
    int select = 0;
    while (1)
    {
        showMenu();
        scanf("%d", &select);
        switch (select)
        {
        case 1:
            add(&abs);
            break;
        case 2:
            find(&abs);
            break;
        case 3:
            deleted(&abs);
            break;
        case 4:
            break;
        case 5:
            break;
        case 6:
            break;
        case 0:
            printf("baybay\n");
            system("pause");
            exit(0);
            break;
        default:
            break;
        }
    }

    return 0;
}
