```json
{
  "id": "6318eeb88d848ed3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293226,
  "host_pid": "9e6742732c60:1",
  "hash": "7018e25b0b951e7cd5500781ce2be07d795f02ae3777ea26ccca1a98a8c748a5",
  "cid": "QmV17018e25b0b951e7cd5500781ce2be07d795f02ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293226,
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
      "evaluated_at": 1760293226
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
  "sig": "225a7e9926476ac9c3035c347b651334d1de4907a9146e9ce8bd94f71c5ac8d4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277214063
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 61322770, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285763, 'matching_hash': 'ff6f9f90137c8ef9'}}}