<template>
  <div class="right_cont">
    <div class="top">
      <Breadcrumb>
        <Breadcrumb-item href="/">信息存证</Breadcrumb-item>
        <Breadcrumb-item href="/">数据存证</Breadcrumb-item>
      </Breadcrumb>
    </div>
    <div class="center">
      <div class="top_center">
          <p><Row><Col span="4">用户姓名:</Col><Col span="18"><Input v-model="value" placeholder="请输入"></Input></Col></Row></p>
          <p><Row><Col span="4">标签:</Col><Col span="18">
            <Select v-model="model1" style="width:200px">
              <Option v-for="(item ,index) in cityList" :value="item.value" :key="index">{{ item.label }}</Option>
            </Select>
          </Col></Row></p>
        <div>
          <Row><Col span="4">文件上传:</Col><Col span="20">
            <Upload></Upload>
          </Col></Row>
        </div>
        <p style="text-align: center;margin-top: 9rem;padding-bottom: 6rem"><Button type="primary"  @click="handleSubmit ('formValidate')">存证</Button></p>
      </div>
    </div>
  </div>
</template>

<script>
  import Upload from './leading/upload'
  export default {
    name: 'file',
    components: {
      Upload
    },
    data () {
      return {
        value: '',
        model1: '',
        cityList:[
          {
            value: 'beijing',
            label: '北京市'
          },
        ]
      }
    },
    methods: {
      // 存证提示
      handleSubmit (name) {
        this.$refs[name].validate((valid) => {
          if (valid) {
            this.$Message.success('存证成功!');
          } else {
            this.$Message.error('表单验证失败!');
          }
        })
      }
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
