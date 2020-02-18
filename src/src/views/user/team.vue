<template>
  <div style="margin:1rem 1.5rem;background: #fff;height:37rem">
    <div class="team_head">
      <Button type="primary" @click="modal1 = true">新增</Button>
      <Modal v-model="modal1" title="新增">
        <Tabs value="name1" :animated="false">
          <Tab-pane label="法人用户" name="name1">

            <div>
              <Form ref="formValidate" :model="formValidate" :rules="ruleValidate" :label-width="105">
                <Form-item label="用户名称" prop="name">
                  <Input v-model="formValidate.name" placeholder="请输入用户名称"></Input>
                </Form-item>
                <Form-item label="密码" prop="password">
                  <Input v-model="formValidate.password" placeholder="请输入密码"></Input>
                </Form-item>
                <Form-item label="机构名称" prop="username">
                  <Input v-model="formValidate.username" placeholder="请输入机构名称"></Input>
                </Form-item>
                <Form-item label="社会信用代码" prop="society">
                  <Input v-model="formValidate.society" placeholder="请输入社会信用代码"></Input>
                </Form-item>
                <Form-item label="单位注册地址" prop="address">
                  <Input v-model="formValidate.address" placeholder="请输入社会信用代码"></Input>
                </Form-item>
                <Form-item label="法人代表" prop="deputy">
                  <Input v-model="formValidate.deputy" placeholder="请输入社会信用代码"></Input>
                </Form-item>
                <Form-item label="法人证件类型" prop="papers">
                  <Select v-model="formValidate.papers" placeholder="请选择证件类型">
                    <Option value="card">二代身份证</Option>
                  </Select>
                </Form-item>
                <Form-item label="法人证件号码" prop="num">
                  <Input v-model="formValidate.num" placeholder="请输入法人证件号码"></Input>
                </Form-item>
                <Form-item label="运营联系方式" prop="touch">
                  <Input v-model="formValidate.qu" placeholder="区号" style="width:20%"></Input>
                  <span>——</span>
                  <Input v-model="formValidate.phone" placeholder="联系号码" style="width: 71%"></Input>
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
              </Form>
            </div>

          </Tab-pane>
          <Tab-pane label="自然用户" name="name2">
            <Nature></Nature>
          </Tab-pane>
        </Tabs>
        <div slot="footer">
          <Button type="primary" @click="handleSubmit('formValidate')">确定</Button>
          <Button @click="cancel" style="margin-left: 8px">取消</Button>
        </div>
      </Modal>
      <div class="team_cont">
        <Input v-model="value" placeholder="请输入关键字搜索" size="small" style="width: 87%"></Input>
        <svg-icon icon-class="搜索" />
      </div>
    </div>
    <Table :columns="columns1" :data="data1" style="clear:both;margin: 2rem auto 0;width:70%"></Table>

<!--    编辑-->
    <Modal v-model="modal2" title="编辑">
        <Form ref="formValidate" :model="forms" :label-width="105">
          <Form-item label="用户名称" prop="uname">
            <Input v-model="forms.uname" placeholder="请输入用户名称"></Input>
          </Form-item>
          <Form-item label="密码" prop="passwords">
            <Input v-model="forms.passwords" placeholder="请输入密码"></Input>
          </Form-item>
          <Form-item label="机构名称" prop="jgmc">
            <Input v-model="forms.jgmc" placeholder="请输入机构名称"></Input>
          </Form-item>
          <Form-item label="社会信用代码" prop="shxydm">
            <Input v-model="forms.shxydm" placeholder="请输入社会信用代码"></Input>
          </Form-item>
          <Form-item label="单位注册地址" prop="dwzcdz">
            <Input v-model="forms.dwzcdz" placeholder="请输入社会信用代码"></Input>
          </Form-item>
          <Form-item label="法人代表" prop="frdb">
            <Input v-model="forms.frdb" placeholder="请输入社会信用代码"></Input>
          </Form-item>
          <Form-item label="法人证件类型" prop="frzjlx">
            <Select v-model="forms.frzjlx" placeholder="请选择证件类型">
              <Option value="card">二代身份证</Option>
            </Select>
          </Form-item>
          <Form-item label="法人证件号码" prop="frnum">
            <Input v-model="forms.frnum" placeholder="请输入法人证件号码"></Input>
          </Form-item>
          <Form-item label="运营联系方式" prop="tell">
            <Input v-model="forms.qh" placeholder="区号" style="width:20%"></Input>
            <span>——</span>
            <Input v-model="forms.lianxi" placeholder="联系号码" style="width: 71%"></Input>
          </Form-item>
          <Form-item label="有效时间" prop="yxsj">
            <Row>
              <Col span="11">
                <Form-item prop="date">
                  <Date-picker type="date" placeholder="开始时间" v-model="forms.starttime"></Date-picker>
                </Form-item>
              </Col>
              <Col span="2" style="text-align: center">-</Col>
              <Col span="11">
                <Form-item prop="time">
                  <Date-picker type="date" placeholder="结束时间" v-model="forms.endtime"></Date-picker>
                </Form-item>
              </Col>
            </Row>
          </Form-item>
          <Form-item label="状态" prop="zt">
            <Radio-group v-model="forms.zt">
              <Radio label="ons">开启</Radio>
              <Radio label="offs">关闭</Radio>
            </Radio-group>
          </Form-item>
        </Form>
      <div slot="footer">
        <Button type="primary" @click="handleSubmit('formValidate')">确定</Button>
        <Button @click="cancel" style="margin-left: 8px">取消</Button>
      </div>
    </Modal>
  </div>
</template>

<script>
import Nature from './nature/nature'
  export default {
    name: 'team',
    components: {
      Nature
    },
    data () {
      return {
        value: '',
        modal1: false,
        modal2: false,
        // 新增
        formValidate: {
          name: '',
          password: '',
          username: '',
          society: '',
          address: '',
          deputy: '',
          papers: '',
          num: '',
          qu: '',
          phone: '',
          status: 'on',
          date: '',
          time: '',
          valid: ''
        },
        // 编辑
        forms: {
          uname: '',
          passwords: '',
          jgmc: '',
          shxydm: '',
          dwzcdz: '',
          frdb: '',
          frzjlx: '',
          frnum: '',
          qh: '',
          lianxi: '',
          zt: 'ons',
          starttime: '',
          endtime: '',
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
          society: [
            { required: true, message: '社会信用代码不能为空', trigger: 'blur' }
          ],
          valid: [
            { required: true, type: 'valid', message: '请选择日期', trigger: 'change' }
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
        },
        // 表格
        columns1: [
          {
            type: 'index',
            title: '序号'
          },
          {
            title: '用户名',
            key: 'name'
          },
          {
            title: '密码',
            key: 'password'
          },
          {
            title: '用户类型',
            key: 'type'
          },
          {
            width: 150,
            title: '机构名称/真实姓名',
            key: 'username'
          },
          {
            title: '倒计时',
            key: 'time'
          },
          {
            title: '状态',
            key: 'status'
          },
          {
            title: '操作',
            key: 'action',
            width: 150,
            align: 'center',
            render: (h, params) => {
              return h('div', [
                h('Button', {
                  props: {
                    type: 'primary',
                    size: 'small'
                  },
                  style: {
                    marginRight: '5px'
                  },
                  on: {
                    click: () => {
                      this.doEdit(params.row)
                      // this.modal2 =true
                    }
                  }
                }, '编辑'),
                h('Button', {
                  props: {
                    type: 'error',
                    size: 'small'
                  },
                  on: {
                    click: () => {
                      this.doDelete(params.row)
                    }
                  }
                }, '删除')
              ])
            }
          }
        ],
        data1: [
          {
            name: '王小明',
            password: 18,
            type: '12',
            username: '王小明',
            time: 10,
            status: '已完成'
          },
          {
            name: '王小明',
            password: 18,
            type: '12',
            username: '王小明',
            time: 10,
            status: '已完成'
          }
        ]
      }
    },
    methods: {
      handleSubmit (name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            this.$Message.success('提交成功!')
            this.modal1 = false
          } else {
            this.$Message.error('表单验证失败!')
          }
        })
      },
      cancel () {
        this.$Message.info('点击了取消')
        this.modal1 = false
      },
      doEdit (row) {
        console.log(row)
        this.modal2 = true
      }
    }
  }
</script>

<style lang="css">
.team_head{
  width: 70%;
  margin: 0 auto;
  padding-top: 3rem;
  padding-bottom:2rem;
}
.team_cont{
  float: right;
  border: 1px solid #ccc;
  border-radius: 5px;
  position: relative;
}
.team_cont input{
  border:0
}
.team_cont .svg-icon{
  font-size: 17px;
  position: absolute;
  top:0.2rem;
}
.ivu-table-default{
 width:100%
}
</style>
