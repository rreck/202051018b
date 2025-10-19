```json
{
  "id": "75eea08aec966fd9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289430,
  "host_pid": "9e6742732c60:1",
  "hash": "33c3eca136431efe8105769866b035f7433218e230271ec3168cd37c2d0c6657",
  "cid": "QmV133c3eca136431efe8105769866b035f7433218e2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289430,
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
      "evaluated_at": 1760289430
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
  "sig": "90a1a6511ff12fe568b2e6c5e7085bfe6095f83d01bf8ab65ea68356108cdf96"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240515775
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 29331441, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285763, 'matching_hash': 'c332d96fce6ec0fa'}}}