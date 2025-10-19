```json
{
  "id": "3de414461a923182",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290672,
  "host_pid": "9e6742732c60:1",
  "hash": "0d4e187b1c819142b4e81269b05252cff866c11f3338f8f6dba70541bd2a4282",
  "cid": "QmV10d4e187b1c819142b4e81269b05252cff866c11f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290672,
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
      "evaluated_at": 1760290672
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
  "sig": "4d89e71a232003726faac6d22bde82516bb4b40b3a616fd5619479fbbb9128d4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460644681
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 53237028, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285764, 'matching_hash': '02c671505c0a8698'}}}