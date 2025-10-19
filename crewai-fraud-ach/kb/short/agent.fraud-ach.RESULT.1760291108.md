```json
{
  "id": "0af9b9c3e2a85dde",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291108,
  "host_pid": "9e6742732c60:1",
  "hash": "bc34bcdc3de7819aac380f407222fedb347220c5365fbbb5192fd209799763e3",
  "cid": "QmV1bc34bcdc3de7819aac380f407222fedb347220c5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291108,
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
      "evaluated_at": 1760291108
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
  "sig": "20219ef7d53ed3bee1e27af89b2d2e1cb360ad9ed34ddb502413255767cc89e3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248887344
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285764, 'matching_hash': '5acb0608ecf9576e'}}}een': 1760285763, 'matching_hash': '7b1e6accdb666d6e'}}}