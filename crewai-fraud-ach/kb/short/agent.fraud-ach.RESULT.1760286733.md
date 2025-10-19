```json
{
  "id": "8de10b91c6f87028",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286733,
  "host_pid": "9e6742732c60:1",
  "hash": "0c7b9d4eeb747ad6068058c488b816f5d4b4619827bb51426feec71665b62aa5",
  "cid": "QmV10c7b9d4eeb747ad6068058c488b816f5d4b46198",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286733,
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
      "evaluated_at": 1760286733
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
  "sig": "6e1a69bfdfc7d909ca8002b710fe48c962ed3f3ab9f7ae07cdce7b6b6cd6181e"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 021000026547506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 35000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285764, 'matching_hash': 'e0a909ce459a76c8'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}