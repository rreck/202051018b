```json
{
  "id": "b50d1eb640f3eec8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288855,
  "host_pid": "9e6742732c60:1",
  "hash": "5a5f08a2e553bd546e1f385ccf3b1b7d7978005b5b845e7346e78f29bd209080",
  "cid": "QmV15a5f08a2e553bd546e1f385ccf3b1b7d7978005b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288855,
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
      "evaluated_at": 1760288855
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
  "sig": "291fc35e53acccfd1ff72ae656be32cafa6bbdf9a2cf216527cf24cf6622e175"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248452995
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 20419310, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285763, 'matching_hash': '319e0dd4a1544393'}}}