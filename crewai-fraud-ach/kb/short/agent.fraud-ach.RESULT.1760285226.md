```json
{
  "id": "136952e48de93f0d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285226,
  "host_pid": "9e6742732c60:1",
  "hash": "f28c2da7270128ecc36a4befb770cc5a4695e620da7bd539f171aa46bafc9aa9",
  "cid": "QmV1f28c2da7270128ecc36a4befb770cc5a4695e620",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285226,
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
      "evaluated_at": 1760285226
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "7d1937db920f975050ad06f6d73075a1faaf0583a5565adfc0487acf3222cb05"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10534850, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}