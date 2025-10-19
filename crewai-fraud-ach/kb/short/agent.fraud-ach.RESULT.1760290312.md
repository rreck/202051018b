```json
{
  "id": "e8f7246be1264373",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290312,
  "host_pid": "9e6742732c60:1",
  "hash": "ecae2fc84ff8617cedbbd980540262a648e451700f7e3631b7173d327f11c042",
  "cid": "QmV1ecae2fc84ff8617cedbbd980540262a648e45170",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290312,
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
      "evaluated_at": 1760290312
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
  "sig": "401fbc1efd36d441300735eb9345bbc06b2a0c224b43da18601c1120d96bb00c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026876887
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 39227244, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285763, 'matching_hash': 'ac27634a0ee0b6ee'}}}