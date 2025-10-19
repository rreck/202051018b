```json
{
  "id": "f547c4b00d5ae558",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287168,
  "host_pid": "9e6742732c60:1",
  "hash": "8be6cb507526f9c0aaa99ac40b43a9e90a6a60f6eba0fecb8eb12c9841c9c865",
  "cid": "QmV18be6cb507526f9c0aaa99ac40b43a9e90a6a60f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287168,
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
      "evaluated_at": 1760287168
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
  "sig": "d3e4b6a754760b5a3a5c11e2eecc75524df4d29b60829db72ea2f7544602d890"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15912400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}