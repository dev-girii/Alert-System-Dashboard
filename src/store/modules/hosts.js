import { io } from "socket.io-client";

const socket = io("http://localhost:3000");

export default {
  namespaced: true,
  state: () => ({
    hosts: {},
    metrics: {
      cpu: '42%',
      memory: '65%',
      disk: '78%'
    }
  }),
  mutations: {
    updateHostData(state, data) {
      state.hosts = { ...state.hosts, ...data };
      console.log(state.hosts); // Overwrite hosts with the incoming data
    },
  },
  actions: {
      initSocket({ commit, state }) {
      socket.on("cpu_data", (cpuData) => {
        commit("updateHostData", { ...state.hosts, cpu: cpuData });
      });

      socket.on("disk_data", (diskData) => {
        commit("updateHostData", { ...state.hosts, disk: diskData });
      });

      socket.on("mem_data", (memData) => {
        commit("updateHostData", { ...state.hosts, memory: memData });
      });
    },
  },
  getters: {}
};