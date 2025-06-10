<template>
  <!-- <aside class="sidebar"> -->
  <nav class="sidebar" aria-label="Primary navigation">
    <a href="#" data-tooltip="Linux" aria-label="Linux" style="margin-bottom: 16px;">
  <i class="fab fa-linux"></i>
</a>
<RouterLink to="/">
  <a href="#" data-tooltip="Dashboard" aria-label="Dashboard" class="active">
    <i class="fas fa-tachometer-alt"></i>
  </a>
</RouterLink>
<RouterLink to="/statistics">
  <a href="#" data-tooltip="Explore" aria-label="Explore">
    <i class="fas fa-chart-bar"></i>
  </a>
</RouterLink>
<RouterLink to='/notifications'>
  <a href="#" data-tooltip="Alerts" aria-label="Alerts">
    <i class="fas fa-bell"></i>
  </a>
</RouterLink>

<a href="#" data-tooltip="Settings" aria-label="Settings" style="margin-top: auto;">
  <i class="fas fa-cog"></i>
</a>

  </nav>
  <!-- </aside> -->
</template>

<style scoped>
.sidebar {
  background-color: #212121;
  width: 60px;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 15px 0;
  gap: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.5);
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
}

.sidebar a {
  color: #999999;
  font-size: 19px;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 36px;
  height: 36px;
  position: relative;
  cursor: pointer;
  text-decoration: none;
  border-radius: 6px;
  transition: background-color 0.2s ease, color 0.2s ease;
}

.sidebar a:hover, .router-link-active {
    color: #f0efff;
    background-color: #3e3d4a;
}

@media (max-width: 600px) {
.sidebar{
  display: none;
}
}
</style>
