```json
{
  "id": "fe5544a24cf897ec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292134,
  "host_pid": "9e6742732c60:1",
  "hash": "52a28100d43d25ed915e66753850cab8ce980cdbe5055f0530df3d9a127f85e3",
  "cid": "QmV152a28100d43d25ed915e66753850cab8ce980cdb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292134,
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
      "evaluated_at": 1760292134
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
  "sig": "38dac1abaf9fcea706cfbecd4fc31da8bef6b4739311eedf4657bfbeb2b360f8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249881393
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 77283375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': '72e20928773d23d6'}}}