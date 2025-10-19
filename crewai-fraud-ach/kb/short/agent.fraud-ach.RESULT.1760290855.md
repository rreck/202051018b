```json
{
  "id": "daf5787c52491f8c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290855,
  "host_pid": "9e6742732c60:1",
  "hash": "1c0b44b3283d95602f547ecd10384c332cd1fe1f56d26c28a40a9f447b36dc0f",
  "cid": "QmV11c0b44b3283d95602f547ecd10384c332cd1fe1f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290855,
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
      "evaluated_at": 1760290855
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
  "sig": "07f0f953aac41912854946284c83688369e44fc77f3ffae1685a2af44eb3303a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038197650
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 30278787, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285763, 'matching_hash': '1b9150809eb731a5'}}}