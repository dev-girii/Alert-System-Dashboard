
export default {
  namespaced: true,
  state: () => ({
    hosts: [
      { id: 1, name: 'Host A', ip: '192.168.1.2', status: 'online' },
      { id: 2, name: 'Host B', ip: '192.168.1.3', status: 'offline' },
      { id: 3, name: 'Host C', ip: '192.168.1.4', status: 'offline' },
      { id: 4, name: 'Host D', ip: '192.168.1.5', status: 'offline' },
      { id: 5, name: 'Host E', ip: '192.168.1.6', status: 'offline' }
    ],
    metrics: {
      cpu: '42%',
      memory: '65%',
      disk: '78%'
    }
  }),
  mutations: {},
  actions: {},
  getters: {}
};