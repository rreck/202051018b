```json
{
  "id": "b8bc0cd0a7947c54",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290930,
  "host_pid": "9e6742732c60:1",
  "hash": "071685587ab01c55571d7eb397e8e528e3f81029f5dc8aabeff38dc6cda30031",
  "cid": "QmV1071685587ab01c55571d7eb397e8e528e3f81029",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290930,
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
      "evaluated_at": 1760290930
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
  "sig": "66efd73b00bd544795e6d94369c191223ea4ccf10ab39c8e4120a67aa65d904c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242021792
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 70269952, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': '6b62929422267286'}}}