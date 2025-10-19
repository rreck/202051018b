```json
{
  "id": "a6d8934ddfc124b2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294694,
  "host_pid": "9e6742732c60:1",
  "hash": "d51732b637a3e724dbeec45d5200c435555c6ef93036f4433880eb45636ec7f2",
  "cid": "QmV1d51732b637a3e724dbeec45d5200c435555c6ef9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294694,
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
      "evaluated_at": 1760294694
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
  "sig": "235515746443cf13e111ddbaab55be55f0b53e415c65c5629ad55edf3b3faa65"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 063100279773830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 121500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '49e9eab15cee1f0f'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}