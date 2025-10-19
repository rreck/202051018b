```json
{
  "id": "5776d4f9eb55d1dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290790,
  "host_pid": "9e6742732c60:1",
  "hash": "272e6f7af125d6ede5242a17dff2513a9d1a32f9a0fca5a665cfd6c0cfb7cf84",
  "cid": "QmV1272e6f7af125d6ede5242a17dff2513a9d1a32f9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290790,
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
      "evaluated_at": 1760290790
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
  "sig": "3adb3255fccf301527ccf4953f8f311d6eb1b28d5e9dbd0753ae58ce73c5bf55"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024765233
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 54228222, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285763, 'matching_hash': 'feb1cc4bc40c71bc'}}}