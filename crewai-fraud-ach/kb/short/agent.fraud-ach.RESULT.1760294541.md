```json
{
  "id": "a9de85f1ca83eb99",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294541,
  "host_pid": "9e6742732c60:1",
  "hash": "f00aa2a266003417d05272fb8ce01fdd34991f44bc5c8ac3b9341d853f4d4566",
  "cid": "QmV1f00aa2a266003417d05272fb8ce01fdd34991f44",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294541,
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
      "evaluated_at": 1760294541
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
  "sig": "98e4ab1e9cd600e886f9f53ec8b1021a33ff5ac532b20bd9a2a7adad17af02a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028841300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 44864400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': 'f5bed59f6c250fae'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '036223730', 'validation_error': 'Invalid routing number checksum'}}}