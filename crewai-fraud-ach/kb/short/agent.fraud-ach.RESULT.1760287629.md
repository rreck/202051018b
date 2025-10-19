```json
{
  "id": "5a31ca3317ab7f93",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287629,
  "host_pid": "9e6742732c60:1",
  "hash": "c9ea709ce1e86ebc294f909f8f53d9707924a29e8d9ff30d61a73661c55fceb4",
  "cid": "QmV1c9ea709ce1e86ebc294f909f8f53d9707924a29e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287629,
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
      "evaluated_at": 1760287629
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
  "sig": "468a5fe57e74813e06ec1601cab25066f8620e47840a479a0327def4e9262b52"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 026009596004100
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50, 'total_amount': 10641007, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285763, 'matching_hash': '0723803785cdf871'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '530764331', 'validation_error': 'Invalid routing number checksum'}}}