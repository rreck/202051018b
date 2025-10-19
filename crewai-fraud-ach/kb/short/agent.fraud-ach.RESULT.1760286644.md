```json
{
  "id": "58a549e74aff0200",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286644,
  "host_pid": "9e6742732c60:1",
  "hash": "9939e822515cb2dd6139b0003aaa7c6e5708d8655209e0df8be732e47f6b35a3",
  "cid": "QmV19939e822515cb2dd6139b0003aaa7c6e5708d865",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286644,
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
      "evaluated_at": 1760286644
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
  "sig": "c76fa0f5129c46689271646b42144d77570bdb76587a86b28c83da7ddce8efd4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000243277611
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285763, 'matching_hash': '2d64263c5765c58b'}}}