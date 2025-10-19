```json
{
  "id": "3e3ba67f10d07d24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292300,
  "host_pid": "9e6742732c60:1",
  "hash": "87d5e50358a29d172a98fec7fe16dabb3e602e43b67c904c5d068ded621e26af",
  "cid": "QmV187d5e50358a29d172a98fec7fe16dabb3e602e43",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292300,
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
      "evaluated_at": 1760292300
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
  "sig": "e91148a0ac0b11e3c5609aec295e766017fc605f1bf39f67c2c366aae65729d5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 61740112, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}