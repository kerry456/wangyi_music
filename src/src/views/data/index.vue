<template>
  <div class="right_cont">
    <div class="top">
      <Breadcrumb>
        <Breadcrumb-item href="/">信息存证</Breadcrumb-item>
        <Breadcrumb-item href="/">数据存证</Breadcrumb-item>
      </Breadcrumb>
    </div>
    <div class="center">
      <div class="center_top">
        <Tabs :animated="false">
          <Tab-pane label="单用户数据存证">
            <SingleUser></SingleUser>
          </Tab-pane>
          <!--      多用户导数据-->
          <Tab-pane label="批量用户数据存证">
            <Data></Data>
            <!--        表格-->
            <el-table
              :data="tableData"
              border
              style="width: 100%">
              <el-table-column
                prop="name"
                label="用户名称"
                width="180">
                <el-input v-model="username"></el-input>
              </el-table-column>
              <el-table-column
                prop="tag-1"
                label="标签一"
                width="180">
                <el-input v-model="tag_1"></el-input>
              </el-table-column>
              <el-table-column
                prop="tag-2"
                label="标签二">
                <el-input v-model="tag_2"></el-input>
              </el-table-column>
              <el-table-column
                prop="tag-3"
                label="标签三">
                <el-input v-model="tag_3"></el-input>
              </el-table-column>
              <el-table-column
                prop="tag-4"
                label="标签四">
                <el-input v-model="tag_4"></el-input>
              </el-table-column>
              <el-table-column
                prop="tag-5"
                label="标签五">
                <el-input v-model="tag_5"></el-input>
              </el-table-column>
              <el-table-column
                prop="record"
                label="存证数据">
                <el-input v-model="record"></el-input>
              </el-table-column>
            </el-table>
            <p style="text-align: center;margin-top: 2rem"><Button type="primary"  @click="handleSubmit ('formValidate')">存证</Button></p>
          </Tab-pane>
        </Tabs>
      </div>
    </div>
  </div>
</template>

<script>
  import SingleUser from './single-user/single-user'
  import Data from './leading/data'
  export default{
    name: 'index',
    components: {
      SingleUser,
      Data
    },
    data () {
      return {
        tableData: [{
          name: '',
          tag_1: '',
          tag_2: '',
          tag_3: '',
          tag_4: '',
          tag_5: '',
          record: ''
        }],
        username: '',
        tag_1: '',
        tag_2: '',
        tag_3: '',
        tag_4: '',
        tag_5: '',
        record: ''
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
      // handleReset (name) {
      //   this.$refs[name].resetFields();
      // },
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
    }

    .center_top {
      padding: 1rem 1rem;
    }
  }
</style>
