```json
{
  "id": "053fd21103b055bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293285,
  "host_pid": "9e6742732c60:1",
  "hash": "20829bd2ddf6dfd7b3156e2255f5e9dfe27da5ef1f0ef2e79b2fe25941a5ec0c",
  "cid": "QmV120829bd2ddf6dfd7b3156e2255f5e9dfe27da5ef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293285,
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
      "evaluated_at": 1760293285
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
  "sig": "344a8e8ad2f4f2766b0ddc8708565a925b73452ab88bae79425c2cf67f21a3bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244410720
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 15158575, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': 'eab520de73a5b8cf'}}}