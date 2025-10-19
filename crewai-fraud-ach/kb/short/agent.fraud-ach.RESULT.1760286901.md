```json
{
  "id": "54cebe74ddba9e49",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286901,
  "host_pid": "9e6742732c60:1",
  "hash": "8d418c905a4259875e51c88468b2f5bf6bfe7b2a6b02d75c407fae22fee07277",
  "cid": "QmV18d418c905a4259875e51c88468b2f5bf6bfe7b2a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286901,
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
      "evaluated_at": 1760286901
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
  "sig": "cb73dbcc68087285e117eea024f33b05fcefc8f76f68945c9c13b8a820234140"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000020703113
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11789263, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285763, 'matching_hash': '6c2ac9b0cec56c2f'}}}