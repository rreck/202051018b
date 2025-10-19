```json
{
  "id": "7ef6e10d2bd7276d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292635,
  "host_pid": "9e6742732c60:1",
  "hash": "a0e60067e1a7c4b67ec9139b5ae852801d92c2aff674577a362e346705d15fc2",
  "cid": "QmV1a0e60067e1a7c4b67ec9139b5ae852801d92c2af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292635,
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
      "evaluated_at": 1760292635
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
  "sig": "f44f8d8273fac764bf901a7ecfafcc444c4c1fa488dcccf45f838e5b97382970"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038823890
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 42206082, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': '81df70e06ca09887'}}}