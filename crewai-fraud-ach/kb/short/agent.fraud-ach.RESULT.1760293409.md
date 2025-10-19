```json
{
  "id": "85351d3a58c366f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293409,
  "host_pid": "9e6742732c60:1",
  "hash": "e29bd8649d63dcf48f449e1f830d26789e6dea0dc97c06ab3a9f1fc857348e77",
  "cid": "QmV1e29bd8649d63dcf48f449e1f830d26789e6dea0d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293409,
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
      "evaluated_at": 1760293409
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
  "sig": "a352112e19087db9142f08db42f1e0a169e26c313ce9cc302d1ccc5e207d8422"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460204606
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 29108886, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': 'ff63dbf095b2d177'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '036223730', 'validation_error': 'Invalid routing number checksum'}}}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}