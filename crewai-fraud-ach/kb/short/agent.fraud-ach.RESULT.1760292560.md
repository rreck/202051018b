```json
{
  "id": "f8c8987787a32345",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292560,
  "host_pid": "9e6742732c60:1",
  "hash": "a1e568aa9f3b921e1883588ee89326d81492150ebbb075405e4816389fc3b3a1",
  "cid": "QmV1a1e568aa9f3b921e1883588ee89326d81492150e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292560,
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
      "evaluated_at": 1760292560
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
  "sig": "f44f67e82ba36a4be118abff877c061931c6ab6c091f68cffe433a4053d58493"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460216158
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 276, 'threshold': 50, 'total_amount': 72880008, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 275, 'first_seen': 1760284979, 'matching_hash': 'd03ac62e4cd65436'}}}