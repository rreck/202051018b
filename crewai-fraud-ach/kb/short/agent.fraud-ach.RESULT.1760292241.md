```json
{
  "id": "203da3f7eb97d907",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292241,
  "host_pid": "9e6742732c60:1",
  "hash": "fcaf86e85ea1474c12c8417b0f0fa7c1379a5ef90d6752038c9b9ca0c7e62d72",
  "cid": "QmV1fcaf86e85ea1474c12c8417b0f0fa7c1379a5ef9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292241,
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
      "evaluated_at": 1760292241
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
  "sig": "1d2d0947dce99523364b1ea3872e120d1faa2c57817c4987a99383c304aa20d8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155376461
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 58071963, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285765, 'matching_hash': 'ed3a1cd9da35e724'}}}