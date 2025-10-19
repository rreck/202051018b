```json
{
  "id": "6244baff9f538ad0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290836,
  "host_pid": "9e6742732c60:1",
  "hash": "b0328c9130f68c6ec6dc02cd9f1ddf58fc23cf93c6b5b5c7e660c1d75363e731",
  "cid": "QmV1b0328c9130f68c6ec6dc02cd9f1ddf58fc23cf93",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290836,
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
      "evaluated_at": 1760290836
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
  "sig": "891c375a6a84415fa96d60b45d9c72d818c014446d5a7ea243254660a6eac1b1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156610976
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50, 'total_amount': 40828320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285765, 'matching_hash': 'a1f55d60bf5ccf18'}}}