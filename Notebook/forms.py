from wtforms import Form, StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired,Length,ValidationError,Email,EqualTo
from flask_wtf import FlaskForm
from mysql_util import MysqlUtil

# Register Form Class
class LoginForm(FlaskForm):
    username = StringField(
        '用户名',
        validators=[
            DataRequired(message='请输入用户名'),
            Length(min=2, max=25,message='长度在4-25个字符之间')
        ]
    )
    password = PasswordField(
        '密码',
        validators = [
            DataRequired(message='密码不能为空'),
            Length(min=6,max=20,message='长度在6-20个字符之间'),
        ]
    )

    def validate_username(self,field):
        sql = "SELECT * FROM users  WHERE username = '%s'" % (field.data) # 根据用户名查找user表中记录
        db = MysqlUtil() # 实例化数据库操作类
        result = db.fetchone(sql) # 获取一条记录
        if not result:
            raise ValidationError("用户名不存在")
    def validate_password(self,field):
        sql = "SELECT * FROM users  WHERE password = '%s'" % (field.data) # 根据用户名查找user表中记录
        db = MysqlUtil() # 实例化数据库操作类
        result = db.fetchone(sql) # 获取一条记录
        if not result:
            raise ValidationError("")

class RegisterForm(FlaskForm):
    username = StringField(
        '用户名',
        validators=[
            DataRequired(message='请输入用户名'),
            Length(min=4, max=25,message='长度在4-25个字符之间')
        ]
    )
    password = PasswordField(
        '密码',
        validators = [
            DataRequired(message='密码不能为空'),
            Length(min=6,max=20,message='长度在6-20个字符之间'),
        ]
    )
    email = StringField(validators=[Email(message="请输入正确的邮箱格式！")])
    check = PasswordField(validators=[EqualTo("password",message="两次密码不一致！")])


    def validate_email(self,field):
        sql = "SELECT * FROM users  WHERE email = '%s'" % (field.data) # 根据用户名查找user表中记录
        db = MysqlUtil() # 实例化数据库操作类
        result = db.fetchone(sql) # 获取一条记录
        if result:
            raise ValidationError("该邮箱已经注册过了！")
    def validate_username(self,field):
        sql = "SELECT * FROM users  WHERE username = '%s'" % (field.data) # 根据用户名查找user表中记录
        db = MysqlUtil() # 实例化数据库操作类
        result = db.fetchone(sql) # 获取一条记录
        if result:
            raise ValidationError("用户名已存在")


# Article Form Class
class ArticleForm(Form):
    title = StringField(
        '标题',
        validators=[
            DataRequired(message='长度在2-30个字符'),
            Length(min=2,max=30)
        ]
    )
    content = TextAreaField(
        '内容',
        validators=[
            DataRequired(message='长度不少于5个字符'),
            Length(min=5)
        ]
    )