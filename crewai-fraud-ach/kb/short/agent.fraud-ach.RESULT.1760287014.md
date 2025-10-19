```json
{
  "id": "975bcbe08d9a08bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287014,
  "host_pid": "9e6742732c60:1",
  "hash": "dd7133cbc6dc1ee691c62b1db26b0f43403ba11c33aef0e3761ad0858bcc722b",
  "cid": "QmV1dd7133cbc6dc1ee691c62b1db26b0f43403ba11c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287014,
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
      "evaluated_at": 1760287014
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
  "sig": "1b6e84a6b422fc7d9879ccf0259802ca0cc1ec83df5d67f9264dc8ee72b2ccea"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009598660548
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10346805, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285763, 'matching_hash': '4ba6ddd8e6715c89'}}}