<template>
  <div>
    <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="105">
      <Form-item label="用户名称" prop="name">
        <Input v-model="formValidate.name" placeholder="请输入用户名称"></Input>
      </Form-item>
      <Form-item label="密码" prop="password">
        <Input v-model="formValidate.password" placeholder="请输入密码"></Input>
      </Form-item>
      <Form-item label="真实姓名" prop="username">
        <Input v-model="formValidate.username" placeholder="请输入真实姓名"></Input>
      </Form-item>
      <Form-item label="证件类型" prop="papers">
        <Select v-model="formValidate.papers" placeholder="请选择证件类型">
          <Option value="card">二代身份证</Option>
        </Select>
      </Form-item>
      <Form-item label="证件号码" prop="num">
        <Input v-model="formValidate.num" placeholder="请输入证件号码"></Input>
      </Form-item>
      <Form-item label="运营联系方式" prop="touch">
        <Input v-model="formValidate.qu" placeholder="区号" style="width:20%"></Input>
        <span>——</span>
        <Input v-model="formValidate.phone" placeholder="联系号码" style="width: 71%"></Input>
      </Form-item>
      <Form-item label="邮箱" prop="emal">
        <Input v-model="formValidate.emal" placeholder="请输入邮箱"></Input>
      </Form-item>
      <Form-item label="有效时间" prop="valid">
        <Row>
          <Col span="11">
            <Form-item prop="date">
              <Date-picker type="date" placeholder="开始时间" v-model="formValidate.date"></Date-picker>
            </Form-item>
          </Col>
          <Col span="2" style="text-align: center">-</Col>
          <Col span="11">
            <Form-item prop="time">
              <Date-picker type="date" placeholder="结束时间" v-model="formValidate.time"></Date-picker>
            </Form-item>
          </Col>
        </Row>
      </Form-item>
      <Form-item label="状态" prop="status">
        <Radio-group v-model="formValidate.status">
          <Radio label="on">开启</Radio>
          <Radio label="off">关闭</Radio>
        </Radio-group>
      </Form-item>
      <!--        <Form-item>-->
      <!--          <Button type="primary" @click="handleSubmit('formValidate')">确定</Button>-->
      <!--          <Button type="ghost" @click="handleReset('formValidate')" style="margin-left: 8px">重置</Button>-->
      <!--        </Form-item>-->
    </Form>
  </div>
</template>

<script>
  export default {
    name: 'nature',
    data () {
      return {
        formValidate: {
          name: '',
          password: '',
          username: '',
          papers: '',
          num: '',
          qu: '',
          emal: '',
          phone: '',
          status: 'on',
          date: '',
          time: '',
          valid: ''
        },
        ruleValidate: {
          name: [
            { required: true, message: '姓名不能为空', trigger: 'blur' }
          ],
          password: [
            { required: true, message: '密码不能为空', trigger: 'blur' },
            { type: 'password', message: '邮箱格式不正确', trigger: 'blur' }
          ],
          username: [
            { required: true, message: '机构名称不能为空', trigger: 'blur' }
          ],
          emal: [
            { required: true, message: '不能邮箱为空', trigger: 'blur' }
          ],
          valid: [
            { required: true, type: 'valid', message: '请选择日期', trigger: 'change' }
          ],
          touch: [
            { required: true, message: '运营联系方式不能为空', trigger: 'blur' }
          ],
          date: [
            { required: true, type: 'date', message: '请选择日期', trigger: 'change' }
          ],
          time: [
            { required: true, type: 'date', message: '请选择时间', trigger: 'change' }
          ],
          desc: [
            { required: true, message: '请输入个人介绍', trigger: 'blur' },
            { type: 'string', min: 20, message: '介绍不能少于20字', trigger: 'blur' }
          ]
        }
      }
    },
    methods: {
    }
  }
</script>

<style scoped>

</style>
