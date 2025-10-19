```json
{
  "id": "cbc4b4f1fefb2f91",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291362,
  "host_pid": "9e6742732c60:1",
  "hash": "1d3a527c3485e34779b84c0712c9aa2323b8155eaba1355ac70e7c2faaca58ad",
  "cid": "QmV11d3a527c3485e34779b84c0712c9aa2323b8155e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291362,
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
      "evaluated_at": 1760291362
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
  "sig": "a23b224f5c211604b8af310ac5925a69bdc55c15448ed5a58d2ff8df5f4a8280"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270359022
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 38657369, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760285763, 'matching_hash': 'b3fe4d9c14539f22'}}}