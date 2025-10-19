```json
{
  "id": "494a351cf527221e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292423,
  "host_pid": "9e6742732c60:1",
  "hash": "25362c451fef1f307aad9f8405d11c8da72613bd6f46afffc6d7807135c541a6",
  "cid": "QmV125362c451fef1f307aad9f8405d11c8da72613bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292423,
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
      "evaluated_at": 1760292423
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
  "sig": "277c40cec3a888e5dfd48b4d6cdb1bf57f55231d8490248428709fd4609490cf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594873577
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 273, 'threshold': 50, 'total_amount': 109978323, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 272, 'first_seen': 1760284979, 'matching_hash': '5add1f4a09a12b51'}}}