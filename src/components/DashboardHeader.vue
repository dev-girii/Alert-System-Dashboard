<template>
  <header class="dashboard-header">
    <div>
        <div class="headerTitle">
            <h1>Linux Hosts Dashboard</h1>
        </div>
        <!-- <div class="lastUpdated">
            <i class="fas fa-clock"></i><span>&nbsp;</span>
            Last Updated: <span id="time">&nbsp;12:45 PM</span> 
        </div> -->
    </div>
  </header>
</template>

<style scoped>
.dashboard-header {
  color: #2c3e50;
  padding: 1.3rem 1rem 1rem 1rem;
  border-bottom: 1px solid;
}
.dashboard-header div{
    display: flex;
    justify-content: center;
    align-items: center;
}
.headerTitle{
    font-size: 0.75rem;
}

@media (max-width: 600px) {
  .headerTitle{
    margin: 0 auto;
  }
.lastUpdated{
  display: none !important;
}
}
</style>
