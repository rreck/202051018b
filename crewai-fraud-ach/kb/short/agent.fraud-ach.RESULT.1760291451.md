```json
{
  "id": "2ee7ff18ea8d694d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291451,
  "host_pid": "9e6742732c60:1",
  "hash": "630b54fa81d178803daa991dcb540220407c44c9fdfd8062405643935c289787",
  "cid": "QmV1630b54fa81d178803daa991dcb540220407c44c9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291451,
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
      "evaluated_at": 1760291451
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
  "sig": "9f62f39ed210b68d1c52700f4cc528258b1500788a19a95176f9f717d7e5f8c8"
}
```

Fraud detected: amount_anomaly (score: 88)
Transaction: 111000024639540
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 1342607350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285765, 'matching_hash': '9eefc6a12f8b62a3'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 79, 'details': {'zscore': 3.96, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 7672042}}}