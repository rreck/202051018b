```json
{
  "id": "e99201d19cfaa2f5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287410,
  "host_pid": "9e6742732c60:1",
  "hash": "46f2c530d77aa5a81a960a8aa1e53551b5c3fca5fda86c20c6b4a659ac4aab28",
  "cid": "QmV146f2c530d77aa5a81a960a8aa1e53551b5c3fca5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287410,
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
      "evaluated_at": 1760287410
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
  "sig": "8e89c4f4b218bfe83d2e14f32d5ca5425fb037cf7f893988013231c609962d9e"
}
```

Fraud detected: duplicate_transaction (score: 76)
Transaction: 021000021533630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 68, 'details': {'transaction_count': 59, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285765, 'matching_hash': 'e04be99e47eedc93'}}}een': 1760285763, 'matching_hash': '01e7bf5fcf2bbeec'}}}57b'}}}