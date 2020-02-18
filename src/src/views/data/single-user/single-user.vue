<template>
  <div class="cont">
    <p><Row><Col span="2">用户姓名:</Col><Col span="6"><Input v-model="value3" placeholder="请输入"></Input></Col></Row></p>
    <p><Row><Col span="2">标签:</Col><Col span="6"><Input v-model="value4" placeholder="请输入..."></Input></Col></Row></p>
    <p><Row><Col span="2">存证方式:</Col>
      <Radio-group v-model="vertical" vertical>
        <Radio label="people" @click="cur=0" style="display: inline-block">
          <span @click="cur=0">单条数据</span>
        </Radio>
        <Radio label="peoples" @click="cur=1" style="display: inline-block">
          <span @click="cur=1">批量导入</span>
        </Radio>
      </Radio-group>
    </Row></p>
    <p v-show="cur==0"><Row><Col span="2">数据存证:</Col><Col span="8"><Form ref="formDynamic" :model="formDynamic" :label-width="80">
      <Form-item
        v-for="(item, index) in formDynamic.items"
        :key="index"
        :prop="'items.' + index + '.value'"
        :rules="{required: true, message: '数据存证' + (index + 1) +'不能为空', trigger: 'blur'}">
        <Row>
          <Col span="4">
            <Input type="text" v-model="item.value1" :placeholder="(index +1)"></Input>
          </Col>
          <Col span="14">
            <Input type="text" v-model="item.value" placeholder="请输入..."></Input>
          </Col>
          <Col span="1" offset="1">
            <svg-icon icon-class="删除" />
            <!--                          <Button type="ghost" @click="handleRemove(index)"><i class="ivu-icon ios-minus-outline"></i></Button>-->
          </Col>
        </Row>
      </Form-item>
      <Form-item>
        <Row>
          <Col span="18">
            <Button type="dashed" long @click="handleAdd">新增</Button>
          </Col>
        </Row>
      </Form-item>
      <Form-item style="text-align: center">
        <!--              <Button type="primary" @click="handleSubmit('formDynamic')">存证</Button>-->
        <!--                      <Button type="ghost" @click="handleReset('formDynamic')" style="margin-left: 8px">重置</Button>-->
      </Form-item>
    </Form></Col></Row>
    </p>
    <div v-show="cur==1">
      <Data></Data>
    </div>
    <Col span="6">
      <el-table
        :data="tableData"
        border>
        <el-table-column
          prop="num"
          label="序号">
          <el-input v-model="num"></el-input>
        </el-table-column>
        <el-table-column
          prop="datas"
          label="存证数据">
          <el-input v-model="datas"></el-input>
        </el-table-column>
      </el-table>
    </Col>
    <p style="text-align: center;margin-top: 2rem;width: 69%"><Button type="primary"  @click="handleSubmit ('formValidate')">存证</Button></p>
  </div>
</template>

<script>
  import Data from '../leading/data'
  export default {
    name: 'single-user',
    components: {
      'Data':Data
    },
    data () {
      return {
        // 序号
        num: '',
        // 存证数据
        datas: '',
        // 单用户导入的表格
        tableData: '',
        // 默认单条数据
        vertical: 'people',
        //默认输入条数显示
        cur: 0,
        // 手动输入数据存证
        formDynamic: {
          items: [
            {
              //
              value: '',
              // 编号
              value1: ''
            }
          ]
        },
        data1: [
          {
            num: '',
            datas: ''
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
      },
      // 新增一行数据存证
      handleAdd () {
        this.formDynamic.items.push({
          value: ''
        })
      },
      // 数据存证数量
      handleRemoves (index) {
        this.formDynamic.items.splice(index, 1);
      },
    }
  }
</script>

<style lang="css">
.cont {
  margin-left:5rem
}
  .ivu-form-item-content{
    margin-left: 0!important;
  }
  .ivu-col-offset-1{
    font-size: 20px;
    margin-left: 1rem;
  }
  .cont p{
    margin-top: 1rem;
  }
</style>
