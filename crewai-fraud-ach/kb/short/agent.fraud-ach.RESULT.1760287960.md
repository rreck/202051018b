```json
{
  "id": "def674f930fdf1a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287960,
  "host_pid": "9e6742732c60:1",
  "hash": "53b535d3b6567b55acff9bd8e28fd37ffadcee5161c98ab58e65a251cfdfaced",
  "cid": "QmV153b535d3b6567b55acff9bd8e28fd37ffadcee51",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287960,
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
      "evaluated_at": 1760287960
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
  "sig": "6b2e18c369c01843b7eb4513e03617c001c3c0df7dfea56c813cba13c0619314"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240945799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285763, 'matching_hash': '2868277a63cf50ca'}}}5765, 'matching_hash': '9c7c32bd8fa37035'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '118929079', 'validation_error': 'Invalid routing number checksum'}}}