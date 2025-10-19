```json
{
  "id": "cf236c72fe669d9f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294352,
  "host_pid": "9e6742732c60:1",
  "hash": "3943b02430ac4b412d93c5f6b908367945f08c5e25b25c40a11a1e52f573e037",
  "cid": "QmV13943b02430ac4b412d93c5f6b908367945f08c5e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294352,
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
      "evaluated_at": 1760294352
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
  "sig": "cb5e654a7af88956bdaa7b99dc180f9b033b24949490dabf7816d1b4e6d89eaf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597908242
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 27014212, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': 'd5ac49343fc3272b'}}}