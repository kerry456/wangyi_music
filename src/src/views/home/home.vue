<style lang="less">
  @import './home.less';
</style>
<template>
  <div class="right_cont">
    <div class="top_cont">
      <p class="top_p">概览</p>
      <Row>
        <Col span="15">
          <Col class="hair"><img src="../../assets/img/20160821194924_UCvFZ.png"></Col>
          <Col span="6">
            <p @on-success-valid="handleSubmit" class="every">祝你开心每一天</p>
            <span class="people"><span>普通员工</span><span>|</span><span>***公司</span></span>
          </Col>
          <Col span="3" class="try">
            <Button type="primary" @click="modal1 = true">用户类型变更</Button>
            <Modal v-model="modal1" width="360">
              <p slot="header" style="color:#666;text-align:left;font-size: 18px;font-weight: normal">
                <Icon type="information-circled"></Icon>
                <span>用户类型变更</span>
              </p>
              <div style="text-align:left">
                <p>请选择登录身份</p>
                <p style="border-bottom: 1px solid;margin-bottom: 1rem;padding-bottom: 1rem;">谢谢</p>
                <p>请选择您常用身份</p>
                <Radio-group v-model="vertical" vertical>
                  <Radio label="jianguan">
                    <span>监管节点用户</span>
                  </Radio>
                  <Radio label="jisuan">
                    <span>计算节点用户</span>
                  </Radio>
                </Radio-group>
              </div>
              <div slot="footer">
                <Button type="primary" size="large" long @click="change">开始使用</Button>
              </div>
            </Modal>
          </Col>
        </Col>
        <Col class="letter">
          <div>
            <img src="../../assets/img/feiji.png">
            <p class="img_top">您已经存证 &nbsp <span>30条</span> &nbsp 信息</p>
            <p>已通过检验 &nbsp <span>30条</span> &nbsp 信息</p>
          </div>
        </Col>
      </Row>
    </div>
    <div class="bottom_cont" style="margin:0">
      <Row>
        <Col span="14" class="left">
          <Input v-model="cont">
            <Select v-model="select1" slot="prepend" style="width: 80px">
              <Option value="day">选项</Option>
              <Option value="month">月活</Option>
            </Select>
            <Button slot="append" to="/census" style="color: #fff">搜索</Button>
          </Input>
          <row class="font">
            <Col span="3">标签一</Col>
            <Col span="3">标签二</Col>
            <Col span="3">标签三</Col>
            <Col span="3">标签四</Col>
            <Col span="3">标签五</Col>
            <Col span="3">标签六</Col>
            <Col span="3">标签七</Col>
            <Col span="3">标签八</Col>
          </row>
        </Col>
        <Col span="9" class="right">
          <div class="titles">我要存证</div>
          <div class="file">
            <Row>
              <Col span="12"><Button type="primary">文件存证</Button></Col>
              <Col span="12"><Button type="primary">数据存证</Button></Col>
            </Row>
          </div>
        </Col>
      </Row>
    </div>
    <div class="bot_cont">
      <Row>
        <Col span="14" class="left">
          <div class="titles">我的任务<p>全部任务</p></div>
          <div class="renwu">
            <Row>
              <router-link to="/i18n_page"><Col span="8" class="list">
                <p>
                  <img src="../../assets/img/u97.png">
                  <span>区块高度:</span>
                  <span>158977</span>
                </p>
                <p>区块哈希:sdhioasfuoiamsfbhjskdmffsaiodl</p>
                <p><span>王富贵</span><span>5小时前</span></p>
              </Col></router-link>
              <Col span="8" class="list">
                <p>
                  <img src="../../assets/img/u97.png">
                  <span>区块高度:</span>
                  <span>158977</span>
                </p>
                <p>区块哈希:sdhioasfuoiamsfbhjskdmffsaiodl</p>
                <p><span>王富贵</span><span>5小时前</span></p>
              </Col>
              <Col span="8" class="list">
                <p>
                  <img src="../../assets/img/u97.png">
                  <span>区块高度:</span>
                  <span>158977</span>
                </p>
                <p>区块哈希:sdhioasfuoiamsfbhjskdmffsaiodl</p>
                <p><span>王富贵</span><span>5小时前</span></p>
              </Col>
            </Row>
          </div>
        </Col>
        <Col span="9" class="right">
          <div class="titles" style="font-weight: 400">存储动态</div>
          <div class="file">
            <p>
              <img src="../../assets/img/u180.png">
              <span>用户A</span>
              <span>3S前</span>
              <span>在</span>
              <span>计算节点A</span>
              <span>存储</span>
              <span>区块</span>
              <span>#158786</span>
            </p>
          </div>
          <div class="file">
            <p>
              <img src="../../assets/img/u180.png">
              <span>用户A</span>
              <span>3S前</span>
              <span>在</span>
              <span>计算节点A</span>
              <span>存储</span>
              <span>区块</span>
              <span>#158786</span>
            </p>
          </div>
          <div class="file">
            <p>
              <img src="../../assets/img/u180.png">
              <span>用户A</span>
              <span>3S前</span>
              <span>在</span>
              <span>计算节点A</span>
              <span>存储</span>
              <span>区块</span>
              <span>#158786</span>
            </p>
          </div>
        </Col>
      </Row>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'home' ,
    data () {
      return {
        // 默认单选
        vertical: 'jianguan',
        username: '',
        cont: '',
        select1: 'day',
        // 对话框
        modal1: false,
        danhao: '的方法V领快递费是服我就OK了麻烦发的'
      }
    },
    mounted () {
      //
    },
    methods: {
      handleSubmit ({ userName, password }) {
        this.handleLogin({ userName , password }).then(res => {
          this.getUserInfo().then(res => {
            this.$on('on-success-valid', {
              userName: this.form.userName
            })
          })
        })
      },
      // 点击变更按钮状态
      change () {
        // this.modal_loading = true
        setTimeout(() => {
          // this.modal_loading = false
          this.modal1 = false
          this.$Message.success('更改用户成功')
        }, 2000)
      },
      jump () {

      },
      copy () {
        document.getElementById("danhao").select(); // 选择对象
        document.execCommand("Copy"); // 执行浏览器复制命令
        alert('复制成功')
      }
    }
  }
</script>

<style lang="less">

</style>
