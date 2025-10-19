```json
{
  "id": "8ba50d45690613ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285320,
  "host_pid": "9e6742732c60:1",
  "hash": "6e11b9da0e1c99ec0272573977a3bc61b7609adaba74ca57416d496dfdf37f1e",
  "cid": "QmV16e11b9da0e1c99ec0272573977a3bc61b7609ada",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285320,
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
      "evaluated_at": 1760285320
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
  "sig": "938e04baadf502c91514ed7ba19830f51438adb281870a7b804c25a75f782640"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14327396, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}