```json
{
  "id": "b51adee2619933a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290988,
  "host_pid": "9e6742732c60:1",
  "hash": "78b712f5f86ed49c5e17b84a8eda83fa319408021912054e9b0753978f3155f5",
  "cid": "QmV178b712f5f86ed49c5e17b84a8eda83fa31940802",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290988,
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
      "evaluated_at": 1760290988
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "3d5abead9fc1f198ddda33a62321edc0e8f8f4570aa0b02db1430c501f5422f5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034789126
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 51374640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760284979, 'matching_hash': '5ec025bcbfaa0fd9'}}}maly': {'fraud_detected': True, 'risk_score': 92, 'details': {'zscore': 5.26, 'mean': 719745.9652321531, 'stdev': 1757577.609495364, 'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9966572}}}