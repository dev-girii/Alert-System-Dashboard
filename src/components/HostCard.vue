<template>
  <div class="host-card critical">
    <span class="status-label"></span>
    <!-- <div class="instanceName">
      TN Tenders
    </div> -->
    <div class="host-top">
      <div class="host-info">
        <div class="host-ip" title="192.168.1.20"><span>Instance:</span> {{ host.instance }}</div>
        <div class="host-name" title="app-server"><span>Host:</span> {{ host.host}}</div>
      </div>
      <div class="host-info">
        <div class="node-type">
          <span>Node: </span>{{host.role}}
        </div>
        <div class="host-uptime">
          <span>Uptime: </span>10d 2h
        </div>
      </div>
    </div>
    <div class="metrics">
      <div class="metric-box">
        <span class="metric-label">CPU</span>
        <span class="metric-value status-green">{{ host.used_percent }}</span>
      </div>
      <div class="metric-box">
        <span class="metric-label">Memory</span>
        <span class="metric-value status-green">3.3 GB / 8 GB</span>
      </div>
      <div class="metric-box">
        <span class="metric-label">Disk</span>
        <span class="metric-value status-green">50%</span>
      </div>
      <div class="metric-box">
        <span class="metric-label">Network RX/TX</span>
        <span class="metric-value">30 / 25 MB/s</span>
      </div>
    </div>
    <div class="details-link">
      <Router-link :to="`/view-details-${host.instance}`">
<a href="#"><i class="fas fa-search"></i> View Details</a>
      </Router-link> 
    </div>
  </div>
</template>

<script>
export default {
  props: ["host"],
  mounted(){
    console.log(this.host);
  }
};
</script>

<style scoped>
.host-card {
  background-color: #f0f2fa;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  padding: 18px 20px;
  display: flex;
  flex-direction: column;
  word-wrap: break-word;
  border: 3px solid transparent; /* default no border */
  transition: border-color 0.3s ease;
  border-top: 6px solid;
  position: relative;
}
/* Criticality borders */
.critical {
  border-color: #e74c3c; /* red */
}
.warning {
  border-color: #f39c12; /* orange */
}

/* Host top row: IP, hostname, uptime */
.host-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  flex-wrap: wrap;
  gap: 8px;
}

.host-info {
  display: flex;
  flex-direction: column;
  min-width: 0; /* allow text truncation */
}

.host-ip {
  font-size: 1em;
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 220px;
  color: #1e202a;
}

.host-name, .host-uptime, .node-type{
  font-size: 0.95em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  max-width: 220px;
  color: #1e202a;
  font-weight: 500;
}


/* .host-uptime {
  font-size: 0.85em;
  color: #1e202a;
  white-space: nowrap;
  flex-shrink: 0;
  font-weight: 500;
  min-width: 70px;
  text-align: right;
} */

.host-ip span, .host-name span, .host-uptime span, .node-type span{
    opacity: 0.75;
}

.metrics {
  display: flex;
  gap: 12px;
  margin-top: 10px;
  flex-wrap: wrap;
  justify-content: flex-start;
}

.metric-box {
  background-color: rgba(255, 255, 255, 0.05);
  border-radius: 6px;
  padding: 12px 15px;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-size: 0.95em;
  min-width: 90px;
  max-width: 150px;
  flex: 1 1 120px;
  box-sizing: border-box;
  white-space: normal;
  word-break: break-word;

  transition: background-color 0.3s ease, color 0.3s ease;
  background-color: #f9fafb;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.metric-label {
  color: #525252;
  font-weight: 700;
  margin-bottom: 5px;
  text-align: center;
}

.metric-value {
  font-weight: bold;
}

.status-green {
  color: #2ecc71;
}
.status-yellow {
  color: #f1c40f;
}
.status-red {
  color: #e74c3c;
}

.details-link {
  text-align: right;
  margin-top: 15px;
  white-space: nowrap;
}

.details-link a {
  color: #70c1b3;
  text-decoration: none;
  font-size: 0.9em;
}
/* 
.details-link a:hover {
  text-decoration: underline;
} */

/* Responsive tweaks */
@media (max-width: 480px) {
  .metrics {
    justify-content: center;
  }
  .metric-box {
    min-width: 80px;
    max-width: 120px;
    font-size: 0.9em;
    padding: 10px 12px;

    transition: background-color 0.3s ease, color 0.3s ease;
    background-color: #f9fafb;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
  }
  .host-ip {
    font-size: 1.1em;
    max-width: 140px;
  }
  .host-name {
    font-size: 0.85em;
    max-width: 140px;
  }
  .host-uptime {
    min-width: 60px;
    font-size: 0.8em;
  }
}

/* .status-label {
  font-size: 0.85em;
  font-weight: 600;
  margin-bottom: 10px;
  text-align: right;
  color: #e74c3c;
} */
.status-label {
    position: absolute;
    top: -12px;
    left: 16px;
    background-color: #fff;
    padding: 0 8px;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
}

.instanceName{
    display: flex;
    gap: 28px;    
    justify-content: center;
    font-weight: 700;
    font-size: 1.2rem;
    margin-bottom: 15px;
}
.host-card.critical .status-label::after {
  content: "ALERT";
  color: #e74c3c;
}

.host-card.warning .status-label::after {
  content: "WARNING";
  color: #f39c12;
}
/* 
.host-card {
  background-color: #ffffff;
  border: 2px solid transparent;
  transition: border-color 0.3s ease;
}

.host-card.critical {
  border-color: #e74c3c;
}

.host-card.warning {
  border-color: #f39c12;
} */
</style>
