```json
{
  "id": "4caa1afafb62d3c4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287602,
  "host_pid": "9e6742732c60:1",
  "hash": "f819c2807518aa1b2edaf099bebdeb41c7e556728bd26b2db51f9a09c30d8a34",
  "cid": "QmV1f819c2807518aa1b2edaf099bebdeb41c7e55672",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287602,
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
      "evaluated_at": 1760287602
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
  "sig": "de95e0164ef74d2bc973b16df6c4d0f0a5d82b0e40f994d031136efdd0366131"
}
```

Fraud detected: duplicate_transaction (score: 83)
Transaction: 121000242172457
Details: {'velocity': {'fraud_detected': True, 'risk_score': 82, 'details': {'transaction_count': 66, 'threshold': 50, 'total_amount': 31097220, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 65, 'first_seen': 1760285763, 'matching_hash': '180325de6151a8c9'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '868351851', 'validation_error': 'Invalid routing number checksum'}}}