```json
{
  "id": "949d66855ed17209",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290382,
  "host_pid": "9e6742732c60:1",
  "hash": "54e82147ac27fe7ed0b35066667b95d3f55a4c434f038cb0c9865c8c4b410984",
  "cid": "QmV154e82147ac27fe7ed0b35066667b95d3f55a4c43",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290382,
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
      "evaluated_at": 1760290382
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
  "sig": "c531ed1335306b340340eef1f2f9d5a61bb60da3b24100ce27a8ab774bc15910"
}
```

Fraud detected: amount_anomaly (score: 92)
Transaction: 063100277197484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 1482160812, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285763, 'matching_hash': '4232e93b8d4c62d2'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 92, 'details': {'zscore': 5.25, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9947388}}}