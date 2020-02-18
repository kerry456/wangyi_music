<template>
  <div style="background: #fff;margin:1rem 1rem;padding:1rem;height:37rem">
    <Tabs :animated="false">
      <Tab-pane label="基础信息">
        <Row style="margin-top: 3rem">
          <Col span="12" class="top_head">
            <div class="img-head">
              <img src="../../assets/img/20160821194924_UCvFZ.png">
            </div>
            <p>银监会</p>
            <p>dfghsjkn(组织机构代码密文)</p>
            <p>北京市海淀区西二旗辉煌国际39号</p>
          </Col>
          <Col span="12" style="font-size: 10px;color:#666666">
            <p style="margin-bottom:1.5rem;margin-top: 2rem">企业名称:<span>银监会</span></p>
            <p style="margin-bottom:1.5rem">法人代表:<span>王富贵</span></p>
            <p style="margin-bottom:1.5rem">法人证件类型:<span>身份证</span></p>
            <p style="margin-bottom:1.5rem">有效时间:<span>2018.11.11~2019.11.11</span></p>
          </Col>
        </Row>
      </Tab-pane>
      <Tab-pane label="修改信息">
        <div class="bottom_head">
          <p><Row><Col span="4">用户名:</Col><Col span="10"><span>银监会</span></Col></Row></p>
          <p><Row><Col span="4">旧密码:</Col><Col span="10"><Input v-model="value1" placeholder="请输入"></Input></Col></Row></p>
          <p><Row><Col span="4">新密码:</Col><Col span="10"><Input v-model="value2" placeholder="请输入"></Input></Col></Row></p>
          <p><Row><Col span="4">运营联系方式:</Col><Col span="16">
            <Input v-model="value3" placeholder="请输入" style="width:17%"></Input>
            <span >——</span>
            <Input v-model="value4" placeholder="请输入" style="width:38%"></Input>
          </Col></Row></p>
        </div>
        <p style="text-align: center;margin-top: 5rem"><Button type="primary">确定</Button></p>
      </Tab-pane>
    </Tabs>
  </div>
</template>

<script>
  export default {
    name: 'index',
    data () {
      return {
        // 旧密码
        value1: '',
        //  新密码
        value2: '',
        //  运营联系方式1
        value3: '',
        //  运营联系方式2
        value4: ''
      }
    }
  }
</script>

<style lang="less">
  @import './index.less';
</style>
