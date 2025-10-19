```json
{
  "id": "880e4efa42b6ced1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290627,
  "host_pid": "9e6742732c60:1",
  "hash": "6480a7b37c34caa02bad80ff8f991fae468c2868b7d04e530ae4f5ac18893322",
  "cid": "QmV16480a7b37c34caa02bad80ff8f991fae468c2868",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290627,
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
      "evaluated_at": 1760290627
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
  "sig": "3c747eacdfab479711f0ea9f0d77f6f50f1fe70f8885110c48adc15dc74f6fe1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246878582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 63007560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760284979, 'matching_hash': '3e968f91ba41b0b5'}}}