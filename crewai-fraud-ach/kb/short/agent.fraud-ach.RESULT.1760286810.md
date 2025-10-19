```json
{
  "id": "4b2c3b8420f27ae2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286810,
  "host_pid": "9e6742732c60:1",
  "hash": "feae259da140a65ce86d8a9e322a6006b501312703b4575fac63229a742f1732",
  "cid": "QmV1feae259da140a65ce86d8a9e322a6006b5013127",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286810,
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
      "evaluated_at": 1760286810
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
  "sig": "fdc5f6f31fad8ae7141642dff687ce85199ec57330496042cd77ee8a1556d565"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201466524554
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14532416, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760285763, 'matching_hash': 'c9a1c21cbf3363ae'}}}round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}routing number checksum'}}}