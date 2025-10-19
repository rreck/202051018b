```json
{
  "id": "38b8b59802ecd6d6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291704,
  "host_pid": "9e6742732c60:1",
  "hash": "6eb40daf947bc1cfc8c55c3060653da8442e4d37f30052a14a66d0441e32a528",
  "cid": "QmV16eb40daf947bc1cfc8c55c3060653da8442e4d37",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291704,
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
      "evaluated_at": 1760291704
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
  "sig": "61d7327149d69b766e24cbd831f3d6eb9aac01cc44d14d8b7d93b6a92ce611fe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029347324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 27866579, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': '03de14fe5a3852ae'}}}