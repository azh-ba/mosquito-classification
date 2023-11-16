<?php

class DBConnect {
    private $host   = '172.17.0.1'; # find localhost ip address on your machine --> linux: ifconfig (docker0) // windows: ipconfig
    private $dbName = 'mosq_imagesdb';
    private $user   = 'root';
    private $pass   = '12345';
    private $port   = 3307;
    public function connect() {
        try {
            $conn = new PDO('mysql:host=' . $this->host . '; port=' . $this->port . '; dbname=' . $this->dbName, $this->user, $this->pass);
            $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            return $conn;
        } catch (PDOException $e) {
            echo 'Database Error: ' . $e->getMessage();
        }
    }
}

?>