```json
{
  "id": "0dc55e21effbfd6c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294870,
  "host_pid": "9e6742732c60:1",
  "hash": "ca4285b9d9d6409a8760493e1096424dd828193b52c820003f72f7af3d79ebc3",
  "cid": "QmV1ca4285b9d9d6409a8760493e1096424dd828193b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294870,
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
      "evaluated_at": 1760294870
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
  "sig": "f9da32cabf4b75c9c9bbad7bbd93c1ee3f2a3683ecb94bd263a5e38894c360e6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155818462
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 80641260, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': '4e45a5675434ecee'}}}