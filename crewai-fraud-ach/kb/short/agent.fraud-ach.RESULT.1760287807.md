```json
{
  "id": "faa64cee71873b47",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287807,
  "host_pid": "9e6742732c60:1",
  "hash": "06fe07a7374aefab9a4df3690f2403dfb079307bc23a19a5b20c22dfa7752209",
  "cid": "QmV106fe07a7374aefab9a4df3690f2403dfb079307b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287807,
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
      "evaluated_at": 1760287807
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
  "sig": "6c47ddbe5750916a74c59cc1699b61a69cbd786b8df5701571b9d5fb0b103e35"
}
```

Fraud detected: round_amount_pattern (score: 73)
Transaction: 111000022758137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 36500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285763, 'matching_hash': '98fae2ebc6a98bc5'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}