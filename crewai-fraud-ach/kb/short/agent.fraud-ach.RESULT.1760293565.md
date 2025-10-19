```json
{
  "id": "64cdb63c486c6ad4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293565,
  "host_pid": "9e6742732c60:1",
  "hash": "00b24feaabb1c93fd5bf1d5d396096e19c75d1c0a706203cf1b6d7e26c1a30bd",
  "cid": "QmV100b24feaabb1c93fd5bf1d5d396096e19c75d1c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293565,
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
      "evaluated_at": 1760293565
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
  "sig": "9d707e14472d52609032c770652aaeecb37220ffa8e5825652487ab16a0a02e1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028559782
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 49370958, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': '551fe21bbee5d648'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '051442869', 'validation_error': 'Invalid routing number checksum'}}}