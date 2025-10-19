```json
{
  "id": "2edc9c6ff797ae5b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289638,
  "host_pid": "9e6742732c60:1",
  "hash": "44894bc6b6074e2dc5ce078e61b03243986639ff447889a0e45fe1dafad572f4",
  "cid": "QmV144894bc6b6074e2dc5ce078e61b03243986639ff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289638,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760289638
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "726dd009bed8ac3d8934defd6fde3b94c095757b6dfe9862218fb178517bbce9"
}
```

Fraud detected: amount_anomaly (score: 89)
Transaction: 111000028341368
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 129, 'threshold': 50, 'total_amount': 1101979662, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 128, 'first_seen': 1760285763, 'matching_hash': 'b11d2debe374bbec'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.45, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 8542478}}}