```json
{
  "id": "45e947bc68f52aae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288930,
  "host_pid": "9e6742732c60:1",
  "hash": "aef9dec5d790af9fba0cbd0c8e77cdb57da72004ad810705edff70d79f049376",
  "cid": "QmV1aef9dec5d790af9fba0cbd0c8e77cdb57da72004",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288930,
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
      "evaluated_at": 1760288930
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
  "sig": "731079d965cc31d4f2c9cd5c4a9a9b6aed3223e8567f34c76083658152611e11"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151422831
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 11040948, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285764, 'matching_hash': 'e9fc645b92693d6a'}}}