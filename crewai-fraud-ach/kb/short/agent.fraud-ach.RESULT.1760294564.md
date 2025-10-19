```json
{
  "id": "39c8e7c422d18abe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294564,
  "host_pid": "9e6742732c60:1",
  "hash": "9d6d96452aa90b4d868accf549cfe7a46eae41f8aa104ba83d833f0376da488c",
  "cid": "QmV19d6d96452aa90b4d868accf549cfe7a46eae41f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294564,
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
      "evaluated_at": 1760294564
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
  "sig": "e453c78bcc3560e54b02e35d6209a767058d5f097b46202e9ab3ffd0ff383248"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241250323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 23758320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': 'd18939bbbb7c2a14'}}}