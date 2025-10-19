```json
{
  "id": "a67fad2015e841c8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292875,
  "host_pid": "9e6742732c60:1",
  "hash": "47f9809e5646fd92a49b72cd3571188245cdc9c2d91ea0b065d33c2e0683b807",
  "cid": "QmV147f9809e5646fd92a49b72cd3571188245cdc9c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292875,
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
      "evaluated_at": 1760292875
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
  "sig": "5bedfe86b4377ec1912b1184db3332b2a0da70edc0df4a50266d99aa19095585"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466882033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 62013474, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': '7e4548b1f8f2bba3'}}}