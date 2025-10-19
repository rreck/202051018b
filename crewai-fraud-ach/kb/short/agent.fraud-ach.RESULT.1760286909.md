```json
{
  "id": "38aeb493c7ed6628",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286909,
  "host_pid": "9e6742732c60:1",
  "hash": "08bff641bc473e1e74d8dfdccb47743ef5a9ea97083769f2b01cab7efa7382ad",
  "cid": "QmV108bff641bc473e1e74d8dfdccb47743ef5a9ea97",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286909,
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
      "evaluated_at": 1760286909
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
  "sig": "eeb17ce408037f5abd80959b63aca2cba395449eaacef95c5754b5c6bf694f16"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105153543170
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285765, 'matching_hash': 'bc1f881c41cfe07c'}}}