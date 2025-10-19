```json
{
  "id": "b14cfe6df4d0ee8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285743,
  "host_pid": "9e6742732c60:1",
  "hash": "aaded54009d428adc8203ca1683fcdfd0ff3fa37e414a509a8b7db2caf9bd995",
  "cid": "QmV1aaded54009d428adc8203ca1683fcdfd0ff3fa37",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285743,
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
      "evaluated_at": 1760285743
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
  "sig": "6aaa198938f99c5930a2a6150c708c4f5b72a8183fb17360c9aa3ecca90cc01d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 31604550, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}