```json
{
  "id": "abc1401238daa7be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288728,
  "host_pid": "9e6742732c60:1",
  "hash": "170eea8c839bd5403615a6055242c8bd6cb0f488998b61b2a82e0319db6c89f8",
  "cid": "QmV1170eea8c839bd5403615a6055242c8bd6cb0f488",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288728,
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
      "evaluated_at": 1760288728
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
  "sig": "1080a48c65d7a653b027530f816328017fc5c12a9e14f6c1564136eb41461a8d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240116635
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 38740926, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285763, 'matching_hash': 'faa8e9f78afe3726'}}}