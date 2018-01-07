<template>
	 <div>
	{{ message }}

	<nav class="navbar navbar-expand-lg navbar-light bg-light">
		<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
			<span class="navbar-toggler-icon"></span>
		</button>
		<div class="collapse navbar-collapse" id="navbarNav">
			<ul class="navbar-nav">
				<li class="nav-item active">
					<a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
				</li>
				<li class="nav-item">
					<a class="nav-link" href="#">Features</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" href="#">Pricing</a>
				</li>
				<li class="nav-item">
					<a class="nav-link disabled" href="#">Disabled</a>
				</li>
			</ul>
		</div>
	</nav>

	<table class="table table-striped table-hover">
		<thead class="thead-light">
			<tr>
				<th scope="col">#</th>
				<th scope="col">name</th>
				<th scope="col">price</th>
				<th scope="col">volume</th>
				<th scope="col">1h</th>
				<th scope="col">24h</th>
				<th scope="col">7d</th>
			</tr>
		</thead>
		<tbody>
			<tr v-for="ticker in tickers">
				<td>{{ticker.rank}}</td>
				<td>{{ticker.name}} ({{ticker.symbol}})</td>
				<td>{{ticker.price_usd}}$</td>
				<td>{{ticker["24h_volume_usd"]}}$</td>
				<td>{{ticker.percent_change_1h}}</td>
				<td>{{ticker.percent_change_24h}}</td>
				<td>{{ticker.percent_change_7d}}</td>
			</tr>
		</tbody>
	</table>
</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Market',
  data () {
    return {
      message: 'Hello from app vue',
      tickers: [],
      errors: []
    }
  },
  created () {
    axios.get('http://localhost:8888/api/tickers', { crossdomain: true })
    .then(response => {
      this.tickers = response.data
    })
    .catch(e => {
      console.log(e)
      this.errors = e
    })
  }
}
</script>