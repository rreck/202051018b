```json
{
  "id": "505809e7f8733250",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290619,
  "host_pid": "9e6742732c60:1",
  "hash": "f7cdabacc17f76830bf0e833b3169f617a6da2d8222feeef9cab8e38a59bf72b",
  "cid": "QmV1f7cdabacc17f76830bf0e833b3169f617a6da2d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290619,
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
      "evaluated_at": 1760290619
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
  "sig": "b51a4b60dd81b6c51e49774524aac550db647b03236c876b4dea6d902bca054f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247830233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 21985355, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285763, 'matching_hash': '6844006e916a1387'}}}