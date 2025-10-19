```json
{
  "id": "153879e4b265a7e2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291699,
  "host_pid": "9e6742732c60:1",
  "hash": "07c468125610059c49bc47cbafc6b6705ccffcb56f50cf6e317db9e6119ef9bd",
  "cid": "QmV107c468125610059c49bc47cbafc6b6705ccffcb5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291699,
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
      "evaluated_at": 1760291699
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
  "sig": "b952461861d1d996a874a0791103785ce0894354e2231d68fa4b69c1b5e18e2a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026198505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 84780581, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285764, 'matching_hash': '8ff7ad30241d2e02'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '113877666', 'validation_error': 'Invalid routing number checksum'}}}