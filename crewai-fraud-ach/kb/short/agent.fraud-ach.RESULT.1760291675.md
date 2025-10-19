```json
{
  "id": "4ebf3cb1f24642d6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291675,
  "host_pid": "9e6742732c60:1",
  "hash": "0e733f17e14bb9383e8e87cbb8d4fef4b8c9aad59592074bf4bac83dbd52f5ea",
  "cid": "QmV10e733f17e14bb9383e8e87cbb8d4fef4b8c9aad5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291675,
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
      "evaluated_at": 1760291675
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
  "sig": "7b3461ed0893fc7be6438f5741863ea0a45768bfed221a3171d91fbc02c9fbe9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022683015
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 44044200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285765, 'matching_hash': 'a34aa564f21aebc1'}}}