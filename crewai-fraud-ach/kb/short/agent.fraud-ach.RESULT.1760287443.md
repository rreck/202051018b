```json
{
  "id": "1d75ec08b41f3814",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287443,
  "host_pid": "9e6742732c60:1",
  "hash": "b8fd68dda0b047998a838f5238c0bcd83141615dd13da82e03724f27cc4eb5be",
  "cid": "QmV1b8fd68dda0b047998a838f5238c0bcd83141615d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287443,
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
      "evaluated_at": 1760287443
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
  "sig": "7e8e6ce529d59332e328ad11997c7add94e0b02a9fe827aa6929303454cfed5e"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000248914863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285765, 'matching_hash': '9c0338b7ffb65590'}}}