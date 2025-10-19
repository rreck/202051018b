```json
{
  "id": "408f709fa5585ed8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292944,
  "host_pid": "9e6742732c60:1",
  "hash": "7b8f944e541d15893a572ab0eb1df00af543a39abb7e71378050c646e08aaa2e",
  "cid": "QmV17b8f944e541d15893a572ab0eb1df00af543a39a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292944,
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
      "evaluated_at": 1760292944
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
  "sig": "68b353b593f4cc6625d8552e4deb5905f6bfdeda2efe7dd304a2854e1093e878"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 122105157067764
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 104000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285765, 'matching_hash': '7786da7b6c5a4316'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}