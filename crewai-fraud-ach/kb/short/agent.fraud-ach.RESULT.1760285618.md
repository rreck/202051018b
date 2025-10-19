```json
{
  "id": "96116308d5797f81",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285618,
  "host_pid": "9e6742732c60:1",
  "hash": "d363ac2db7c54cac05c636ff3d1f84a10e3572d1f831143e7060c5fc0bf84361",
  "cid": "QmV1d363ac2db7c54cac05c636ff3d1f84a10e3572d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285618,
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
      "evaluated_at": 1760285618
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
  "sig": "1ae0225177448b68b5dde8e20fc8209c3024a7847ed39f24add53ba34b0f5f71"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 021000027783214
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 30566403, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760284979, 'matching_hash': '00d004b11e9e3015'}}}