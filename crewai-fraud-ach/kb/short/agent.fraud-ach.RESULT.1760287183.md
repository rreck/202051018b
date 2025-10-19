```json
{
  "id": "8dc3883be40463a5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287183,
  "host_pid": "9e6742732c60:1",
  "hash": "6325a85585b62be1b5af215d091da57a5dba0e5e029d52880d0dd4b9b3a3031b",
  "cid": "QmV16325a85585b62be1b5af215d091da57a5dba0e5e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287183,
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
      "evaluated_at": 1760287183
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "d35a24c6d3d460389adf14edbc5127be28b86a5ccb64b1e37da9e00e15bb7a89"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100271109324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 12750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285764, 'matching_hash': '28f72b559ab32ea0'}}}g': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '291093507', 'validation_error': 'Invalid routing number checksum'}}}