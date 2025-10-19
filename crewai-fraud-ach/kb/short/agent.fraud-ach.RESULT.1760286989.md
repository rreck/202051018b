```json
{
  "id": "2a503343a97ce0e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286989,
  "host_pid": "9e6742732c60:1",
  "hash": "b48ad219b0cb4f4d4811210e1d0ee51475c70ca5ed27b689bdc390a12fe433d7",
  "cid": "QmV1b48ad219b0cb4f4d4811210e1d0ee51475c70ca5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286989,
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
      "evaluated_at": 1760286989
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
  "sig": "20820cdf9feeb91046edd43e9a96b17694965605af2e713b2bc0b0838ceb1ee7"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156494107
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 21959388, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285764, 'matching_hash': 'c1327b457e76afdd'}}}