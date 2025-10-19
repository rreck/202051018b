```json
{
  "id": "7e8b35761e118d10",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289203,
  "host_pid": "9e6742732c60:1",
  "hash": "5060dea87680f3a2bafc6aa514929d8eecb72695f2a9c123c4b8e5f303b98384",
  "cid": "QmV15060dea87680f3a2bafc6aa514929d8eecb72695",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289203,
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
      "evaluated_at": 1760289203
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
  "sig": "a462edd3e0c2a626410265517d1e1e98825904738a815964b4aee26bdb084e9e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150658717
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 38793648, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285765, 'matching_hash': 'c0bd022b5af03ee8'}}}