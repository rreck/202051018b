```json
{
  "id": "3ad5b14cec70aafa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288946,
  "host_pid": "9e6742732c60:1",
  "hash": "23f70748c3720c8fd30b85963d7460f10ac441d36e9517b1775c6a96e54532bb",
  "cid": "QmV123f70748c3720c8fd30b85963d7460f10ac441d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288946,
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
      "evaluated_at": 1760288946
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
  "sig": "4876272e9fcd90be132024d415db161eceea8a009fa9ed79931c55d5d535c003"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201467541453
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 54500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285763, 'matching_hash': '2d82340c3dc0e840'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}