<template>
	<section>
		<div class="diary-wrap">
			<div class="diary-header">
				<p>{{ diaryData.title }}</p>
				<img
					src="@/assets/images/menu.svg"
					class="diary-header__menu"
					alt="메뉴"
					@click="onOpenMenu"
				/>
				<ul class="diary-header__func">
					<li>
						<img
							src="@/assets/images/pencil.svg"
							alt="수정"
							@click="openThemeModal"
						/>
					</li>
					<li>
						<img
							src="@/assets/images/trash.svg"
							alt="삭제"
							@click="openMusicModal"
						/>
					</li>
				</ul>
			</div>
			<div class="diary-image">
				<img
					class="diary-image__value"
					src="@/assets/images/photos.svg"
					alt="일기사진"
				/>
			</div>
			<div class="diary-text">
				<p class="diary-text__content">{{ diaryData.content }}</p>
			</div>
		</div>
	</section>
</template>

<script>
import { fetchDiary } from '@/api/diary';
export default {
	data() {
		return {
			diaryData: null,
		};
	},
	props: {
		diaryId: Number,
	},
	methods: {
		onOpenMenu() {
			const menu = document.querySelector('.diary-header__menu');
			const menus = document.querySelector('.diary-header__func');
			menu.style.display = 'none';
			menus.style.right = '0px';
			menus.style.transition = '.5s';
		},
		async onfetchDiary() {
			try {
				const { data } = await fetchDiary(this.diaryId);
				this.diaryData = data;
				console.log(data);
			} catch (error) {
				// bus.$emit('show:warning', '정보를 불러오는데 실패했어요 :(');
				console.log(error.response);
			}
		},
	},
	created() {
		this.onfetchDiary();
	},
};
</script>

<style lang="scss">
.diary-wrap {
	display: flex;
	flex-direction: column;
	justify-content: center;
	.diary-header {
		width: 100%;
		display: flex;
		justify-content: space-between;
		margin: 10px 0;
		position: relative;
		overflow: hidden;
		.diary-header__menu {
			width: 18px;
		}
		.diary-header__func {
			display: flex;
			margin: 0;
			padding: 0;
			position: absolute;
			top: 0;
			right: -110px;
			list-style-type: none;
			li {
				img {
					width: 18px;
					margin: 0 6px;
				}
			}
		}
	}
	.diary-image {
		display: flex;
		justify-content: center;
		border-radius: 4px;
		background: rgba(151, 151, 151, 0.3);
		.diary-image__value {
			width: 100%;
		}
	}
	.diary-text {
		margin-top: 10px;
		.diary-text__content {
			width: 100%;
			padding: 5px 10px;
			line-height: 2;
			font-size: 15.5px;
			box-sizing: border-box;
			border: none;
			resize: none;
			background-attachment: local;
			background-image: linear-gradient(to right, white 10px, transparent 10px),
				linear-gradient(to left, white 10px, transparent 10px),
				repeating-linear-gradient(
					white,
					white 30px,
					#ccc 30px,
					#ccc 31px,
					white 31px
				);
		}
	}
}
</style>