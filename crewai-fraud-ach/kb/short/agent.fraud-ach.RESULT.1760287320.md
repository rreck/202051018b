```json
{
  "id": "1cfb2932244190b7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287320,
  "host_pid": "9e6742732c60:1",
  "hash": "954db35c2cbee0cdc8fb099de01fb880f754a2ce17b24a925170a5f2a9b18b33",
  "cid": "QmV1954db35c2cbee0cdc8fb099de01fb880f754a2ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287320,
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
      "evaluated_at": 1760287320
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "e460067f553ae7b33b6d15560b2ef86d4dd6afe7140081a3184bb09b5ea176ec"
}
```

Fraud detected: invalid_routing (score: 83)
Transaction: 472304306013162
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 56, 'threshold': 50, 'total_amount': 25384072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 55, 'first_seen': 1760285764, 'matching_hash': '18e6c75ff941397c'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '472304300', 'validation_error': 'Invalid routing number checksum'}}}