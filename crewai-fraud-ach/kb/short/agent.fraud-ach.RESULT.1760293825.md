```json
{
  "id": "92844ad1f0c3312e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293825,
  "host_pid": "9e6742732c60:1",
  "hash": "4fc90f41102084725fd6904e883c5234dd7d2554209401f71f6f0be1bc65248a",
  "cid": "QmV14fc90f41102084725fd6904e883c5234dd7d2554",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293825,
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
      "evaluated_at": 1760293825
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
  "sig": "fae4981579141f654d65c66501c9155a948a28af89d3b6b3d7a1b9e2f7beabfc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031291734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 76969724, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': 'b88361d419e7152d'}}}}