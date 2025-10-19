```json
{
  "id": "f85ab1c2d21b13eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294438,
  "host_pid": "9e6742732c60:1",
  "hash": "d694a8dc9ac24324893b5971b0fba17adc31111cd8d7fe7ae2ff962184bc8751",
  "cid": "QmV1d694a8dc9ac24324893b5971b0fba17adc31111c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294438,
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
      "evaluated_at": 1760294438
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
  "sig": "ba3ccab80c855494a7ce74b559be6eb0cceace4e48dfab87cffba8cd18cc95f9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276330055
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 107209004, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285763, 'matching_hash': '5c86a9c2afef995d'}}}