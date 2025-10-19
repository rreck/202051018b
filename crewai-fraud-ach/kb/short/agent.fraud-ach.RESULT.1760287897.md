```json
{
  "id": "f44acb9f87d110a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287897,
  "host_pid": "9e6742732c60:1",
  "hash": "eb10388e655c45be0f2ab42bace3ce95c295b11c40cbf678dc43294ab082a6a4",
  "cid": "QmV1eb10388e655c45be0f2ab42bace3ce95c295b11c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287897,
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
      "evaluated_at": 1760287897
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
  "sig": "444ae47e221b3ca08bf3aec38ac7c4e6c12d6e1a660c56f5d8d1d8d7129e9e8f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463206672
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50, 'total_amount': 25900344, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285763, 'matching_hash': 'e7b1640c0f17a3db'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '472304300', 'validation_error': 'Invalid routing number checksum'}}}