```json
{
  "id": "a6e10933d23bfd9e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294252,
  "host_pid": "9e6742732c60:1",
  "hash": "24d28bb614cd409dd3ba36316a37c085429795b2f11e58dcf04e6369ebe9ca6b",
  "cid": "QmV124d28bb614cd409dd3ba36316a37c085429795b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294252,
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
      "evaluated_at": 1760294252
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
  "sig": "d2ccdb475957d93997d61e67e1d954777466869ff4ad590f2ebe6fd5a8544f85"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029832912
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 107356626, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285765, 'matching_hash': 'ede6214022caf300'}}}