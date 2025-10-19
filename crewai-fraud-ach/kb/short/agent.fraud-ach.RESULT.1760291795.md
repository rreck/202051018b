```json
{
  "id": "e70375b49f4d22d0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291795,
  "host_pid": "9e6742732c60:1",
  "hash": "c4f628b94d01b99388acb27d1d832d0852ae4bdd6d8a874f0c86221ba1c7bd66",
  "cid": "QmV1c4f628b94d01b99388acb27d1d832d0852ae4bdd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291795,
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
      "evaluated_at": 1760291795
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
  "sig": "68450c0015391ee1af24513a46f1eefd18208d6ff09b6845d28d32a768a23571"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241821144
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 89764428, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285763, 'matching_hash': '9191e5c904ced497'}}}