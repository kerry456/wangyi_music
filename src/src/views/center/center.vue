<template>
  <div class="right_cont">
    <div class="top">
      <Breadcrumb>
        <Breadcrumb-item href="/">日志中心</Breadcrumb-item>
        <Breadcrumb-item href="/">业务数据日志统计</Breadcrumb-item>
      </Breadcrumb>
    </div>
    <Row style="padding:1.5rem;background: #fff;margin-top: 1rem">
      <Col span="22">
        <Col span="8">
          <Col span="5">区块号:</Col>
          <Col span="16">
            <Input @on-change="handleClear1" clearable placeholder="请输入" class="search-input" v-model="searchValue1"/>
          </Col>
        </Col>
        <Col span="8">
          <Col span="5">区块地址:</Col>
          <Col span="16">
            <Input @on-change="handleClear" clearable placeholder="请输入" class="search-input" v-model="searchValue"/>
          </Col>
        </Col>
        <Col span="8">
          <Col span="5">标签:</Col>
          <Col span="16">
            <Input @on-change="handleClear2" clearable placeholder="请输入" class="search-input" v-model="searchValue2"/>
          </Col>
        </Col>
      </Col>
      <Col span="22" style="margin-top: 1rem">
        <Col span="8">
          <Col span="5">操作类型:</Col>
          <Col span="16">
            <Select v-model="searchKey" class="search-col">
              <Option v-for="item in data2" :value="item.username">{{ item.username }}</Option>
            </Select>
          </Col>
        </Col>
        <Col span="8">
          <Col span="5">操作人:</Col>
          <Col span="16">
            <Select v-model="searchKey1" class="search-col">
              <Option v-for="item in data3" v-if="item.key !== 'handle'" :value="item.label">{{ item.label }}</Option>
            </Select>
          </Col>
        </Col>
        <Col span="8">
          <Col span="5">操作时间:</Col>
          <Col span="16">
            <Date-picker type="daterange" placement="bottom-end" placeholder="选择日期" v-model="times"></Date-picker>
          </Col>
        </Col>
      </Col>
      <Col style="clear:both;padding-top:1rem">
        <Button type="dashed" @click="handleReset('formValidate')" style="float:right;margin-left: 8px;margin-right: 5rem;">重置</Button>
        <Button type="primary" style="float:right" @click="selectGet">查询</Button>
      </Col>
    </Row>
    <Table border :columns="columns1" :data="data1"></Table>
    <p style="background: #fff;text-align: right;padding: 1rem 1rem 25rem 0"><Page :total="40" show-elevator show-sizer></Page></p>
  </div>
</template>

<script>
  export default {
    name: 'center',
    data () {
      return{
        // 区块地址
        searchValue: '',
        // 区块
        searchValue1: '',
        // 标签
        searchValue2: '',
        // 操作类型
        searchKey: '',
        // 操作人
        searchKey1: '',
        times: '',
        data2: [
          {
            value: 'beijing',
            label: '北京市'
          }
        ],
        data3: [
          {
            value: 'beijing',
            label: '北京市'
          }
        ],
        columns1: [
          {
            title: '区块号',
            key: 'num',
            width: 100
          },
          {
            title: '交易地址',
            key: 'address'
          },
          {
            title: '标签',
            key: 'label',
            width: 100
          },
          {
            title: '操作人',
            key: 'user',
            width: 100
          },
          {
            title: '操作类型',
            key: 'type',
            width: 150
          },
          {
            title: 'IP地址',
            key: 'ipAddress',
            width: 150
          },
          {
            title: '操作时间',
            key: 'times',
            width: 150
          }
        ],
        data1: [
          {
            num: '#10',
            address: '0x59c86db35bd86f1138019800a713a158ba2a14d81a3652c6b5da6d3e18aa2cd7',
            label: '财政  金融',
            user: '张三',
            ipAddress: '222.29.151.102',
            type: '存证-新增',
            times: '2020-01-13 14:46:45'
          }
        ]
      }
    },
    methods: {
      // 重置
      handleReset (name) {
        this.searchValue = ''
        this.searchValue1 = ''
        this.searchValue2 = ''
        this.searchKey = ''
        this.searchKey1 = ''
        this.times = ''
      },
      handleClear (e) {
        if (e.target.value === '') this.data1 = this.value
      },
      handleClear1 (e) {
        if (e.target.value === '') this.data1 = this.value
      },
      handleClear2 (e) {
        if (e.target.value === '') this.data1 = this.value
      },
      // 查询
      selectGet () {
        let param = {
          name: this.searchValue,
          num: this.searchValue1,
          panel: this.searchValue2,
          username: this.searchKey,
          label: this.searchKey1,
          time: this.times
        }
        console.log(param)
      }
    }
  }
</script>

<style lang="css">
  .top{
    background: #fff;
    line-height: 3rem;
    padding-left: 3rem;
    height: 3rem;
    font-size: 14px;
  }
  .ivu-table-wrapper{
    border:0
  }
</style>
