```json
{
  "id": "29333ff11d91e272",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292370,
  "host_pid": "9e6742732c60:1",
  "hash": "2a36d8a70ae2b9b19bfaa18d5bda6ae7d1d7d115870875edf6ce4885f82b84da",
  "cid": "QmV12a36d8a70ae2b9b19bfaa18d5bda6ae7d1d7d115",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292370,
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
      "evaluated_at": 1760292370
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
  "sig": "cdb19804830c66808fa0b3f1ec8574fa2f50f592b0b2f50fdcb37fb57535c399"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201463963144
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 98000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285765, 'matching_hash': '4b7135c5b7384c49'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}