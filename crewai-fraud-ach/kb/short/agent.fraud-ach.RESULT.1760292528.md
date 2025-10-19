```json
{
  "id": "97974fcb27f658ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292528,
  "host_pid": "9e6742732c60:1",
  "hash": "05570d03b86163d7ddd269f9f852b6dbab1b681f2538f52159794df723978c08",
  "cid": "QmV105570d03b86163d7ddd269f9f852b6dbab1b681f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292528,
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
      "evaluated_at": 1760292528
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
  "sig": "c62b6acb611f5591fd8f1a128d5008c24e2e99810b2a5c4555d4c6493a117789"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022243877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 49750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285765, 'matching_hash': '9c2417d6ee361cba'}}}