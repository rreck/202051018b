```json
{
  "id": "266220b0cd34d310",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292007,
  "host_pid": "9e6742732c60:1",
  "hash": "b67bcf349d0fb46fc95e5ac430a9425b9661f67519c7fcaf7d587b87acc0fd8f",
  "cid": "QmV1b67bcf349d0fb46fc95e5ac430a9425b9661f675",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292007,
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
      "evaluated_at": 1760292007
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
  "sig": "a93a359e40f31aaf39412c94899ae43ed5a64177b6540c63e1e6f18698dda9e3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240945799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 12850928, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285763, 'matching_hash': '2868277a63cf50ca'}}}