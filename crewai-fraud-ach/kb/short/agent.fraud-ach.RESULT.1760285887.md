```json
{
  "id": "277f049e38ccd577",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285887,
  "host_pid": "9e6742732c60:1",
  "hash": "b3b8fce8eeb07b363534b209f4c48118a2867bf7eb9fc08d72cd7d62d48f2b8c",
  "cid": "QmV1b3b8fce8eeb07b363534b209f4c48118a2867bf7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285887,
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
      "evaluated_at": 1760285887
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
  "sig": "5909c3b6701612cf6da669335475c6e1273340a0561408984894a8c5443a2139"
}
```

Fraud detected: round_amount_pattern (score: 62)
Transaction: 026009594828050
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760285763, 'matching_hash': '3e77f188c48013ab'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}