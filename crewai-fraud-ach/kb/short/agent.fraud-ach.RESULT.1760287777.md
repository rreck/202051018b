```json
{
  "id": "d98d482043a6047f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287777,
  "host_pid": "9e6742732c60:1",
  "hash": "30a731012e6afe439263f51d7fa294ffc0fa606f828e868b77e31aed79d56615",
  "cid": "QmV130a731012e6afe439263f51d7fa294ffc0fa606f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287777,
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
      "evaluated_at": 1760287777
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
  "sig": "dfe617c3cf0cfd2d858813011ae9f456a728a494d2b1851cdfbcdd84ede3a033"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 021000027294403
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50, 'total_amount': 14382576, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285763, 'matching_hash': '8d40dd17cbab8bca'}}}