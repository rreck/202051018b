```json
{
  "id": "278d29d60f2b771c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286844,
  "host_pid": "9e6742732c60:1",
  "hash": "1f768b2cc1a6985b50f8f37e84892829e793d62b278b0b51282343e1e6b05340",
  "cid": "QmV11f768b2cc1a6985b50f8f37e84892829e793d62b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286844,
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
      "evaluated_at": 1760286844
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "814b5385f35d4ea8021df9d8f14ee03725ec6c0fe57264a23ac2564ed63d36e1"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105155322765
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16761693, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285763, 'matching_hash': '7a27d1bb592c5069'}}}