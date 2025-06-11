import { io } from "socket.io-client";

const socket = io("http://localhost:3000");

export default {
  namespaced: true,
  state: () => ({
    hosts: [],
    metrics: {
      cpu: '42%',
      memory: '65%',
      disk: '78%'
    }
  }),
  mutations: {
    updateHostData(state, newHostData) {
      const index = state.hosts.findIndex(
        host => host.host === newHostData.host && host.instance === newHostData.instance
      );

      if (index !== -1) {
        // Update existing host
        state.hosts.splice(index, 1, {
          ...state.hosts[index],
          ...newHostData
        });
      } else {
        // Add new host
        state.hosts.push(newHostData);
      }

      console.log("Updated Hosts:", state.hosts);
    }
  },
  actions: {
    initSocket({ commit }) {
      socket.on("system_metrics", (data) => {
        commit("updateHostData", data);
      });
    }
  },
  getters: {}
};