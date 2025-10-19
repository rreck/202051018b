```json
{
  "id": "f83f605a10307add",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290937,
  "host_pid": "9e6742732c60:1",
  "hash": "664f682f3a40818a6456053bd0113dd919bb38c8a57c01c4761446ac20b55aef",
  "cid": "QmV1664f682f3a40818a6456053bd0113dd919bb38c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290937,
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
      "evaluated_at": 1760290937
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
  "sig": "55ea38c28ca79993ab46abf843cb162806e78826930eae9c326bc418f72f56b1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028364021
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': 'f023f2061dd68ffa'}}}een': 1760285763, 'matching_hash': '755a8d21dcb7f46a'}}}