```json
{
  "id": "59c1618357753a17",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293658,
  "host_pid": "9e6742732c60:1",
  "hash": "ed28edc9e20e17c529bc9da726221f4d27c7a28509f73fd1dabd643cc8938d3a",
  "cid": "QmV1ed28edc9e20e17c529bc9da726221f4d27c7a285",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293658,
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
      "evaluated_at": 1760293658
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
  "sig": "59aedbba7ef60e90cdc7d5b8e17d9f5e702b054630e8ba58d929f7abf07fbd42"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028760265
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 61978390, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': 'ff1172b8afcaa4bc'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '182683957', 'validation_error': 'Invalid routing number checksum'}}}