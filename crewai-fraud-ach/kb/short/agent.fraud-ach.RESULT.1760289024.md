```json
{
  "id": "9d8d915cbad6aede",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289024,
  "host_pid": "9e6742732c60:1",
  "hash": "40cbfe02d4dd42cb70a1b86566a2ad9005fd801e3c4d4a5a7962b409ab73e192",
  "cid": "QmV140cbfe02d4dd42cb70a1b86566a2ad9005fd801e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289024,
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
      "evaluated_at": 1760289024
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
  "sig": "eb682ac15fc3bcad92c48d1cdc7e344e369815e3d74e0bf1760d0e0104091d40"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596885140
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 36578052, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285763, 'matching_hash': '3e2459e11de91d22'}}}