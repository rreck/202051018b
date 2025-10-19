```json
{
  "id": "3c1d3bc6bb743395",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286183,
  "host_pid": "9e6742732c60:1",
  "hash": "3c73fa05ccf89d897737136bc7ba40d3ee845ba2ffa08260430fe318400750e8",
  "cid": "QmV13c73fa05ccf89d897737136bc7ba40d3ee845ba2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286183,
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
      "evaluated_at": 1760286183
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
  "sig": "6c2da9ac8ac002642d29112a0b85229501f89502e568241ac68a960fc8350df5"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000036272460
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285763, 'matching_hash': '9a32e66a4f8079bf'}}}