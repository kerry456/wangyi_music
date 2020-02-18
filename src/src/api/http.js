// /*引入axios*/
import axios from 'axios';
import {
	Message,
	MessageBox
} from 'element-ui' // element库的消息提示，可以不用
// import router from '../router'
// 创建axios实例
const CancelToken = axios.CancelToken;
const source = CancelToken.source();
var service = axios.create({
	baseURL: '/beaas',
	headers: {
		'content-type': 'multipart/form-data',
		'data-type': 'json'
	}
});
export default {
// 验证码
getvercode(params) {
  return this.post('/api/login/',params);
},
// /*弹框*/
messageFun(type, message) {
  return Message({
    showClose: true,
    message: message,
    type: type,
    duration: 2000
  })
},
// get请求，其他类型请求复制粘贴，修改method
get(url, param) {
  return new Promise((cback, reject) => {
    service({
      method: "get",
      url,
      params: param,
      cancelToken: source.token
    }).then(res => {
      // axios返回的是一个promise对象
      var res_code = res.status.toString();
      if(res_code.charAt(0) == 2) {
        cback(res) // cback在promise执行器内部
      }
    }).catch(err => {
      if(axios.isCancel(err)) {

      } else {

      }
    });
  });
},
post(url, data) {
  return new Promise((cback, reject) => {
    service({
      method: "post",
      url,
      data,
      cancelToken: source.token
    }).then(res => {
      //axios返回的是一个promise对象
      var res_code = res.status.toString();
      if(res_code.charAt(0) == 2) {
        cback(res); //cback在promise执行器内部
      }
    }).catch(err => {
      if(axios.isCancel(err)) {

      } else {

      }
    });
  });
}
};
