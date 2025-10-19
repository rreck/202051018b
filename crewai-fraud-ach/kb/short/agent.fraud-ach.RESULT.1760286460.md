```json
{
  "id": "cf1ee8828985e889",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286460,
  "host_pid": "9e6742732c60:1",
  "hash": "d63b92625c328a60a45c3a56543b2a3853c868a9baffdf00b0c50098c2c7db42",
  "cid": "QmV1d63b92625c328a60a45c3a56543b2a3853c868a9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286460,
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
      "evaluated_at": 1760286460
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
  "sig": "0f8bf97b28c3cdcb51b6e498dde1a1d715df84569bac9afc42a5190e388ea831"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009596367142
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11779612, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 25, 'first_seen': 1760285763, 'matching_hash': '4f1a5a8d43b99e0b'}}}g number checksum'}}}