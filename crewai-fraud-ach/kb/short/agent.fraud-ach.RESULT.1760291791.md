```json
{
  "id": "c1e21392efe95c33",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291791,
  "host_pid": "9e6742732c60:1",
  "hash": "66b6cab6b15f8b72a79c03c479140726cdf6bc22397ff40f5b50b6b432ec8a82",
  "cid": "QmV166b6cab6b15f8b72a79c03c479140726cdf6bc22",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291791,
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
      "evaluated_at": 1760291791
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
  "sig": "f74e1f02db58748af3e88e9c9a608499e03c3e748f4f6bb96b4fc6e5f59d8a1a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157479316
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 21427836, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285764, 'matching_hash': 'd3845a7ded8f78ea'}}}