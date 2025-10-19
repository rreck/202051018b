```json
{
  "id": "c1f6f3a4b7fdafd6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290173,
  "host_pid": "9e6742732c60:1",
  "hash": "ddf01ebbef17c4079a4478464771df57d0c1c5657a69da245e71567b14cb0aa7",
  "cid": "QmV1ddf01ebbef17c4079a4478464771df57d0c1c565",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290173,
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
      "evaluated_at": 1760290173
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
  "sig": "6ed9a631c573f65a475c324349bf3577bf8b10b17e1cf3b6e64f52cc4401f838"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038917834
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 41540356, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285765, 'matching_hash': '760f57350f86dbe3'}}}