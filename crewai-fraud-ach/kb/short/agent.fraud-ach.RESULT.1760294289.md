```json
{
  "id": "a4ecc1c6469f81e3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294289,
  "host_pid": "9e6742732c60:1",
  "hash": "2f764455c1ede6d5d765831f40f10cb874b82c7320c28fc51c6aee10d5aba6f8",
  "cid": "QmV12f764455c1ede6d5d765831f40f10cb874b82c73",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294289,
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
      "evaluated_at": 1760294289
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
  "sig": "5100c4c42ad050299d34754ae9a585a8fdbbde68e46c920952159d6f276a5322"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028666977
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 35130855, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '3b5947d2333162a8'}}}