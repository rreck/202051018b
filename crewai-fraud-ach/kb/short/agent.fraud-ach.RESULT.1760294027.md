```json
{
  "id": "17878b795ce4d338",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294027,
  "host_pid": "9e6742732c60:1",
  "hash": "4cbb4999e6cd271afe2d536e97bb4b77d1458309409843137825e431f1c98b7f",
  "cid": "QmV14cbb4999e6cd271afe2d536e97bb4b77d1458309",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294027,
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
      "evaluated_at": 1760294027
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
  "sig": "ca619c156e8795a5f87bfe10ae8458658cffce5e46a92db8bb32e3e2e15d43d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027329696
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 105445110, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '9d5d387a3c2fb6f6'}}}'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '053611749', 'validation_error': 'Invalid routing number checksum'}}}