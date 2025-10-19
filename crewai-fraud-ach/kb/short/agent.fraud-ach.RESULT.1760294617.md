```json
{
  "id": "3ccc1cb751e184db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294617,
  "host_pid": "9e6742732c60:1",
  "hash": "0191c083e65aa684e0fc590700fd3b5d034d44ef6d3a9a5168ffa1f131eb12f3",
  "cid": "QmV10191c083e65aa684e0fc590700fd3b5d034d44ef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294617,
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
      "evaluated_at": 1760294617
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
  "sig": "31dd401c530c6c8cc3b0b778a3b2473dafc581a2f309d3031f48cfaa35c7084c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037578651
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 19496177, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': '25cb229761d99325'}}}