```json
{
  "id": "48b49a22990b9b98",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288202,
  "host_pid": "9e6742732c60:1",
  "hash": "67a392baaea925589c47fb43420cbaa5c05b298efc427afdc18b1765910d8402",
  "cid": "QmV167a392baaea925589c47fb43420cbaa5c05b298e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288202,
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
      "evaluated_at": 1760288202
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
  "sig": "b032d54dad76cd2f6085cc94b38d98a1b74bceb275ceb1233b98254c995ff9fe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242331672
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285763, 'matching_hash': '532e279550beef55'}}}een': 1760285763, 'matching_hash': '5f413645b746a025'}}}