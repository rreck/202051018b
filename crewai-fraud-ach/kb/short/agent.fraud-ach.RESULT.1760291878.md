```json
{
  "id": "a274125f856e7657",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291878,
  "host_pid": "9e6742732c60:1",
  "hash": "1628333afac7c92f3e89c880e810e6acc9c6eccb6bbbd3f2145fa01ab8f5bb74",
  "cid": "QmV11628333afac7c92f3e89c880e810e6acc9c6eccb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291878,
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
      "evaluated_at": 1760291878
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
  "sig": "1b374a310f8c4ba02e69eb56cb8c930793c9d95826162e59e4bfb8479b88fb6c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022401094
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 185, 'threshold': 50, 'total_amount': 75515705, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 184, 'first_seen': 1760285763, 'matching_hash': '4e5cfda15432477b'}}}