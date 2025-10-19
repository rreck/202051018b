```json
{
  "id": "587ef138c5331ba2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288221,
  "host_pid": "9e6742732c60:1",
  "hash": "1b4b06c2c0cdce8139c829ef08372b2512c5537d6b3705c5a23026013156e053",
  "cid": "QmV11b4b06c2c0cdce8139c829ef08372b2512c5537d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288221,
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
      "evaluated_at": 1760288221
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
  "sig": "d4f5fd01fce1fa4b88f12286bfbe72118445f76922eb1e84f2e8dc6fc283c8a9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025375881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285765, 'matching_hash': '7f563b0766db4821'}}}