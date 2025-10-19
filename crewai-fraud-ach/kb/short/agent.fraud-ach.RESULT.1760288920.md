```json
{
  "id": "0421c34cf8330bee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288920,
  "host_pid": "9e6742732c60:1",
  "hash": "28c9428d823d72130c69115a72bcb902141dcb6b2b8d7d86a37209e1e569470d",
  "cid": "QmV128c9428d823d72130c69115a72bcb902141dcb6b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288920,
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
      "evaluated_at": 1760288920
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
  "sig": "41f4f8f23bc330da8c3dba3e65fdd345a34fd364646d1d55db935dc515b0061c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245035140
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 43743780, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285763, 'matching_hash': 'af29b59576821758'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '728187403', 'validation_error': 'Invalid routing number checksum'}}}