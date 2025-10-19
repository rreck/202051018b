```json
{
  "id": "e2131036418346f0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292609,
  "host_pid": "9e6742732c60:1",
  "hash": "48c3322e238cbcff2ab9db4d0ba7a5a9a09421ec786623f7a7bb605b41fd2c63",
  "cid": "QmV148c3322e238cbcff2ab9db4d0ba7a5a9a09421ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292609,
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
      "evaluated_at": 1760292610
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
  "sig": "193dd8f4b56acad856a6c27d2b826377780f5855348660977a9a42ce487c1ef8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154887163
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 277, 'threshold': 50, 'total_amount': 97448323, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 276, 'first_seen': 1760284979, 'matching_hash': '445784114b53d57b'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '906924178', 'validation_error': 'Invalid routing number checksum'}}}