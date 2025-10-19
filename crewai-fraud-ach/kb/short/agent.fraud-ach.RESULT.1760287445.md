```json
{
  "id": "49de63cdf74b5ea8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287445,
  "host_pid": "9e6742732c60:1",
  "hash": "db0801c7039024e7c01a4ffa5d5a26526a98128cd7a9395f75caad00508bd8a6",
  "cid": "QmV1db0801c7039024e7c01a4ffa5d5a26526a98128c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287445,
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
      "evaluated_at": 1760287445
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
  "sig": "fb6becb554e16decb554fcc274b27b9b1fdaa934d5386aa061b484fcd8bfc8d8"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009597862857
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 60, 'threshold': 50, 'total_amount': 11989320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 59, 'first_seen': 1760285765, 'matching_hash': 'eac3ff1003c03af8'}}}