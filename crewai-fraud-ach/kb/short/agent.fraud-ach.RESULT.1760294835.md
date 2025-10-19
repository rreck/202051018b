```json
{
  "id": "50c788b01c405da5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294835,
  "host_pid": "9e6742732c60:1",
  "hash": "2fc99e2c7f64abbacccc4479dbe975fd4564fbc333197b2b9b912b0b3b89f7d8",
  "cid": "QmV12fc99e2c7f64abbacccc4479dbe975fd4564fbc3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294835,
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
      "evaluated_at": 1760294835
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "03b77358e27c8723d8e8e7a096ffa265b6c7d6e89a676b653205cf292f14e4b0"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 122105157067764
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 122500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285765, 'matching_hash': '7786da7b6c5a4316'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}