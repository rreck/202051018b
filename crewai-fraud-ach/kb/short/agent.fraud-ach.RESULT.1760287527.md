```json
{
  "id": "e3b57ad9d4c3af61",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287527,
  "host_pid": "9e6742732c60:1",
  "hash": "cd465af072d333883206e544c933fa51038c8d0866bfa7ffbbe70ed4386a5ebb",
  "cid": "QmV1cd465af072d333883206e544c933fa51038c8d08",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287527,
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
      "evaluated_at": 1760287527
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
  "sig": "14b0a894637bce38e41b3626bb54e1c330456dbb76a759c5e1c46ef73e0d512e"
}
```

Fraud detected: duplicate_transaction (score: 80)
Transaction: 111000021011137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 76, 'details': {'transaction_count': 63, 'threshold': 50, 'total_amount': 20986875, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 62, 'first_seen': 1760285764, 'matching_hash': '3868aeea45d72d6f'}}}