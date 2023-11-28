-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql
-- Generation Time: Nov 28, 2023 at 03:32 PM
-- Server version: 8.2.0
-- PHP Version: 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ProjecPython`
--

-- --------------------------------------------------------

--
-- Table structure for table `User_In_Proxy`
--

CREATE TABLE `User_In_Proxy` (
  `id` int NOT NULL,
  `pretty_host` text CHARACTER SET utf8mb4 COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `method` text CHARACTER SET utf8mb4 COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `address` text CHARACTER SET utf8mb4 COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `http_version` text CHARACTER SET utf8mb4 COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `status_code` text CHARACTER SET utf8mb4 COLLATE utf8mb4_vietnamese_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;

--
-- Dumping data for table `User_In_Proxy`
--

INSERT INTO `User_In_Proxy` (`id`, `pretty_host`, `method`, `url`, `address`, `http_version`, `status_code`) VALUES
(905, 'push.services.mozilla.com', 'GET', 'https://push.services.mozilla.com/', '192.168.56.1', 'HTTP/1.1', '101'),
(906, 'contile.services.mozilla.com', 'GET', 'https://contile.services.mozilla.com/v1/tiles', '192.168.56.1', 'HTTP/2.0', '204'),
(907, 'www.facebook.com', 'GET', 'https://www.facebook.com/', '192.168.56.1', 'HTTP/2.0', '200'),
(908, 'firefox.settings.services.mozilla.com', 'GET', 'https://firefox.settings.services.mozilla.com/v1/buckets/main/collections/ms-language-packs/records/cfr-v1-en-US', '192.168.56.1', 'HTTP/2.0', '304'),
(909, 'www.facebook.com', 'POST', 'https://www.facebook.com/ajax/bz?__a=1&__ccg=MODERATE&__dyn=7xe6E5aQ1PyUbFuC1swgE98nwgU29zEdEc8uwdK0lW4o3Bw5VCwjE3awbG78b87C0yE7i0n24o5-0me2218w5uw5Uwdq0Ho2eU5O0PU1AE17U2ZwrU19E36w&__hs=19687.BP%3ADEFAULT.2.0..0.0&__hsi=7305781144667570875&__req=c&__rev=1010034075&__s=qw84t9%3A8bw3yv%3Ai3ztcb&__spin_b=trunk&__spin_r=1010034075&__spin_t=1701009726&__user=0&dpr=1&jazoest=2835&lsd=AVqRDaOBAB0', '192.168.56.1', 'HTTP/2.0', '200'),
(910, 'facebook.com', 'GET', 'https://facebook.com/security/hsts-pixel.gif', '192.168.56.1', 'HTTP/2.0', '200'),
(911, 'safebrowsing.googleapis.com', 'GET', 'https://safebrowsing.googleapis.com/v4/fullHashes:find?$ct=application/x-protobuf&key=AIzaSyD3uzXks34szqk9WhKoFZypVPgdDbT3uPw&$httpMethod=POST&$req=ChUKE25hdmNsaWVudC1hdXRvLWZmb3gSGwoNCAUQBhgBIgMwMDEwARDu9hMaAhgKrvBe3houCAUQAhoGCgTjUssAGgYKBDjVGPUaBgoEjVo0VRoGCgTBQiNNGgYKBM46gv0gAQ==', '192.168.56.1', 'HTTP/2.0', '200'),
(912, 'www.exploit-db.com', 'GET', 'https://www.exploit-db.com/ghdb/8355', '192.168.56.1', 'HTTP/2.0', '200'),
(913, 'consent.cookiebot.com', 'GET', 'https://consent.cookiebot.com/uc.js', '192.168.56.1', 'HTTP/2.0', '304'),
(914, 'www.facebook.com', 'POST', 'https://www.facebook.com/ajax/bz?__a=1&__ccg=MODERATE&__dyn=7xe6E5aQ1PyUbFuC1swgE98nwgU29zEdEc8uwdK0lW4o3Bw5VCwjE3awbG78b87C0yE7i0n24o5-0me2218w5uw5Uwdq0Ho2eU5O0PU1AE17U2ZwrU19E36w&__hs=19687.BP%3ADEFAULT.2.0..0.0&__hsi=7305791679030680964&__req=1&__rev=1010034075&__s=qw84t9%3A8bw3yv%3Ap535j2&__spin_b=trunk&__spin_r=1010034075&__spin_t=1701012179&__user=0&dpr=1&jazoest=2860&lsd=AVqRDaOB0l0', '192.168.56.1', 'HTTP/2.0', '200'),
(915, 'www.google-analytics.com', 'GET', 'https://www.google-analytics.com/analytics.js', '192.168.56.1', 'HTTP/2.0', '304'),
(916, 'www.google-analytics.com', 'POST', 'https://www.google-analytics.com/j/collect?v=1&_v=j101&a=707922286&t=pageview&_s=1&dl=https%3A%2F%2Fwww.exploit-db.com%2Fghdb%2F8355&ul=en-us&de=UTF-8&dt=site%3A*.edu.*%20intitle%3A%22index%20of%22%20*.ics%20-%20Files%20Containing%20Juicy%20Info%20GHDB%20Google%20Dork&sd=24-bit&sr=1920x1080&vp=1920x929&je=0&_u=AACAAAABAAAAACAAI~&jid=1943126266&gjid=471371726&cid=835176682.1700569844&tid=UA-1981501-4&_gid=1031828525.1701008173&_r=1&_slc=1&z=1075462337', '192.168.56.1', 'HTTP/2.0', '200'),
(917, 'stats.g.doubleclick.net', 'POST', 'https://stats.g.doubleclick.net/j/collect?t=dc&aip=1&_r=3&v=1&_v=j101&tid=UA-1981501-4&cid=835176682.1700569844&jid=1943126266&gjid=471371726&_gid=1031828525.1701008173&_u=AACAAAAAAAAAACAAI~&z=629665814', '192.168.56.1', 'HTTP/2.0', '200'),
(918, 'www.googletagmanager.com', 'GET', 'https://www.googletagmanager.com/gtag/js?id=G-N0K6XSDCRJ&cx=c&_slc=1', '192.168.56.1', 'HTTP/2.0', '200'),
(919, 'analytics.google.com', 'POST', 'https://analytics.google.com/g/collect?v=2&tid=G-N0K6XSDCRJ&gtm=45je3b81v9135346505&_p=1701012184149&_gaz=1&gcs=G111&gcd=11n1n1l1l6&dma=0&gdid=dMWZhNz&ul=en-us&sr=1920x1080&cid=835176682.1700569844&_eu=ABAI&_s=1&dl=https%3A%2F%2Fwww.exploit-db.com%2Fghdb%2F8355&dt=site%3A*.edu.*%20intitle%3A%22index%20of%22%20*.ics%20-%20Files%20Containing%20Juicy%20Info%20GHDB%20Google%20Dork&sid=1701008175&sct=6&seg=1&en=page_view&_ee=1&tfd=4994', '192.168.56.1', 'HTTP/2.0', '204'),
(920, 'www.google.com.vn', 'GET', 'https://www.google.com.vn/ads/ga-audiences?v=1&t=sr&slf_rd=1&_r=4&tid=G-N0K6XSDCRJ&cid=835176682.1700569844&gtm=45je3b81v9135346505&aip=1&dma=0&gcs=G111&gcd=11n1n1l1l6&z=835014522', '192.168.56.1', 'HTTP/2.0', '200'),
(921, 'www.google.com.vn', 'GET', 'https://www.google.com.vn/ads/ga-audiences?t=sr&aip=1&_r=4&slf_rd=1&v=1&_v=j101&tid=UA-1981501-4&cid=835176682.1700569844&jid=1943126266&_u=AACAAAAAAAAAACAAI~&z=1387608292', '192.168.56.1', 'HTTP/2.0', '200'),
(922, 'www.google.com', 'GET', 'https://www.google.com/ads/ga-audiences?t=sr&aip=1&_r=4&slf_rd=1&v=1&_v=j101&tid=UA-1981501-4&cid=835176682.1700569844&jid=1943126266&_u=AACAAAAAAAAAACAAI~&z=1387608292', '192.168.56.1', 'HTTP/2.0', '200'),
(923, 'www.facebook.com', 'POST', 'https://www.facebook.com/ajax/webstorage/process_keys/?state=1', '192.168.56.1', 'HTTP/2.0', '200'),
(924, 'www.facebook.com', 'POST', 'https://www.facebook.com/ajax/bz?__a=1&__ccg=MODERATE&__dyn=7xe6E5aQ1PyUbFuC1swgE98nwgU29zEdEc8uwdK0lW4o3Bw5VCwjE3awbG78b87C0yE7i0n24o5-0me2218w5uw5Uwdq0Ho2eU5O0PU1AE17U2ZwrU19E36w&__hs=19687.BP%3ADEFAULT.2.0..0.0&__hsi=7305791679030680964&__req=3&__rev=1010034075&__s=qw84t9%3A8bw3yv%3Ap535j2&__spin_b=trunk&__spin_r=1010034075&__spin_t=1701012179&__user=0&dpr=1&jazoest=2860&lsd=AVqRDaOB0l0', '192.168.56.1', 'HTTP/2.0', '200');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `User_In_Proxy`
--
ALTER TABLE `User_In_Proxy`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `User_In_Proxy`
--
ALTER TABLE `User_In_Proxy`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=925;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
