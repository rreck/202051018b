```json
{
  "id": "a4a0ee7e7a36c97b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292682,
  "host_pid": "9e6742732c60:1",
  "hash": "09a8ca96d927e26d4145a1a18569cca184c44dc5192d504b6b9951858266812d",
  "cid": "QmV109a8ca96d927e26d4145a1a18569cca184c44dc5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292682,
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
      "evaluated_at": 1760292682
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
  "sig": "114f494bb56c1ff573ac62c2d73db2bdf2705dce3f64fd5bec690217be49d89e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274159227
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 25461072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': 'c6403d45da933f2b'}}}