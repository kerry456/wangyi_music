<template>
  <div class="right_cont">
    <div class="top">
      <Breadcrumb>
        <Breadcrumb-item href="/">信息存证</Breadcrumb-item>
        <Breadcrumb-item href="/">数据存证</Breadcrumb-item>
      </Breadcrumb>
    </div>
    <div class="center">
      <div style="width:90%;margin:0 auto">
        <Row>
          <Col sapn="22">
            <Col span="8">
              <Col span=5>用户名称:</Col>
              <Col span="16"><Select v-model="model1" style="width:90%">
                <Option v-for="item in cityList" :value="item.value">{{ item.label }}</Option>
              </Select></Col>
            </Col>
            <Col span="7">
              <Col span="4">标签:</Col>
              <Col span="16"><Input v-model="value1" placeholder="请输入"></Input></Col>
            </Col>
            <Col span="9">
              <Col span="5">文件名称:</Col>
              <Col span="15">
                <Select v-model="model2" style="width:90%">
                  <Option v-for="item in file" :value="item.value">{{ item.label }}</Option>
                </Select>
              </Col>
            </Col>
          </Col>
          <Col span="8" style="margin-top: 1rem;clear: both">
            <Col span=5>存证状态:</Col>
            <Col span="16"><Select v-model="model3" style="width:90%">
              <Option v-for="item in state" :value="item.value">{{ item.label }}</Option>
            </Select></Col>
          </Col>
          <p style="clear: both;text-align: right;margin-top: 1rem">
            <Button type="primary">查询</Button>
            <Button @click="handleReset('formValidate')" style="margin-left: 8px;margin-right: 5rem">重置</Button>
          </p>
        </Row>
        <Table border :stripe="true" :context="self" :columns="columns1" :data="data1" style="margin-top: 2rem"></Table>
      </div>
    </div>
  </div></template>

<script>
  export default {
    name: 'status',
    data () {
      return {
        // 表格
        self: this,
        // 标签
        value1: '',
        // 用户名称
        model1: '',
        // 文件名称
        model2: '',
        // 存证状态
        model3: '',
        // 用户名称选项
        cityList: [
          {
            value: 'beijing',
            label: '北京市'
          },
        ],
        // 文件名声选项
        file: [
          {
            value: 'aaa',
            label: '文件'
          }
        ],
        //存证状态选项
        state: [
          {
            value: 'yiwancheng',
            label: '已完成'
          }
        ],
        // 表格名称
        columns1: [
          {
            title: '序号',
            type: 'index',
            align: 'center'
          },
          {
            title: '用户名称',
            key: 'name'
          },
          {
            title: '标签',
            key: 'tag'
          },
          {
            title: '存整数据',
            key: 'number'
          },
          {
            title: '文件名称',
            key: 'fileName'
          },
          {
            title: '存证状态',
            key: 'record'
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
                      console.log(111)
                    }
                  }
                }, '重传')
              ])
            }
          }
        ],
        // 表格内容
        data1: [
          {
            name: 'aaa',
            tag: '1',
            number: '10',
            fileName: '文件',
            record: '已上传'
          }
        ]
      }
    },
    methods: {
      handleReset (name) {
        this.$refs[name].resetFields();
      },
      handleEdit(index, row) {
        console.log(index, row);
      },
    }
  }
</script>

<style lang="less">
  .right_cont {
    padding: 0;
    .top {
      background: #fff;
      line-height: 3rem;
      padding-left: 2rem;
      height: 3rem;
      font-size: 14px;
    }
    .center {
      margin: 1.5rem 1rem;
      background: #fff;
      padding-top: 4rem;
      height:30rem;
    }
    .top_center {
      width: 31%;
      margin: 0 auto;
      p{
        margin-bottom: 1rem;
      }
    }
  }
</style>
