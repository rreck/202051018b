```json
{
  "id": "adc95e833b5c4eca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289979,
  "host_pid": "9e6742732c60:1",
  "hash": "02a1bc0223439a0c686b0717bec1687233da194b17fc8957863fc4ef51d543b3",
  "cid": "QmV102a1bc0223439a0c686b0717bec1687233da194b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289979,
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
      "evaluated_at": 1760289979
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
  "sig": "0a44764322c6f8da8c50bce3fadfe74362f2f3df24c8f7a3c52f236a7951e7df"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 021000028490637
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 69000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285765, 'matching_hash': '1f028817acc0361c'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}routing number checksum'}}}