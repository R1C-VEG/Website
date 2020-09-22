<?php 
    class eAsistentClient {
        function getFutureEvaluations() {
            $result = shell_exec("python Python-Scripts/getFutureEvaluations.py");
            $resultData = json_decode($result, true);
            return $resultData;
        }

        function getTodaySchedule() {
            $result = shell_exec("python Python-Scripts/getTodaySchedule.py");
            $resultData = json_decode($result, true);
            return $resultData;
        }
    }

    $eAC = new eAsistentClient;
?>