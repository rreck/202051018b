```json
{
  "id": "4a3c48c768c0e102",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285711,
  "host_pid": "9e6742732c60:1",
  "hash": "6285a1323a8e353e9f6ab4f964b5497c9d1ca8bc619700392a08411b9e9b5a5d",
  "cid": "QmV16285a1323a8e353e9f6ab4f964b5497c9d1ca8bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285711,
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
      "evaluated_at": 1760285711
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
  "sig": "1f57c05811f5b8559052e5d18cc7965d54d586fedafc8d5d85a0cfe597647746"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50, 'total_amount': 30340368, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}