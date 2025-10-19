```json
{
  "id": "21853f2db8126eec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292688,
  "host_pid": "9e6742732c60:1",
  "hash": "ebedb1ee95e1c6590835dca195dd56d8dd51961a7b24c65feae4085e2d1fbd77",
  "cid": "QmV1ebedb1ee95e1c6590835dca195dd56d8dd51961a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292688,
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
      "evaluated_at": 1760292688
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
  "sig": "ff147cdfef24c19aa9ffb9f3169866acf19cbb4e85046b5e729f0866af80e5ed"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 069024451692491
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 43222557, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': '560f842b4bd5b95e'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '069024457', 'validation_error': 'Invalid routing number checksum'}}}