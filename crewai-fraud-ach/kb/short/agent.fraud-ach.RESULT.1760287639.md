```json
{
  "id": "d3368efe8820fa05",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287639,
  "host_pid": "9e6742732c60:1",
  "hash": "6c571205a2484f5ae8fefc6d7ef65744e0447dad988e8128e7a0badb9f44096d",
  "cid": "QmV16c571205a2484f5ae8fefc6d7ef65744e0447dad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287639,
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
      "evaluated_at": 1760287639
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
  "sig": "bc41cdfe9b4b7052c25ca7594a503e4fab884bf76ee2d91c07fe236b1c4c9d6d"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 122105153312612
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285763, 'matching_hash': 'b6b1aeb6185e45bf'}}}