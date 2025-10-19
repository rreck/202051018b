```json
{
  "id": "5f9a587e9d01228e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290386,
  "host_pid": "9e6742732c60:1",
  "hash": "5f5a0d10c4cd0e4e9f6626591f3b63c09e3642389523e06ac72bb3c64e04894f",
  "cid": "QmV15f5a0d10c4cd0e4e9f6626591f3b63c09e364238",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290386,
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
      "evaluated_at": 1760290386
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
  "sig": "5332c827e095f00ec951814661c713d2718c6b458358db9bebd8ac549dcd8d5b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465723283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50, 'total_amount': 63703311, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285764, 'matching_hash': 'e1350af409930159'}}}