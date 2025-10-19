```json
{
  "id": "9c5ea22be606dff3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293422,
  "host_pid": "9e6742732c60:1",
  "hash": "3a09cd1ebd1040a890f27e5d03894abe42a67a64ea604b0fbe2a0c7cae05272b",
  "cid": "QmV13a09cd1ebd1040a890f27e5d03894abe42a67a64",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293422,
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
      "evaluated_at": 1760293422
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
  "sig": "5411432b22b4f4becd66b94b4c29b97638d4ec8e4494a9953149bf983cf2e7cd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037507630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 78642192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': '9b4ed9a2b11bf5fa'}}}