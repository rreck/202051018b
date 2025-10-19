```json
{
  "id": "c248d6c7c1380acd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290051,
  "host_pid": "9e6742732c60:1",
  "hash": "57ec50338f6168cac57a0ae108225f343d8552bb047289cb28d4f652b22969c4",
  "cid": "QmV157ec50338f6168cac57a0ae108225f343d8552bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290051,
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
      "evaluated_at": 1760290051
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
  "sig": "d6455f52d781d50249ee4591aed167065a1511ab9b87babf551e67a4d0671875"
}
```

Fraud detected: amount_anomaly (score: 81)
Transaction: 111000021698868
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 1223215560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760284979, 'matching_hash': '4224f1af7034834c'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5663035}}}