```json
{
  "id": "61e8f1190953c64b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294170,
  "host_pid": "9e6742732c60:1",
  "hash": "0699f8cc5a0262bb8e29637c0266d0a52016c9d8029fa05baabfc19c5ade0d67",
  "cid": "QmV10699f8cc5a0262bb8e29637c0266d0a52016c9d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294170,
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
      "evaluated_at": 1760294171
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
  "sig": "ed33d15e0e81c432d693f0a55a7ab46673a987ac4323a9190d77f3706c832446"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029379143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 113408090, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285763, 'matching_hash': '781972e95177ec49'}}}