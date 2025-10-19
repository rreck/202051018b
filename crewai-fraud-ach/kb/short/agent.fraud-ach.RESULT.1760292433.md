```json
{
  "id": "cde37a5429abeb60",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292433,
  "host_pid": "9e6742732c60:1",
  "hash": "db0d09f4f31971955367b92731bcdd56d6b526759ee7b6c0f3b5e6df8e7a0599",
  "cid": "QmV1db0d09f4f31971955367b92731bcdd56d6b52675",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292433,
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
      "evaluated_at": 1760292433
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
  "sig": "3049dd34b5aa1c9684ad27fbb29cd8b3c73126c53bcb5f6ef8e7b0d47b3cf150"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465368597
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 49001386, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285765, 'matching_hash': 'f57f84d557436d23'}}}