```json
{
  "id": "8528684d42183778",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289553,
  "host_pid": "9e6742732c60:1",
  "hash": "a6ea63664d6d6fb29f5fd48d10b1a967cc8ab1776cd957e890f203753fa236d4",
  "cid": "QmV1a6ea63664d6d6fb29f5fd48d10b1a967cc8ab177",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289553,
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
      "evaluated_at": 1760289553
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
  "sig": "2cf7aee41e1b1e3ce40dec8155711a15f6a6a0ba07c1a939d4156af2c19fff41"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022243877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 31500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285765, 'matching_hash': '9c2417d6ee361cba'}}}