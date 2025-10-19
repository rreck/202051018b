```json
{
  "id": "c7d7269f02efbc8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288625,
  "host_pid": "9e6742732c60:1",
  "hash": "aaeb2a0afabf3bdf083437408fa90000ee7a87495b8dd20e6a2b0b41425fddfd",
  "cid": "QmV1aaeb2a0afabf3bdf083437408fa90000ee7a8749",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288625,
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
      "evaluated_at": 1760288625
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
  "sig": "668af2b223409e896ea29e5368a25cbef205fa7e4ad4aec60ffc7634f96ae0c9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273021249
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 47742255, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285764, 'matching_hash': '8f9c0aaacb6951b9'}}}