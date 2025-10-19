```json
{
  "id": "2c5721b857f6ba67",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292101,
  "host_pid": "9e6742732c60:1",
  "hash": "fbc8272f51b1dca2ac184129e913c82591e637cf8ad693b2e916803c2a19d19e",
  "cid": "QmV1fbc8272f51b1dca2ac184129e913c82591e637cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292101,
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
      "evaluated_at": 1760292101
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
  "sig": "5ba8efd71c296debf3b05df8d0394ad9e754599edd9715684025e378f326ed05"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152187504
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 89764360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285764, 'matching_hash': '4c6bc703d31ba532'}}}