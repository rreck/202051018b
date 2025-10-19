```json
{
  "id": "89fd6074d0d0d8f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293758,
  "host_pid": "9e6742732c60:1",
  "hash": "edc1ed88db84223ca9bac1d9086237e4717e966eaa06836867faf1fbb8940cfe",
  "cid": "QmV1edc1ed88db84223ca9bac1d9086237e4717e966e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293758,
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
      "evaluated_at": 1760293758
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
  "sig": "7fd610a23fc5d90c945359d35db41cdbdd06e9f6bf70454a8ad7de91135e62f9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026797438
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 83973375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285764, 'matching_hash': '15a6693010fc8a85'}}}