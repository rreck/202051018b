```json
{
  "id": "53c42c64c2d7ea5e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291844,
  "host_pid": "9e6742732c60:1",
  "hash": "b3dd6c0e257aca5c1fbb4f77f4915f29a2a3050c15c319fb8a90ec85b0c16f94",
  "cid": "QmV1b3dd6c0e257aca5c1fbb4f77f4915f29a2a3050c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291844,
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
      "evaluated_at": 1760291844
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
  "sig": "3601b03ccb3f8ccfc40033f71e7aebe7d9ed90b920a5da79ad0f1406964df115"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241271841
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 79482664, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285764, 'matching_hash': '100dee2bbeee5c05'}}}