```json
{
  "id": "9ce6ee89325fce27",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290151,
  "host_pid": "9e6742732c60:1",
  "hash": "0e8c6b4535a610c6e1c43e07ca821424215a74ad12536c569788a0eb2655e1ed",
  "cid": "QmV10e8c6b4535a610c6e1c43e07ca821424215a74ad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290151,
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
      "evaluated_at": 1760290151
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
  "sig": "56679e41b68ac4d16d6defe00eae6b1fa068e41bbb38144a2c1d49520a6fe8b1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592077072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 33446127, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': '86add4fc1587ca1b'}}}