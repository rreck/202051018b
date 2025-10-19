```json
{
  "id": "99e9f14f21cf8cac",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291150,
  "host_pid": "9e6742732c60:1",
  "hash": "b976820afe3f804bcdb1039fbc2736806584eab658b8aa374cbd85f46f01979e",
  "cid": "QmV1b976820afe3f804bcdb1039fbc2736806584eab6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291150,
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
      "evaluated_at": 1760291150
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
  "sig": "7255e0896a8a3649bcf83adb3aa5e00cb66f2e3c2c1f998daaa1dddae8592a9b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036272460
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 56776440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285763, 'matching_hash': '9a32e66a4f8079bf'}}}