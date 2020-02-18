<template>
  <div class="level_top">
    <Row style="padding:1.5rem">
      <Col span="22">
        <Col span="8">
          <Col span=5>交易哈希:</Col>
          <Col span="16">
            <Input @on-change="handleClear" clearable placeholder="请输入" class="search-input" v-model="searchValue"/>
          </Col>
        </Col>
        <Col span="8">
          <Col span=5>区块号:</Col>
          <Col span="16">
            <Input @on-change="handleClear1" clearable placeholder="请输入" class="search-input" v-model="searchValue1"/>
          </Col>
        </Col>
        <Col span="8">
          <Col span=5>计算节点:</Col>
          <Col span="16">
            <Input @on-change="handleClear2" clearable placeholder="请输入" class="search-input" v-model="searchValue2"/>
          </Col>
        </Col>
      </Col>
      <Col span="22" style="margin-top: 1rem">
        <Col span="8">
          <Col span=5>用户:</Col>
          <Col span="16">
            <Select v-model="searchKey" class="search-col">
              <Option v-for="item in data1" v-if="item.key !== 'handle'" :value="item.username">{{ item.username }}</Option>
            </Select>
          </Col>
        </Col>
        <Col span="8">
          <Col span=5>标签:</Col>
          <Col span="16">
            <Input clearable placeholder="请输入" class="search-input" v-model="searchKey1"/>
          </Col>
        </Col>
        <Col span="8">
          <Col span=5>时间:</Col>
          <Col span="16">
            <Date-picker type="daterange" placement="bottom-end" placeholder="选择日期" v-model="times"></Date-picker>
          </Col>
        </Col>
      </Col>
      <Col style="clear:both;padding-top:1rem">
        <router-link to="/data"><Button type="primary" style="float:left;">新建</Button></router-link>
        <Button type="dashed" @click="handleReset('formValidate')" style="float:right;margin-left: 8px;margin-right: 5rem;">重置</Button>
        <Button type="primary" style="float:right" @click="selectGet">查询</Button>
      </Col>
    </Row>
    <Table :columns="columns1" :data="data1" style="margin:1rem;border: 0"></Table>
    <p style="background: #fff;text-align: right;padding: 1rem 1rem 0 0"><Page :total="40" show-elevator show-sizer></Page></p>
  </div>
</template>

<script>
  export default {
    name: 'index',
    data () {
      return {
        insideColumns: [],
        insideTableData: [],
        edittingCellId: '',
        edittingText: '',
        // 交易嘻哈
        searchValue: '',
        // 区块
        searchValue1: '',
        // 计算节点
        searchValue2: '',
        // 用户
        searchKey: '',
        // 标签
        searchKey1: '',
        times: '',
        // 用户 选项
        // columns: {
        //   type: Array,
        //   default () {
        //     return []
        //   }
        // },
        columns1: [
          {
            title: '交易哈希',
            key: 'name'
          },
          {
            title: '区块号',
            key: 'num'
          },
          {
            title: '用户',
            key: 'username'
          },
          {
            title: '计算节点',
            key: 'panel'
          },
          {
            title: '标签',
            key: 'label'
          },
          {
            title: '时间',
            key: 'time'
          }
        ],
        data1: [
          {
            name: 'aaaa',
            num: '30',
            username: '老王',
            panel: '4',
            label: '2',
            time: '2020/2/10'
          },
          {
            name: 'bbb',
            num: '30',
            username: '老张',
            panel: '4',
            label: '3',
            time: '2020/2/10'
          }
        ],
        url: {
          // edit:"/agents/agents/edit",
          // list: "/multilevel/level-2-3?/list?audit=4",
          // delete: "/agents/agents/delete",
          // deleteBatch: "/agents/agents/deleteBatch",
          // exportXlsUrl: "agents/agents/exportXls",
          // importExcelUrl: "agents/agents/importExcel",
        },
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
  .level_top{
    background: #fff;
    margin:1rem 1.5rem;
    height:37rem;
  }
</style>
