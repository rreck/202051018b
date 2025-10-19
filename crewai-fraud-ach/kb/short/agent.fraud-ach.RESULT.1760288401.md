```json
{
  "id": "d9c31fcf4666e6b5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288401,
  "host_pid": "9e6742732c60:1",
  "hash": "7720fb0964b3445ce7d566defcb3483a80385ae4ac12a017b0471a7bba343dfe",
  "cid": "QmV17720fb0964b3445ce7d566defcb3483a80385ae4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288401,
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
      "evaluated_at": 1760288401
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
  "sig": "83e06631f5a93451cf245d9b7d00d06d4629e66fe815e964fdf00552ba4eeeb5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248710981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 23609132, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285763, 'matching_hash': '9a1c8fb9d78dcf4a'}}}