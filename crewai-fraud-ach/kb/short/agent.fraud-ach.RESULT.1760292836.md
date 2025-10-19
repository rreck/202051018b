```json
{
  "id": "b91fd890c0a3abf3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292836,
  "host_pid": "9e6742732c60:1",
  "hash": "5bf1d42c99caefecc23044e4a6fe0ffe2bc8d4f8e456679168284630bc5b0274",
  "cid": "QmV15bf1d42c99caefecc23044e4a6fe0ffe2bc8d4f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292836,
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
      "evaluated_at": 1760292836
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
  "sig": "c7c02d04815f49ef9091f36662909af35243d0e2be3953ee8d5655395bb27c8c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464749166
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 73462072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285764, 'matching_hash': '2c72b457e71ecad2'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '113877666', 'validation_error': 'Invalid routing number checksum'}}}