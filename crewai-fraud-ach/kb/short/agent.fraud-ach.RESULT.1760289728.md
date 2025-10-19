```json
{
  "id": "6a5049e206208857",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289728,
  "host_pid": "9e6742732c60:1",
  "hash": "c46f25673743200a5acf29927078a55aabcbb5bcf3a12a62110e79399a07d7f0",
  "cid": "QmV1c46f25673743200a5acf29927078a55aabcbb5bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289728,
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
      "evaluated_at": 1760289728
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
  "sig": "d17d76cb66f2e816a98bca7950f1af744bf796e08629d987f0fa9101673f7c3b"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 763245925890246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50, 'total_amount': 59485135, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285764, 'matching_hash': '634500dd7ac761f0'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '763245921', 'validation_error': 'Invalid routing number checksum'}}}