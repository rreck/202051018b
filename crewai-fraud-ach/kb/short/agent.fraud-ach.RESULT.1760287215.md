```json
{
  "id": "98f1d623c0403c7a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287215,
  "host_pid": "9e6742732c60:1",
  "hash": "6b499e4d786275ec58089145030244ebd98ea07188bcac50bd9eff99e9a163b3",
  "cid": "QmV16b499e4d786275ec58089145030244ebd98ea071",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287215,
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
      "evaluated_at": 1760287215
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
  "sig": "bc4142ba00aaf446408469b9791cf40c92bc5071e67e0ac01469ecbd23671ca0"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000248710981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 13344292, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285763, 'matching_hash': '9a1c8fb9d78dcf4a'}}}