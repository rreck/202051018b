```json
{
  "id": "cc8a2d39790001a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291523,
  "host_pid": "9e6742732c60:1",
  "hash": "976e8c9fc47e97cc57e5531dcd7a9cdcb7d42a5a6433966cbd175411abcf2c20",
  "cid": "QmV1976e8c9fc47e97cc57e5531dcd7a9cdcb7d42a5a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291523,
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
      "evaluated_at": 1760291523
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
  "sig": "eeeb76947beb1b310f95360ad5a129a68eba3a909a1495a3292443fb67007120"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592795708
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 81358227, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': '6f9672c314113419'}}}