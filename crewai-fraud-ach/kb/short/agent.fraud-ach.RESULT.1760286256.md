```json
{
  "id": "e62316f3dccd8102",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286256,
  "host_pid": "9e6742732c60:1",
  "hash": "7fe442f09abb1c2d9304b37c31ec2e6827a3372340260e7879ed1de64758e355",
  "cid": "QmV17fe442f09abb1c2d9304b37c31ec2e6827a33723",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286256,
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
      "evaluated_at": 1760286256
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
  "sig": "f3e579ab1be8df179a22b6efcb6a79f5c675aa1cb4132b1ba9e089be6a704638"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000021513577
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285765, 'matching_hash': '2d9e7d16ad0b5ba4'}}}